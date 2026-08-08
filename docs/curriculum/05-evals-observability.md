# Module 5 · Evals & Observability

## 🔨 The build

**`builds/05-eval-harness`** _(planned)_ — an eval set tiered by difficulty over an earlier build, with programmatic and LLM-as-judge grading, `pass@1` and stability metrics, tracing, and a CI gate. Prove it by catching a regression when you change a prompt, model, or data version.

## Why it matters

Without evals you are shipping vibes. LLM systems fail silently and regress when prompts, models, retrieval data, or tool descriptions change. Evals tell you whether the system works; observability tells you what happened when it did not.

## Understand in depth

### Dataset design

- Representative, adversarial, boundary, and abuse cases.
- Questions sourced from real user work and domain-owner reporting standards.
- Complexity tiers, expected evidence, acceptable variation, and ambiguous cases.
- Dataset versioning, provenance, privacy, and a process for adding failures.
- Live-data evals that store a query or source-of-truth computation instead of a stale golden answer.

### Grading and metrics

- Exact/programmatic checks, rubric-based human review, pairwise comparison, and LLM-as-judge.
- Judge calibration, position bias, verbosity bias, and disagreement analysis.
- Retrieval precision/recall, faithfulness, citation correctness, task success, latency, cost, and stability.
- `pass@k` versus pass rate, and why repeated sampling can hide a flaky system.

### Observability

- Traces, spans, correlation IDs, prompts, model IDs, tools, tokens, cost, latency, and errors.
- Offline evals before deployment versus online monitoring and user feedback after deployment.
- PII-safe logging, retention, sampling, dashboards, alerts, and incident links.

### Quality feedback loops

- Regression suites that gate prompt, schema, model, routing, and index changes.
- Red-teaming and failure injection as complements to ordinary eval cases.
- Turning failures into better data, domain rules, tool descriptions, prompts, or schemas.

## Build

- [ ] Build a 20–50 case eval set with representative, adversarial, and ambiguous examples.
- [ ] Version the dataset and document the source and expected behavior of each case.
- [ ] Combine programmatic grading with a calibrated LLM judge and human spot checks.
- [ ] Measure `pass@1`, stability, faithfulness, cost, and latency.
- [ ] Wire tracing so every run logs steps, tokens, cost, latency, and errors without leaking secrets.
- [ ] Add a CI command that fails when a protected metric regresses beyond a threshold.
- [ ] Catch a regression by changing the model, prompt, retrieval index, or tool schema.

## Checklist

- [ ] I can design a tiered eval set from real, adversarial, and ambiguous cases.
- [ ] I know when LLM-as-judge is trustworthy and when it is not.
- [ ] I measure stability rather than relying on a single successful run.
- [ ] I can evaluate against live-changing data without frozen golden answers.
- [ ] I have tracing that catches a regression before users do.
- [ ] I can turn a production failure into a permanent regression case.

## Resources

- Hamel Husain and Shreya Shankar on LLM evals.
- Langfuse, LangSmith, Phoenix, or another tracing system — learn its trace model.
- Provider eval cookbooks for judge calibration and rubric design.
