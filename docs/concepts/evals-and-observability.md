# Evals & Observability

How you know it works, and catch it when it stops. Mostly **`→ M5`**.

## Evaluation

- **Eval** — a repeatable test of an LLM system's quality on representative + adversarial cases. *→ M5*
- **Golden dataset / ground truth** — the reference answers you grade against. *→ M5*
- **LLM-as-judge** — using a model to grade outputs; powerful but has biases to watch. *→ M5*
- **Pass@k** — probability a correct answer appears within k tries. *→ M5*
- **Stability / consistency** — same question × N → same answer? A key reliability metric. *→ M5*
- **Faithfulness / groundedness** — does a RAG answer actually follow from the retrieved sources? *→ M5*
- **Precision / recall / F1** — standard retrieval/classification quality metrics. *→ M5*
- **Complexity tiers** — grouping eval questions by difficulty to see where a system breaks. *→ M5*
- **Offline vs online eval** — pre-deploy test suites vs production monitoring + user feedback. *→ M5*
- **A/B test** — comparing two variants on live traffic. *→ M5, M6*
- **Live-data eval** — storing the query and comparing against the live source when data changes constantly. *→ M5*
- **Regression suite** — evals that gate every prompt/model/data change. *→ M5, M6*

## Benchmarks (know the names)

- **MMLU** — broad knowledge; **GSM8K** — grade-school math; **HumanEval / MBPP** — code generation; **SWE-bench** — real GitHub issue fixing; **MMMU** — multimodal; **ARC / HellaSwag** — reasoning/commonsense. Useful signal, not a substitute for your own evals. *→ M5*

## Observability

- **Tracing** — recording each step of a multi-step run (prompts, tools, tokens, latency). *→ M5*
- **Span** — one unit of work within a trace. *→ M5*
- **Observability tools** — **LangSmith, Langfuse, Phoenix/Arize, Helicone, Braintrust** — trace, evaluate, and monitor LLM apps. *→ M5*
- **Cost / latency / token metrics** — the operational numbers you log per request. *→ M5, M6*
- **Feedback loop** — evals surface gaps → you fix data/prompts/schema → re-run. Evals drive the system, not just report on it. *→ M5, M7*
- **Human feedback / rubric** — structured human grading against explicit criteria. *→ M5*
- **Red-teaming** — deliberately trying to break the system to find failures. *→ M5, M8*
