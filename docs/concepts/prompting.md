# Prompting & Context

The highest-leverage, lowest-cost skill. Mostly **→ [M2](../curriculum/02-prompting-context.md)**.

## Prompt anatomy

- **Prompt** — the full input you send the model. **Completion** — what it generates back.
- **System / user / assistant roles** — the message roles: system sets behavior, user asks, assistant answers. *→ [M2](../curriculum/02-prompting-context.md)*
- **System prompt** — the standing instructions that shape every turn (persona, rules, output spec). *→ [M2](../curriculum/02-prompting-context.md)*
- **Prompt template** — a reusable prompt with slots for variables.
- **Delimiters** — clear markers (XML tags, fences) that separate instructions from data and reduce confusion/injection. *→ [M2](../curriculum/02-prompting-context.md), [M8](../curriculum/08-capstones.md)*

## Techniques

- **Prompt engineering** — iterating on wording/structure to get reliable outputs. *→ [M2](../curriculum/02-prompting-context.md)*
- **Few-shot prompting** — including examples of the task in the prompt. *→ [M2](../curriculum/02-prompting-context.md)*
- **Chain-of-thought (CoT)** — asking the model to reason step-by-step. *→ [M1](../curriculum/01-llm-internals.md), [M2](../curriculum/02-prompting-context.md)*
- **Self-consistency** — sampling several reasoning paths and taking the majority answer.
- **Decomposition / prompt chaining** — splitting one hard prompt into a chain of reliable steps. *→ [M2](../curriculum/02-prompting-context.md)*
- **Role prompting** — telling the model who to act as.
- **Meta-prompting** — using an LLM to write or improve prompts.

## Structured output

- **Structured output / JSON mode** — constraining the model to return valid JSON. *→ [M0](../curriculum/00-foundations.md), [M2](../curriculum/02-prompting-context.md)*
- **JSON Schema** — the contract the output must satisfy; validated at the boundary. *→ [M0](../curriculum/00-foundations.md), [M2](../curriculum/02-prompting-context.md)*
- **Tool / function calling** — the reliable way to get structured data and let the model trigger actions; the model returns a typed call your code executes. *→ [M2](../curriculum/02-prompting-context.md), [M4](../curriculum/04-agents-tools-mcp.md)*
- **Constrained / structured decoding** — forcing the generator to only produce tokens valid under a schema/grammar.
- **Strict mode** — a guarantee that tool/output arguments exactly match the schema. *→ [M2](../curriculum/02-prompting-context.md)*
- **Output parsing** — extracting and validating fields from a response (don't trust raw text). *→ [M0](../curriculum/00-foundations.md)*

## Context engineering

- **Context engineering** — deciding what goes into the window, in what order, and what to leave out — the real discipline behind reliable prompts. *→ [M2](../curriculum/02-prompting-context.md), [M3](../curriculum/03-rag-memory.md)*
- **Prompt caching** — reusing an unchanged prompt prefix across requests to cut cost and latency; put stable content first. *→ [M2](../curriculum/02-prompting-context.md), [M6](../curriculum/06-production-systems.md)*
- **Context compaction / trimming** — summarizing or dropping old turns to stay within the window on long runs. *→ [M4](../curriculum/04-agents-tools-mcp.md), [M6](../curriculum/06-production-systems.md)*
- **Instruction drift** — a model gradually ignoring earlier instructions over a long conversation. *→ [M2](../curriculum/02-prompting-context.md)*
- **Prompt injection** — untrusted text in the context hijacking the model's instructions (the dark side of context). *→ [M2](../curriculum/02-prompting-context.md), [M6](../curriculum/06-production-systems.md), [M8](../curriculum/08-capstones.md)*
