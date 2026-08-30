# Engineering Core · Prerequisite Track

This unnumbered track follows [Developer Environment & Programming Basics](environment-and-programming.md) and sits before Module 0. It is the minimum software-engineering foundation needed to get value from the AI-engineering modules without treating APIs, databases, tests, and deployment as magic.

It is intentionally practical: learn each topic while building a small service, then reuse the same patterns throughout the course.

## What you will be able to do

By the end of this track, you will be able to:

- build and run a small API-backed service with a database, background job, and tests
- speak HTTP fluently: requests, status codes, timeouts, retries, and API contracts
- design a schema, write a migration, and use transactions deliberately
- ship through Git, CI/CD, and Docker with health checks and graceful shutdown
- treat model calls as unreliable network dependencies behind a small adapter boundary

## 🔨 The build

**`builds/engineering-core`** _(planned)_ — a small API-backed application with a database, background job, tests, Docker, configuration, and a CI check. The application can be simple; the point is learning the engineering seams around an AI feature.

## What it teaches

### Application development

- Python or TypeScript project structure, modules, packages, dependency management, and testing conventions.
- HTTP, REST, JSON, status codes, timeouts, retries, and API contracts.
- Configuration by environment, secrets, local development, and reproducible setup.
- Async programming, bounded concurrency, queues, and background work.

### Data and persistence

- SQL fundamentals, PostgreSQL, indexes, transactions, and migrations.
- Schema design, identifiers, timestamps, audit fields, and data ownership.
- The difference between request-time work, batch work, and event-driven work.

### Quality and delivery

- Unit tests, integration tests, fixtures, mocks, and contract tests.
- Logging, structured errors, health checks, and useful local diagnostics.
- Git branches, pull requests, CI/CD, and deployment promotion between environments.
- Docker images, Compose, readiness versus liveness, and graceful shutdown.

### AI-specific engineering habits

- Treat model calls as unreliable network dependencies.
- Record model ID, prompt version, latency, token usage, and errors.
- Keep provider-specific code behind a small adapter boundary.
- Validate every model-produced object before it reaches application logic.

## 🧪 Lab

Hands-on first: a ten-minute trial, then the build checklist.

### Trial · Watch a request fail well (~15 min)

1. Run `curl -i https://httpbin.org/status/503` and read the status line — that is what a provider outage looks like to your code.
2. In any small script, call `https://httpbin.org/delay/5` with a 2-second timeout, catch the timeout, and retry once.
3. Log the failure as one structured line: timestamp, URL, status, elapsed milliseconds. Diagnosing a request from that one line is the habit this whole track builds.

### Build checklist

- [ ] The service has a documented local setup and a reproducible Docker command.
- [ ] A database schema and migration can be created from scratch.
- [ ] Tests cover the API contract and one real database integration path.
- [ ] A background job has bounded retries and an idempotency key.
- [ ] CI runs linting, tests, and a documentation/build check.
- [ ] Health, readiness, structured logs, and graceful shutdown are demonstrated.
- [ ] The design doc explains what belongs in the request path versus a worker.

## Why this track matters

The later modules assume you can build and operate a small service. This track prevents the course from becoming a collection of isolated LLM demos and gives every later artifact a shared engineering baseline.

## Exit criteria

You are ready for Module 0 when you can explain an API request from client to database and back, write a meaningful test for it, run it in Docker, and diagnose a failed request from logs.
