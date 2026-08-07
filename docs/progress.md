# Progress

One dashboard across all modules. Tick a box here when you can **explain the design tradeoff** *and* **have built the thing**. Keep it honest — this is for you.

!!! note "How tracking works"
    Edit this file, change `- [ ]` to `- [x]`, and commit with a note. Your git log becomes a dated record of how you got here. The per-module checklists hold the detailed items; this page is the high-level view.

## Builds run

A build ticks when it runs under Docker *and* you've extended it once.

- [ ] **00 · hello-llm** — streaming + schema-validated output
- [ ] 01 · model-playground — model/sampling/cost deltas _(to build)_
- [ ] 02 · reliable-extractor — schemas + caching _(to build)_
- [ ] 03 · rag-lab — RAG → hybrid → GraphRAG _(to build)_
- [ ] 04 · agent-and-mcp — bounded agent + MCP _(to build)_
- [ ] 05 · eval-harness — evals + tracing _(to build)_
- [ ] 06 · serving-layer — routing, fallbacks, entitlements _(to build)_
- [ ] 07 · domain-twin — FDE graph twin _(to build)_
- [ ] 08 · capstone(s) — end to end _(to build)_

## Module status

- [ ] **0 · Foundations** — streaming, async, schemas, deploy, cost/latency/quality
- [ ] **1 · LLM Internals** — tokenization, next-token, sampling, training stages, model choice
- [ ] **2 · Prompting & Context** — structured output, context ordering, caching, decomposition
- [ ] **3 · Retrieval, RAG & Memory** — chunking, hybrid+rerank, GraphRAG, similarity≠relationship
- [ ] **4 · Agents, Tools & MCP** — agent loop, tool schemas, MCP, human-in-the-loop
- [ ] **5 · Evals & Observability** — eval design, LLM-as-judge, stability, tracing
- [ ] **6 · Production Systems** — latency budget, fallbacks, routing, entitlements, injection defense
- [ ] **7 · Forward-Deployed Craft** — discovery, domain modeling, A/B demo, serve-where-they-are
- [ ] **8 · Capstones** — at least one shipped, evaluated, and defensible end to end

## Capstones shipped

- [ ] A · Grounded RAG assistant with evals
- [ ] B · Bounded agent with MCP tools
- [ ] C · GraphRAG domain twin (FDE)
- [ ] D · Cost/latency-optimized serving layer

## Log

Add dated entries as you go (newest first):

| Date | What | Notes |
|---|---|---|
| _2026-08-07_ | Curriculum created | Starting Module 0 |
