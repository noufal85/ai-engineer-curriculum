# Agents & Protocols

Letting the model *act* — safely. Mostly **`→ M4`**.

## Core ideas

- **Agent** — an LLM that can call tools, read the results, and decide the next step toward a goal. *→ M4*
- **Agent loop** — plan → act → observe → repeat, until a stop condition. Bounds and logging keep it debuggable. *→ M4*
- **Tool / function calling** — the model requests a typed call; your code executes it and returns the result. *→ M2, M4*
- **Tool schema** — the name, description, and input schema that tell the model when/how to use a tool. *→ M4*
- **ReAct** — an interleaved reason-then-act prompting pattern for agents. *→ M4*
- **Planning** — the model breaking a goal into steps before/while acting. *→ M4*
- **Termination / step limit** — the guard that stops an agent from looping forever. *→ M4*
- **Human-in-the-loop (HITL)** — requiring approval before irreversible actions. *→ M4, M6*
- **Sandboxing** — running tool code / untrusted output in isolation. *→ M4, M6*

## Multi-agent

- **Multi-agent** — several agents cooperating (e.g. orchestrator + workers); use only when one good agent can't do it. *→ M4*
- **Subagent** — a child agent spawned for a bounded sub-task. *→ M4*
- **Orchestration** — coordinating steps, tools, and agents into a workflow. *→ M4*

## Protocols & standards

- **MCP (Model Context Protocol)** — an open standard for exposing tools, data, and prompts to any model via **servers** and **clients**; a single semantic layer over your systems. *→ M4, M7*
- **MCP server / client** — the server publishes capabilities; the client (e.g. an app or Claude) consumes them. *→ M4*
- **Tool use vs computer use** — calling defined tools vs driving a GUI/browser via screenshots and clicks. *→ M4*
- **Agent-to-agent (A2A)** — emerging patterns/standards for agents communicating with each other. *→ M4*

## Frameworks (know the landscape)

- **LangChain / LangGraph** — building blocks and a graph-based agent runtime.
- **LlamaIndex** — retrieval/RAG-centric framework.
- **CrewAI, AutoGen, Semantic Kernel** — multi-agent orchestration frameworks.
- **Claude Agent SDK, OpenAI Agents SDK, Pydantic AI** — provider/first-class agent SDKs.
- **DSPy** — programming (not prompting) LLM pipelines with optimizable modules.
- **Frameworks vs hand-rolled** — know the loop by hand before adopting a framework's abstraction. *→ M4*
