---
title: Evaluation & quality
workspace_layout: hub
hide:
  - toc
---

<div class="workspace-hub" markdown="1">

<div class="hub-intro" markdown="1">

# Evaluation & quality

Turn observations into repeatable measurements and useful failure analysis.
{ .hub-lead }

Bring a prompt, a retrieval experiment, or a small application to evaluate. Define the behavior you need before choosing a metric or grader.

</div>
<div class="hub-tasks" markdown="1">

[Design an evaluation](../curriculum/05-evals-observability.md)
[Measure semantic search](../labs/03-embeddings.md)
[Inspect the glossary](../concepts/evals-and-observability.md)

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

### [Evals & observability](../curriculum/05-evals-observability.md)

Build representative datasets, compare graders, trace failures, and turn regressions into repeatable checks. Begin with the chapter’s paper-and-pencil trial.

Chapter with exercises · Evaluation harness planned
{ .topic-row-meta }

</div>
<div class="topic-row" markdown="1">

### [Evaluate semantic search](../labs/03-embeddings.md)

Use the fifth embeddings experiment to inspect Recall@k, MRR@k, and separate no-answer probes. Freeze a configuration before testing it.

Runnable local lab · Python and a downloaded model
{ .topic-row-meta }

</div>
<div class="topic-row" markdown="1">

### [Record model behavior](../labs/00-foundations.md)

Record streaming latency and output quality when a model setting changes.

Runnable service lab · Docker and Anthropic API key
{ .topic-row-meta }

</div>
<div class="topic-row" markdown="1">

### [Understand the retrieval signal](../curriculum/03-embeddings.md)

Distinguish similarity scores from calibrated confidence and inspect the evidence behind a retrieved result.

Supporting explanation · Embeddings
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

### [An evaluation and observability platform](../system-design/evaluation-observability.md)

Connect datasets, traces, grading, human review, and release gates.

</div>
<div class="topic-row" markdown="1">

### [A feedback and model-adaptation pipeline](../system-design/feedback-model-adaptation.md)

Use observed failures to choose among prompt changes, better retrieval, and model adaptation.

</div>
<div class="topic-row" markdown="1">

### [An incident-triage copilot](../system-design/incident-triage-copilot.md)

Connect telemetry and runbooks while keeping observations distinct from authorized actions.

</div>

</div>

</section>

</div>
<aside class="hub-side" markdown="1">

<section class="feature-box" markdown="1">

## Inspect the misses first.

Pick a labeled development query from the embeddings lab. Read its relevant source article, predict the ranking, and compare the result before looking at aggregate metrics.

<div class="feature-actions" markdown="1">

[Open the embeddings lab](../labs/03-embeddings.md){ .primary }
[Read evaluation concepts](../curriculum/05-evals-observability.md){ .secondary }

</div>

</section>
<section class="reference-block" markdown="1">

## Keep nearby

- [Evals & observability glossary](../concepts/evals-and-observability.md)
- [Retrieval & data](../concepts/retrieval-and-data.md)
- [Platform & SRE](../concepts/platform-and-sre.md)

## Connect quality to value

- [Forward-deployed craft](../curriculum/07-forward-deployed.md)
- [Product & adoption](../concepts/product-and-adoption.md)
- [Your moat is your data model](../notes/moat-is-your-data-model.md)

</section>

</aside>

</div>
<div class="hub-bottom" markdown="1">

**Make the result dependable.** [Explore production & delivery](production.md) to connect your evaluation with release and operating decisions.

</div>

</div>
