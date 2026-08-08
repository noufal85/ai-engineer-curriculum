# Agents & Protocols

Letting the model act — safely. Mostly **→ M4**.

## Core ideas

- **Agent** — an LLM that can call tools, read results, and decide the next step toward a goal. *→ M4*
- **Workflow** — an explicit sequence of steps with known transitions; usually easier to test and operate than an open-ended agent. *→ M4*
- **Agent loop** — plan → act → observe → repeat until a stop condition. *→ M4*
- **Tool / function calling** — the model requests a typed call; application code executes it and returns a result. *→ M2, M4*
- **Tool schema** — the name, description, and input schema that tell the model when and how to use a tool. *→ M4*
- **ReAct** — an interleaved reason-then-act prompting pattern. *→ M4*
- **Planning** — breaking a goal into steps before or while acting. *→ M4*
- **Termination / step limit** — the guard that stops an agent looping forever. *→ M4*
- **Budget** — a limit on tokens, cost, time, tool calls, or risk.
- **Human-in-the-loop** — requiring approval before irreversible actions. *→ M4, M6*
- **Sandboxing** — running tool code or untrusted output in isolation. *→ M4, M6*

## State and reliability

- **Task state** — durable status, inputs, outputs, approvals, and errors for one piece of work.
- **Checkpoint** — persisted progress from which a workflow can resume.
- **Durable execution** — running long workflows through restarts, retries, and delays without losing state.
- **Idempotent tool** — a tool whose repeated invocation has one intended effect. *→ Engineering Core, M6*
- **Compensation** — a corrective action for a partially completed workflow.
- **Escalation** — handing a task to a person or safer path when the model cannot proceed.

## Multi-agent

- **Multi-agent** — several agents cooperating, such as an orchestrator and workers; use only when one good agent cannot do the work. *→ M4*
- **Subagent** — a child agent spawned for a bounded sub-task. *→ M4*
- **Orchestration** — coordinating steps, tools, agents, approvals, and state. *→ M4*

## Protocols and standards

- **MCP (Model Context Protocol)** — an open standard for exposing tools, resources, and prompts to models through servers and clients. *→ M4, M7*
- **MCP server / client** — the server publishes capabilities; the client consumes them. *→ M4*
- **MCP resource** — data or context a client can retrieve through the protocol.
- **MCP prompt** — a reusable prompt or interaction template published by a server.
- **Capability negotiation** — clients and servers declaring supported protocol features.
- **Tool use versus computer use** — calling defined tools versus driving a GUI/browser through screenshots and actions. *→ M4*
- **Agent-to-agent (A2A)** — patterns or standards for agents communicating with each other.

## Frameworks

- **LangChain / LangGraph** — building blocks and graph-based agent runtimes.
- **LlamaIndex** — retrieval/RAG-centric framework.
- **CrewAI, AutoGen, Semantic Kernel** — orchestration frameworks.
- **Claude Agent SDK, OpenAI Agents SDK, Pydantic AI** — provider or first-class agent SDKs.
- **DSPy** — programming LLM pipelines with optimizable modules.
- **Frameworks versus hand-rolled** — know the loop by hand before adopting an abstraction. *→ M4*
