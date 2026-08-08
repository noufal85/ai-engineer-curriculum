from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CurriculumStructureTests(unittest.TestCase):
    def read(self, relative_path: str) -> str:
        return (ROOT / relative_path).read_text()

    def test_engineering_core_track_exists(self) -> None:
        content = self.read("docs/curriculum/engineering-core.md")
        for term in ("Engineering Core", "HTTP", "SQL", "testing", "CI/CD"):
            self.assertIn(term, content)

    def test_new_concept_categories_exist(self) -> None:
        for relative_path in (
            "docs/concepts/engineering-core.md",
            "docs/concepts/platform-and-sre.md",
            "docs/concepts/product-and-adoption.md",
        ):
            self.assertTrue((ROOT / relative_path).exists(), relative_path)

    def test_curriculum_indexes_new_track_and_deeper_topics(self) -> None:
        curriculum_index = self.read("docs/curriculum/index.md")
        concepts_index = self.read("docs/concepts/index.md")
        nav = self.read("mkdocs.yml")

        self.assertIn("Engineering Core", curriculum_index)
        self.assertIn("Engineering core", concepts_index)
        self.assertIn("platform-and-sre.md", nav)
        self.assertIn("product-and-adoption.md", nav)

    def test_core_modules_include_operational_depth(self) -> None:
        retrieval = self.read("docs/curriculum/03-rag-memory.md")
        agents = self.read("docs/curriculum/04-agents-tools-mcp.md")
        evals = self.read("docs/curriculum/05-evals-observability.md")
        production = self.read("docs/curriculum/06-production-systems.md")
        fde = self.read("docs/curriculum/07-forward-deployed.md")
        capstones = self.read("docs/curriculum/08-capstones.md")

        self.assertIn("query rewriting", retrieval.lower())
        self.assertIn("workflow", agents.lower())
        self.assertIn("ci", evals.lower())
        self.assertIn("slo", production.lower())
        self.assertIn("adoption", fde.lower())
        self.assertIn("rubric", capstones.lower())

    def test_specialization_tracks_are_discoverable(self) -> None:
        specializations = self.read("docs/curriculum/specializations.md")
        nav = self.read("mkdocs.yml")

        specializations_lower = specializations.lower()
        for term in ("multimodal", "fine-tuning", "local inference"):
            self.assertIn(term, specializations_lower)
        self.assertIn("specializations.md", nav)


if __name__ == "__main__":
    unittest.main()
