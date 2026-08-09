# Developer Environment & Programming Basics

Start here if words like **terminal**, **process**, **PATH**, **environment variable**, or **API key** are new to you. You do not need to become a software engineer before starting the AI modules. You do need a small mental model of how programs run and how they receive configuration.

This section is deliberately gentle and practical. Copy the commands, run them, and change one thing at a time.

## What you will be able to do

By the end, you should be able to:

- Open a terminal and move around the filesystem.
- Explain the difference between a program, a process, the operating system, and a container.
- Install a language runtime and a project dependency without changing the whole computer accidentally.
- Set an API key as an environment variable for one command, one terminal session, or a project.
- Check whether a variable exists without printing the secret.
- Explain why secrets should not be hard-coded or committed to Git.
- Start a Dockerized build and understand how its variables reach the application.

## The small mental model

- **Operating system** — manages files, programs, memory, networking, and permissions.
- **Program** — instructions stored on disk, such as Python or Docker Compose.
- **Process** — a running instance of a program with its own environment and resources.
- **Terminal** — a text interface for asking the operating system to run commands.
- **Shell** — the program inside the terminal that interprets commands; common shells include zsh, bash, and PowerShell.
- **Directory / path** — a folder and the address used to locate it.
- **Port** — a numbered doorway through which a network service accepts connections, such as `localhost:8000`.
- **Dependency** — code or software your project relies on.
- **Container** — an isolated process with its own filesystem, dependencies, and environment settings.

The important connection is:

```text
terminal → shell → process → program → operating system / network / files
```

## Environment variables

An **environment variable** is a named value attached to a process when it starts. Programs use these values for configuration that should change between machines or environments.

Examples:

```text
ANTHROPIC_API_KEY=your-secret-key
MODEL=claude-haiku-4-5
PORT=8000
```

The program reads them at runtime instead of having configuration hard-coded into the source code:

```python
import os

api_key = os.environ.get("ANTHROPIC_API_KEY")
model = os.environ.get("MODEL", "claude-opus-4-8")
```

This gives us three benefits:

1. **Security** — the secret does not need to live in source code.
2. **Portability** — the same code can run locally, in Docker, CI, or production with different settings.
3. **Changeability** — you can switch a model or port without editing application code.

An environment variable is not automatically global. It belongs to a process and is normally inherited by child processes. That is why a variable set in one terminal may not exist in another terminal or inside Docker unless you pass it through.

## Three places to put configuration

| Location | Scope | Good for |
|---|---|---|
| One command | One process | A quick test |
| Shell profile | Your user account and future terminals | Personal local development |
| Project `.env` file | One project, when explicitly loaded | Repeatable local projects |

For production, use a secret manager or the hosting platform's secret settings. Do not treat a `.env` file as a production secret manager.

## Setting a variable on macOS or Linux

### For one command

This sets the key only for that command:

```bash
ANTHROPIC_API_KEY="your-key" python app.py
```

### For the current terminal session

```bash
export ANTHROPIC_API_KEY="your-key"
export MODEL="claude-haiku-4-5"
python app.py
```

Closing the terminal removes these session variables.

### For future terminals

Most macOS users use zsh. Add the export to `~/.zshrc` and reload it:

```bash
echo 'export ANTHROPIC_API_KEY="your-key"' >> ~/.zshrc
source ~/.zshrc
```

Linux users may use `~/.bashrc` or `~/.zshrc`, depending on their shell. You can check the shell with:

```bash
echo "$SHELL"
```

For API keys, a keychain or secret manager is safer than placing the raw value in a shell profile. The shell-profile example is here to explain the mechanism, not to define the best production practice.

## Setting a variable on Windows PowerShell

For the current PowerShell session:

```powershell
$env:ANTHROPIC_API_KEY = "your-key"
$env:MODEL = "claude-haiku-4-5"
python app.py
```

For a persistent user-level variable:

```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "your-key", "User")
```

Open a new terminal after changing a persistent variable. Existing processes do not automatically refresh their environment.

## Project `.env` files

A project often includes `.env.example` with variable names but no real secrets:

```dotenv
ANTHROPIC_API_KEY=
MODEL=claude-haiku-4-5
```

Copy it to `.env`, fill in the value, and keep `.env` out of Git:

```bash
cp .env.example .env
```

The application or framework must explicitly load the file. Docker Compose does that in this course through:

```yaml
env_file:
  - .env
```

Important: a `.env` file is not magic. It is just a file until Python, the framework, Docker Compose, or another tool reads it and passes the values to the process.

## Check safely without revealing the key

Do not paste your secret into chat, screenshots, logs, or Git. Check only whether it exists.

macOS/Linux:

```bash
if [ -n "$ANTHROPIC_API_KEY" ]; then echo "API key is set"; else echo "API key is missing"; fi
```

PowerShell:

```powershell
if ($env:ANTHROPIC_API_KEY) { "API key is set" } else { "API key is missing" }
```

Python:

```python
import os

print("API key is set" if os.environ.get("ANTHROPIC_API_KEY") else "API key is missing")
```

Never use `print(os.environ["ANTHROPIC_API_KEY"])` as a setup check.

## A first setup exercise

Run this from the repository root:

```bash
cd builds/00-hello-llm
cp .env.example .env
```

Put your provider key in `.env`, then start the service:

```bash
docker compose up --build
```

Open `http://localhost:8000`. The application reads the key inside the container because Compose passes `.env` through `env_file`. If the service cannot start, diagnose in this order:

1. Is the `.env` file in `builds/00-hello-llm/`?
2. Is the variable named exactly `ANTHROPIC_API_KEY`?
3. Did you restart Docker Compose after changing the file?
4. Does `docker compose config` show the expected service configuration without exposing the secret?
5. Is the failure an API-key problem, a network problem, or an application error?

## Safety rules

- Never hard-code an API key in Python, JavaScript, Markdown examples, or Dockerfiles.
- Never commit `.env`; this repository ignores `.env` and `**/.env`.
- Use `.env.example` for names and placeholders only.
- Rotate a key immediately if it appears in a public commit, issue, log, or screenshot.
- Use separate keys and permissions for local development, CI, staging, and production.
- Pass only the variables a process needs; avoid copying your entire environment into a container.

## Exit criteria

- [ ] I can explain what an environment variable is and which process receives it.
- [ ] I can set a variable for one command and for a terminal session.
- [ ] I can create a project `.env` from `.env.example` without committing it.
- [ ] I can check whether a key exists without printing the key.
- [ ] I can explain how Docker Compose passes configuration into the application.
- [ ] I can diagnose a missing-key error using the setup sequence above.
