# Lab 0 · Foundations

**Module:** [0 · Foundations](../curriculum/00-foundations.md) · **Needs:** [Setup](setup.md) done, `00-hello-llm` running

Two things are true about an LLM service and neither is obvious from reading about it: output arrives in pieces, and a schema is the only thing standing between a model's confidence and your database. This lab makes both concrete on a service you can break without consequence.

Start it if it is not already up:

```bash
cd builds/00-hello-llm
docker compose up --build
```

## Trial · Poke the running service (~10 min)

**1. Watch streaming happen one chunk at a time.**

```bash
curl -N -X POST localhost:8000/chat \
  -H 'content-type: application/json' \
  -d '{"message": "Explain tokens in two sentences."}'
```

The `-N` disables curl's buffering, so you see what the browser sees: text arriving progressively rather than all at once. Drop the `-N` and run it again — same response, and it feels completely different.

**2. Push three shapes of input at `/extract`.**

```bash
curl -X POST localhost:8000/extract \
  -H 'content-type: application/json' \
  -d '{"text": "The blender broke after two weeks and support never replied. I want a refund."}'
```

Then run it twice more: once with an empty string, once with a few thousand words pasted in. Watch what the schema accepts, what it rejects, and how the model fills `action_required` when the text gives it nothing to go on. An empty input still produces a confidently-shaped object — that is the behaviour the rest of the course learns to distrust.

**3. Change the model and feel the tradeoff.**

Edit `MODEL` in `.env` to a smaller model, restart with `docker compose up`, and repeat step 1. Note time to first token and whether the answer got worse in a way you'd actually notice.

## Build tasks

- [ ] Run `00-hello-llm` and hit both endpoints from the browser.
- [ ] Add a `/classify` endpoint returning one enum label via a strict schema.
- [ ] Fire 10 `/extract` calls concurrently without tripping rate limits.
- [ ] Switch `MODEL` to Haiku and describe the cost/latency/quality difference.
- [ ] Explain why streaming changes error handling.

## What to record

Keep this table in your Module 0 notes. Module 1 asks you to make a model choice on evidence, and this is the first row of it.

| Model | Prompt | Time to first token | Total latency | Output quality / 5 | Notes |
|---|---|---:|---:|---:|---|
| | | | | | |

## Acceptance

You are done when:

- [ ] `/classify` rejects an invalid label rather than passing it through.
- [ ] Your 10 concurrent calls all returned, and you can say what would have happened at 100.
- [ ] You can explain, out loud, why a streamed response makes error handling harder — what happens when the model fails after 200 bytes are already on the wire.

## Teardown

```bash
docker compose down
```

Leave the image cached; later modules reuse this service. If you want the disk back, `docker compose down --rmi local`.
