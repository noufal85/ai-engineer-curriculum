# Builds

Every module in this curriculum is anchored by a **build** — a small, self-contained, Dockerized app that you run first and understand second. The docs site explains each build; the code lives here.

## Conventions

- **One folder per build**, numbered to match its module: `builds/NN-name/`.
- **Everything Dockerized.** Each build runs with `docker compose up` and stops with `docker compose down`. Build many, keep what you like, `down` and delete the rest — nothing pollutes your machine.
- **Self-contained.** Each folder has its own `Dockerfile`, `docker-compose.yml`, `requirements`, `.env.example`, and a `README.md` that explains *what we built, how it works, and the concept*.
- **Secrets never committed.** Copy `.env.example` → `.env`, fill it in; `.env` is gitignored.

## The builds

| # | Build | Module | What it teaches |
|---|---|---|---|
| 00 | [`hello-llm`](00-hello-llm/) | [0](../docs/curriculum/00-foundations.md) | Streaming + schema-validated output |
| 01 | _planned_ | 1 | Model/sampling/cost tradeoffs, hands-on |
| 02 | _planned_ | 2 | Structured output + context/caching |
| 03 | _planned_ | 3 | RAG → hybrid → GraphRAG on one corpus |
| 04 | _planned_ | 4 | A bounded agent + an MCP server |
| 05 | _planned_ | 5 | Eval harness + tracing |
| 06 | _planned_ | 6 | Routing, fallbacks, entitlements |
| 07 | _planned_ | 7 | Domain graph twin, served via MCP |
| 08 | _planned_ | 8 | Capstones |

## Starting a new build

Copy the shape of `00-hello-llm/`:

```
builds/NN-name/
  app.py (or src/)      # the thing
  Dockerfile
  docker-compose.yml
  requirements.txt
  .env.example          # ANTHROPIC_API_KEY etc. — never commit the real .env
  README.md             # what we built · how it works · the concept · extend it
```

Then write the matching module page: **build first, explain through the build.**
