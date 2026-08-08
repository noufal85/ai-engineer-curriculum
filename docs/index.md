# AI Engineer / Forward-Deployed Engineer Curriculum

A self-tracked, **build-first** path through AI engineering and the forward-deployed engineer (FDE) craft.

!!! quote "How this works"

    **Build first, explain second.** Every core topic is anchored to a small app you can run. You build the thing, observe where it breaks, then study the concept underneath.

## The learning path

1. **Engineering Core** — APIs, data, tests, Docker, CI, and operational habits.
2. **Shared AI-engineering core** — models, prompting, retrieval, agents, evals, and production systems.
3. **FDE craft** — discovery, tacit knowledge, domain modeling, customer delivery, and adoption.
4. **Capstones and specializations** — integrate the system end to end or go deeper in a chosen area.

## Three rules

1. **Everything important gets built.** Reference vocabulary can stay lightweight; working knowledge must have a lab.
2. **Every build is self-contained.** Code lives in [`builds/`](https://github.com/noufal85/ai-engineer-curriculum), with a README, Docker setup, acceptance criteria, and a failure case.
3. **Every claim is measured.** Track quality, latency, cost, security, and user value instead of relying on a successful demo.

## Start here

If you need the software baseline, begin with [Engineering Core](curriculum/engineering-core.md). Then run [Build 00 · hello-llm](https://github.com/noufal85/ai-engineer-curriculum/tree/main/builds/00-hello-llm) and read [Module 0 · Foundations](curriculum/00-foundations.md).

```bash
git clone https://github.com/noufal85/ai-engineer-curriculum
cd ai-engineer-curriculum/builds/00-hello-llm
cp .env.example .env      # add your provider key
docker compose up --build # open http://localhost:8000
```

## Two roles, one core

**AI Engineer** builds LLM-powered products that survive real users, real data, and real operating constraints.

**Forward-Deployed Engineer** adds customer discovery, domain modeling, tacit-knowledge capture, demos, adoption, and handoff.

Modules 0–6 are shared. Module 7 is the FDE differentiator. Module 8 proves integration. Optional specializations cover multimodal systems, model adaptation, local inference, and sandboxed coding agents.

## Track yourself

Use the [Progress](progress.md) page. A checkbox only ticks when the build runs, the required behavior is measured, and you can defend the design tradeoff.

The [Concepts](concepts/index.md) glossary is the vocabulary map; module pages and builds are where the vocabulary becomes skill.
