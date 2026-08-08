# Serving & Ops

Making it fast, cheap, and reliable in production. Mostly **`→ M6`**.

## Latency & throughput

- **Inference** — running the model to produce output. *→ M6*
- **Streaming** — emitting tokens as generated; the biggest lever on *perceived* speed. *→ M0, M6*
- **TTFT (time-to-first-token)** vs **total latency** — where the wait actually is. *→ M6*
- **Throughput (tokens/sec)** — generation speed; scales with batching and hardware. *→ M6*
- **Batching / continuous batching** — serving many requests together for GPU efficiency. *→ M6*
- **KV cache** — cached attention state that speeds up long generations. *→ M6*
- **Speculative decoding** — a draft model proposes tokens a bigger model verifies. *→ M6*

## Cost & reliability

- **Prompt / context caching** — reuse an unchanged prefix to cut cost and latency. *→ M2, M6*
- **Semantic caching** — return a cached answer for a semantically-similar past query. *→ M6*
- **Model routing** — send each request to the cheapest capable model, escalate when needed. *→ M6*
- **Fallback / graceful degradation** — retry on another model/provider when one fails. *→ M6*
- **Rate limits (RPM / TPM)** — requests- and tokens-per-minute caps; handle with backoff and queueing. *→ M0, M6*
- **Retries + exponential backoff** — the standard way to survive transient failures. *→ M0, M6*
- **Batch API** — cheaper, higher-latency processing for non-urgent bulk jobs. *→ M6*
- **Cost per token / cost control** — budgeting and capping spend (incl. runaway agents). *→ M6*
- **Idempotency** — making retried write-operations safe to repeat. *→ M0, M6*

## Self-hosting & infra

- **Inference engine** — **vLLM, TGI (Text Generation Inference), TensorRT-LLM, llama.cpp, Ollama** — software that serves models efficiently. *→ M6*
- **Quantization (serving)** — running lower-precision weights to fit cheaper GPUs and go faster. *→ M6*
- **GPU (A100 / H100), VRAM** — the hardware and memory that bound what you can serve.
- **Inference providers** — **Groq, Together, Fireworks, Replicate, Modal, Baseten** — host models so you don't manage GPUs. *→ M6*
- **Edge / on-device** — running small models locally (phone, browser, laptop) for privacy/latency.
- **Autoscaling / cold start** — scaling instances to load; the first-request delay when scaling from zero. *→ M6*

## Config & delivery

- **Prompt/version management** — treating prompts, schemas, and model IDs as versioned artifacts gated by evals. *→ M5, M6*
- **Serving surface** — meeting users where they are (Claude/ChatGPT/**MCP apps**) vs building your own UI. *→ M6, M7*
