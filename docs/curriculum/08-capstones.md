# Module 8 · Capstones

## 🔨 The builds

Each capstone is its own build under [`builds/`](https://github.com/noufal85/ai-engineer-curriculum/tree/main/builds) — Dockerized, deployed at a public URL, with an eval suite and a design doc. Pick **one or two** and go deep; a finished capstone beats ten started tutorials.

## Why it matters

Modules build skills in isolation; capstones prove you can integrate them into something that works end to end, under real constraints, with evals to back the claim. Pick **one or two** and go deep — a finished capstone is worth more than ten started tutorials.

## Understand in depth

The point of a capstone is to force the tradeoffs together: retrieval quality *and* latency *and* cost *and* evals *and* security *and* a real user. Each capstone below is scoped to exercise most of the stack.

## The capstones

### A · Grounded RAG assistant with evals
A production-shaped RAG app over a real corpus: hybrid retrieval + reranking, citations, streaming UI, an eval suite (`pass@1` + faithfulness), tracing, and per-user entitlements.

- [ ] Retrieval quality measured and improved against a baseline
- [ ] Eval suite gates every prompt/model change
- [ ] Entitlement trimming + PII masking in place
- [ ] Deployed publicly, streamed, traced

### B · Bounded agent with MCP tools
A hand-rolled agent that does real multi-step work through ≥3 tools exposed via MCP, with step limits, human-in-the-loop on irreversible actions, full tracing, and a task-success eval.

- [ ] Agent loop is bounded and fully logged
- [ ] Tools exposed via a real MCP server
- [ ] Irreversible actions gated on approval
- [ ] Task-success eval with stability measured

### C · GraphRAG domain twin (FDE capstone)
The Module 7 build, taken to production: discovery → tacit-knowledge doc → graph model (multi-lens, stitched sources) → MCP-served assistant → A/B demo vs. vector baseline → customer-language evals + feedback loop.

- [ ] Tacit-knowledge doc produced from real discovery
- [ ] Multi-hop question the graph answers and vectors don't, demonstrated
- [ ] Served into an existing surface (MCP)
- [ ] Evals in the domain owner's language, feedback loop run once

### D · Cost/latency-optimized serving layer
Take capstone A or B and make it *cheap and fast*: model routing, prompt caching, fallbacks, batching, and a load test — with a before/after report on cost, p50/p95 latency, and quality held constant.

- [ ] Model routing + caching implemented
- [ ] Fallback/degradation proven under simulated outage
- [ ] Before/after cost + latency report at equal quality

## Definition of done

- [ ] The capstone is deployed at a public URL
- [ ] It has an eval suite and a tracing dashboard
- [ ] There's a written design doc defending the key tradeoffs
- [ ] I can demo it live and explain every layer
