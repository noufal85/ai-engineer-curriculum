# Agents & Protocols

Letting the model act — safely. Mostly **→ [M4](../curriculum/04-agents-tools-mcp.md)**.

## Core ideas

- **Agent** — an LLM that can call tools, read results, and decide the next step toward a goal. *→ [M4](../curriculum/04-agents-tools-mcp.md)*
- **Workflow** — an explicit sequence of steps with known transitions; usually easier to test and operate than an open-ended agent. *→ [M4](../curriculum/04-agents-tools-mcp.md)*
- **Agent loop** — plan → act → observe → repeat until a stop condition. *→ [M4](../curriculum/04-agents-tools-mcp.md)*
- **Tool / function calling** — the model requests a typed call; application code executes it and returns a result. *→ [M2](../curriculum/02-prompting-context.md), [M4](../curriculum/04-agents-tools-mcp.md)*
- **Tool schema** — the name, description, and input schema that tell the model when and how to use a tool. *→ [M4](../curriculum/04-agents-tools-mcp.md)*
- **ReAct** — an interleaved reason-then-act prompting pattern. *→ [M4](../curriculum/04-agents-tools-mcp.md)*
- **Planning** — breaking a goal into steps before or while acting. *→ [M4](../curriculum/04-agents-tools-mcp.md)*
- **Termination / step limit** — the guard that stops an agent looping forever. *→ [M4](../curriculum/04-agents-tools-mcp.md)*
- **Budget** — a limit on tokens, cost, time, tool calls, or risk.
- **Human-in-the-loop** — requiring approval before irreversible actions. *→ [M4](../curriculum/04-agents-tools-mcp.md), [M6](../curriculum/06-production-systems.md)*
- **Sandboxing** — running tool code or untrusted output in isolation. *→ [M4](../curriculum/04-agents-tools-mcp.md), [M6](../curriculum/06-production-systems.md)*

## State and reliability

- **Task state** — durable status, inputs, outputs, approvals, and errors for one piece of work.
- **Checkpoint** — persisted progress from which a workflow can resume.
- **Durable execution** — running long workflows through restarts, retries, and delays without losing state.
- **Idempotent tool** — a tool whose repeated invocation has one intended effect. *→ [Engineering Core](engineering-core.md), [M6](../curriculum/06-production-systems.md)*
- **Compensation** — a corrective action for a partially completed workflow.
- **Escalation** — handing a task to a person or safer path when the model cannot proceed.

## Multi-agent

- **Multi-agent** — several agents cooperating, such as an orchestrator and workers; use only when one good agent cannot do the work. *→ [M4](../curriculum/04-agents-tools-mcp.md)*
- **Subagent** — a child agent spawned for a bounded sub-task. *→ [M4](../curriculum/04-agents-tools-mcp.md)*
- **Orchestration** — coordinating steps, tools, agents, approvals, and state. *→ [M4](../curriculum/04-agents-tools-mcp.md)*

## Protocols and standards

- **MCP (Model Context Protocol)** — an open standard for exposing tools, resources, and prompts to models through servers and clients. *→ [M4](../curriculum/04-agents-tools-mcp.md), [M7](../curriculum/07-forward-deployed.md)*
- **MCP server / client** — the server publishes capabilities; the client consumes them. *→ [M4](../curriculum/04-agents-tools-mcp.md)*
- **MCP resource** — data or context a client can retrieve through the protocol.
- **MCP prompt** — a reusable prompt or interaction template published by a server.
- **Capability negotiation** — clients and servers declaring supported protocol features.
- **Tool use versus computer use** — calling defined tools versus driving a GUI/browser through screenshots and actions. *→ [M4](../curriculum/04-agents-tools-mcp.md)*
- **Agent-to-agent (A2A)** — patterns or standards for agents communicating with each other.

## Frameworks

- **LangChain / LangGraph** — building blocks and graph-based agent runtimes.
- **LlamaIndex** — retrieval/RAG-centric framework.
- **CrewAI, AutoGen, Semantic Kernel** — multi-agent orchestration frameworks: role-based crews, conversation-driven teams, and plugin pipelines. *→ [M4](../curriculum/04-agents-tools-mcp.md)*
- **Strands Agents** — AWS's model-driven agent framework; the loop is delegated to the model with tools and a prompt.
- **Vercel AI SDK** — TypeScript toolkit for AI apps: streaming UI, tool calls, structured output, and agent loops inside web frameworks.
- **Claude Agent SDK, OpenAI Agents SDK, Google ADK, Pydantic AI** — provider or first-class agent SDKs.
- **DSPy** — programming LLM pipelines with optimizable modules.
- **Frameworks versus hand-rolled** — know the loop by hand before adopting an abstraction. *→ [M4](../curriculum/04-agents-tools-mcp.md)*
