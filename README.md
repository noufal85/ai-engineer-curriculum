# AI Engineer / FDE Curriculum

A self-tracked, **learn-by-doing** path to AI engineering and the forward-deployed engineer (FDE) craft. Use the lightest useful format for each topic: a snippet, a local script, a small lab, or a Dockerized application.

**📖 Site:** <https://noufal85.github.io/ai-engineer-curriculum/>

## Run the first build

```bash
cd builds/00-hello-llm
cp .env.example .env      # add your ANTHROPIC_API_KEY
docker compose up --build # open http://localhost:8000
```

## Structure

- `docs/` — the "explain" half (MkDocs Material site). Curriculum, progress tracker, talk notes.
- `snippets/` — short, dependency-light exercises for one concept at a time.
- `builds/` — larger labs and services. Docker is used when isolation, multiple services, or reproducibility make it worthwhile.
- `docs/curriculum/specializations.md` — optional multimodal, adaptation, local-inference, and coding-agent tracks.

The course assumes working familiarity with programming (HTTP, SQL, testing, Git, Docker) and basic AI concepts; the `docs/concepts/` glossary covers the vocabulary.

## Local site preview

```bash
python -m venv .venv && ./.venv/bin/pip install -r requirements.txt
./.venv/bin/mkdocs serve         # http://127.0.0.1:8000
./.venv/bin/mkdocs gh-deploy     # publish to GitHub Pages
```
