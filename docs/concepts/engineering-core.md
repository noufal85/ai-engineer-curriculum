# Engineering Core

The software-engineering vocabulary that makes AI systems deployable. Assumed background for the curriculum, with AI-specific applications repeated throughout Modules 0–6.

## Application foundations

- **API contract** — the documented input, output, and error behavior between components.
- **HTTP status code** — the protocol-level signal describing request success or failure.
- **Timeout** — a bound on how long a dependency may block a request.
- **Retry** — repeating a failed operation when the failure may be transient; retries need limits and idempotency.
- **Idempotency** — making a repeated request produce the same intended effect as one request.
- **Async / concurrency** — overlapping independent work without creating unbounded load.
- **Queue / worker** — moving slow or retryable work out of the user-facing request path.

## Data and persistence

- **Transaction** — an atomic unit of database work.
- **Migration** — a versioned change to a database schema.
- **Index** — a data structure that speeds up lookup at storage and write cost.
- **Data contract** — an agreement on fields, semantics, ownership, and change behavior between systems.
- **Audit field** — metadata such as creator, updater, source, or timestamp that makes data traceable.

## Quality and delivery

- **Unit test** — a focused test of a small unit of behavior.
- **Integration test** — a test across real component boundaries, such as an API and database.
- **Contract test** — a test that verifies two systems still agree on an interface.
- **Fixture** — controlled test data used to make behavior reproducible.
- **CI/CD** — automated validation and delivery of changes.
- **Liveness** — whether a process is running; **readiness** — whether it can safely receive work.
- **Structured logging** — machine-readable logs with stable fields for search and analysis.
- **Provider adapter** — a small boundary that hides model-provider-specific API details.
