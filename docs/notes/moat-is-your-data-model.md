# Your Moat Is Your Data Model

**Speaker:** Mike Phipps — Gates Foundation
**Source:** [youtube.com/watch?v=jt1Pbr_n6oU](https://www.youtube.com/watch?v=jt1Pbr_n6oU)

---

## Thesis

Models, frontends, and agent frameworks all commoditize. The durable, defensible asset is your **data model** plus the **tacit knowledge** of how your organization's questions are supposed to be answered. At the Gates Foundation, 25 years of grantmaking was modeled into a single **Neo4j knowledge graph**, served to Claude through **one MCP server** — the **Strategic Intelligence Platform (SIP)**, rolled out to production for ~4,000 people in the month before the talk.

## The moat argument

As AI moves fast at the frontier, the question is what stays **defensible**. You can build quickly with Claude Code, but production imposes constraints — monitoring, upkeep, downstream dependencies others build on your stack. Open questions the team weighed:

- How much of the deployed stack do you actually want to **own**?
- How much appetite do users have for **decentralized access** — is the access point another chat app, Claude, ChatGPT, something else?
- What's your **product differentiation** vs. SaaS products?

**Conclusion:** their moat is their **understanding of internal processes** — the tacit knowledge needed to run successful AI. This holds no matter how good models get; new model or app releases don't threaten it because the defensible, durable part is the process/tacit-knowledge layer they've modeled into SIP.

## What is being modeled (Gates Foundation scope)

The foundation's work spans child mortality, nutrition, agriculture, education — via creating market incentives, spurring innovation, and public/private collaboration. The relevant lens here is the fourth: **deriving data-driven insights from actual investments (grants).** Over 25 years this produced enormous structure; extracting insights **at scale** is the problem being solved.

**Scale (2023 snapshot):**

- **2,000+ grants** in one year (many $5M+)
- **100+ countries** targeted
- **~4,000 employees**
- Grants across almost **all US states** plus international
- **$7B+** total annual disbursement
- Funding flows through multiple **divisions** — e.g. Global Development, Global Health, Gender Equality, USP

## SIP architecture: structuring operational data for agentic retrieval

A **knowledge graph built for the agent consumer** (not for dashboards). End-to-end flow:

1. **Systems of record** — structured and unstructured, traditionally **siloed**.
2. **Data lakehouse** — the team consolidated everything "under one roof": internal enterprise-wide data plus programmatic data that are outputs of investments.
3. **Data curation layer** — processing over that consolidated data.
4. **SIP** — the graph exposed as a **cross-system semantic layer** that agents reason across, with **agentic chat / agentic workflow** as the UX.

## Engaging data owners (the tacit-knowledge capture)

Critical and repeatedly reinforced: when dealing with complex systems of record, **engagement with data owners is essential** to model the tacit knowledge. You must understand:

- The full **meaning of each field**
- The **structure** of the dataset and **how to join** things together
- **Limitations** and **systematics** of the data
- **Safeguards, security trimmings, reporting conventions**

The key point: it's not enough to answer a question *a* certain way — you have to answer it **the way it has been answered in the past**. That procedural understanding is the moat: the part they own.

## Curation pipeline

Three buckets of considerations feeding the pipeline:

**1. Pre-processing**
- Filtering, **deduplication**
- Handling document **order** and **inconsistencies across documents**, resolved up front

**2. Extraction & tagging**
- **Structured field extraction**
- **Semantic chunking** for unstructured documents
- **Figures → text** conversion so they're retrievable
- Various **tagging** that forms connections in the graph
- Extra **metadata** created during the pipeline → becomes **node properties** in the graph

**3. Governance**
- AI makes previously-hard-to-access data much more accessible, so the **risk sphere is larger**
- **PII masking**
- Reclassifying **sensitive data**
- Enforcing the right **entitlements** per user accessing the system

## The data model

Graph is a flexible, practical representation of a physical model. What's shown in the talk is a **conceptual (flat) data model** — the actual instantiated graph has far more nodes and one-to-N cardinality, so it's more complex.

**Entry point:** **80+ strategy teams**. Each team has **annual reviews** that drive that year's **budgeting**. These reviews are modeled as **meetings**, which are where **unstructured documents enter** the system — but they carry a **structured connection** to the other systems of record.

### Hierarchy 1 — funding lens (additive DAG)

- An **additive DAG** where **all five levels matter** top to bottom, so you must consider everything together.
- Different **rollup patterns** work across it; they use an **in-path shortcut** connecting the funding path.
- **`funds → bow`** is where the **budget** for each funding team is stored.
- Structure: internal **funding teams → portfolios → investments**. **Multiple funding teams can fund a single investment** (end-to-end relationship).
- **Investments are the product / the business.** Internally, **funds prioritize different types of investments.**
- Can be taken down to the **transaction level** or mapped as **annual-based aggregations**.
- From an investment you can map to **organizations** (of different types) and to **observables** investments produce — published reports, products, etc. — all structured and connected to the full organizational picture. (Noted as partly green space still to fill in.)

### Hierarchy 2 — management lens (each level matters individually)

- Here **each level matters in and of itself**, so it's **not necessarily a DAG** — which means you can **precompute shortcuts**.
- Edges: hierarchy goes top→bottom via **`contains` / `connects`**. This is the **investment management** side.
- **Direct management:** e.g. a team at **team-level-2 manages the investment**.
- **Indirect management:** children below team-level-2 should **still be attributed** to team-level-2.
- **`rollup_manages`** is a **derived edge** created *after* the `contains` and `manages` edges, to play these rollup games.
- Net result: **two lenses over one investment** — the **funding lens** and the **management lens** — both modeled in the same graph.

### Hierarchy 3 — people

- **Organizations, org charts, and people** with many roles: owners, meeting attendees, directors, etc.
- Model **who reports to whom** and **team structure**.
- Traditionally lived only in an **HR source system**, but is relevant to the full story — so it's stitched into the graph as structured data spanning systems.

### Stitching siloed systems

Different source systems were siloed. To let the agent understand the whole picture correctly, you find the **common entities** across systems and **stitch them together** on those shared entities. Then the agent can **traverse** and understand the full, complicated organizational structure.

### Combining unstructured documents with structured data

- **Meetings have documents**; **documents have semantic sections / chunks** modeled in the graph.
- **Full-text indexes** placed across chunks aid search/retrieval; the agent can also do **pure graph retrieval**.
- All of it **connects back to the main organizational structure**.
- (Only one document source ingested so far — flagged as an area with much more to do. This unstructured+structured combination is called out as the "magic" you can model with Neo4j.)

### The whole model

Four different systems → **one graph, one semantic layer**, exposed through **MCP** to the agents. From the **agent's perspective** this is the structure it can **dynamically discover and reason across at query time**. A side benefit for developers: modeling **exposes gaps** — you quickly discover what you don't know or a dataset you haven't fully included, which makes the process itself valuable.

## Serving the graph to Claude through MCP

- The graph is connected to AI via **MCP**.
- What was **not defensible**: the **chat interface / UI**, and in some cases the general chat and agent interaction. Users already live in Claude or ChatGPT, so the strategy is to **serve the platform where the users already are**.
- They started from **Neo4j's off-the-shelf MCP servers** but **forked and heavily modified** them:
  - Various **schema updates**
  - Passing **state back** to their system — **conversation IDs**, **message numbers**, etc.
- That's one entry point (general chat). The other, actively being built: **more constrained workflow experiences**, offered through things like **co-work / Claude chat**:
  - **MCP apps** as the standard entry way, porting different UIs into the chat experience
  - **Sandbox-based agents** that run the workflow
  - Constrains the experience vs. open chat while pulling from the **same knowledge-graph backend**

## Retrieval evals and the feedback loop

Evals connect back to data modeling: running evals surfaces **gaps and ambiguities** in the data model and **ambiguous user questions**, and catches answers that **don't conform to reporting standards**.

**Approach:**

- Work with **data owners** to build **targeted eval questions that match their reporting standards**.
- Separate questions into **complexity tiers**.
- Because the **structured data constantly changes**, each eval question stores the **graph query** itself; at runtime the eval **pulls from the live graph** and compares that to the agent's delivered answer.
- **Feedback loop with LLM-as-judge**, measuring:
  - **pass@1**
  - **stability** — ask the same question multiple times and check you get the same answer back
- The loop feeds updates to the **data model**, **domain rules**, and **schema descriptions** to fill the discovered gaps.
- **Reported results:** pass@1 and stability are **very strong**. The remaining misses tend to be **ambiguous** questions — answers that are **right but not what the user intended** — the constant struggle.

## What's ahead for SIP

- Continue filling out data from systems of record that fit the current data model.
- Expand the **primary graph to additional enterprise-wide datasets**.
- Strong demand for a **federated graph experience**: a main enterprise system with **specific teams linking their own data** to it.
- More **agentic experiences** (the constrained-workflow / MCP-app direction above).

## Tools & technologies named

- **Neo4j** — knowledge graph store; off-the-shelf **MCP servers** (forked and modified).
- **MCP** — single semantic-layer interface exposing the graph to agents.
- **Claude / Claude Code / co-work / Claude chat**, **ChatGPT** — where users already are; the serving surface.
- **Data lakehouse** — consolidation layer over siloed systems of record.
- **LLM-as-judge**, **pass@1**, **stability** — retrieval eval metrics.
- **Full-text indexes**, **semantic chunking**, **derived edges** (`rollup_manages`), **additive DAG** — modeling/retrieval techniques.
