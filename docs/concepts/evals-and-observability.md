# Evals & Observability

How you know an AI system works and catch it when it stops. Mostly **→ [M5](../curriculum/05-evals-observability.md)**.

## Evaluation

- **Eval** — a repeatable test of quality on representative and adversarial cases. *→ [M5](../curriculum/05-evals-observability.md)*
- **Golden dataset / ground truth** — reference behavior or evidence used for grading. *→ [M5](../curriculum/05-evals-observability.md)*
- **Eval dataset version** — a named, reviewable snapshot of cases and expected behavior.
- **LLM-as-judge** — using a model to grade outputs; powerful but biased. *→ [M5](../curriculum/05-evals-observability.md)*
- **Judge calibration** — checking model grading against human decisions and known counterexamples.
- **Pass@k** — the chance a correct answer appears within k attempts. *→ [M5](../curriculum/05-evals-observability.md)*
- **Stability / consistency** — whether repeated runs answer the same question consistently. *→ [M5](../curriculum/05-evals-observability.md)*
- **Faithfulness / groundedness** — whether a RAG answer follows from its evidence. *→ [M5](../curriculum/05-evals-observability.md)*
- **Precision / recall / F1** — standard retrieval and classification metrics. *→ [M5](../curriculum/05-evals-observability.md)*
- **Complexity tiers** — grouping cases by difficulty. *→ [M5](../curriculum/05-evals-observability.md)*
- **Offline versus online eval** — pre-deploy suites versus production monitoring and feedback. *→ [M5](../curriculum/05-evals-observability.md)*
- **Regression suite** — evals that gate prompt, model, schema, routing, or data changes. *→ [M5](../curriculum/05-evals-observability.md), [M6](../curriculum/06-production-systems.md)*
- **Red-teaming** — deliberately trying to break the system. *→ [M5](../curriculum/05-evals-observability.md), [M8](../curriculum/08-capstones.md)*

## Benchmarks

- **MMLU**, **GSM8K**, **HumanEval / MBPP**, **SWE-bench**, **MMMU**, **ARC**, and **HellaSwag** are useful signals, not substitutes for domain evals.

## Observability

- **Trace** — a complete record of one request or workflow. *→ [M5](../curriculum/05-evals-observability.md)*
- **Span** — one unit of work within a trace. *→ [M5](../curriculum/05-evals-observability.md)*
- **Correlation ID** — an identifier connecting logs, tools, model calls, and user-visible work.
- **Cost / latency / token metrics** — operational numbers logged per request or step. *→ [M5](../curriculum/05-evals-observability.md), [M6](../curriculum/06-production-systems.md)*
- **Human rubric** — explicit criteria for structured human grading. *→ [M5](../curriculum/05-evals-observability.md)*
- **Feedback loop** — failures feed changes to data, prompts, schemas, tools, or domain rules. *→ [M5](../curriculum/05-evals-observability.md), [M7](../curriculum/07-forward-deployed.md)*
