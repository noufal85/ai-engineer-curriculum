# Resources

A short, curated set — deliberately not a link dump. Module pages carry their own targeted resources; this is the standing shelf.

## Read the primary docs

- **Anthropic** and **OpenAI** API docs — especially streaming, structured output/tool use, and prompt caching. Read these before any tutorial.
- **Model Context Protocol (MCP)** spec — the integration standard behind Modules 4, 6, 7.

## Foundational intuition

- **Karpathy** — "Intro to LLMs", "Let's build the GPT tokenizer" (mental model for Module 1).
- **"Lost in the Middle"** (Liu et al.) — context ordering (Module 2).
- **Anthropic — "Building effective agents"** — agent patterns without the hype (Module 4).

## RAG, graphs & memory

- **Neo4j GraphAcademy** (`dev.neo4j.com/ga-rag`) — GraphRAG + agent-memory courses.
- A vector DB quickstart (**PGVector** or **LanceDB**) + a reranker.
- Talk notes in this site: [CrabRAG](notes/crabrag-graph-memory.md), [Your Moat Is Your Data Model](notes/moat-is-your-data-model.md).

## Evals & production

- **Hamel Husain** and **Shreya Shankar** on LLM evals — the practitioner canon (Module 5).
- One tracing tool: **Langfuse**, **LangSmith**, or **Phoenix** — learn its trace model.
- **OWASP Top 10 for LLM Applications** — security baseline (Module 6).

## The forward-deployed role

- **Palantir FDE** talks/writing — the canonical framing (Module 7).
- Domain-driven design / event-storming basics — for domain modeling.

## Staying current

- Provider changelogs (model releases, pricing, context limits) — check before making model-choice decisions; don't rely on memory.
- A small set of practitioner blogs/newsletters over doomscrolling; depth over feed.
