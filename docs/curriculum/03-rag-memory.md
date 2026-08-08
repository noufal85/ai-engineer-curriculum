# Module 3 · Retrieval, RAG & Memory

## 🔨 The build

**`builds/03-rag-lab`** _(planned)_ — ingest a corpus, parse and enrich it, build **vector RAG**, add **hybrid search + a reranker**, then build a **GraphRAG** variant over the same data. The payoff: find a multi-hop question the vector version fails and the graph version answers. Dockerized with a reproducible corpus and eval set.

Build it, then the sections below explain why similarity is not a relationship.

## Why it matters

Models do not know your private data, and you cannot fit everything into the context window at scale. Retrieval is how a system knows things it was not trained on. In practice, most RAG quality problems originate before generation: poor parsing, weak metadata, stale indexes, missing permissions, bad chunk boundaries, or a query that was never formulated correctly.

## Understand in depth

### Ingestion and document quality

- Connectors, ETL/ELT, incremental ingestion, and source ownership.
- PDF, HTML, table, figure, and OCR extraction.
- Fixed, semantic, structure-aware, and parent-child chunking.
- Metadata, document versions, deduplication, freshness, and point-in-time behavior.
- Data contracts and schema evolution for indexes.

### Retrieval and query planning

- Embeddings, cosine/dot-product similarity, vector databases, ANN, HNSW, and IVF.
- Metadata filtering, lexical/BM25 search, hybrid retrieval, and reranking.
- Query rewriting, query decomposition, multi-query retrieval, and hypothetical-document techniques.
- Top-k selection, context budgets, citation assembly, and query-specific retrieval policies.
- Retrieval quality versus answer quality: measure the retriever before blaming the model.

### Graphs and relationships

- Nodes, edges, properties, ontologies, entity resolution, and semantic layers.
- Why similarity is not a relationship and where vector-only retrieval fails.
- The hybrid pattern: vector search selects seed nodes, then graph traversal supplies related evidence.
- When GraphRAG is justified and when a relational database, metadata filter, or hybrid index is simpler and better.

### Memory

- Short-term context, session state, user preferences, and long-term retrieved memory.
- Memory write policies, forgetting, correction, provenance, and privacy.
- Why a pile of markdown files becomes expensive and difficult to govern at scale.
- Memory as a service exposed through a stable API or MCP server.

## Build

- [ ] Ingest a small corpus with source IDs, timestamps, permissions, and version metadata.
- [ ] Build baseline RAG: ingest → chunk → embed → vector search → answer with citations.
- [ ] Add hybrid search, metadata filters, and a reranker; measure retrieval quality before and after.
- [ ] Add query rewriting or decomposition and show one case where it changes retrieval.
- [ ] Build a GraphRAG variant over the same corpus and find a multi-hop question the vector version misses.
- [ ] Add a stale-document or permission test and prove the system handles it.

## Checklist

- [ ] I can explain, with an example, why vector similarity fails multi-hop questions.
- [ ] I can design chunking and parsing for a messy document with tables or figures.
- [ ] I can build hybrid retrieval + reranking and show the quality gain.
- [ ] I can separate ingestion, retrieval, generation, and citation failures.
- [ ] I can decide vector-only, hybrid, relational, or GraphRAG for a problem and defend it.
- [ ] I can model a domain as entities + relationships and stitch two siloed sources.
- [ ] I can enforce freshness and authorization metadata at retrieval time.

## Resources

- [CrabRAG / Graph Memory](../notes/crabrag-graph-memory.md) and [Your Moat Is Your Data Model](../notes/moat-is-your-data-model.md).
- Neo4j GraphAcademy — GraphRAG, graph modeling, and agent-memory courses.
- A vector DB quickstart such as PGVector or LanceDB plus a reranker.
