---
title: Prompting & context
workspace_layout: hub
hide:
  - toc
---

<div class="workspace-hub" markdown="1">

<div class="hub-intro" markdown="1">

# Prompting & context

Make the task clear, supply the right evidence, and define the output your application can use.
{ .hub-lead }

Begin with a working model call. These lessons connect prompt structure to repeatable behavior and show where validation belongs.

</div>
<div class="hub-tasks" markdown="1">

[Read the chapter](../curriculum/02-prompting-context.md)
[Practice schema validation](../labs/00-foundations.md)
[Look up a term](../concepts/prompting.md)

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

### [Prompting & context engineering](../curriculum/02-prompting-context.md)

Explore instructions, examples, structured output, context ordering, caching, and decomposition. The chapter includes a short JSON-output experiment.

Chapter with exercises · Extractor build planned
{ .topic-row-meta }

</div>
<div class="topic-row" markdown="1">

### [Test a schema boundary](../labs/00-foundations.md)

Use the existing Foundations service to probe inputs, then add a schema-constrained classification endpoint.

Runnable service lab · Docker and Anthropic API key
{ .topic-row-meta }

</div>
<div class="topic-row" markdown="1">

### [Connect prompting to model behavior](../curriculum/01-llm-internals.md)

Use sampling and model training to reason about why the same prompt can produce different results.

Supporting chapter · Module 1
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

### [Document intelligence](../system-design/document-intelligence.md)

Follow extraction, layout, validation, and human review through two document-processing designs.

</div>
<div class="topic-row" markdown="1">

### [Natural-language analytics over SQL](../system-design/natural-language-sql.md)

Explore semantic definitions, validated queries, and the boundary between a model request and database execution.

</div>
<div class="topic-row" markdown="1">

### [Caching for AI applications](../system-design/ai-caching.md)

Compare exact and semantic caches, versioning, tenant boundaries, and stale answers.

</div>

</div>

</section>

</div>
<aside class="hub-side" markdown="1">

<section class="feature-box" markdown="1">

## Try a prompt you can break.

Ask for three fields as JSON, repeat the request, and count results a downstream parser would accept. Then compare a schema-based approach. The exercise is in the chapter; the full extractor build is planned.

<div class="feature-actions" markdown="1">

[Open the chapter exercise](../curriculum/02-prompting-context.md){ .primary }

</div>

</section>
<section class="reference-block" markdown="1">

## Keep nearby

- [Prompting & context glossary](../concepts/prompting.md)
- [Safety & security](../concepts/safety-and-security.md)
- [Foundations glossary](../concepts/foundations.md)

## Go deeper

- [GPT-3 and learning from examples](../papers/gpt-3.md)
- [Intro to large language models](../notes/intro-to-large-language-models.md)
- [Optional model-adaptation track](../curriculum/specializations.md)

</section>

</aside>

</div>
<div class="hub-bottom" markdown="1">

**Need information beyond the prompt?** [Explore retrieval & knowledge](retrieval.md).

</div>

</div>
