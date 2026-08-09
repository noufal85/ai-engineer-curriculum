# Resources

A short, curated shelf. Module pages carry their own targeted references; this page keeps the durable starting points in one place.

## Engineering and production

- A beginner terminal/shell tutorial for your operating system, plus Python installation and virtual-environment documentation.
- Documentation for the language, HTTP framework, SQL database, Docker, testing stack, and CI system you choose.
- One SRE reference covering SLOs, backpressure, incident response, and graceful degradation.
- Your cloud provider's identity, secrets, logging, deployment, and database guidance.

## Read primary docs

- **Anthropic** and **OpenAI** API docs — especially streaming, structured output, tool use, and prompt caching.
- **Model Context Protocol (MCP)** specification — the integration standard behind Modules 4, 6, and 7.
- **OWASP Top 10 for LLM Applications** — security baseline for Module 6.

## Foundational intuition

- Karpathy, *Intro to LLMs* and *Let's build GPT tokenizer* — mental model for Module 1.
- *Lost in the Middle* (Liu et al.) — context ordering for Module 2.
- Anthropic, *Building effective agents* — agent patterns without hype for Module 4.

## Retrieval, graphs, and memory

- Neo4j GraphAcademy — GraphRAG, graph modeling, and agent-memory courses.
- A vector database quickstart such as PGVector or LanceDB plus a reranker.
- Talk notes: [CrabRAG](notes/crabrag-graph-memory.md) and [Your Moat Is Your Data Model](notes/moat-is-your-data-model.md).

## Evals and observability

- Hamel Husain and Shreya Shankar on practical LLM evaluation.
- One tracing tool such as Langfuse, LangSmith, or Phoenix; learn its trace model, not just its UI.
- A judge-calibration and rubric workflow that can be run in CI.

## Forward-deployed role

- Palantir FDE talks and writing for the role framing.
- Domain-driven design, event storming, workflow mapping, and service blueprinting.

## Staying current

- Check provider changelogs for model releases, pricing, context limits, and API behavior before making model-choice decisions.
- Prefer a small number of deep sources over a large feed of shallow updates.
- See [Image Credits](image-credits.md) for the license and attribution of sourced lesson images.
