# Safety & Security

Non-negotiable, not a v2 feature. Mostly **→ M6**, with red-teaming in [M5](../curriculum/05-evals-observability.md) and [M8](../curriculum/08-capstones.md).

## Attacks and untrusted input

- **Prompt injection** — untrusted content overriding instructions. **Direct** injection appears in user input; **indirect** injection is hidden in retrieved documents, web pages, or tool output. *→ M2, M6, M8*
- **Jailbreak** — coaxing a model past its safety behavior. *→ M6*
- **Prompt leaking** — tricking a system into revealing hidden instructions or sensitive context. *→ M6*
- **Data exfiltration** — using a model or agent to move private data outside its authorized boundary. *→ M6*
- **Tool injection** — malicious or malformed tool results steering later actions. *→ M4, M6*
- **SSRF** — inducing a server-side request to an internal or unintended network target. *→ M6*
- **Data poisoning** — inserting or altering source data to influence retrieval or model behavior. *→ M3, M6*
- **Denial wallet** — driving up token or tool costs through adversarial requests. *→ M6*
- **The data ≠ instructions boundary** — treat everything the model reads as data unless the application explicitly authorizes it as a command. *→ M2, M6*
- **OWASP LLM Top 10** — a catalog of common LLM application risks. *→ M6*

## Identity and authorization

- **Authentication** — proving who a user or service is.
- **Authorization** — deciding what that identity may read or do.
- **RBAC / ABAC** — permissions based on roles / attributes such as tenant, project, or sensitivity.
- **Tenant isolation** — ensuring one customer cannot observe or influence another customer's data or budget.
- **Least privilege** — giving a model, tool, worker, or service only the access it needs. *→ M4, M6*
- **Security trimming** — applying authorization filters before retrieval results enter model context. *→ M6, M7*
- **Audit log** — an append-only record of sensitive reads, writes, approvals, and policy decisions.

## Data protection and governance

- **PII** — personally identifiable information that must be handled according to policy and regulation. *→ M6*
- **PII masking / redaction** — removing or transforming sensitive data before it reaches models or logs. *→ M6*
- **Secrets management** — keeping API keys, tokens, and credentials out of code, prompts, and logs. *→ Engineering Core, M6*
- **Data retention** — defining how long prompts, outputs, traces, and source data are kept.
- **Output handling** — validating and escaping model output before it reaches a database, browser, shell, or external system.
- **Moderation** — screening inputs or outputs for prohibited or unsafe content.

## Safety controls

- **Red-teaming** — deliberately trying to break a system and documenting the resulting failures. *→ M5, M8*
- **Threat model** — a structured analysis of assets, actors, attack paths, and mitigations.
- **Human approval** — requiring a person before an irreversible or outward-facing action. *→ M4, M6*
- **Sandboxing** — isolating code execution and untrusted content from sensitive systems. *→ M4, M6*
- **Policy enforcement point** — the application boundary that checks identity, permissions, budgets, and action policy before execution.
