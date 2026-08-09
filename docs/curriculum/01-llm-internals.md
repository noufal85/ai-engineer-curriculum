# Module 1 · LLM Internals

## 🔨 The build

**`snippets/01-model-playground.py`** _(planned)_ — a small local script that runs the same prompt across models and sampling settings, and shows the **quality / cost / latency deltas side by side**. Docker is optional if the experiment later becomes a service.

Build it, then the sections below explain what you just watched — reference, not a lecture.

## Why it matters

You don't need to train a model, but you need a **correct mental model** of what it does — otherwise every failure looks like magic. Hallucination, context limits, cost, and latency all fall out of the internals. Understand the machine and the rest of the curriculum stops being guesswork.

## Understand in depth

- **Tokenization** — text → tokens, why token ≠ word, why this drives cost, context limits, and weird failures (counting letters, JSON escaping). Look at a real tokenizer's output.
- **Next-token prediction** — the whole model is a conditional distribution over the next token. Internalize this: it explains hallucination (a plausible token is not a true fact) and why prompting works (you're steering the distribution).
- **Attention & context, conceptually** — why the model can "see" the whole prompt, why long contexts cost quadratically-ish, and what "lost in the middle" means for how you order context.
- **Sampling** — temperature, top-p, top-k. What each knob actually does to the distribution, and when determinism (temp 0) matters vs. hurts.
- **Training stages** — pretraining → supervised fine-tuning → preference optimization (RLHF/DPO). What each stage buys, and why "it was RLHF'd to be helpful" explains a lot of model behavior.
- **Reasoning models** — how test-time compute / chain-of-thought models differ, when the extra latency/cost is worth it, and when a fast model wins.
- **The model landscape** — frontier vs. small/open models; the axes that matter (context window, cost, latency, tool-use quality, structured-output reliability). How to pick, not which is "best."
- **Why models hallucinate** — and the levers that reduce it (retrieval, constraints, tool use, evals) — the thread that runs through Modules 3–5.

## Build

- [ ] Run the same prompt across temp 0 / 0.7 / 1.2 and across a frontier + a small model; write up the quality/cost/latency deltas.
- [ ] Tokenize a document, count tokens, and estimate the cost of putting it in context vs. retrieving from it (motivates Module 3).

## Checklist

- [ ] I can explain hallucination in terms of next-token prediction
- [ ] I can predict how temperature/top-p change outputs and pick them deliberately
- [ ] I can describe what SFT and RLHF/DPO each contribute to a model's behavior
- [ ] I can choose a model for a task by cost/latency/context/tool-use, and justify it
- [ ] I know when a reasoning model earns its extra latency and when it doesn't

## Resources

- Karpathy, *"Let's build the GPT tokenizer"* and *"Intro to LLMs"* talks.
- Your provider's tokenizer playground.
- The 3Blue1Brown / Karpathy transformer explainers — for intuition, not implementation.
