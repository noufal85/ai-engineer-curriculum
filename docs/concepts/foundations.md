# Foundations

Core vocabulary for how AI and large language models work. Start with [Module 0](../curriculum/00-foundations.md) for the friendly introduction, then use this page as the deeper reference. Mostly **→ [M1](../curriculum/01-llm-internals.md)**, with pieces in [M0](../curriculum/00-foundations.md).

## The ladder from AI to LLMs

- **Artificial intelligence (AI)** — the broad field of building systems that perform tasks associated with human intelligence, such as recognizing patterns, understanding language, or choosing actions. *→ [M0](../curriculum/00-foundations.md)*
- **Machine learning (ML)** — a way to build systems by learning patterns from examples instead of writing every rule by hand. *→ [M0](../curriculum/00-foundations.md)*
- **Deep learning** — machine learning using large neural networks with learned parameters. *→ [M0](../curriculum/00-foundations.md), [M1](../curriculum/01-llm-internals.md)*
- **Generative AI** — models that generate new text, code, images, audio, or video. *→ [M0](../curriculum/00-foundations.md)*
- **Foundation model** — a large pretrained model that can be adapted to many tasks. *→ [M1](../curriculum/01-llm-internals.md)*
- **LLM (Large Language Model)** — a model trained to predict the next token in text. *→ [M0](../curriculum/00-foundations.md), [M1](../curriculum/01-llm-internals.md)*
- **Inference** — using a trained model to produce an output for a new request. *→ [M0](../curriculum/00-foundations.md)*
- **Training** — adjusting model parameters using many examples. *→ [M0](../curriculum/00-foundations.md), [M1](../curriculum/01-llm-internals.md)*

## The model

- **LLM (Large Language Model)** — a neural network trained to predict the next token; the engine under every build here.
- **Transformer** — the architecture behind modern LLMs; uses *attention* to relate every token to every other. *→ [M1](../curriculum/01-llm-internals.md)*
- **Attention** — the mechanism that lets the model weigh which earlier tokens matter for the next one. *→ [M1](../curriculum/01-llm-internals.md)*
- **Parameters (weights)** — the learned numbers in the model; "7B", "70B", "405B" count them (billions). More ≈ more capable and more expensive.
- **Base model** — a raw pretrained model that just continues text. **Instruct / chat model** — a base model post-trained to follow instructions and hold a conversation. *→ [M1](../curriculum/01-llm-internals.md)*
- **Reasoning model** — a model trained to spend extra compute "thinking" before answering (test-time compute / chain-of-thought). Better on hard problems, slower and pricier. *→ [M1](../curriculum/01-llm-internals.md)*
- **Multimodal** — handles more than text: images, audio, video in and/or out.
- **Model card** — the datasheet for a model: capabilities, training data, limits, intended use.

## Tokens & context

- **Token** — the unit an LLM reads and writes; roughly ¾ of a word. Cost and limits are counted in tokens. *→ [M1](../curriculum/01-llm-internals.md)*
- **Tokenization / BPE** — splitting text into tokens (Byte-Pair Encoding is common). Explains odd failures like letter-counting. *→ [M1](../curriculum/01-llm-internals.md)*
- **Context window** — the max tokens a model can consider at once (input + output). The hard constraint behind retrieval and memory. *→ [M1](../curriculum/01-llm-internals.md), [M3](../curriculum/03-rag-memory.md)*
- **Prompt / completion tokens** — input tokens vs generated output tokens; usually priced differently.
- **Max tokens** — the cap you set on output length; hitting it truncates the response.
- **"Lost in the middle"** — models attend best to the start and end of a long context; ordering matters. *→ [M2](../curriculum/02-prompting-context.md)*

## Generation & sampling

- **Next-token prediction** — the model outputs a probability distribution over the next token; everything else follows from this. *→ [M1](../curriculum/01-llm-internals.md)*
- **Logits** — the raw pre-probability scores over the vocabulary for the next token.
- **Sampling** — how a token is picked from the distribution.
- **Temperature** — randomness knob: 0 ≈ deterministic, higher = more varied/creative. *→ [M1](../curriculum/01-llm-internals.md)*
- **Top-p (nucleus) / Top-k** — restrict sampling to the most probable tokens. *→ [M1](../curriculum/01-llm-internals.md)*
- **Repetition / frequency penalties** — knobs that discourage repeating tokens; useful when generations loop.
- **Greedy / deterministic decoding** — always take the most likely token; note it still isn't bit-for-bit reproducible.
- **Stop sequence** — a string that ends generation when produced.
- **Streaming** — sending tokens as they're generated instead of all at once. *→ [M0](../curriculum/00-foundations.md), [M6](../curriculum/06-production-systems.md)*

## Behavior & limits

- **Hallucination** — a fluent, confident, wrong output; a direct consequence of next-token prediction. *→ [M1](../curriculum/01-llm-internals.md), [M3](../curriculum/03-rag-memory.md), [M5](../curriculum/05-evals-observability.md)*
- **Grounding** — tying answers to provided/retrieved sources to reduce hallucination. *→ [M3](../curriculum/03-rag-memory.md)*
- **In-context learning** — the model "learns" a task from examples in the prompt, without weight updates. *→ [M2](../curriculum/02-prompting-context.md)*
- **Zero-shot / one-shot / few-shot** — zero, one, or several examples given in the prompt. *→ [M2](../curriculum/02-prompting-context.md)*
- **Chain-of-thought (CoT)** — prompting or training the model to reason step-by-step before answering. *→ [M1](../curriculum/01-llm-internals.md), [M2](../curriculum/02-prompting-context.md)*
- **Knowledge cutoff** — the date the training data ends; the model doesn't know newer facts without retrieval/tools. *→ [M3](../curriculum/03-rag-memory.md), [M4](../curriculum/04-agents-tools-mcp.md)*

## Cost, latency, quality

- **Cost/latency/quality triangle** — the recurring trade: you optimize two, every design picks a corner. *→ [M0](../curriculum/00-foundations.md), [M6](../curriculum/06-production-systems.md)*
- **TTFT (time-to-first-token)** — how long until streaming starts; a big part of perceived speed. *→ [M6](../curriculum/06-production-systems.md)*
- **Throughput** — tokens generated per second. *→ [M6](../curriculum/06-production-systems.md)*
- **Token accounting** — counting/estimating tokens to predict cost and stay under limits. *→ [M6](../curriculum/06-production-systems.md)*
