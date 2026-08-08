# Evals & Observability

How you know an AI system works and catch it when it stops. Mostly **→ M5**.

## Evaluation

- **Eval** — a repeatable test of quality on representative and adversarial cases. *→ M5*
- **Golden dataset / ground truth** — reference behavior or evidence used for grading. *→ M5*
- **Eval dataset version** — a named, reviewable snapshot of cases and expected behavior.
- **LLM-as-judge** — using a model to grade outputs; powerful but biased. *→ M5*
- **Judge calibration** — checking model grading against human decisions and known counterexamples.
- **Pass@k** — the chance a correct answer appears within k attempts. *→ M5*
- **Stability / consistency** — whether repeated runs answer the same question consistently. *→ M5*
- **Faithfulness / groundedness** — whether a RAG answer follows from its evidence. *→ M5*
- **Precision / recall / F1** — standard retrieval and classification metrics. *→ M5*
- **Complexity tiers** — grouping cases by difficulty. *→ M5*
- **Offline versus online eval** — pre-deploy suites versus production monitoring and feedback. *→ M5*
- **Regression suite** — evals that gate prompt, model, schema, routing, or data changes. *→ M5, M6*
- **Red-teaming** — deliberately trying to break the system. *→ M5, M8*

## Benchmarks

- **MMLU**, **GSM8K**, **HumanEval / MBPP**, **SWE-bench**, **MMMU**, **ARC**, and **HellaSwag** are useful signals, not substitutes for domain evals.

## Observability

- **Trace** — a complete record of one request or workflow. *→ M5*
- **Span** — one unit of work within a trace. *→ M5*
- **Correlation ID** — an identifier connecting logs, tools, model calls, and user-visible work.
- **Cost / latency / token metrics** — operational numbers logged per request or step. *→ M5, M6*
- **Human rubric** — explicit criteria for structured human grading. *→ M5*
- **Feedback loop** — failures feed changes to data, prompts, schemas, tools, or domain rules. *→ M5, M7*
