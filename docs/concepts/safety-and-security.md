# Safety & Security

Non-negotiable, not a v2 feature. Mostly **`→ M6`**, with red-teaming in [M5](../curriculum/05-evals-observability.md)/[M8](../curriculum/08-capstones.md).

## Attacks

- **Prompt injection** — untrusted content in the context overriding your instructions. **Direct** (in the user input) vs **indirect** (hidden in a retrieved doc, web page, or tool output). *→ M2, M6, M8*
- **Jailbreak** — coaxing a model past its safety training. *→ M6*
- **Prompt / system-prompt leaking** — tricking the model into revealing its hidden instructions. *→ M6*
- **Data exfiltration** — using the model/agent to leak private data out of the system. *→ M6*
- **Denial of wallet** — driving up token cost as an attack. *→ M6*
- **The data ≠ instructions boundary** — the core defense mindset: everything the model reads is data, not commands. *→ M2, M6*
- **OWASP LLM Top 10** — the canonical catalog of LLM app risks (injection, data leakage, insecure output handling, etc.). *→ M6*

## Data protection

- **PII (personally identifiable information)** — must be masked/handled per regulation (GDPR, CCPA). *→ M6*
- **PII masking / redaction** — removing sensitive data before it reaches the model or logs. *→ M6*
- **Entitlements / security trimming** — ensuring retrieval never returns what a user isn't allowed to see. *→ M6, M7*
- **Secrets management** — keeping API keys/tokens out of prompts, code, and logs. *→ M0, M6*
- **Least privilege** — giving tools/agents only the access they need. *→ M4, M6*
- **Output filtering / moderation** — screening generations for unsafe or disallowed content. *→ M6*

## Model & org safety

- **Guardrails** — input/output checks that constrain what a model can accept or produce. *→ M6*
- **Alignment** — training a model to be helpful, honest, and harmless. *→ M1*
- **Red-teaming** — adversarial testing to find failures before attackers do. *→ M5, M8*
- **Bias & toxicity** — systematic unfairness or harmful output to test and mitigate. *→ M5*
- **Hallucination as a safety issue** — confident wrong answers in high-stakes settings. *→ M1, M3, M5*
- **Provenance / watermarking** — tracing or marking AI-generated content.
- **Authorization for actions** — confirm irreversible/outward-facing actions before an agent takes them. *→ M4, M6*
