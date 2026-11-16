---
title: Models & foundations
workspace_layout: hub
hide:
  - toc
---

<div class="workspace-hub" markdown="1">
<div class="hub-intro" markdown="1">

# Models & foundations

Understand what a model does, make your first call, and learn to compare the results.
{ .hub-lead }

Start here if you are new to AI engineering. The course assumes working programming knowledge; the references below fill vocabulary gaps as you go.

</div>
<div class="hub-tasks" markdown="1">

[Understand an LLM](../curriculum/00-foundations.md)
[Run the first lab](../labs/00-foundations.md)
[Explore model internals](../curriculum/01-llm-internals.md)

</div>
<div class="hub-grid" markdown="1">
<div class="hub-main" markdown="1">
<section class="topic-panel" markdown="1">
<div class="topic-panel-head" markdown="1">

## Understand & practice

Build the mental model, then inspect the behavior of a small running service.

</div>
<div class="topic-list" markdown="1">
<div class="topic-row" markdown="1">

### [Foundations & environment](../curriculum/00-foundations.md)

Place AI, machine learning, and LLMs in one picture. Follow a request from your application to a model and back.

Core chapter · Module 0
{ .topic-row-meta }

</div>
<div class="topic-row" markdown="1">

### [Set up the first service](../labs/setup.md)

Prepare Docker and an Anthropic API key, run the example service, and stop it cleanly.

Setup guide · Docker and API key required
{ .topic-row-meta }

</div>
<div class="topic-row" markdown="1">

### [Foundations lab](../labs/00-foundations.md)

Watch a streamed answer, probe schema validation, and change the model. Record latency and output quality before drawing conclusions.

Runnable service lab · Complete setup first
{ .topic-row-meta }

</div>
<div class="topic-row" markdown="1">

### [LLM internals](../curriculum/01-llm-internals.md)

Connect tokens, attention, sampling, training, and reasoning to practical model choices. Try the chapter's prompt experiments as you read.

Chapter with exercises · Model-playground script planned
{ .topic-row-meta }

</div>
</div>
</section>
<section class="topic-panel" markdown="1">
<div class="topic-panel-head" markdown="1">

## Explore the designs

Use these worked examples when the model becomes one component of a larger application.

</div>
<div class="topic-list" markdown="1">
<div class="topic-row" markdown="1">

### [A multi-provider model gateway](../system-design/llm-gateway.md)

Compare routing, quotas, fallback behavior, and cost attribution across providers.

</div>
<div class="topic-row" markdown="1">

### [Self-hosted inference](../system-design/self-hosted-inference.md)

Reason about managed APIs versus owning the serving stack, capacity, and recovery work.

</div>
<div class="topic-row" markdown="1">

### [Edge and on-device AI](../system-design/edge-on-device-ai.md)

Explore local models, offline operation, synchronization, and cloud fallbacks.

</div>
</div>
</section>
</div>
<aside class="hub-side" markdown="1">
<section class="feature-box" markdown="1">

## Prefer a local experiment?

The embeddings lab starts with vector geometry using only Python. Later examples download a model and run on your CPU; no API key or Docker is needed.

<div class="feature-actions" markdown="1">

[Try embeddings](../labs/03-embeddings.md){ .primary }
[Read the explanation](../curriculum/03-embeddings.md){ .secondary }

</div>
</section>
<section class="reference-block" markdown="1">

## Keep nearby

- [Developer environment](../concepts/developer-environment.md)
- [Engineering core](../concepts/engineering-core.md)
- [Foundations glossary](../concepts/foundations.md)
- [Models & providers](../concepts/models-and-providers.md)
- [Intro to large language models](../notes/intro-to-large-language-models.md)

## Read the research

- [AlexNet](../papers/alexnet.md)
- [Residual networks](../papers/resnet.md)
- [Generative adversarial networks](../papers/generative-adversarial-networks.md)
- [Attention Is All You Need](../papers/attention-is-all-you-need.md)
- [BERT](../papers/bert.md)
- [GPT-3](../papers/gpt-3.md)

[Browse the paper reading paths](../papers/index.md)

</section>
</aside>
</div>
<div class="hub-bottom" markdown="1">

**Next, shape the request.** [Explore prompting & context](prompting.md), or follow the [complete course sequence](../curriculum/index.md).

</div>
</div>
