# Labs

Every module has a lab. The module page explains the idea; the lab is where you run it, break it, and record what happened.

Labs are numbered to match their module — Lab 0 belongs to [Module 0 · Foundations](../curriculum/00-foundations.md) — with one unnumbered lab at the front that gets your machine ready.

| Lab | Belongs to | You will |
|---|---|---|
| [Setup](setup.md) | *before everything* | Install Docker, wire an API key, run and tear down your first container |
| [0 · Foundations](00-foundations.md) | [Module 0](../curriculum/00-foundations.md) | Poke a streaming service, break its schema, extend it with a new endpoint |
| [3 · Embeddings](03-embeddings.md) | [Embeddings chapter](../curriculum/03-embeddings.md) → [Module 3](../curriculum/03-rag-memory.md) | Run five examples: vector geometry, sentence similarity, semantic search, chunking, and retrieval evaluation |

Additional labs land as their builds are written; [`builds/`](https://github.com/noufal85/ai-engineer-curriculum/tree/main/builds) tracks what exists today.

## How a lab is shaped

- **What you will be able to do** — the lab's learning objectives, stated up front.
- **Trial** — 10–20 minutes, run it now. Often needs nothing but a chat window or one `curl`. The trial is designed to *fail* in an instructive way; that failure is the lesson.
- **Build tasks** — the substantial work, written as a checklist you can tick.
- **What to record** — labs ask for numbers, not impressions. Latency, token counts, cost, and pass rates are what make a later module's comparison meaningful.
- **Teardown** — every lab ends by stopping what it started. Leaving nine sets of containers running across a course is its own lesson in operational hygiene, and not a good one.

## Before you start

Labs assume the prerequisites in the [curriculum index](../curriculum/index.md) — HTTP, SQL, testing, Git, CI/CD, and Docker — plus an Anthropic API key. The [Setup lab](setup.md) does not teach Docker; it installs it and proves it works.

The [Embeddings lab](03-embeddings.md) is a local alternative with its own setup: the first example uses only Python, and the learned examples download a model once and run on your CPU. It requires no provider account or Docker.

Keep your lab notes in one file per module. Module 1 asks you to compare models on evidence, and evidence you did not write down at the time is not evidence.
