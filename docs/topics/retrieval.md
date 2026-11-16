---
title: Retrieval & knowledge
workspace_layout: hub
hide:
  - toc
---

<div class="workspace-hub" markdown="1">

<div class="hub-intro" markdown="1">

# Retrieval & knowledge

Find useful evidence, connect it to a question, and inspect what the search missed.
{ .hub-lead }

Start with embeddings, then move to ingestion, retrieval, grounded answers, and memory. Keep the source text available while you investigate rankings.

</div>
<div class="hub-tasks" markdown="1">

[Understand embeddings](../curriculum/03-embeddings.md)
[Run the five experiments](../labs/03-embeddings.md)
[Explore RAG](../curriculum/03-rag-memory.md)

</div>
<div class="hub-grid" markdown="1">

<div class="hub-main" markdown="1">

<section class="topic-panel" markdown="1">

<div class="topic-panel-head" markdown="1">

## Understand & practice

Choose an explanation or a practical exercise below.

</div>
<div class="topic-list" markdown="1">

<div class="topic-row" markdown="1">

### [Embeddings: from vectors to semantic search](../curriculum/03-embeddings.md)

Connect vector geometry, model training, text preparation, and similarity scores to a small search system.

Explanation · Before Module 3
{ .topic-row-meta }

</div>
<div class="topic-row" markdown="1">

### [Embeddings lab](../labs/03-embeddings.md)

Run five experiments over 24 synthetic support articles: geometry, sentence pairs, search, chunking, and retrieval evaluation.

Runnable local lab · Python · No API key or Docker
{ .topic-row-meta }

</div>
<div class="topic-row" markdown="1">

### [Retrieval, RAG & memory](../curriculum/03-rag-memory.md)

Extend the picture to parsing, hybrid retrieval, reranking, structured queries, GraphRAG, and governed memory.

Chapter with exercises · Full RAG build planned
{ .topic-row-meta }

</div>

</div>

</section>
<section class="topic-panel" markdown="1">

<div class="topic-panel-head" markdown="1">

## Explore the designs

Worked architectures and trade-offs. These are reference studies, not completed implementations.

</div>
<div class="topic-list" markdown="1">

<div class="topic-row" markdown="1">

### [Search with OpenSearch](../system-design/opensearch-retrieval.md)

Combine lexical and semantic retrieval with filters and operational controls.

</div>
<div class="topic-row" markdown="1">

### [PostgreSQL and pgvector](../system-design/postgres-pgvector.md)

Decide whether relational data and vector retrieval should share a database.

</div>
<div class="topic-row" markdown="1">

### [A dedicated vector database](../system-design/vector-databases.md)

Compare filtering, update visibility, capacity, and migrations for the actual workload.

</div>
<div class="topic-row" markdown="1">

### [Managed RAG with Bedrock Knowledge Bases](../system-design/bedrock-knowledge-bases.md)

Explore a managed pipeline from ingestion to retrieved evidence and grounded answers.

</div>
<div class="topic-row" markdown="1">

### [Enterprise retrieval with Azure AI Search](../system-design/azure-ai-search.md)

Study identity, enrichment, hybrid retrieval, and evidence handling.

</div>
<div class="topic-row" markdown="1">

### [GraphRAG and connected facts](../system-design/graphrag.md)

Work through cases where explicit relationships supply evidence that similarity alone can miss.

</div>
<div class="topic-row" markdown="1">

### [Retrieval across multiple sources](../system-design/federated-retrieval.md)

Compare federated search and central indexes while retaining source permissions and freshness.

</div>
<div class="topic-row" markdown="1">

### [Long-term memory](../system-design/long-term-memory.md)

Decide what to remember, how to retrieve it, and how to correct or forget it.

</div>

</div>

</section>

</div>
<aside class="hub-side" markdown="1">

<section class="feature-box" markdown="1">

## Make meaning searchable.

Compare a question with nearby support articles, then try a question the corpus cannot answer. A nearest match is a starting point for inspection, not proof that the answer exists.

<div class="feature-actions" markdown="1">

[Try embeddings](../labs/03-embeddings.md){ .primary }
[Read the explanation](../curriculum/03-embeddings.md){ .secondary }

</div>

</section>
<section class="reference-block" markdown="1">

## Keep nearby

- [Retrieval & data glossary](../concepts/retrieval-and-data.md)
- [Evaluation & observability](../concepts/evals-and-observability.md)
- [Safety & security](../concepts/safety-and-security.md)

## Go deeper

- [Graph memory talk notes](../notes/crabrag-graph-memory.md)
- [Your moat is your data model](../notes/moat-is-your-data-model.md)
- [Multimodal retrieval](../system-design/multimodal-retrieval.md)
- [Fresh indexes with streaming data](../system-design/streaming-indexes.md)

</section>

</aside>

</div>
<div class="hub-bottom" markdown="1">

**Measure before adding more machinery.** [Explore evaluation & quality](evaluation.md) to turn retrieval failures into useful test cases.

</div>

</div>
