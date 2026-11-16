---
title: Course plan
---

# Your AI engineering course plan

Follow six stages from a first model call to a capstone you can demonstrate and defend. The core contains nine modules, with an embeddings chapter and lab before Module 3.

**The goal:** build an AI application around a real task, connect it to useful data and tools, evaluate its behavior, and explain its reliability, security, cost, and delivery decisions. This is a course in **applied AI engineering**, focused on LLM-backed applications.

[Start the course](00-foundations.md){ .primary }

## Before you start

**What we assume:** working familiarity with programming and the software **Engineering Core** — HTTP and APIs, JSON, SQL, testing, Git, CI/CD, and basic Docker usage. You should be able to run a Python script and inspect a list or array. These software skills are prerequisites; AI concepts begin with the Foundations chapter.

Use the [Engineering core](../concepts/engineering-core.md) and [Developer environment](../concepts/developer-environment.md) glossaries when a term is unfamiliar. No advanced mathematics is required to start; the embeddings chapter introduces the vector operations used in its lab.

For the Foundations service, complete the [Setup guide](../labs/setup.md): it prepares Docker and an Anthropic API key. The Embeddings lab has separate Python setup and needs no API key or Docker; its learned examples download a model once and run locally.

## How to work through the course

1. Follow the chapters and practice links in each stage's order.
2. Read the objective, predict a result, and run the available experiment or chapter exercise.
3. Change one thing and record the result, including failures and limitations.
4. Use the stage checkpoint to explain what you learned before moving on. Keep evidence in your notes and [progress checklist](../progress.md).

**Practice available today:** two runnable labs, Foundations and Embeddings, plus the setup guide. Other core chapters include inline trials and build tasks. Their larger implementations are explicitly marked **planned**; capstones and specializations are projects for you to implement.

| Practice format | What you do | Where it is available |
|---|---|---|
| Service lab | Run an existing service, inspect its behavior, and extend it | [Foundations lab](../labs/00-foundations.md) |
| Local Python lab | Run controlled experiments and compare their results | [Embeddings lab](../labs/03-embeddings.md) |
| Inline exercise | Follow the chapter's **🧪 Lab** or trial using a chat interface, your notes, or an earlier build | LLM Internals and Modules 2–7 |
| Project brief | Implement the described system and collect your own evidence | Planned module builds, capstones, and specializations |

Use the smallest useful format: a snippet, a local experiment, or a service. A build is Dockerized only when its dependencies, service boundaries, or reproducibility justify it.

## Stage 1 · Foundations { #stage-1-foundations }

**Work through in order:**

1. [Module 0 · Foundations & Environment](00-foundations.md).
2. [Setup](../labs/setup.md), then the [Foundations lab](../labs/00-foundations.md).
3. [Module 1 · LLM Internals](01-llm-internals.md), including its small experiments.

**Topics covered:** AI, machine learning, and LLMs; training versus inference; model APIs; streaming and schema validation; tokenization, attention, sampling, context windows, training stages, reasoning, and model selection.

**Practice:** run the existing Foundations service, inspect streaming and structured output, and compare behavior after changing a model setting. Module 1 has inline experiments; its model-playground script is planned.

**Checkpoint:** explain a request from input text to model output, show a streamed response and a validated object, and record one quality/latency trade-off. Explain why fluent output can still be wrong.

## Stage 2 · Prompting { #stage-2-prompting }

**Work through:** [Module 2 · Prompting & Context Engineering](02-prompting-context.md).

**Topics covered:** roles and instructions; examples; output schemas; tool/function calling for structured output; context selection and ordering; token budgets; decomposition; prompt caching; instruction drift and injection risk.

**Practice:** use the chapter's JSON-output trial, compare repeated responses, and revisit schema validation in your Foundations service. The reliable-extractor build is planned.

**Checkpoint:** write a clear input/output contract, compare two prompt or context arrangements on the same cases, and record which outputs meet the contract. Identify what application code must validate.

## Stage 3 · Retrieval { #stage-3-retrieval }

**Work through in order:**

1. [Embeddings · From vectors to semantic search](03-embeddings.md).
2. [Embeddings lab](../labs/03-embeddings.md).
3. [Module 3 · Retrieval, RAG & Memory](03-rag-memory.md).

**Topics covered:** vectors and similarity; embedding models; text preparation, truncation, and chunking; semantic search; Recall@k and MRR@k; ingestion and metadata; lexical and hybrid retrieval; reranking and query rewriting; text-to-SQL/Cypher; graphs, memory, freshness, and permissions.

**Practice:** run all five local embedding experiments, compare retrieval configurations, and inspect missing-answer cases. Follow the RAG chapter's relationship-reasoning trial. The complete RAG/GraphRAG build is planned.

**Checkpoint:** retrieve a relevant source passage, explain a failed match, report development and held-out retrieval results separately, and describe when a relational query or explicit relationship is more useful than similarity search.

## Stage 4 · Agents { #stage-4-agents }

**Work through:** [Module 4 · Agents, Workflows, Tools & MCP](04-agents-tools-mcp.md).

**Topics covered:** tool schemas; the plan–act–observe loop; deterministic workflows versus model decisions; state, persistence, and recovery; retries, idempotency, and cancellation; MCP discovery, authentication, and authorization; budgets, stopping conditions, sandboxing, and human approval.

**Practice:** play the agent runtime by hand in the chapter's trial. Trace a proposed tool call, provide its result, and identify where the application should stop or request review. The runnable agent-and-MCP build is planned.

**Checkpoint:** draw and trace one bounded workflow, define the inputs and outputs of its tools, and explain how it handles a tool failure, repeated action, or exhausted budget.

## Stage 5 · Evaluation & production { #stage-5-evaluation-and-production }

**Work through in order:**

1. [Module 5 · Evals & Observability](05-evals-observability.md).
2. [Module 6 · Production Systems, Platform & Security](06-production-systems.md).

**Topics covered:** labeled representative and adversarial datasets; programmatic, human, and model grading; judge calibration; tracing; regression checks; latency and cost budgets; timeouts, retries, and fallbacks; caching and routing; SLOs, releases, and rollback; tenant isolation, permissions, privacy, PII, governance, and prompt-injection defenses.

**Practice:** use the paper-and-pencil evaluation trial, apply a small evaluation set to an earlier experiment, and follow the security trial in Module 6. The evaluation harness and hardened serving-layer builds are planned.

**Checkpoint:** define measurable success and a regression case for your application, identify the trace evidence needed to diagnose a failure, and write a recovery plan for a provider outage or denied data access. Record what you tested and what still needs implementation.

## Stage 6 · Delivery & capstone { #stage-6-delivery-and-capstone }

**Work through in order:**

1. [Module 7 · Forward-Deployed Craft](07-forward-deployed.md).
2. [Module 8 · Capstones](08-capstones.md), then choose one project.

**Topics covered:** customer discovery; tacit rules; domain modeling and entity relationships; source ownership; user workflows; adoption, feedback, handoff, and integrated system design.

**Practice:** conduct the discovery exercise and capture the rules behind a real workflow. Then implement a capstone: a grounded RAG assistant, bounded agent with MCP tools, GraphRAG domain twin, or cost/latency optimization project. The domain-twin module build is planned; the capstones provide briefs, acceptance criteria, and a rubric.

**Checkpoint:** demonstrate one completed project with an evaluation set, failure evidence, a design explanation, and an ownership/handoff plan. Use the [capstone definition of done and rubric](08-capstones.md) to assess the actual implementation.

## After the core · Choose a specialization

Choose a track when your capstone or work needs it. These are outlines and suggested builds, with their own data, evaluation, and operating questions.

| Track | Additional topics |
|---|---|
| [Multimodal and realtime systems](specializations.md#multimodal-and-realtime-systems) | Images, OCR, tables, image generation, speech, video, and modality-specific evaluation |
| [Model adaptation and open weights](specializations.md#model-adaptation-and-open-weights) | Dataset curation, fine-tuning, LoRA/QLoRA, distillation, quantization, licensing, and baselines |
| [Local inference and model serving](specializations.md#local-inference-and-model-serving) | Local runtimes, GPU/VRAM sizing, batching, privacy, capacity, and load testing |
| [Coding and sandboxed agents](specializations.md#coding-and-sandboxed-agents) | Repository context, restricted execution, test feedback, review, and rollback |

Deeper study of classical machine learning, mathematical optimization, or training models from scratch belongs in a separate learning track.

## Reference paths for deeper study

Use these after the core, or open an individual reference when a lesson raises a specific question. They supplement the sequence above.

- **System design:** browse the [30-study catalog](../system-design/catalog.md) by retrieval, agents, multimodal applications, serving, or operations. The catalog is unranked; choose a design relevant to your project and defend its trade-offs.
- **Papers:** follow the [paper reading paths](../papers/index.md). The LLM path connects residual networks, attention, BERT, and GPT-3; the image path connects AlexNet, ResNet, and GANs.
- **Talks and domain knowledge:** explore [talk notes](../notes/index.md), including graph memory and domain modeling, when you need a different explanation or a concrete application perspective.
- **Vocabulary and further resources:** keep the [Concepts glossary](../concepts/index.md) nearby and use [Resources](../resources.md) to extend a topic deliberately.

[Begin Stage 1](00-foundations.md){ .primary }
