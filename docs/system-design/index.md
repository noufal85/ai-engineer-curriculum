# System Design for AI Applications

An AI application is a system of data sources, retrieval, models, tools, permissions, and feedback loops. These design studies explain how the pieces fit together, why a particular technology earns its place, and what would make us choose something else.

Read these alongside [Retrieval, RAG & Memory](../curriculum/03-rag-memory.md), [Evals & Observability](../curriculum/05-evals-observability.md), and [Production Systems](../curriculum/06-production-systems.md).

## Design studies

Browse the [complete design-study catalog](catalog.md) for 30 researched studies. The collection remains unranked: choose what to study or implement based on your interests. Each chapter includes technology fundamentals, trade-offs, alternatives, two worked designs, and source references.

| Area | Studies | Topics |
|---|---|---|
| [Retrieval, search, and knowledge](catalog.md#retrieval-search-and-knowledge) | R01–R08 | OpenSearch, pgvector, vector databases, managed RAG, Azure AI Search, graphs, federation, memory |
| [Agents, workflows, and tools](catalog.md#agents-workflows-and-tools) | A01–A07 | Durable workflows, tool agents, MCP, SQL, coding sandboxes, browsers, coordination |
| [Documents, audio, and multimodal applications](catalog.md#documents-audio-and-multimodal-applications) | D01–D05 | Document extraction, multimodal retrieval, voice, meetings, video |
| [Model serving and inference](catalog.md#model-serving-and-inference) | S01–S05 | Model gateways, GPU serving, batch processing, caching, edge inference |
| [Data pipelines, evaluation, and operations](catalog.md#data-pipelines-evaluation-and-operations) | P01–P05 | Streaming indexes, evaluations, adaptation, tenant isolation, incident triage |

Start with [Retrieval with Amazon OpenSearch](opensearch-retrieval.md) for the reference format, or select any chapter from the catalog.

## How to study a design

1. State the user problem and measurable requirements before selecting infrastructure.
2. Follow one document through ingestion and one request through serving.
3. Identify the source of truth, derived indexes, and authorization boundaries.
4. Explain ranking, consistency, failure behavior, and operating cost.
5. Compare the design against a simpler alternative using the same evaluation set.
6. Change a requirement and defend how the architecture should change.

Each study is a design reference. Numerical targets are illustrative assumptions until measured; reading a chapter does not mark an implementation or lab complete.
