# Module 2 · Prompting & Context Engineering

## What you will be able to do

By the end of this module, you will be able to:

- structure a prompt deliberately: roles, instructions, context, examples, output spec
- get reliable structured output with tool calling and schemas instead of hoping for valid JSON
- order context to beat "lost in the middle" and stay inside a token budget
- lay out prompts to hit the prompt cache and show the cost and latency savings
- decide when to decompose a task into a chain of calls versus keep it in one
- spot instruction drift and prompt-injection risk before they ship

## 🔨 The build

**`builds/02-reliable-extractor`** _(planned)_ — take a flaky "please return JSON" prompt and make it **reliable** with tool-calling + schema validation and a **cache-friendly** prompt layout; the local lab measures the failure-rate drop and the latency/cost win over 100 runs. Dockerize it only if the experiment becomes a reusable service.

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

## 🧪 Lab

Hands-on first: a trial you can run right now with nothing but a chat UI or API key, then the build tasks.

### Trial · Break "just return JSON" (~15 min)

1. Run this prompt 10 times (chat UI or a 5-line API script):

    ```text
    Extract the customer name, product, and complaint from this email as JSON:

    "Hi, I bought the AcmePro blender three weeks ago and the lid cracked.
    Please sort this out. — Dana Whitfield"
    ```

2. Count how many of the 10 outputs a downstream parser would accept. A prose preamble ("Here is the JSON..."), a markdown fence, or a renamed key all count as failures.
3. Define the same three fields as a tool/function schema (or strict JSON mode) and run 10 more. Compare failure counts — that gap is the module's core lesson.
4. Lost in the middle: bury one critical instruction ("respond in French") in the middle of a ~30-line prompt, then move it to the end. Compare compliance.

### Build tasks

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
