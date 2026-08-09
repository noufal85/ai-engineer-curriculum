# Serving & Ops

Making AI systems fast, cheap, reliable, and operable. Mostly **→ [M6](../curriculum/06-production-systems.md)**.

## Latency and throughput

- **Inference** — running a model to produce output. *→ [M6](../curriculum/06-production-systems.md)*
- **TTFT** versus **total latency** — time until streaming begins versus time until completion. *→ [M6](../curriculum/06-production-systems.md)*
- **Throughput** — generated tokens or completed requests per second. *→ [M6](../curriculum/06-production-systems.md)*
- **Batching / continuous batching** — serving multiple requests together for efficiency. *→ [M6](../curriculum/06-production-systems.md)*
- **KV cache** — cached attention state that speeds long generations.
- **Speculative decoding** — a draft model proposes tokens a larger model verifies. *→ [M6](../curriculum/06-production-systems.md)*
- **Attention optimizations** — Flash Attention and MQA/GQA reduce memory and compute inside the model; recognize the names when tuning a self-hosted stack.

## Cost and reliability

- **Prompt/context caching** — reusing an unchanged prefix. *→ [M2](../curriculum/02-prompting-context.md), [M6](../curriculum/06-production-systems.md)*
- **Semantic caching** — reusing a result for a sufficiently similar query, subject to freshness and authorization.
- **Model routing** — sending each request to the cheapest capable model. *→ [M6](../curriculum/06-production-systems.md)*
- **Fallback / graceful degradation** — switching to a reduced or alternate experience when a dependency fails. *→ [M6](../curriculum/06-production-systems.md)*
- **Rate limits** — requests- and tokens-per-minute caps. *→ [M6](../curriculum/06-production-systems.md)*
- **Retries + exponential backoff** — surviving transient failures within a bounded policy. *→ [Engineering Core](../curriculum/engineering-core.md), [M6](../curriculum/06-production-systems.md)*
- **Backpressure** — controlling admission when downstream capacity is exhausted. *→ [M6](../curriculum/06-production-systems.md)*
- **Circuit breaker** — temporarily stopping calls to a failing dependency.
- **Cost budget** — a per-request, per-user, or per-workflow spend limit. *→ [M6](../curriculum/06-production-systems.md)*
- **Idempotency** — making repeated writes safe. *→ [Engineering Core](../curriculum/engineering-core.md), [M6](../curriculum/06-production-systems.md)*

## Self-hosting and infrastructure

- **Inference engine** — vLLM, TGI, TensorRT-LLM, llama.cpp, or Ollama serving model weights.
- **Quantization** — lower-precision weights that reduce memory and may trade quality. *→ [M6](../curriculum/06-production-systems.md)*
- **GPU / VRAM** — hardware and memory constraints for self-hosted inference.
- **Inference provider** — a service hosting open-weight models behind an API.
- **Edge / on-device** — running a small model locally for privacy or latency.
- **Autoscaling / cold start** — changing capacity with demand and the startup delay when capacity is absent. *→ [M6](../curriculum/06-production-systems.md)*

## Configuration and delivery

- **Prompt/model release artifact** — a versioned prompt, schema, model ID, or routing policy gated by evals. *→ [M5](../curriculum/05-evals-observability.md), [M6](../curriculum/06-production-systems.md)*
- **Model gateway** — a normalization, routing, fallback, and usage-accounting layer.
- **Serving surface** — the place users access the capability: API, UI, MCP app, or existing chat. *→ [M6](../curriculum/06-production-systems.md), [M7](../curriculum/07-forward-deployed.md)*
