from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import unittest
from markdown import Markdown


ROOT = Path(__file__).resolve().parents[1]


class WorkspaceNavigationTests(unittest.TestCase):
    def setUp(self):
        path = ROOT / "hooks/workspace.py"
        self.assertTrue(path.exists(), "The topic navigation hook must exist")
        spec = spec_from_file_location("workspace", path)
        self.workspace = module_from_spec(spec)
        spec.loader.exec_module(self.workspace)
        self.pages = {p.relative_to(ROOT / "docs").as_posix() for p in (ROOT / "docs").rglob("*.md")}

    def test_every_published_page_has_valid_context_and_links(self):
        for path in self.pages:
            with self.subTest(path=path):
                context = self.workspace.workspace_for(path, self.pages)
                self.assertTrue(context["kind"])
                if context["topic"]:
                    self.assertIn(context["topic"]["source"], self.pages)
                for tab in context["tabs"]:
                    self.assertIn(tab["source"], self.pages)
                    self.assertFalse(tab["url"].startswith("/"), "Keep GitHub Pages subpaths")

    def test_embeddings_explanation_and_lab_share_topic_and_modes(self):
        explanation = self.workspace.workspace_for("curriculum/03-embeddings.md", self.pages)
        practice = self.workspace.workspace_for("labs/03-embeddings.md", self.pages)
        self.assertEqual(explanation["topic"]["id"], "retrieval")
        self.assertEqual(explanation["topic"], practice["topic"])
        self.assertEqual([tab["label"] for tab in practice["tabs"]], ["Understand", "Practice"])
        self.assertEqual([tab["active"] for tab in explanation["tabs"]], [True, False])
        self.assertEqual([tab["active"] for tab in practice["tabs"]], [False, True])

    def test_topic_context_spans_lessons_studies_papers_and_glossary(self):
        examples = {
            "papers/attention-is-all-you-need.md": "models",
            "concepts/prompting.md": "prompting",
            "system-design/opensearch-retrieval.md": "retrieval",
            "system-design/tool-using-agents.md": "agents",
            "system-design/evaluation-observability.md": "evaluation",
            "concepts/platform-and-sre.md": "production",
        }
        for path, topic in examples.items():
            self.assertEqual(self.workspace.workspace_for(path, self.pages)["topic"]["id"], topic)

    def test_missing_optional_lab_is_never_offered(self):
        pages = self.pages - {"labs/03-embeddings.md"}
        context = self.workspace.workspace_for("curriculum/03-embeddings.md", pages)
        self.assertFalse(any(tab["label"] == "Practice" for tab in context["tabs"]))

    def test_inline_practice_links_resolve_to_real_headings(self):
        def heading_ids(tokens):
            return {token["id"] for token in tokens} | {
                value for token in tokens for value in heading_ids(token["children"])
            }

        for source in self.workspace.INLINE_LABS:
            rendered = Markdown(extensions=["toc", "fenced_code"])
            rendered.convert((ROOT / "docs" / source).read_text())
            practice = self.workspace.workspace_for(source, self.pages)["tabs"][1]
            self.assertIn(practice["url"].split("#")[1], heading_ids(rendered.toc_tokens), source)

    def test_all_topic_entry_points_are_real_pages(self):
        self.assertEqual(len(self.workspace.TOPICS), 6)
        for topic in self.workspace.TOPICS:
            self.assertIn(topic["source"], self.pages)
            self.assertEqual(topic["url"], f"topics/{topic['id']}/")


if __name__ == "__main__":
    unittest.main()
