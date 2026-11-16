---
title: Agents & workflows
workspace_layout: hub
hide:
  - toc
---

<div class="workspace-hub" markdown="1">

<div class="hub-intro" markdown="1">

# Agents & workflows

Choose where a model decides, where code decides, and how the work stops.
{ .hub-lead }

Begin with a clear task and a working model call. Add tools, state, and coordination when they help the workflow you are trying to complete.

</div>
<div class="hub-tasks" markdown="1">

[Understand the agent loop](../curriculum/04-agents-tools-mcp.md)
[Study a tool-using agent](../system-design/tool-using-agents.md)
[Look up MCP and tools](../concepts/agents-and-protocols.md)

</div>
<div class="hub-grid" markdown="1">

<div class="hub-main" markdown="1">

<section class="topic-panel" markdown="1">

<div class="topic-panel-head" markdown="1">

## Understand & practice

Choose an explanation or a practical exercise below.

</div>
<div class="topic-list" markdown="1">

<div class="topic-row" markdown="1">

### [Agents, workflows, tools & MCP](../curriculum/04-agents-tools-mcp.md)

Trace the plan–act–observe loop and reason about state, retries, budgets, tools, and approvals. The chapter includes a manual runtime exercise.

Chapter with exercises · Agent-and-MCP build planned
{ .topic-row-meta }

</div>
<div class="topic-row" markdown="1">

### [Prompting & context engineering](../curriculum/02-prompting-context.md)

Prepare clear instructions, schemas, and context before asking a model to choose a tool.

Supporting chapter · Module 2
{ .topic-row-meta }

</div>
<div class="topic-row" markdown="1">

### [Coding and sandboxed agents](../curriculum/specializations.md)

Explore the optional track for repository context, restricted execution, tests, review, and rollback.

Specialization outline · Suggested build
{ .topic-row-meta }

</div>

</div>

</section>
<section class="topic-panel" markdown="1">

<div class="topic-panel-head" markdown="1">

## Explore the designs

Worked architectures and trade-offs. These are reference studies, not completed implementations.

</div>
<div class="topic-list" markdown="1">

<div class="topic-row" markdown="1">

### [Tool-using agents](../system-design/tool-using-agents.md)

Compare an agent-driven loop with a bounded workflow, including state and stopping conditions.

</div>
<div class="topic-row" markdown="1">

### [Durable AI workflows](../system-design/durable-workflows.md)

Account for retries, waiting, approvals, and recovery after a process restarts.

</div>
<div class="topic-row" markdown="1">

### [An MCP tool gateway](../system-design/mcp-tool-gateway.md)

Connect enterprise capabilities with identity, authorization, and an audit trail.

</div>
<div class="topic-row" markdown="1">

### [Multi-agent coordination](../system-design/multi-agent-coordination.md)

Decide when specialization and parallel work justify their coordination cost.

</div>
<div class="topic-row" markdown="1">

### [Coding agents with isolated execution](../system-design/coding-agent-sandboxes.md)

Walk through repository access, test feedback, sandbox boundaries, and human review.

</div>
<div class="topic-row" markdown="1">

### [Browser agents](../system-design/browser-agents.md)

Compare browser automation with direct APIs and verify the outcome of each action.

</div>

</div>

</section>

</div>
<aside class="hub-side" markdown="1">

<section class="feature-box" markdown="1">

## Play the runtime.

Execute the tool loop by hand: inspect a requested tool call, supply a result, and decide when the workflow must pause. The chapter has the exercise; the full agent lab is planned.

<div class="feature-actions" markdown="1">

[Open the chapter exercise](../curriculum/04-agents-tools-mcp.md){ .primary }

</div>

</section>
<section class="reference-block" markdown="1">

## Keep nearby

- [Agents & protocols glossary](../concepts/agents-and-protocols.md)
- [Prompting & context](../concepts/prompting.md)
- [Safety & security](../concepts/safety-and-security.md)

## Connected decisions

- [Long-term memory](../system-design/long-term-memory.md)
- [Natural-language analytics over SQL](../system-design/natural-language-sql.md)
- [Evaluation & quality](evaluation.md)

</section>

</aside>

</div>
<div class="hub-bottom" markdown="1">

**What counts as a successful run?** [Explore evaluation & quality](evaluation.md) before expanding the agent’s responsibilities.

</div>

</div>
