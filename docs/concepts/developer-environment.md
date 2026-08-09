# Developer Environment

The vocabulary for getting a program running on your computer. Mostly **→ [Developer Environment & Programming Basics](../curriculum/environment-and-programming.md)**, with project and deployment applications in [Engineering Core](engineering-core.md) and [M6](../curriculum/06-production-systems.md).

## Computers and processes

- **Operating system** — manages programs, files, memory, networking, and permissions.
- **Program** — instructions stored on disk.
- **Process** — a running instance of a program.
- **Terminal** — a text interface for running commands.
- **Shell** — the command interpreter inside a terminal, such as zsh, bash, or PowerShell.
- **Current working directory** — the folder a command starts from.
- **Path** — the address of a file or directory.
- **Port** — a numbered network endpoint, such as port 8000.
- **Localhost** — the current computer, commonly addressed as `127.0.0.1`.
- **Container** — an isolated process with its own filesystem, dependencies, and environment.

## Configuration

Environment variables are the main configuration mechanism introduced in this track.

- **Environment variable** — a named value attached to a process when it starts.
- **System-level variable** — a variable configured for a user account or operating-system environment rather than one project.
- **Project-level configuration** — settings loaded for one project, commonly from `.env`.
- **`.env` file** — a local configuration file containing key/value pairs; it must be protected and ignored by Git.
- **`.env.example`** — a safe template listing required variable names without real secrets.
- **`PATH`** — the list of directories a shell searches for executable commands.
- **Secret** — a credential such as an API key, password, or access token.
- **Secret manager** — a system for storing and delivering secrets without putting them in source code.
- **Configuration precedence** — the rule deciding which value wins when a setting exists in several places.

## Programming setup

- **Runtime** — software that executes a programming language.
- **Package / dependency** — reusable code another project installs.
- **Virtual environment** — an isolated set of language packages for one project.
- **Version pinning** — recording dependency versions so a project is reproducible.
- **Standard output / standard error** — the normal and error streams a command writes to.
- **Exit code** — the numeric result a process returns to indicate success or failure.
- **Stack trace** — a structured description of where an error occurred in a program.
- **AI coding assistant** — a tool such as Claude Code, Cursor, or Copilot that reads, writes, and runs code with you; a daily productivity multiplier and a preview of the agent patterns built later in the course.

## Configuration boundaries

- **Process inheritance** — child processes usually receive a copy of the parent's environment.
- **Container environment** — variables explicitly passed into a container; host variables do not all appear automatically.
- **Build-time secret** — a value needed while building an image; avoid baking secrets into image layers.
- **Runtime secret** — a value supplied only when the application starts.
- **Configuration drift** — two environments having different settings when they were expected to match.
