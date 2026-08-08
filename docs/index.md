# AI Engineer / Forward-Deployed Engineer Curriculum

A self-tracked, **build-first** path to AI engineering and the **forward-deployed engineer (FDE)** craft. The rule here is simple:

!!! quote "How this works"
    **Build first, explain second.** Every topic is anchored by a small app you actually run. You build the thing, watch it work, *then* we discuss what it does, how it works, and the concept underneath. No theory dumps — the concept is taught *through* the build.

## The three rules

1. **Everything is a build.** Each module ships a runnable app. If a concept can't be turned into something you run, it doesn't get its own page — it gets folded into a build.
2. **Every build is a repo or a module in a repo.** All the code lives in [`builds/`](https://github.com/noufal85/ai-engineer-curriculum/tree/main/builds), one self-contained folder per build.
3. **Everything is Dockerized.** `docker compose up` to run it, `docker compose down` to forget it. Build many things, keep what you like, delete the rest — your machine stays clean.

The docs on this site are the **"explain" half**: what we built, how it works, the concept. The [`builds/`](https://github.com/noufal85/ai-engineer-curriculum/tree/main/builds) folder is the **"build" half**.

Alongside the modules there's a **[Concepts](concepts/index.md)** glossary — the full vocabulary an AI engineer should know by the end (vector DBs, the model providers, OpenRouter, distillation, quantization, MCP, evals, prompt injection…), each pointing to the module where it's covered.

## Start here

**[Build 00 · hello-llm](https://github.com/noufal85/ai-engineer-curriculum/tree/main/builds/00-hello-llm)** — the smallest useful LLM service (stream a response + extract a validated object), fully Dockerized. Run it, then read [Module 0](curriculum/00-foundations.md).

```bash
git clone https://github.com/noufal85/ai-engineer-curriculum
cd ai-engineer-curriculum/builds/00-hello-llm
cp .env.example .env      # add your ANTHROPIC_API_KEY
docker compose up --build # open http://localhost:8000
```

## The two roles this targets

=== "AI Engineer"
    Builds LLM-powered products: retrieval, agents, evals, serving, cost/latency. Lives in the gap between "works in a notebook" and "works in production for real users."

=== "Forward-Deployed Engineer (FDE)"
    Embeds with a customer/domain, extracts the **tacit knowledge** of how the work actually gets done, and turns it into a deployed AI solution against messy real systems. AI engineering **plus** discovery, data modeling, and demos. See [Module 7](curriculum/07-forward-deployed.md).

Modules 0–6 are shared core; Module 7 is the FDE differentiator; Module 8 is capstones.

## How to track yourself

- Each module has a **checklist**; the [Progress](progress.md) page is the dashboard.
- A box only ticks when **the build runs** *and* you can **explain the design tradeoff**. Change `- [ ]` to `- [x]`, commit — your git history is your progress log.

## Map

| Module | Build | Concept it makes concrete |
|---|---|---|
| [0](curriculum/00-foundations.md) | hello-llm | Streaming + validated output; the cost/latency/quality knob |
| [1](curriculum/01-llm-internals.md) | model playground | What the model does, and where it breaks |
| [2](curriculum/02-prompting-context.md) | reliable extractor | Controlling the model: schemas, context, caching |
| [3](curriculum/03-rag-memory.md) | RAG → GraphRAG | Knowing things it wasn't trained on |
| [4](curriculum/04-agents-tools-mcp.md) | bounded agent + MCP | Letting the model *act*, safely |
| [5](curriculum/05-evals-observability.md) | eval harness | Knowing it works; catching regressions |
| [6](curriculum/06-production-systems.md) | serving layer | Fast, cheap, secure in production |
| [7](curriculum/07-forward-deployed.md) | domain twin | Deploying *at a customer* and making it stick |
| [8](curriculum/08-capstones.md) | capstones | The whole thing, end to end |
