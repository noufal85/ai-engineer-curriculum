# Module 0 · Foundations & Environment

If HTTP, async programming, SQL, testing, or Docker are unfamiliar, complete the [Engineering Core prerequisite track](engineering-core.md) first.

## 🔨 The build

**[`builds/00-hello-llm`](https://github.com/noufal85/ai-engineer-curriculum/tree/main/builds/00-hello-llm)** — a Dockerized FastAPI service with two endpoints: one **streams** a model response token-by-token, the other returns a **schema-validated object** from free text.

```bash
cd builds/00-hello-llm
cp .env.example .env      # add ANTHROPIC_API_KEY
docker compose up --build # open http://localhost:8000
```

Run it before reading on. Every later build is a variation on these two moves.

## What we built

A ~90-line service (`app.py`) that proves out the two primitives you'll reuse everywhere:

- `POST /chat` — streams the answer as it's generated.
- `POST /extract` — forces the model to fill a Pydantic schema (`sentiment`, `topics`, `summary`, `action_required`) and validates it before returning.

The full walkthrough is in the [build's README](https://github.com/noufal85/ai-engineer-curriculum/tree/main/builds/00-hello-llm#how-it-works).

## What it teaches (the concepts, through the build)

- **Streaming is a UX decision.** `messages.stream(...)` shows the first token in ~1s instead of blocking on the full response. Changes your error handling too — you're committed once bytes start flowing.
- **Structured output beats "please return JSON."** A schema + `messages.parse(output_format=...)` gives you a validated object, not a hopeful parse of prose. This is the backbone of every reliable LLM feature: *make the model fill a schema, validate at the boundary.*
- **The cost/latency/quality triangle is a knob you can feel.** Set `MODEL=claude-haiku-4-5` in `.env` and rerun — same code, you just moved along the triangle. You'll apply this trade in every module.
- **Validation at the trust boundary.** The model's output is untrusted until it passes the schema — the cheapest reliability you'll ever buy.

## Baseline you need (learn it by hitting it in the build)

Don't pre-study these — reach for them when the build makes you:

- **HTTP & streaming** — request/response, status codes, and **SSE / chunked streaming** (that's what `/chat` is).
- **Async & bounded concurrency** — firing N calls without tripping rate limits (`asyncio.Semaphore` / `p-limit`). You'll need it the first time you batch.
- **Schemas at the boundary** — Pydantic (Py) / Zod (TS); the backbone of structured output.
- **Docker & compose** — enough to `up`/`down` a service. This whole curriculum assumes it.
- **The cost/latency/quality triangle** — the mental model behind every design choice.
- **Embeddings intuition** — what a vector *is* (dot product, cosine). Skip the proofs; you'll use this in Module 3.

## Extend the build (make it stick)

- [ ] Ran `00-hello-llm` and hit both endpoints from the browser
- [ ] Added a `/classify` endpoint returning one enum label via a strict schema
- [ ] Fired 10 `/extract` calls concurrently without tripping rate limits (bounded concurrency)
- [ ] Switched `MODEL` to Haiku and can describe the cost/latency/quality delta
- [ ] Can explain why streaming changes error handling

## Checklist

- [ ] The build runs under Docker and I've torn it down cleanly
- [ ] I can explain streaming (SSE) and why it's a UX decision
- [ ] I use a schema + validation for structured output, not string-parsing
- [ ] I can state the cost/latency/quality tradeoff for a design in one sentence
- [ ] I extended the build with at least one new endpoint

## Resources

- Anthropic API docs — the **streaming** and **structured output** sections specifically.
- Pydantic (Py) / Zod (TS) docs.
- The [build README](https://github.com/noufal85/ai-engineer-curriculum/tree/main/builds/00-hello-llm) — your model for how every module's "explain" half should read.
