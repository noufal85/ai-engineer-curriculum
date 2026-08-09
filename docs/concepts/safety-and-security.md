# Safety & Security

Non-negotiable, not a v2 feature. Mostly **→ [M6](../curriculum/06-production-systems.md)**, with red-teaming in [M5](../curriculum/05-evals-observability.md) and [M8](../curriculum/08-capstones.md).

## Attacks and untrusted input

- **Prompt injection** — untrusted content overriding instructions. **Direct** injection appears in user input; **indirect** injection is hidden in retrieved documents, web pages, or tool output. *→ [M2](../curriculum/02-prompting-context.md), [M6](../curriculum/06-production-systems.md), [M8](../curriculum/08-capstones.md)*
- **Jailbreak** — coaxing a model past its safety behavior. *→ [M6](../curriculum/06-production-systems.md)*
- **Prompt leaking** — tricking a system into revealing hidden instructions or sensitive context. *→ [M6](../curriculum/06-production-systems.md)*
- **Data exfiltration** — using a model or agent to move private data outside its authorized boundary. *→ [M6](../curriculum/06-production-systems.md)*
- **Tool injection** — malicious or malformed tool results steering later actions. *→ [M4](../curriculum/04-agents-tools-mcp.md), [M6](../curriculum/06-production-systems.md)*
- **SSRF** — inducing a server-side request to an internal or unintended network target. *→ [M6](../curriculum/06-production-systems.md)*
- **Data poisoning** — inserting or altering source data to influence retrieval or model behavior. *→ [M3](../curriculum/03-rag-memory.md), [M6](../curriculum/06-production-systems.md)*
- **Denial wallet** — driving up token or tool costs through adversarial requests. *→ [M6](../curriculum/06-production-systems.md)*
- **The data ≠ instructions boundary** — treat everything the model reads as data unless the application explicitly authorizes it as a command. *→ [M2](../curriculum/02-prompting-context.md), [M6](../curriculum/06-production-systems.md)*
- **OWASP LLM Top 10** — a catalog of common LLM application risks. *→ [M6](../curriculum/06-production-systems.md)*

## Identity and authorization

- **Authentication** — proving who a user or service is.
- **Authorization** — deciding what that identity may read or do.
- **RBAC / ABAC** — permissions based on roles / attributes such as tenant, project, or sensitivity.
- **Tenant isolation** — ensuring one customer cannot observe or influence another customer's data or budget.
- **Least privilege** — giving a model, tool, worker, or service only the access it needs. *→ [M4](../curriculum/04-agents-tools-mcp.md), [M6](../curriculum/06-production-systems.md)*
- **Security trimming** — applying authorization filters before retrieval results enter model context. *→ [M6](../curriculum/06-production-systems.md), [M7](../curriculum/07-forward-deployed.md)*
- **Audit log** — an append-only record of sensitive reads, writes, approvals, and policy decisions.

## Data protection and governance

- **PII** — personally identifiable information that must be handled according to policy and regulation. *→ [M6](../curriculum/06-production-systems.md)*
- **PII masking / redaction** — removing or transforming sensitive data before it reaches models or logs. *→ [M6](../curriculum/06-production-systems.md)*
- **Secrets management** — keeping API keys, tokens, and credentials out of code, prompts, and logs. *→ [Engineering Core](../curriculum/engineering-core.md), [M6](../curriculum/06-production-systems.md)*
- **Data retention** — defining how long prompts, outputs, traces, and source data are kept.
- **Output handling** — validating and escaping model output before it reaches a database, browser, shell, or external system.
- **Moderation** — screening inputs or outputs for prohibited or unsafe content.

## Safety controls

- **Red-teaming** — deliberately trying to break a system and documenting the resulting failures. *→ [M5](../curriculum/05-evals-observability.md), [M8](../curriculum/08-capstones.md)*
- **Threat model** — a structured analysis of assets, actors, attack paths, and mitigations.
- **Human approval** — requiring a person before an irreversible or outward-facing action. *→ [M4](../curriculum/04-agents-tools-mcp.md), [M6](../curriculum/06-production-systems.md)*
- **Sandboxing** — isolating code execution and untrusted content from sensitive systems. *→ [M4](../curriculum/04-agents-tools-mcp.md), [M6](../curriculum/06-production-systems.md)*
- **Policy enforcement point** — the application boundary that checks identity, permissions, budgets, and action policy before execution.

## Responsible AI

- **Bias and fairness** — systematic skew in model behavior across groups, dialects, or contexts; measure it on your own data, not just published benchmarks. *→ [M5](../curriculum/05-evals-observability.md), [M6](../curriculum/06-production-systems.md)*
- **Harmful-content policy** — the categories your product refuses or restricts, and the moderation layer that enforces them on inputs and outputs. *→ [M6](../curriculum/06-production-systems.md)*
- **Transparency and disclosure** — telling users when they are interacting with AI and what the system can and cannot do. *→ [M6](../curriculum/06-production-systems.md), [M7](../curriculum/07-forward-deployed.md)*
- **Human oversight** — keeping a person accountable for consequential decisions rather than fully delegating them. *→ [M4](../curriculum/04-agents-tools-mcp.md), [M6](../curriculum/06-production-systems.md)*
- **Regulatory awareness** — the EU AI Act, sector rules, and customer AI policies that constrain what a deployed system may do. *→ [M6](../curriculum/06-production-systems.md), [M7](../curriculum/07-forward-deployed.md)*
- **Model behavior provenance** — knowing what alignment, system prompts, and safety layers shape the output you ship. *→ [M1](../curriculum/01-llm-internals.md), [M6](../curriculum/06-production-systems.md)*
