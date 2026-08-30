# Module 4 · Agents, Workflows, Tools & MCP

## What you will be able to do

By the end of this module, you will be able to:

- hand-roll the plan → act → observe loop with bounded steps, budgets, and logging
- choose between a deterministic workflow, a single tool call, a bounded agent, and multi-agent orchestration
- write tool schemas and descriptions the model can actually use well
- persist, resume, cancel, and reconcile long-running work
- expose a capability as an MCP server and consume one from a client
- gate irreversible actions behind authorization and human approval

## 🔨 The build

**`builds/04-agent-and-mcp`** _(planned)_ — a hand-rolled bounded workflow that uses 2–3 tools, persists state, logs every step, exposes one capability as an MCP server, and pauses for human approval before an irreversible action. Start as a local lab; Dockerize it when the server boundary or reproducibility becomes part of the lesson.

Build it, then the sections below explain the loop and why bounds matter.

## Why it matters

An agent can act: it calls tools, reads results, and decides what to do next. But many useful systems are better modeled as explicit workflows with a few model-powered steps. Choosing between a deterministic workflow and an open-ended agent is a core engineering decision.

## Understand in depth

### Tool use and the loop

- Tool/function calling, typed arguments, validation, descriptions, and result envelopes.
- Plan → act → observe → repeat, termination conditions, step limits, budgets, and cancellation.
- Tool errors as data the model can recover from, versus errors that must stop the run.
- Retries, idempotent writes, compensation, and safe handling of partial completion.

### Workflow versus agent

- Deterministic workflows for known sequences and predictable approvals.
- Single-shot tool use for simple lookups or actions.
- Bounded agents for tasks with uncertain paths but clear tools and stop conditions.
- Multi-agent orchestration only when one good agent cannot do the work cleanly.

### State and durability

- Conversation state, task state, checkpoints, resumability, and expiration.
- Queues and background workers for long-running work.
- Exactly-once as an aspiration: design practical idempotency and reconciliation instead.
- Human approval, cancellation, escalation, and recovery after a process restart.

### MCP and protocols

- MCP servers and clients; tools, resources, prompts, lifecycle, transports, and capability negotiation.
- Authentication, authorization, versioning, compatibility, error handling, and observability.
- A semantic layer over systems versus one bespoke integration per application.
- Forking and extending an MCP server while preserving a stable contract.

### Safety and isolation

- Least-privilege tools, per-user permissions, sandboxing, untrusted tool output, and human gates.
- Browser/computer use versus defined tool calls.
- Preventing destructive actions, data exfiltration, prompt injection, and runaway spend.

## 🧪 Lab

Hands-on first: a zero-setup trial, then the build tasks.

### Trial · Be the agent runtime (~15 min)

1. Paste this into a chat:

    ```text
    You are an agent with two tools:
    - get_weather(city) -> {"temp_c": number, "conditions": string}
    - send_email(to, subject, body) -> {"status": string}

    To use a tool, reply with ONLY a JSON tool call. I will reply with the
    tool result. Task: email dana@example.com whether she needs an umbrella
    in Amsterdam tomorrow.
    ```

2. Play the runtime yourself: when the model emits a tool call, type a fake JSON result back, e.g. `{"temp_c": 9, "conditions": "heavy rain"}`. Continue until it emits the `send_email` call. You are hand-executing the plan → act → observe loop.
3. Now inject a failure — reply `{"error": "service unavailable"}` — and watch what it does: retry, give up, or hallucinate a forecast anyway. Whatever you just observed is the behavior the build must bound with step limits, error handling, and human gates.

### Build tasks

- [ ] Hand-roll an agent/workflow loop with 2–3 tools, bounded steps, cancellation, and full logging.
- [ ] Persist task state and resume after a simulated process restart.
- [ ] Expose one tool as an MCP server and drive it from an MCP client.
- [ ] Add tool authorization based on the requesting user.
- [ ] Add a human gate before an irreversible call and prove the gate cannot be bypassed.
- [ ] Inject a tool failure and show recovery, escalation, or safe termination.

## Checklist

- [ ] I can build an agent loop from scratch with bounded steps and logging.
- [ ] I can identify when a deterministic workflow is better than an agent.
- [ ] I can write clean tool schemas and explain why descriptions matter.
- [ ] I can persist, resume, cancel, and reconcile a long-running task.
- [ ] I can build and consume an MCP server with an explicit compatibility contract.
- [ ] I gate irreversible actions behind authorization and human approval.
- [ ] I can justify single-agent versus multi-agent design.

## Resources

- Anthropic, *Building effective agents*.
- The MCP specification and a reference server/client.
- Read one agent framework's runtime source after hand-rolling the loop — LangGraph, CrewAI, Strands Agents, the Vercel AI SDK, or a provider agent SDK — and map it back to the loop you built.
