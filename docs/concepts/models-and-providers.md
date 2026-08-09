# Models & Providers

Who makes the models, how you reach them, and the model-level concepts behind them. Mostly **`→ M1`** and [M6](../curriculum/06-production-systems.md).

## Frontier / proprietary providers

- **OpenAI** — maker of the **GPT** family and the **o-series** reasoning models; the OpenAI API shape is a de-facto standard many tools mimic.
- **Anthropic** — maker of **Claude**. Model tiers: **Opus** (most capable), **Sonnet** (balanced), **Haiku** (fast/cheap), plus frontier tiers. Strong on tool use, structured output, and long context. Powers the builds in this course.
- **Google** — the **Gemini** family (e.g. Pro / Flash tiers), natively multimodal, very large context windows; served via the Gemini API and Vertex AI.
- **xAI** — the **Grok** family.
- **Cohere** — enterprise focus; notable for strong **embedding** and **reranking** models. *→ [M3](../curriculum/03-rag-memory.md)*

## Open-weights model families

Downloadable weights you can self-host or run through a provider.

- **Meta Llama** — the most widely used open-weights family; a common base for fine-tunes.
- **Mistral** — open and hosted models (incl. Mixtral, a mixture-of-experts model).
- **DeepSeek** — open models known for strong reasoning at low cost.
- **Qwen (Alibaba)** — capable open multilingual family.
- **Gemma (Google)**, **Phi (Microsoft)** — small, efficient open models.
- **Open-weights vs open-source vs proprietary** — open-weights = you get the weights (license varies); open-source = weights + data + training code; proprietary = API-only.

## Gateways, aggregators & hubs

- **OpenRouter** — a single API/endpoint that routes to hundreds of models across many providers; switch models by changing a string, with unified billing and fallbacks. *→ [M6](../curriculum/06-production-systems.md)*
- **LiteLLM** — open-source proxy/SDK that normalizes 100+ providers to one OpenAI-style API; common for model routing. *→ [M6](../curriculum/06-production-systems.md)*
- **Hugging Face** — the model & dataset **hub**, plus hosted **Inference** and the `transformers` library; where most open models live.
- **Model routing** — sending each request to the cheapest model that can handle it, escalating when needed. *→ [M6](../curriculum/06-production-systems.md)*

## Cloud model platforms

- **AWS Bedrock** — multi-provider model API on AWS (includes Claude, Llama, others).
- **Google Vertex AI** — Google Cloud's model platform (Gemini + others).
- **Azure AI Foundry / Azure OpenAI** — Microsoft's hosted OpenAI and open models.
- **Why they exist** — enterprise data residency, IAM, and billing inside an existing cloud. *→ [M6](../curriculum/06-production-systems.md)*

## Inference providers (fast/cheap hosting of open models)

- **Groq** — custom hardware (LPU) for very low-latency inference.
- **Together, Fireworks, Baseten, Replicate, Modal, Anyscale** — host open-weights models behind an API so you don't manage GPUs. *→ [M6](../curriculum/06-production-systems.md)*

## Model-level concepts

How models are made smaller, cheaper, or specialized.

- **Pretraining** — the giant self-supervised phase that produces a base model. *→ [M1](../curriculum/01-llm-internals.md)*
- **Fine-tuning (SFT)** — further training on curated examples to specialize behavior. *→ [M1](../curriculum/01-llm-internals.md)*
- **RLHF / RLAIF / DPO** — preference optimization: aligning a model to human (or AI) preferences after SFT. *→ [M1](../curriculum/01-llm-internals.md)*
- **Model distillation** — training a smaller **student** model to mimic a larger **teacher**; cheaper/faster inference for much of the quality. (Your example — very common for shipping small fast models.)
- **Quantization** — storing weights at lower precision (int8/int4; GGUF, AWQ, GPTQ) to shrink memory and speed up inference, trading a little quality. *→ [M6](../curriculum/06-production-systems.md)*
- **LoRA / QLoRA / PEFT** — parameter-efficient fine-tuning: train a few small adapter weights instead of the whole model — cheap to train and swap.
- **Mixture-of-Experts (MoE)** — only a subset of the network ("experts") runs per token; more capacity at lower inference cost.
- **Context-length extension** — techniques (e.g. RoPE scaling) to grow a model's usable context window.
- **Speculative decoding** — a small draft model proposes tokens a big model verifies, speeding generation. *→ [M6](../curriculum/06-production-systems.md)*
- **Embedding model** — a model that turns text into vectors for search (a different job than a chat model). *→ [M3](../curriculum/03-rag-memory.md)*
- **Reranker (cross-encoder)** — a model that re-scores retrieved candidates for relevance. *→ [M3](../curriculum/03-rag-memory.md)*
- **Choosing a model** — pick by context window, cost, latency, tool-use quality, and structured-output reliability — not "which is best." *→ [M1](../curriculum/01-llm-internals.md), [M6](../curriculum/06-production-systems.md)*

## Standards & interop

- **OpenAI-compatible API** — the request/response shape many providers and tools adopt so clients are swappable.
- **Model ID / alias** — the exact string that selects a model+version (e.g. a dated snapshot vs a rolling alias). Wrong string = error. *→ [M6](../curriculum/06-production-systems.md)*
- **Tokenizer differences** — the same text is a different token count per model family, so re-baseline cost/limits when you switch. *→ [M1](../curriculum/01-llm-internals.md)*
