# Module 4 · Agents, Tools & MCP

## 🔨 The build

**`builds/04-agent-and-mcp`** _(planned)_ — a **hand-rolled agent loop** (no framework) with 2–3 tools, a step limit, and full step logging; expose one tool as an **MCP server** and add a **human-in-the-loop gate** before any irreversible action. Dockerized (`docker compose up`).

Build it, then the sections below explain the loop and why bounds matter.

## Why it matters

An agent is a model that can *act* — call tools, read results, decide the next step. This is where AI stops being a chatbot and starts doing work. It's also where reliability gets hard: loops, wrong tool choices, runaway cost. Designing agents that are bounded and debuggable is the skill.

## Understand in depth

- **Tool/function calling** — how the model requests a call, how you execute and feed results back, and why clean tool schemas + descriptions are half the battle.
- **The agent loop** — plan → act → observe → repeat. Termination conditions, step limits, and why an unbounded loop is a bug waiting to happen.
- **Planning & decomposition** — single-shot tool use vs. multi-step plans vs. ReAct-style interleaving. When each is appropriate.
- **MCP (Model Context Protocol)** — the standard for exposing tools/data/prompts to any model. Servers vs. clients, why a **single semantic layer over your systems** (see the [moat notes](../notes/moat-is-your-data-model.md)) beats bespoke integrations. Forking/extending off-the-shelf MCP servers, passing state (conversation/message IDs).
- **Multi-agent** — orchestrator/worker patterns, when splitting agents helps vs. adds failure surface. Default to *one* good agent until you can prove you need more.
- **Sandboxing & safety** — running tool code and untrusted output safely; least-privilege tools; human-in-the-loop for irreversible actions.
- **Reliability engineering** — retries, idempotent tools, guarding against the model calling `delete` / destructive tools, and making every step traceable (→ Module 5).
- **Frameworks vs. hand-rolled** — what LangGraph/Agents SDKs give you vs. the cost of the abstraction. Know how to build the loop by hand first.

## Build

- [ ] Hand-roll an agent loop (no framework) with 2–3 tools, a step limit, and full step logging.
- [ ] Expose one of your tools as an **MCP server** and drive it from an MCP client.
- [ ] Add a **human-in-the-loop gate** before any irreversible tool call; prove the agent can't act without approval.

## Checklist

- [ ] I can build an agent loop from scratch with bounded steps and logging
- [ ] I can write clean tool schemas and explain why descriptions matter
- [ ] I can build and consume an MCP server
- [ ] I gate irreversible actions behind human approval
- [ ] I can justify single-agent vs. multi-agent for a task instead of defaulting to multi

## Resources

- Anthropic *"Building effective agents"* (patterns, not hype).
- MCP spec + a reference server/client; Claude Code as a real-world MCP client example.
- Read one agent framework's source (LangGraph or the Agents SDK) *after* hand-rolling.
