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

    def test_course_can_be_followed_in_order_from_foundations_to_capstone(self):
        source = "curriculum/00-foundations.md"
        visited = []
        previous = None
        stages = []
        while source:
            self.assertNotIn(source, visited, "The course must not loop")
            context = self.workspace.workspace_for(source, self.pages).get("course")
            self.assertIsNotNone(context, "Course pages need sequential navigation")
            self.assertEqual(context["position"], len(visited) + 1)
            self.assertEqual(context["total"], len(self.workspace.COURSE))
            self.assertEqual(context["previous"]["source"] if context["previous"] else None, previous)
            visited.append(source)
            stages.append(context["stage"]["number"])
            previous = source
            source = context["next"]["source"] if context["next"] else None
        self.assertEqual(visited, self.workspace.COURSE)
        self.assertEqual(visited[-1], "curriculum/08-capstones.md")
        self.assertEqual(sorted(set(stages)), list(range(1, 7)))
        self.assertEqual(stages, sorted(stages))
        self.assertLess(visited.index("curriculum/03-embeddings.md"), visited.index("labs/03-embeddings.md"))
        self.assertLess(visited.index("labs/03-embeddings.md"), visited.index("curriculum/03-rag-memory.md"))

    def test_course_navigation_skips_unavailable_steps(self):
        pages = self.pages - {"labs/03-embeddings.md"}
        context = self.workspace.workspace_for("curriculum/03-embeddings.md", pages).get("course")
        self.assertIsNotNone(context, "The chapter needs a next course step")
        self.assertEqual(context["next"]["source"], "curriculum/03-rag-memory.md")
        self.assertEqual(context["total"], len(self.workspace.COURSE) - 1)

    def test_course_stage_links_resolve_to_the_full_plan(self):
        plan = Markdown(extensions=["toc", "attr_list"])
        plan.convert((ROOT / "docs/curriculum/index.md").read_text())

        def ids(tokens):
            return {token["id"] for token in tokens} | {value for token in tokens for value in ids(token["children"])}

        anchors = ids(plan.toc_tokens)
        for source in self.workspace.COURSE:
            context = self.workspace.workspace_for(source, self.pages).get("course")
            self.assertIsNotNone(context)
            self.assertEqual(context["plan_url"], "curriculum/")
            self.assertIn(context["stage"]["url"].split("#")[1], anchors)
            self.assertEqual(context["stage"]["total"], 6)
            for direction in ("previous", "next"):
                if context[direction]:
                    target = context[direction]
                    self.assertIn(target["source"], self.pages)
                    self.assertEqual(target["url"], self.workspace.page_url(target["source"]))

    def test_reference_pages_are_not_assigned_a_course_step(self):
        for source in ("index.md", "topics/models.md", "concepts/foundations.md", "papers/bert.md"):
            self.assertIsNone(self.workspace.workspace_for(source, self.pages).get("course"))


if __name__ == "__main__":
    unittest.main()
