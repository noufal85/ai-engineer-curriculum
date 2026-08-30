# AI Engineer / Forward-Deployed Engineer Curriculum

A self-tracked, **build-first** path through AI engineering and the forward-deployed engineer (FDE) craft.

!!! quote "How this works"

    **Do the smallest useful experiment first.** Some topics use a five-line snippet, some use a local script, and some need a service or multi-component build. You run the artifact, observe where it breaks, then study the concept underneath.

## The learning path

1. **Shared AI-engineering core** — models, prompting, retrieval, agents, evals, and production systems.
2. **FDE craft** — discovery, tacit knowledge, domain modeling, customer delivery, and adoption.
3. **Capstones and specializations** — integrate the system end to end or go deeper in a chosen area.

Working familiarity with programming (HTTP, SQL, testing, Git, Docker) and basic AI concepts is assumed throughout.

## Three rules

1. **Everything important gets practiced.** Reference vocabulary can stay lightweight; working knowledge gets a snippet, lab, or build.
2. **Use the lightest format that teaches the idea.** Snippets should stay small. Docker is reserved for services, multi-component systems, isolation, and reproducibility.
3. **Every claim is measured.** Track quality, latency, cost, security, and user value instead of relying on a successful demo.

## Learning formats

| Format | Use it when | Typical shape |
|---|---|---|
| **Snippet** | One concept can be demonstrated in minutes | One file, standard library or one small dependency |
| **Local lab** | The learner needs a few files or repeated experiments | A small folder, virtual environment, and a local command |
| **Dockerized build** | The lesson needs a service boundary, multiple dependencies, or reproducibility | A self-contained folder with Docker and an operational README |

## Start here

This course assumes working familiarity with programming — HTTP, SQL, testing, Git, Docker — and basic AI concepts. Run [Build 00 · hello-llm](https://github.com/noufal85/ai-engineer-curriculum/tree/main/builds/00-hello-llm), read [Module 0 · Foundations](curriculum/00-foundations.md), and use the [Concepts](concepts/index.md) glossary to fill any vocabulary gaps.

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
