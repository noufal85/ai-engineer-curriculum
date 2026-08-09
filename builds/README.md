# Builds

The larger, service-shaped labs in the curriculum. Use a build when the lesson benefits from a real service boundary, multiple dependencies, isolation, or a reproducible operational environment.

Short concepts should use a [snippet](../snippets/README.md) or local lab instead. Dockerized only when it adds learning value.

## Formats

- **Snippet** — one file, a few minutes, no container, and a single concept.
- **Local lab** — a small folder with a virtual environment and a repeatable local command.
- **Dockerized build** — a service or multi-component system with Docker, Compose, an operational README, and acceptance criteria.

## Conventions

- **One folder per substantial build.** Numbered folders match numbered modules: `builds/NN-name/`.
- **Dockerized only when useful.** Use Docker for service boundaries, multiple dependencies, isolation, or reproducibility.
- **Self-contained.** A Dockerized build owns its `Dockerfile`, `docker-compose.yml`, requirements, `.env.example`, and README.
- **Secrets are never committed.** Copy `.env.example` to `.env`, fill it in locally, and keep the real file ignored.
- **Every artifact has an acceptance check.** Record expected behavior, a small eval or test set, and at least one deliberate failure.

## Builds

| Track | Build | Curriculum | Format | What it teaches |
|---|---|---|---|---|
| Setup | _planned_ | [Developer Environment](../docs/curriculum/environment-and-programming.md) | Snippet/local lab | Terminal, environment variables, API keys, `.env`, and Docker configuration |
| Core | _planned_ | [Engineering Core](../docs/curriculum/engineering-core.md) | Local lab | API, database, tests, CI, and operational seams |
| 00 | [`hello-llm`](00-hello-llm/) | [0](../docs/curriculum/00-foundations.md) | Dockerized build | Streaming + schema-validated output |
| 01 | _planned_ | 1 | Snippet/local lab | Model, sampling, and cost tradeoffs |
| 02 | _planned_ | 2 | Local lab | Structured output, context, and caching |
| 03 | _planned_ | 3 | Dockerized build | Ingestion, RAG, hybrid retrieval, reranking, and GraphRAG |
| 04 | _planned_ | 4 | Local lab/service | A bounded workflow/agent + MCP server |
| 05 | _planned_ | 5 | Local lab | Eval harness, tracing, regression gates, and red-teaming |
| 06 | _planned_ | 6 | Dockerized build | Routing, fallbacks, SLOs, entitlements, and security |
| 07 | _planned_ | 7 | Dockerized build | Domain twin, discovery, adoption, and MCP delivery |
| 08 | _planned_ | 8 | Dockerized build | Capstones with production and customer-value criteria |

## Starting a new Dockerized build

Copy the shape of [`00-hello-llm`](00-hello-llm/):

```text
builds/NN-name/
  app.py (or src/)        # the thing
  Dockerfile
  docker-compose.yml
  requirements.txt
  .env.example            # variable names only; never real secrets
  README.md               # what we built, how it works, concepts, extensions
```

Then write the curriculum page: **run first, explain through the artifact, measure what changed.**
