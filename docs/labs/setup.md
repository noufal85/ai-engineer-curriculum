# Lab · Setup

**Goal:** Docker running on your machine, an API key wired in, one container started and cleanly removed. About 20 minutes, most of it downloading.

This lab installs tools. It does not teach Docker — the curriculum [assumes it](../curriculum/index.md), and Module 0 is where Compose becomes a lesson rather than a prerequisite. If every command below already works on your machine, skip to [Lab 0](00-foundations.md).

## 1 · Install Docker

You need the engine and the `compose` plugin. Docker Desktop bundles both.

=== "macOS"

    Download [Docker Desktop](https://www.docker.com/products/docker-desktop/) and pick the **Apple silicon** build on an M-series Mac, Intel otherwise. Open it once after installing so the engine starts.

    Prefer something lighter? [OrbStack](https://orbstack.dev/) and [Colima](https://github.com/abiosoft/colima) both provide the same `docker` and `docker compose` commands.

=== "Windows"

    Install [WSL 2](https://learn.microsoft.com/windows/wsl/install) first, then [Docker Desktop](https://www.docker.com/products/docker-desktop/) with the WSL 2 backend. Run every command in this course from your WSL shell, not PowerShell — line endings and volume mounts both behave better there.

=== "Linux"

    Follow [Docker Engine install](https://docs.docker.com/engine/install/) for your distribution, then the [post-install step](https://docs.docker.com/engine/install/linux-postinstall/) that adds your user to the `docker` group. Without it every command needs `sudo`.

!!! note "Licensing"

    Docker Desktop is free for personal use, education, and small businesses, but requires a paid subscription at larger companies. On a work machine, check before installing — OrbStack, Colima, or plain Docker Engine avoid the question.

## 2 · Prove it works

```bash
docker --version          # Docker version 27.x or newer
docker compose version    # Docker Compose version v2.x — note: no hyphen
docker run --rm hello-world
```

The third command pulls a tiny image, runs it, prints a paragraph, and deletes the container (`--rm`). If you get *"Cannot connect to the Docker daemon"*, the engine is not running — open Docker Desktop, or `sudo systemctl start docker` on Linux.

## 3 · Wire your API key

Get a key from the [Anthropic Console](https://console.anthropic.com/). Then, from the repo root:

```bash
cd builds/00-hello-llm
cp .env.example .env
```

Open `.env` and paste the key after `ANTHROPIC_API_KEY=`. Now check it without printing it to your terminal or your shell history:

```bash
grep -q '^ANTHROPIC_API_KEY=sk-' .env && echo "key present" || echo "key missing"
```

!!! danger "The one rule"

    `.env` is gitignored and stays that way. Never commit it, never paste a key into a chat or an issue, and never `echo $ANTHROPIC_API_KEY` while screen-sharing. If a key is ever exposed, revoke it in the Console — rotating is cheap, leaking is not.

## 4 · Start your first container

Still in `builds/00-hello-llm`:

```bash
docker compose up --build
```

The first run takes a few minutes: it downloads a Python base image and installs dependencies. Later runs start in seconds because those layers are cached.

When it settles, open <http://localhost:8000>. Two boxes, one streaming a response and one extracting structured data. Check the service can see your key:

```bash
curl localhost:8000/health
```

A model name in the response means the key was read. An error means `.env` is wrong — fix it and `docker compose up` again.

## 5 · Tear it down

Stop with `Ctrl-C`, then:

```bash
docker compose down          # stops and removes the container
docker compose ps            # confirms nothing is left running
```

`down` leaves the built image on disk, which is what makes the next start fast. To reclaim that space too:

```bash
docker compose down --rmi local   # also deletes the image this build made
docker system df                  # what Docker is still holding
```

Run `docker system df` now and again during the course. Images accumulate quietly, and a laptop that suddenly has no disk left is almost always Docker.

## Checklist

- [ ] `docker compose version` reports v2 or newer.
- [ ] `docker run --rm hello-world` completes without `sudo`.
- [ ] `.env` holds a working key and is not tracked by Git.
- [ ] `curl localhost:8000/health` returned a model name.
- [ ] `docker compose down` left nothing in `docker compose ps`.
- [ ] I know how to check disk usage with `docker system df`.

## When it goes wrong

| Symptom | Cause | Fix |
|---|---|---|
| `Cannot connect to the Docker daemon` | Engine not running | Open Docker Desktop; `sudo systemctl start docker` on Linux |
| `docker-compose: command not found` | Looking for the old v1 binary | Use `docker compose`, two words, no hyphen |
| `port is already allocated` | Something else holds :8000 | `lsof -i :8000`, stop it, or change the port mapping in `docker-compose.yml` |
| `permission denied` on the socket | User not in the `docker` group | Run the Linux post-install step, then log out and back in |
| Health check returns an auth error | Key missing or malformed in `.env` | Re-check step 3; the value takes no quotes and no trailing spaces |
| Build is very slow every time | Rebuilding unchanged layers | Drop `--build` unless you changed the Dockerfile or requirements |

---

Next: **[Lab 0 · Foundations](00-foundations.md)** — with the service still running, go break it.
