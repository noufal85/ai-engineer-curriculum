# Module 4 · Agents, Workflows, Tools & MCP

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

## Build

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
- Read one agent framework's runtime source after hand-rolling the loop.
