# System Design for AI Applications

An AI application is a system of data sources, retrieval, models, tools, permissions, and feedback loops. These design studies explain how the pieces fit together, why a particular technology earns its place, and what would make us choose something else.

Read these alongside [Retrieval, RAG & Memory](../curriculum/03-rag-memory.md), [Evals & Observability](../curriculum/05-evals-observability.md), and [Production Systems](../curriculum/06-production-systems.md).

## Design studies

| Study | Applications | Decisions to practice |
|---|---|---|
| [Retrieval with Amazon OpenSearch](opensearch-retrieval.md) | Enterprise knowledge assistant; product-discovery assistant | Lexical vs. vector vs. hybrid search, AWS deployment choices, tenant isolation, freshness, ranking, sizing, and alternatives |

## How to study a design

1. State the user problem and measurable requirements before selecting infrastructure.
2. Follow one document through ingestion and one request through serving.
3. Identify the source of truth, derived indexes, and authorization boundaries.
4. Explain ranking, consistency, failure behavior, and operating cost.
5. Compare the design against a simpler alternative using the same evaluation set.
6. Change a requirement and defend how the architecture should change.

Each study is a design reference. Numerical targets are illustrative assumptions until measured; reading a chapter does not mark an implementation or lab complete.
