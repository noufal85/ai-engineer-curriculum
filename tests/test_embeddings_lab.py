"""Offline correctness checks; learned rankings are inspected in the live lab."""

import importlib.util
import contextlib
import io
import math
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "builds/03-embeddings-lab"
SCRIPT = LAB / "embeddings_lab.py"


class UnitVectorBatch(list):
    """Controlled numeric test fixture, never a substitute lab embedding model."""

    @property
    def shape(self):
        return (len(self), 2)


class OfflineEncoder:
    def encode(self, texts, **kwargs):
        return UnitVectorBatch([[1.0, 0.0] for _ in texts])

    encode_query = encode
    encode_document = encode


class EmbeddingsLabTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SCRIPT.exists(), "The runnable embeddings lab is missing")
        spec = importlib.util.spec_from_file_location("embeddings_lab", SCRIPT)
        self.lab = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.lab)

    def test_similarity_and_distance_have_distinct_scaling_behavior(self):
        lab = self.lab
        self.assertAlmostEqual(lab.cosine([1, 0], [0.8, 0.6]), 0.8)
        self.assertAlmostEqual(lab.cosine([1, 0], [8, 6]), 0.8)
        self.assertAlmostEqual(lab.dot([1, 0], [8, 6]), 8)
        self.assertAlmostEqual(lab.euclidean([1, 0], [8, 6]), math.sqrt(85))
        self.assertAlmostEqual(lab.cosine([1, 0], [-1, 0]), -1)

    def test_invalid_vectors_do_not_silently_produce_scores(self):
        for left, right in [([], []), ([1], [1, 2]), ([math.nan], [1])]:
            with self.subTest(left=left, right=right), self.assertRaises(ValueError):
                self.lab.cosine(left, right)
        with self.assertRaises(ValueError):
            self.lab.cosine([0, 0], [1, 0])

    def test_rankings_use_descending_score_and_stable_id_ties(self):
        self.assertEqual(
            self.lab.rank_scores(["c", "b", "a"], [0.1, 0.9, 0.9], 2),
            [("a", 0.9), ("b", 0.9)],
        )
        with self.assertRaises(ValueError):
            self.lab.rank_scores(["a"], [1], 0)
        with self.assertRaises(ValueError):
            self.lab.rank_scores(["a", "a"], [1, 2], 1)
        with self.assertRaises(ValueError):
            self.lab.rank_scores(["a"], [math.inf], 1)

    def test_keyword_baseline_matches_casefolded_whole_tokens(self):
        self.assertEqual(self.lab.keyword_score("RESET password", "Password reset link"), 1)
        self.assertEqual(self.lab.keyword_score("reset password", "reset billing"), 0.5)
        self.assertEqual(self.lab.keyword_score("reset", "resetting"), 0)

    def test_recall_uses_all_relevant_documents_and_rr_uses_first_hit(self):
        metrics = self.lab.retrieval_metrics(["x", "b", "a", "z"], ["a", "b"], 2)
        self.assertEqual(metrics["recall_at_k"], 0.5)
        self.assertEqual(metrics["reciprocal_rank_at_k"], 0.5)
        self.assertEqual(metrics["first_relevant_rank"], 2)

    def test_hits_outside_k_do_not_improve_metrics(self):
        metrics = self.lab.retrieval_metrics(["x", "b"], ["b"], 1)
        self.assertEqual(metrics["recall_at_k"], 0)
        self.assertEqual(metrics["reciprocal_rank_at_k"], 0)
        self.assertEqual(metrics["first_relevant_rank"], 2)
        with self.assertRaises(ValueError):
            self.lab.retrieval_metrics(["a"], [], 1)
        with self.assertRaises(ValueError):
            self.lab.retrieval_metrics(["a", "a"], ["a"], 2)

    def test_fixture_labels_exist_and_query_splits_do_not_overlap(self):
        docs, queries = self.lab.load_data()
        self.assertEqual(len(docs), 24)
        self.assertGreaterEqual(len(queries["dev"]), 6)
        self.assertGreaterEqual(len(queries["test"]), 6)
        self.assertGreaterEqual(len(queries["no_answer"]), 2)
        self.lab.validate_dataset(docs, queries)
        bad_queries = dict(queries, test=queries["dev"])
        with self.assertRaises(ValueError):
            self.lab.validate_dataset(docs, bad_queries)

    def test_paragraphs_keep_their_source_and_repeat_the_title(self):
        chunks = self.lab.paragraph_chunks([
            {"id": "article", "title": "Account", "text": "First paragraph.\n\nSecond paragraph."}
        ])
        self.assertEqual([chunk["id"] for chunk in chunks], ["article-p01", "article-p02"])
        self.assertEqual([chunk["source_id"] for chunk in chunks], ["article", "article"])
        self.assertTrue(all(self.lab.document_text(chunk).startswith("Account\n") for chunk in chunks))

    def test_default_cli_and_fixture_check_run_without_site_packages(self):
        # -S forbids third-party imports, proving geometry and --check work offline.
        for flags, expected in [([], "MANUAL VECTORS"), (["--check"], "24 documents")]:
            result = subprocess.run(
                [sys.executable, "-S", str(SCRIPT), *flags],
                capture_output=True, text=True, timeout=15,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(expected, result.stdout)

    def test_cli_rejects_blank_query_and_invalid_top_k(self):
        for flags in [["--top-k", "0"], ["--query", "   "]]:
            result = subprocess.run(
                [sys.executable, "-S", str(SCRIPT), *flags],
                capture_output=True, text=True, timeout=15,
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("error:", result.stderr)

    def test_pairs_report_measured_norms(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.lab.pairs_example(OfflineEncoder())
        self.assertIn("norm=1.000000", output.getvalue())
        self.assertIn("norm range: min=1.000000, max=1.000000", output.getvalue())

    def test_search_reports_separate_encoding_and_scoring_times(self):
        docs, _ = self.lab.load_data()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.lab.search_example(OfflineEncoder(), docs, "password", 3)
        for label in ("Document encoding:", "Query encoding:", "Learned scoring and ranking:"):
            self.assertIn(label, output.getvalue())

    def test_evaluation_reports_timings_for_answerable_queries(self):
        docs, queries = self.lab.load_data()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.lab.evaluate_example(OfflineEncoder(), docs, queries, "dev", 3)
        for label in ("Document encoding:", "Query encoding:", "Learned scoring and ranking:", "answerable queries only"):
            self.assertIn(label, output.getvalue())


if __name__ == "__main__":
    unittest.main()
