# AI Engineer / FDE Curriculum

A self-tracked, **build-first** path to AI engineering and the forward-deployed engineer (FDE) craft. Build a small Dockerized app for each topic, run it, then read the concept it makes concrete.

**📖 Site:** <https://noufal85.github.io/ai-engineer-curriculum/>

## Run the first build

```bash
cd builds/00-hello-llm
cp .env.example .env      # add your ANTHROPIC_API_KEY
docker compose up --build # open http://localhost:8000
```

## Structure

- `docs/` — the "explain" half (MkDocs Material site). Curriculum, progress tracker, talk notes.
- `builds/` — the "build" half. One self-contained, Dockerized folder per build.
- `docs/curriculum/engineering-core.md` — prerequisite software-engineering track before Module 0.
- `docs/curriculum/specializations.md` — optional multimodal, adaptation, local-inference, and coding-agent tracks.

## Local site preview

```bash
python -m venv .venv && ./.venv/bin/pip install -r requirements.txt
./.venv/bin/mkdocs serve         # http://127.0.0.1:8000
./.venv/bin/mkdocs gh-deploy     # publish to GitHub Pages
```
