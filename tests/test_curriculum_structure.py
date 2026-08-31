from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CurriculumStructureTests(unittest.TestCase):
    def read(self, relative_path: str) -> str:
        return (ROOT / relative_path).read_text()

    def test_beginner_tracks_are_assumed_not_taught(self) -> None:
        nav = self.read("mkdocs.yml")
        curriculum_index = self.read("docs/curriculum/index.md")

        for relative_path in (
            "docs/curriculum/environment-and-programming.md",
            "docs/curriculum/engineering-core.md",
        ):
            self.assertFalse((ROOT / relative_path).exists(), relative_path)
        self.assertNotIn("curriculum/environment-and-programming.md", nav)
        self.assertNotIn("curriculum/engineering-core.md", nav)

        self.assertIn("What we assume", curriculum_index)
        for term in ("HTTP", "SQL", "Docker"):
            self.assertIn(term, curriculum_index)

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

    def test_environment_vocabulary_stays_available_in_concepts(self) -> None:
        concepts = self.read("docs/concepts/developer-environment.md")
        nav = self.read("mkdocs.yml")

        self.assertIn("developer-environment.md", nav)
        concepts_lower = concepts.lower()
        for term in ("environment variable", "api key"):
            self.assertIn(term, concepts_lower)

    def test_foundations_has_beginner_ai_onramp_and_visuals(self) -> None:
        foundations = self.read("docs/curriculum/00-foundations.md")
        foundations_lower = foundations.lower()

        for term in ("what is ai", "machine learning", "large language model", "tokens"):
            self.assertIn(term, foundations_lower)
        self.assertIn("```mermaid", foundations_lower)
        self.assertIn("why this matters", foundations_lower)
        self.assertIn("a short history", foundations_lower)
        self.assertIn("## Suggested reading", foundations)

    def test_foundations_has_attributed_web_images(self) -> None:
        foundations = self.read("docs/curriculum/00-foundations.md")
        credits = self.read("docs/image-credits.md")

        for relative_path in (
            "docs/assets/images/ai-ml-dl.svg",
            "docs/assets/images/ml-system-workflow.png",
        ):
            self.assertTrue((ROOT / relative_path).exists(), relative_path)

        self.assertIn("ai-ml-dl.svg", foundations)
        self.assertIn("ml-system-workflow.png", foundations)
        self.assertIn("Wikimedia Commons", credits)
        self.assertIn("CC BY-SA 4.0", credits)

    def test_mermaid_fence_is_configured_for_rendering(self) -> None:
        mkdocs = self.read("mkdocs.yml")

        self.assertIn("custom_fences:", mkdocs)
        self.assertIn("name: mermaid", mkdocs)
        self.assertIn("class: mermaid", mkdocs)

    def test_roadmap_gap_topics_are_covered(self) -> None:
        retrieval = self.read("docs/curriculum/03-rag-memory.md")
        security = self.read("docs/concepts/safety-and-security.md")
        production = self.read("docs/curriculum/06-production-systems.md")
        specializations = self.read("docs/curriculum/specializations.md")
        dev_env = self.read("docs/concepts/developer-environment.md")

        self.assertIn("text-to-sql", retrieval.lower())
        self.assertIn("responsible ai", security.lower())
        self.assertIn("responsible ai", production.lower())
        self.assertIn("image generation", specializations.lower())
        self.assertIn("coding assistant", dev_env.lower())

    def test_course_supports_snippets_and_tiered_build_formats(self) -> None:
        builds = self.read("builds/README.md")
        home = self.read("docs/index.md")
        curriculum = self.read("docs/curriculum/index.md")

        combined = (builds + home + curriculum).lower()
        self.assertIn("snippet", combined)
        self.assertIn("dockerized only when", combined)
        self.assertNotIn("everything is dockerized", builds.lower())

    def test_paper_catalog_and_guides_are_discoverable(self) -> None:
        nav = self.read("mkdocs.yml")
        catalog = self.read("docs/papers/index.md")

        guides = {
            "alexnet.md": "AlexNet",
            "generative-adversarial-networks.md": "Generative Adversarial Networks",
            "resnet.md": "Deep Residual Learning",
            "attention-is-all-you-need.md": "Attention Is All You Need",
            "bert.md": "BERT",
            "gpt-3.md": "Language Models are Few-Shot Learners",
        }

        self.assertIn("Papers:", nav)
        self.assertIn("papers/index.md", nav)
        for filename, title in guides.items():
            relative_path = f"docs/papers/{filename}"
            self.assertTrue((ROOT / relative_path).exists(), relative_path)
            self.assertIn(filename, nav)
            self.assertIn(title, catalog)

    def test_paper_guides_use_a_consistent_beginner_friendly_structure(self) -> None:
        guide_paths = (
            "docs/papers/alexnet.md",
            "docs/papers/generative-adversarial-networks.md",
            "docs/papers/resnet.md",
            "docs/papers/attention-is-all-you-need.md",
            "docs/papers/bert.md",
            "docs/papers/gpt-3.md",
        )

        required_sections = (
            "## The paper in one sentence",
            "## The problem",
            "## The core idea",
            "## How it works",
            "## What changed after this paper",
            "## What the paper does not solve",
            "## Check your understanding",
            "## Read the original",
        )

        for relative_path in guide_paths:
            content = self.read(relative_path)
            for section in required_sections:
                self.assertIn(section, content, f"{section} missing from {relative_path}")
            self.assertIn("```mermaid", content, relative_path)

    def test_attention_guide_explains_transformers_without_hiding_key_concepts(self) -> None:
        attention = self.read("docs/papers/attention-is-all-you-need.md").lower()

        for term in (
            "query",
            "key",
            "value",
            "self-attention",
            "multi-head attention",
            "positional encoding",
            "encoder",
            "decoder",
            "residual",
            "feed-forward",
            "mask",
        ):
            self.assertIn(term, attention)

    # Modules whose lab work has moved into the Labs section. The module page
    # keeps a pointer; the trial and build tasks live on the lab page.
    MIGRATED_LABS = {
        "docs/curriculum/00-foundations.md": "docs/labs/00-foundations.md",
    }

    def test_each_core_module_has_a_separated_lab_section(self) -> None:
        lab_pages = (
            "docs/curriculum/00-foundations.md",
            "docs/curriculum/01-llm-internals.md",
            "docs/curriculum/02-prompting-context.md",
            "docs/curriculum/03-rag-memory.md",
            "docs/curriculum/04-agents-tools-mcp.md",
            "docs/curriculum/05-evals-observability.md",
            "docs/curriculum/06-production-systems.md",
            "docs/curriculum/07-forward-deployed.md",
        )
        trial_pages = set(lab_pages) - {
            "docs/curriculum/01-llm-internals.md",
        }

        for relative_path in lab_pages:
            content = self.read(relative_path)
            self.assertIn("## \U0001F9EA Lab", content, relative_path)

            migrated = self.MIGRATED_LABS.get(relative_path)
            if migrated is not None:
                self.assertIn("../labs/", content, relative_path)
                self.assertIn("## Trial \u00B7", self.read(migrated), migrated)
            elif relative_path in trial_pages:
                self.assertIn("### Trial \u00B7", content, relative_path)

        curriculum_index = self.read("docs/curriculum/index.md")
        self.assertIn("\U0001F9EA Lab", curriculum_index)

    def test_labs_section_leads_with_workspace_setup(self) -> None:
        nav = self.read("mkdocs.yml")
        self.assertIn("  - Labs:", nav)

        for relative_path in (
            "docs/labs/index.md",
            "docs/labs/setup.md",
            "docs/labs/00-foundations.md",
        ):
            self.assertTrue((ROOT / relative_path).exists(), relative_path)
            self.assertIn(f"labs/{Path(relative_path).name}", nav, relative_path)

        setup = self.read("docs/labs/setup.md")
        for token in (
            "docker compose version",
            "hello-world",
            "ANTHROPIC_API_KEY",
            "docker compose down",
        ):
            self.assertIn(token, setup, token)

        # The setup lab installs Docker. Teaching Docker stays out of the
        # curriculum, which lists it as an assumed prerequisite.
        self.assertIn("does not teach Docker", setup)
        self.assertIn("Docker", self.read("docs/curriculum/index.md"))

    def test_each_module_states_learning_objectives(self) -> None:
        for relative_path in (
            "docs/curriculum/00-foundations.md",
            "docs/curriculum/01-llm-internals.md",
            "docs/curriculum/02-prompting-context.md",
            "docs/curriculum/03-rag-memory.md",
            "docs/curriculum/04-agents-tools-mcp.md",
            "docs/curriculum/05-evals-observability.md",
            "docs/curriculum/06-production-systems.md",
            "docs/curriculum/07-forward-deployed.md",
            "docs/curriculum/08-capstones.md",
        ):
            content = self.read(relative_path)
            self.assertIn("## What you will be able to do", content, relative_path)

    def test_career_page_tracks_ai_engineer_and_fde_jobs_to_linkedin(self) -> None:
        career = self.read("docs/career.md")
        nav = self.read("mkdocs.yml")

        self.assertIn("Career: career.md", nav)
        self.assertIn("AI Engineer", career)
        self.assertIn("Forward-Deployed Engineer", career)
        self.assertIn("Live LinkedIn searches", career)
        self.assertIn("Tracked openings", career)
        self.assertGreaterEqual(career.count("https://www.linkedin.com/jobs/view/"), 6)
        self.assertGreaterEqual(career.count("https://www.linkedin.com/jobs/search/"), 4)
        self.assertIn("Last reviewed: August 10, 2026", career)


if __name__ == "__main__":
    unittest.main()
