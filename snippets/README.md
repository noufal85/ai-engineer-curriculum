# Snippets

Snippets are the smallest learning artifacts in the course. They should make one idea concrete without requiring Docker, a multi-service setup, or a large framework.

## Rules

- One file whenever possible.
- Prefer the standard library or one small dependency.
- Include comments explaining the concept, not every line of syntax.
- Print safe, useful output that helps the learner see what happened.
- Never print or commit secrets.
- Add a short “try changing this” exercise to the related curriculum page.

## Available snippets

| Snippet | Topic | Run |
|---|---|---|
| [`00-hello-env.py`](00-hello-env.py) | Environment variables and process configuration | `python snippets/00-hello-env.py` |

Snippets can grow into local labs or Dockerized builds when the concept eventually needs more structure.
