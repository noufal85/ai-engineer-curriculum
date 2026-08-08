# Builds

Every curriculum module is anchored by a small, self-contained, Dockerized app. You run the build first, then read the docs to understand the design and tradeoffs.

## Conventions

- **One folder per build.** Numbered folders match numbered modules: `builds/NN-name/`.
- **Engineering Core is unnumbered.** `builds/engineering-core/` is the prerequisite track and does not change the public numbering of the existing builds.
- **Everything is Dockerized.** Each build runs with `docker compose up` and stops with `docker compose down`.
- **Self-contained.** Each folder owns its `Dockerfile`, `docker-compose.yml`, requirements, `.env.example`, and README.
- **Secrets are never committed.** Copy `.env.example` to `.env`, fill it in locally, and keep the real file ignored.
- **Every build has an acceptance test.** Record the expected behavior, a small eval or test set, and at least one deliberate failure.

## Builds

| Track | Build | Curriculum | What it teaches |
|---|---|---|---|
| Core | _planned_ | [Engineering Core](../docs/curriculum/engineering-core.md) | API, database, tests, Docker, CI, and operational seams |
| 00 | [`hello-llm`](00-hello-llm/) | [0](../docs/curriculum/00-foundations.md) | Streaming + schema-validated output |
| 01 | _planned_ | 1 | Model/sampling/cost tradeoffs, hands-on |
| 02 | _planned_ | 2 | Structured output + context/caching |
| 03 | _planned_ | 3 | Ingestion, RAG, hybrid retrieval, reranking, and GraphRAG |
| 04 | _planned_ | 4 | A bounded workflow/agent + MCP server |
| 05 | _planned_ | 5 | Eval harness, tracing, regression gates, and red-teaming |
| 06 | _planned_ | 6 | Routing, fallbacks, SLOs, entitlements, and security |
| 07 | _planned_ | 7 | Domain twin, discovery, adoption, and MCP delivery |
| 08 | _planned_ | 8 | Capstones with production and customer-value criteria |

## Starting a new build

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

Then write the curriculum page: **build first, explain through the build, measure what changed.**
