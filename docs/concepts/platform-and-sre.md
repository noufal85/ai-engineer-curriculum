# Platform & SRE

The operational vocabulary for keeping AI systems reliable, observable, secure, and affordable. Mostly **→ M6**, with evaluation gates in [M5](../curriculum/05-evals-observability.md).

## Reliability

- **SLO (service-level objective)** — the target reliability or latency level a service promises to achieve.
- **SLI (service-level indicator)** — the measured signal used to evaluate an SLO.
- **Error budget** — the acceptable amount of unreliability before delivery speed or change scope must slow down.
- **Backpressure** — slowing or rejecting work when downstream capacity is exhausted.
- **Graceful degradation** — providing a reduced but useful experience when a dependency fails.
- **Circuit breaker** — temporarily stopping calls to a failing dependency so the failure does not cascade.
- **Bulkhead isolation** — separating resources so one workload cannot consume everything.
- **Load test** — measuring behavior under representative traffic and concurrency.

## Delivery and operations

- **Environment promotion** — moving a tested artifact through development, staging, and production.
- **Rollback** — returning to a known-good application, prompt, model, or schema version.
- **Feature flag** — controlling a behavior without redeploying the whole application.
- **Configuration drift** — environments diverging from their declared configuration.
- **Cold start** — startup latency incurred when a service or model worker is not already running.
- **Autoscaling** — changing capacity in response to demand.
- **Disaster recovery** — restoring service and data after a major failure.

## AI operations

- **Prompt/model release artifact** — a versioned prompt, schema, model ID, or routing policy that can be evaluated and rolled back.
- **Cost budget** — a per-request, per-user, or per-workflow spend limit.
- **Semantic cache** — reusing a result for a sufficiently similar request, subject to freshness and authorization checks.
- **Model gateway** — a service that normalizes provider access, routing, fallbacks, and usage accounting.
- **Runtime policy** — the rules governing which models, tools, data, and actions a request may use.
