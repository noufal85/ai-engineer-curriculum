# Module 5 · Evals & Observability

## 🔨 The build

**`builds/05-eval-harness`** _(planned)_ — an eval set (tiered by difficulty) over an earlier build, with programmatic + **LLM-as-judge** grading, **pass@1 and stability** metrics, and **tracing** that logs steps/tokens/cost/latency. Prove it by catching a regression when you change the model version. Dockerized (`docker compose up`).

Build it, then the sections below explain what the numbers mean.

## Why it matters

Without evals you're shipping vibes. LLM systems fail silently and regress when you change a prompt, a model version, or your data. Evals are how you know it works, and observability is how you catch it when it stops. This is the discipline that separates a demo from a product.

## Understand in depth

- **Why LLM testing is different** — non-determinism, no single "correct" output, and grading natural language. You can't `assertEqual` your way out.
- **Eval design** — building a dataset of representative + adversarial cases, tiered by **complexity**, sourced from real user questions and **domain owners' reporting standards** (see the [moat notes](../notes/moat-is-your-data-model.md)).
- **Grading methods** — exact/programmatic checks, **LLM-as-judge** (and its biases/failure modes), human review, and pairwise comparison. When each is trustworthy.
- **Metrics** — `pass@k`, **stability** (same question × N → same answer?), faithfulness/groundedness for RAG, task success for agents. What each actually tells you.
- **Live-data evals** — when the underlying data changes constantly, store the *query* and compare against the **live source at eval time**, not a frozen golden answer.
- **The feedback loop** — evals surface gaps/ambiguities → you fix the data model, domain rules, prompts, schema descriptions → re-run. Evals are a driver of the system, not a report at the end.
- **Observability** — tracing multi-step runs, logging prompts/tools/tokens/cost/latency per step, and alerting on regressions. Tools like LangSmith/Langfuse/Phoenix — but understand the trace model, not just the UI.
- **Offline vs. online** — pre-deploy eval suites vs. production monitoring + user feedback signals.

## Build

- [ ] An eval set (20–50 cases, tiered by difficulty) for one of your earlier builds, with a mix of programmatic + LLM-as-judge grading.
- [ ] Measure `pass@1` **and** stability; find and document a case that's "right but not what the user intended."
- [ ] Wire tracing so every agent/RAG run logs steps, tokens, cost, and latency; catch a regression by changing the model version.

## Checklist

- [ ] I can design a tiered eval set from real + adversarial cases
- [ ] I know when LLM-as-judge is trustworthy and when it isn't
- [ ] I measure stability, not just single-shot accuracy
- [ ] I can eval against live-changing data without frozen golden answers
- [ ] I have tracing that catches a regression before users do

## Resources

- Hamel Husain / Shreya Shankar writing on LLM evals (the practitioner canon).
- Langfuse / LangSmith / Phoenix docs — pick one, learn its trace model.
- OpenAI/Anthropic eval cookbooks for LLM-as-judge patterns.
