# Module 8 · Capstones

## What you will be able to do

By the end of this module, you will be able to:

- scope a capstone around a customer-value narrative and explicit acceptance criteria
- integrate the whole stack — retrieval, agents, evals, observability, and production hardening — in one system
- demonstrate quality with an eval suite and tracing rather than a one-off demo
- defend your design tradeoffs in a written design document
- present the finished system as a portfolio piece: deployment, walkthrough, and rubric self-assessment

## 🔨 Builds

Each capstone is a Dockerized build with a public or reviewable deployment, an eval suite, tracing, a design document, and a customer-value narrative. Pick one or two and go deep; a finished capstone is worth more than ten started tutorials.

## Why it matters

The modules build skills in isolation. A capstone proves you can integrate retrieval quality, latency, cost, reliability, security, evaluation, and real user value under constraints.

## Capstone options

### A · Grounded RAG assistant

Hybrid retrieval + reranking, citations, streaming UI, faithfulness and retrieval evals, tracing, PII handling, and per-user entitlements.

### B · Bounded agent and MCP tools

A hand-rolled workflow/agent performs real multi-step work through at least three MCP-exposed tools, with state, step limits, authorization, human approval, tracing, and task-success evals.

### C · GraphRAG domain twin

Discovery → tacit-knowledge document → multi-lens graph model → stitched sources → MCP-served customer-language experience → feedback loop.

### D · Cost and latency optimized serving

Take A or B and make it cheaper and faster through routing, caching, batching, fallbacks, load testing, and a before/after report at equal quality.

## Definition of done

- [ ] The system has a clear user, workflow, wedge, and acceptance criteria.
- [ ] A representative and adversarial eval suite exists and runs repeatably.
- [ ] Prompt, model, schema, data, and routing changes are versioned.
- [ ] Quality, stability, latency, cost, and security are measured.
- [ ] The deployment has auth, secrets handling, logs, traces, health checks, and a rollback path.
- [ ] The system handles at least one provider, data, tool, or permission failure safely.
- [ ] The design document defends the major architectural tradeoffs.
- [ ] The demo shows evidence, uncertainty, correction, and human handoff where relevant.
- [ ] There is an ownership, runbook, adoption, and post-launch feedback plan.

## Capstone rubric

Score each area from 0–3: 0 = absent, 1 = demonstrated locally, 2 = measured and repeatable, 3 = production-shaped and defended.

| Area | What good looks like |
|---|---|
| User value | A real workflow, clear wedge, and measurable outcome |
| Quality | Representative, adversarial, and regression-tested behavior |
| Reliability | Bounded failure modes, recovery, SLOs, and rollback |
| Security | Auth, least privilege, data protection, and abuse tests |
| Operations | Deployment, observability, cost controls, and ownership |
| Communication | Clear demo, design doc, tradeoff reasoning, and handoff |

## Resources

- Reuse the build templates and eval conventions from Modules 0–7.
- Prefer a narrow domain with realistic constraints over a generic chatbot.
