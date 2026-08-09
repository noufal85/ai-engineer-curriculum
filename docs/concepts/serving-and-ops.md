# Serving & Ops

Making AI systems fast, cheap, reliable, and operable. Mostly **→ M6**.

## Latency and throughput

- **Inference** — running a model to produce output. *→ M6*
- **TTFT** versus **total latency** — time until streaming begins versus time until completion. *→ M6*
- **Throughput** — generated tokens or completed requests per second. *→ M6*
- **Batching / continuous batching** — serving multiple requests together for efficiency. *→ M6*
- **KV cache** — cached attention state that speeds long generations.
- **Speculative decoding** — a draft model proposes tokens a larger model verifies. *→ M6*
- **Attention optimizations** — Flash Attention and MQA/GQA reduce memory and compute inside the model; recognize the names when tuning a self-hosted stack.

## Cost and reliability

- **Prompt/context caching** — reusing an unchanged prefix. *→ M2, M6*
- **Semantic caching** — reusing a result for a sufficiently similar query, subject to freshness and authorization.
- **Model routing** — sending each request to the cheapest capable model. *→ M6*
- **Fallback / graceful degradation** — switching to a reduced or alternate experience when a dependency fails. *→ M6*
- **Rate limits** — requests- and tokens-per-minute caps. *→ M6*
- **Retries + exponential backoff** — surviving transient failures within a bounded policy. *→ Engineering Core, M6*
- **Backpressure** — controlling admission when downstream capacity is exhausted. *→ M6*
- **Circuit breaker** — temporarily stopping calls to a failing dependency.
- **Cost budget** — a per-request, per-user, or per-workflow spend limit. *→ M6*
- **Idempotency** — making repeated writes safe. *→ Engineering Core, M6*

## Self-hosting and infrastructure

- **Inference engine** — vLLM, TGI, TensorRT-LLM, llama.cpp, or Ollama serving model weights.
- **Quantization** — lower-precision weights that reduce memory and may trade quality. *→ M6*
- **GPU / VRAM** — hardware and memory constraints for self-hosted inference.
- **Inference provider** — a service hosting open-weight models behind an API.
- **Edge / on-device** — running a small model locally for privacy or latency.
- **Autoscaling / cold start** — changing capacity with demand and the startup delay when capacity is absent. *→ M6*

## Configuration and delivery

- **Prompt/model release artifact** — a versioned prompt, schema, model ID, or routing policy gated by evals. *→ M5, M6*
- **Model gateway** — a normalization, routing, fallback, and usage-accounting layer.
- **Serving surface** — the place users access the capability: API, UI, MCP app, or existing chat. *→ M6, M7*
