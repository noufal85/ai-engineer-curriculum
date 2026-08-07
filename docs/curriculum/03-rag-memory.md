# Module 3 · Retrieval, RAG & Memory

## 🔨 The build

**`builds/03-rag-lab`** _(planned)_ — ingest a corpus, build **vector RAG**, add **hybrid search + a reranker**, then build a **GraphRAG** variant over the same data. The payoff: find a **multi-hop question the vector version fails and the graph version answers** — the [CrabRAG talk](../notes/crabrag-graph-memory.md) demo, reproduced by you. Dockerized (`docker compose up`).

Build it, then the sections below explain why similarity isn't a relationship.

## Why it matters

Models don't know your data, and you can't fit everything in the context window at scale. Retrieval is how the system knows things it wasn't trained on — and getting it right (chunking, hybrid search, reranking, *when to use a graph*) is where most real-world AI quality lives.

## Understand in depth

- **Embeddings** — what they encode, how similarity (cosine/dot) works, and their limits.
- **Vector databases** — indexing (HNSW/IVF), what they're good at (fuzzy semantic recall) and bad at (precision, relationships). PGVector, LanceDB, etc.
- **Chunking** — fixed vs. semantic chunking, overlap, and why chunk boundaries make or break retrieval. Handling tables/figures (→ text).
- **Hybrid search & reranking** — combining lexical (BM25) + vector, then a reranker. Why pure vector recall is rarely enough.
- **The core limit: similarity ≠ relationship** — why vector-only retrieval hallucinates on **multi-hop** questions, and can't answer "what's connected to what." Study the [CrabRAG talk notes](../notes/crabrag-graph-memory.md) for the concrete demo.
- **GraphRAG & knowledge graphs** — nodes/edges/properties, the **hybrid pattern (vector picks seed nodes → graph traverses/ranks)**, and why it's accurate, explainable, and auditable. When the extra modeling cost is justified.
- **Agent memory** — short-term (context) vs. long-term (retrieved) memory; why "memory as a pile of markdown files" burns tokens and breaks at scale; memory as an MCP service.
- **Data modeling for retrieval** — the design that makes an FDE valuable: entities, relationships, and stitching siloed systems. See [Your Moat Is Your Data Model](../notes/moat-is-your-data-model.md).

## Build

- [ ] A baseline RAG pipeline: ingest → chunk → embed → vector search → answer, with citations.
- [ ] Add **hybrid search + a reranker**; measure retrieval quality before/after on a small eval set.
- [ ] Build a **GraphRAG** variant over the same corpus and find a **multi-hop question the vector version fails and the graph version answers** — write it up.

## Checklist

- [ ] I can explain, with an example, why vector similarity fails multi-hop questions
- [ ] I can design chunking for a messy real document (tables, figures, sections)
- [ ] I can build hybrid retrieval + reranking and show the quality gain
- [ ] I can decide vector-only vs. GraphRAG for a given problem and defend it
- [ ] I can model a domain as entities + relationships and stitch two siloed sources

## Resources

- [CrabRAG / Graph Memory](../notes/crabrag-graph-memory.md) and [Your Moat Is Your Data Model](../notes/moat-is-your-data-model.md) (talk notes in this site).
- Neo4j GraphAcademy — GraphRAG + agent-memory courses (`dev.neo4j.com/ga-rag`).
- A vector DB quickstart (PGVector or LanceDB) + a reranker (Cohere/bge).
