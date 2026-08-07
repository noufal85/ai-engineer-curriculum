# Module 6 · Production Systems

## 🔨 The build

**`builds/06-serving-layer`** _(planned)_ — harden an earlier build for production: **streaming, timeouts, retries, a fallback model, model routing** (cheap→expensive), **per-user entitlement trimming**, and a **prompt-injection defense**. Simulate a provider outage and show graceful degradation. Dockerized (`docker compose up`).

Build it, then the sections below explain each guardrail.

## Why it matters

"Works on my machine with one user" is not a product. Production means latency budgets, cost ceilings, rate limits, fallbacks, security, and data pipelines that don't fall over. This is the AI-engineer half of "forward-deployed" — the system has to survive contact with real load and real data.

## Understand in depth

- **Serving & latency** — streaming responses, time-to-first-token vs. total time, and where latency actually comes from (retrieval, model, tools, network). Budgeting each.
- **Cost control** — token accounting, prompt caching, model routing (small model for easy cases, escalate for hard ones), batching, and capping runaway agents.
- **Reliability** — timeouts, retries with backoff, **fallback models/providers**, graceful degradation, and idempotency for anything that writes.
- **Rate limits & quotas** — provider limits, queueing, and backpressure so a traffic spike doesn't cascade.
- **Data pipelines** — ingestion → curation → indexing; the **lakehouse / "everything under one roof"** pattern; dedup, ordering, extraction, and metadata that becomes graph properties (see the [moat notes](../notes/moat-is-your-data-model.md)).
- **Security & governance** — **prompt injection** and the untrusted-content boundary (data ≠ instructions); **PII masking**, sensitive-data classification, and **per-user entitlements / security trimming** so retrieval never returns what a user shouldn't see. This is non-negotiable, not a v2 feature.
- **Prompt/version management** — treating prompts, schemas, and model versions as versioned artifacts with CI and eval gates (ties to Module 5).
- **Deployment surface** — meeting users where they are (Claude/ChatGPT/MCP apps) vs. building your own UI; when the UI is *not* your moat.

## Build

- [ ] Add **streaming, timeouts, retries, and a fallback model** to a prior build; simulate a provider outage and show graceful degradation.
- [ ] Implement **model routing** (cheap→expensive escalation) and measure the cost drop at equal quality.
- [ ] Add **entitlement/security trimming** to your RAG so two users with different permissions get different retrievable sets.
- [ ] Write a prompt-injection test that tries to make your agent ignore its instructions via retrieved content; defend against it.

## Checklist

- [ ] I can budget and attribute end-to-end latency across retrieval/model/tools
- [ ] I implement fallbacks + graceful degradation for provider failures
- [ ] I route across models to control cost without losing quality
- [ ] I enforce PII masking and per-user entitlements in retrieval
- [ ] I can demonstrate a prompt-injection defense on untrusted content
- [ ] I version prompts/schemas/models and gate changes on evals

## Resources

- Your provider's production/best-practices + prompt-caching docs.
- OWASP Top 10 for LLM Applications (prompt injection, data leakage, etc.).
- A tracing/observability tool from Module 5, now pointed at a live service.
