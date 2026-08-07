# Module 2 · Prompting & Context Engineering

## 🔨 The build

**`builds/02-reliable-extractor`** _(planned)_ — take a flaky "please return JSON" prompt and make it **reliable** with tool-calling + schema validation and a **cache-friendly** prompt layout; the app measures the failure-rate drop and the latency/cost win over 100 runs. Dockerized (`docker compose up`).

Build it, then the sections below explain the levers you pulled.

## Why it matters

The prompt *is* the program. Before you reach for fine-tuning or a bigger model, most quality problems are solved by better context engineering. This is the highest-leverage, lowest-cost skill in the whole stack.

## Understand in depth

- **Prompt anatomy** — system vs. user vs. assistant roles, instructions, context, examples, output spec. What belongs where and why.
- **Structured output** — JSON mode, schema-constrained generation, and **tool/function calling as the reliable way to get structured data**. Why "just ask for JSON" is fragile and schemas aren't.
- **Few-shot & example selection** — when examples beat instructions, how many, and how bad examples poison output.
- **Decomposition** — breaking one hard prompt into a chain of reliable steps; when to split vs. keep it in one call.
- **Context engineering** (the real discipline) — what to put in the window, in what order, and what to leave out. **"Lost in the middle,"** recency effects, and the token budget as a hard constraint. This is the through-line to RAG (Module 3) and agents (Module 4).
- **Prompt caching** — how it works, what it saves, and how to structure prompts (stable prefix first) to actually hit the cache. Directly cuts cost/latency.
- **Reasoning vs. instruction models** — how prompting differs (don't over-scaffold a reasoning model's chain of thought).
- **Failure modes** — prompt injection preview (full treatment in Module 6), instruction drift in long conversations, and over-constraining.

## Build

- [ ] Take a flaky "give me JSON" prompt and make it reliable with tool-calling + schema validation; measure the failure-rate drop over 100 runs.
- [ ] Restructure a long prompt to be **cache-friendly** (stable prefix) and measure the latency/cost change.
- [ ] Decompose a task that fails as one prompt into a 3-step chain that succeeds.

## Checklist

- [ ] I use tool-calling/schemas for structured output instead of hoping for valid JSON
- [ ] I can order context to beat "lost in the middle"
- [ ] I structure prompts to hit the prompt cache and can show the savings
- [ ] I know when to decompose a prompt vs. keep it monolithic
- [ ] I can spot and mitigate instruction drift in long conversations

## Resources

- Anthropic prompt-engineering guide + prompt-caching docs.
- OpenAI structured-outputs / function-calling docs.
- "Lost in the Middle" paper (Liu et al.) — read for the ordering intuition.
