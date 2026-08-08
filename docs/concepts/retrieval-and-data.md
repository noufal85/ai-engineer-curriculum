# Retrieval & Data

How a system knows things it wasn't trained on. Mostly **`→ M3`**, with data-pipeline pieces in [M6](../curriculum/06-production-systems.md) and [M7](../curriculum/07-forward-deployed.md).

## Embeddings & similarity

- **Embedding** — a vector that encodes the meaning of text (or an image); similar meanings land near each other. *→ M3*
- **Embedding model** — the model that produces embeddings (separate from your chat model). *→ M3*
- **Vector** — an array of numbers; the geometric object embeddings live in.
- **Cosine similarity / dot product** — how "closeness" between two vectors is measured. *→ M3*
- **Dimensions** — the length of the vector; higher can capture more but costs more to store/search.

## Vector databases & indexing

- **Vector database** — a store built for fast nearest-neighbor search over embeddings. Examples: **pgvector, Pinecone, Weaviate, Qdrant, Milvus, Chroma, LanceDB**. *→ M3*
- **ANN (approximate nearest neighbor)** — fast, slightly-inexact vector search that makes large-scale retrieval feasible. *→ M3*
- **HNSW / IVF** — common ANN index structures (graph-based / cluster-based). *→ M3*
- **Metadata filtering** — narrowing vector search by structured fields (date, owner, type). *→ M3, M6*

## RAG & search

- **RAG (Retrieval-Augmented Generation)** — retrieve relevant context, then generate an answer grounded in it. *→ M3*
- **Chunking** — splitting documents into retrievable pieces; **overlap** and **semantic chunking** preserve meaning across boundaries. *→ M3*
- **Top-k** — how many chunks you retrieve per query. *→ M3*
- **Lexical / BM25 search** — keyword search; precise where vectors are fuzzy. *→ M3*
- **Hybrid search** — combining lexical + vector retrieval. *→ M3*
- **Reranking** — a cross-encoder re-scores retrieved candidates for relevance; usually a big quality win. *→ M3*
- **Citations / grounding** — pointing answers back at the source chunks. *→ M3*
- **Multi-hop question** — needs chaining several facts/relationships; where pure vector similarity fails. *→ M3*

## Graphs & knowledge

- **Knowledge graph** — data as **nodes** (entities), **edges** (relationships), and **properties**. *→ M3, M7*
- **GraphRAG** — retrieval that seeds with vectors, then **traverses the graph** — accurate, explainable, auditable on multi-hop questions. *→ M3, M7*
- **Similarity ≠ relationship** — the core reason vector-only RAG hallucinates on connected/multi-hop questions. *→ M3*
- **Ontology / schema** — the entity and relationship types your graph models. *→ M7*
- **Entity resolution / stitching** — merging the same real-world thing across siloed sources. *→ M7*
- **Semantic layer** — a unified, queryable model over many systems that agents reason across. *→ M7*

## Memory & pipelines

- **Agent memory** — short-term (in context) vs long-term (retrieved/persisted) knowledge across sessions. *→ M3, M4*
- **Data pipeline / ingestion (ETL)** — getting source data cleaned, chunked, and indexed. *→ M6, M7*
- **Data lakehouse** — consolidating siloed systems "under one roof" before indexing. *→ M6, M7*
- **Deduplication** — removing repeated content before it pollutes retrieval. *→ M6*
- **Point-in-time / freshness** — keeping retrieved facts current; stale indexes give wrong answers. *→ M5, M6*
- **Tacit knowledge** — the undocumented "how it's really done" you must capture to model a domain well. *→ M7*
