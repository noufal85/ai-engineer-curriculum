# Build 00 · hello-llm

The smallest LLM service worth running: **stream a response** and **extract a validated object from text**. Many later artifacts are variations on these two moves; simpler concepts may stay as snippets or local experiments.

## Run it

New to API keys or environment variables? Read [Developer Environment & Programming Basics](../../docs/curriculum/environment-and-programming.md) first. It explains `.env`, shell variables, Docker Compose, and how to check a key without printing it.

```bash
cp .env.example .env      # then paste your ANTHROPIC_API_KEY into .env
docker compose up --build
```

Open <http://localhost:8000> — a tiny page with two boxes to try both endpoints. Tear it down with `docker compose down`. This service is Dockerized because it has a network boundary and a repeatable runtime; simpler lessons do not need the same setup.

Prefer curl:

```bash
# streaming chat
curl -N localhost:8000/chat -H 'content-type: application/json' \
  -d '{"message":"Explain embeddings in two sentences."}'

# schema-validated extraction
curl localhost:8000/extract -H 'content-type: application/json' \
  -d '{"text":"The dashboard is fast but login keeps timing out and support went quiet."}'
```

## What we built

A FastAPI service (`app.py`, ~90 lines) with three endpoints:

| Endpoint | Does | Teaches |
|---|---|---|
| `POST /chat` | Streams the model's answer token-by-token | **Streaming** — why chat UIs feel instant |
| `POST /extract` | Returns a validated `Analysis` object from free text | **Structured output** — turning text into data you can trust |
| `GET /health` | Liveness + which model is wired | The smallest ops surface |

## How it works

**Streaming** (`/chat`). `client.messages.stream(...)` yields text chunks as the model generates them; FastAPI's `StreamingResponse` forwards each chunk to the browser, which appends it to the page. First token shows in ~1s instead of waiting for the full answer. This is the difference between a UI that feels fast and one that feels broken.

**Structured output** (`/extract`). We define the output as a Pydantic model (`Analysis`: sentiment, topics, summary, action_required) and pass it to `client.messages.parse(output_format=Analysis)`. The model is *constrained* to that schema and the SDK validates the result before we return it — so downstream code gets a real typed object, never a hopeful `json.loads()` of a string that might be prose. This one pattern is the backbone of every reliable LLM feature: **make the model fill a schema, validate at the boundary.**

**The model is a knob.** `MODEL` defaults to `claude-opus-4-8` (best quality); set `MODEL=claude-haiku-4-5` in `.env` for cheap, fast iteration while you're learning. Same code — you just moved along the cost/latency/quality triangle. That triangle is [Module 1](../../docs/curriculum/01-llm-internals.md)'s whole point, and you can now feel it by editing one line.

## Concepts this build makes concrete

- **Streaming** and why it's a UX decision, not a nicety.
- **Structured output via schema** as the reliable alternative to "please return JSON."
- **The cost/latency/quality knob** — one env var moves you along it.
- **Validation at the trust boundary** — the model's output is untrusted until it passes the schema.

Ties to [Module 0 · Foundations](../../docs/curriculum/00-foundations.md).

## Extend it (make the concept stick)

- [ ] Add a `/classify` endpoint that returns one enum label via a strict schema.
- [ ] Add bounded concurrency: fire 10 `/extract` calls in parallel without tripping rate limits.
- [ ] Log tokens + latency per request (the first inch of [Module 5 · Evals & Observability](../../docs/curriculum/05-evals-observability.md)).
- [ ] Make `/chat` keep short conversation history (send prior turns back each call).
