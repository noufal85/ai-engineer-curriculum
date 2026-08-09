# Retrieval & Data

How a system knows things it was not trained on. Mostly **→ M3**, with data-pipeline pieces in [M6](../curriculum/06-production-systems.md) and [M7](../curriculum/07-forward-deployed.md).

## Embeddings and similarity

- **Embedding** — a vector that encodes the meaning of text or another modality. *→ M3*
- **Embedding model** — a model that produces embeddings, separate from a chat model. *→ M3*
- **Cosine similarity / dot product** — measures of vector closeness. *→ M3*
- **Dimensions** — the length of a vector; higher is not automatically better.

## Vector databases and indexing

- **Vector database** — a store built for nearest-neighbor search over embeddings. *→ M3*
- **ANN** — approximate nearest-neighbor search that trades a little exactness for speed. *→ M3*
- **HNSW / IVF** — common ANN index structures. *→ M3*
- **Metadata filtering** — narrowing retrieval by structured fields such as date, owner, tenant, or type. *→ M3, M6*

## RAG and search

- **RAG** — retrieve relevant context, then generate an answer grounded in it. *→ M3*
- **Chunking** — splitting documents into retrievable pieces; boundaries and overlap matter. *→ M3*
- **Top-k** — how many candidates are retrieved.
- **Text-to-SQL / text-to-Cypher (query construction)** — generating a validated database query from natural language when the answer lives in structured data. *→ M3, M7*
- **Query rewriting** — transforming a user question into a retrieval-friendly query. *→ M3*
- **Query decomposition** — splitting a multi-part question into smaller retrieval tasks. *→ M3*
- **Multi-query retrieval** — issuing several reformulations to improve recall.
- **Lexical / BM25 search** — keyword search; precise where vectors are fuzzy. *→ M3*
- **Hybrid search** — combining lexical and vector retrieval. *→ M3*
- **Reranking** — a cross-encoder re-scores candidates for relevance. *→ M3*
- **Citations / grounding** — pointing an answer back to evidence. *→ M3*
- **Multi-hop question** — a question requiring several facts or relationships. *→ M3*

## Graphs and knowledge

- **Knowledge graph** — nodes, edges, and properties representing connected data. *→ M3, M7*
- **GraphRAG** — vector-seeded retrieval followed by graph traversal. *→ M3, M7*
- **Similarity ≠ relationship** — the reason vector-only retrieval struggles with connected facts. *→ M3*
- **Ontology / schema** — entity and relationship types in a graph. *→ M7*
- **Entity resolution / stitching** — identifying the same real-world thing across sources. *→ M7*
- **Semantic layer** — a unified queryable model over several systems. *→ M7*

## Memory and pipelines

- **Agent memory** — short-term context plus persisted or retrieved knowledge across sessions. *→ M3, M4*
- **Data pipeline / ingestion** — getting source data cleaned, enriched, and indexed. *→ M3, M6, M7*
- **Data contract** — an agreement on field meaning, ownership, and change behavior. *→ Engineering Core, M6, M7*
- **Freshness / point-in-time** — whether retrieved facts match the required time. *→ M5, M6*
- **Deduplication** — removing repeated content before it pollutes retrieval. *→ M6*
- **Tacit knowledge** — undocumented rules needed to model a domain correctly. *→ M7*
