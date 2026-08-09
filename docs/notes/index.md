# Talk Notes

Full, code-verified write-ups of talks that feed directly into the curriculum. The format is the standard I hold myself to for a "ticked" learning item: **capture every technical detail, cut the fluff, and be able to defend the design.**

- [**Intro to Large Language Models**](intro-to-large-language-models.md) — Andrej Karpathy. From next-token pretraining to assistant fine-tuning, tools, multimodality, the LLM-as-OS mental model, and the security boundary around prompt injection. Feeds [Module 1](../curriculum/01-llm-internals.md), [Module 2](../curriculum/02-prompting-context.md), [Module 3](../curriculum/03-rag-memory.md), [Module 4](../curriculum/04-agents-tools-mcp.md), and [Module 6](../curriculum/06-production-systems.md).
- [**CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens**](crabrag-graph-memory.md) — Stephen Chin (Neo4j). Vector vs. graph agent memory; why similarity isn't a relationship; the hybrid vector-seed → graph-traverse pattern. Feeds [Module 3](../curriculum/03-rag-memory.md).
- [**Your Moat Is Your Data Model**](moat-is-your-data-model.md) — Mike Phipps (Gates Foundation). Modeling a domain as a graph, stitching siloed systems, serving via MCP, and the eval feedback loop. Feeds [Module 3](../curriculum/03-rag-memory.md), [Module 5](../curriculum/05-evals-observability.md), and especially [Module 7](../curriculum/07-forward-deployed.md).

> Add new write-ups here as you work through talks and papers. When a note is thorough enough that you can defend the design from it, that's a signal you've actually learned the thing.
