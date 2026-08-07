# CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens

**Speaker:** Stephen Chin — Head of Developer Relations, Neo4j
**Source:** [youtube.com/watch?v=Q0VkgCyNVUg](https://www.youtube.com/watch?v=Q0VkgCyNVUg)

---

## Thesis

Two copies of the same agent were given the same facts about a home network. One stored them in a **vector database**, the other in a **graph**. Asked the same operational security questions, the vector agent couldn't produce specifics; the graph agent traversed the connections and returned precise, actionable answers. **Same source data — the storage model is the only variable.** Similarity in vector space is not a relationship, so multi-hop questions fail on vectors and succeed on graphs.

## The agent memory loop

The agent cycle is prompt → think about the response → call tools → observe what happens. The hard part is **memory**: what you put into context and what you recall from. Everything below is about how that memory is stored.

## Markdown-file memory

Most tools structure memory as **markdown files**. Taking OpenClaw as the example, you have:

- Agent memory (`AGENTS.md` / "solved" file)
- Memory files
- Tool files
- Daily memory files

They are all markdown. Advantages: human-readable, easy to scan, easy to compact (spot what's not needed and drop it), and intentionally kept **small** — because the context window is limited and you need the right things at the **top** of context.

**The cost:** if your entire memory is markdown, you waste tokens. In practice these agents load **at least ~100k tokens per round**. They run many skills and add to context constantly; it's highly repetitive because the agent loads up **everything** in the hope that something in it turns out useful.

- **Small scale:** works — with a high-quality model and small data you get the answers you want.
- **Large scale:** does not work.

## Skills are also markdown

- **Hermes agent** has a stronger memory system: at the end of each task it **reflects** and adds back new skills / new things it needs. Powerful, but still relies heavily on markdown files.
- **Skills are basically markdown files.** You can teach an agent a lot with skills, and if the **right** skill gets loaded, good things happen — but sometimes the wrong skill loads, or you need the right **chain** of skills rather than a single one.
- Neo4j (work by Bennet) has an **arXiv paper on a "graph for skills"** — using a graph to figure out which skills are the right ones.

## Goose: memory as an MCP server

- **Goose** is part of the **Agentic AI Foundation** — a new foundation that MCP is part of, backed by Anthropic; Neo4j is also a member.
- It's an automation tool for enterprise workflows, also usable as a personal assistant. It relies heavily on **MCP as the layer**, with **over 70 MCP extensions**.
- It treats **memory as just another MCP server** — pluggable, with commands to **retrieve**, **remember**, and **forget** memories.
- Memories are still **plain files on disk**, so they're directly manipulable. Same idea, same fundamental problem: agent memory is stored as markdown files on disk.
- **Failure mode:** with MCP tools exposed, the agent is one step away from calling the **`forget`** command and wiping its own memory.

## Vector databases

- Store everything, create **embeddings**, put them in a **vector database**, and run **similarity searches** to pull back relevant information. A real improvement: large knowledge repository, related info retrievable.
- **OpenClaw ships with PGVector out of the box** — given an embedding, you can start using it immediately.
- **LanceDB** is another strong option. Both PGVector and LanceDB are used in the demo.

**The core limitation:** what a vector gives you is **similarity in vector space, which is not the same as an actual relationship.** Consequences:

- **Hallucinations** and general problems when vector lookup is the *sole* source of the answer.
- The problem **compounds** in complex scenarios (e.g. a digital twin).
- **Large multi-hop reasoning chains don't work** on similarity search — sometimes it's **impossible to reach the answer even when all the facts are present**, because the chain of hops isn't a similarity relationship.
- Multi-hop is also **very expensive on traditional relational databases**.
- Things that **look similar aren't exactly the same** — you retrieve facts that are "related in some way" but are not the correct item.

## Graphs

Graphs are built for **connected data** — finding relationships, resolving identities, mapping paths, and getting the **full chain**.

- **Structure:** first-class **nodes** (entities), **edges** (relationships between objects), and **properties** on top to store information.
- You can also **store embeddings inside the graph**, which lets you use **vectors and graphs together**.

**Demo architecture — hybrid vector + graph retrieval:**

1. **Vector search** selects the **seed nodes** where traversal starts.
2. **Graph search** pulls the **nearest neighbors** of those seeds and **ranks them by how related they are**.

This combination solves **complex multi-hop queries** for more difficult, domain-specific problems.

**Why graphs win on quality:**

- **Accurate** — precise information.
- **Explainable** — you can inspect the graph that was returned.
- **Auditable** — you can point to the exact part of the graph that produced the answer.

This gives the developer more control: when the answer is wrong you know where it came from, you can **introspect the graph**, change how **extraction** is done, **reduce duplicate nodes**, and **converge quickly** on a good answer.

**Claude + Cypher:**

- You don't need to be a graph expert — **Claude writes Cypher** (per the speaker, better than he does), can **build entity extractors**, and can do most of what's needed to get started, as long as you know the basic model of what you want.
- **Working pattern:** have Claude **write each action into the graph as it works**; then answer by **traversing the graph, not re-reading** it; in a **fresh session**, pull the results back out.

## Demo: home-lab digital twin, A/B tested

**Setup (built over the prior week or two):**

- A full **digital twin** of the speaker's home lab, modeled as a graph.
- **Two environments built from the same original markdown files:**
  - **A test — vector database store**
  - **B test — graph store**, built on **Cognee** (a memory-space startup with a **Neo4j backend**)
- **Hardware/topology:** a handful of **Proxmox** servers (a couple of computers around a desk). A **separate VLAN** was built for the demo, **segmented off the real network**.
- The model was **trained on the real network** but then **cut off** — it can **only answer from memory**, cannot look up hosts, and cannot pull dynamic information.
- Interface: a "GrabRAG cockpit" with **five questions queued**, each with schematics matching the home-lab diagram.

### Query 1 — WAN-exposed end-of-life software

Goal: find anything exposed to the WAN/internet running out-of-date software that puts the lab at risk.

- **Expected finding:** a host named **"Tinkster Lands"** — the speaker's **daughter's Minecraft server**, running **Debian 8 (Jessie)**.
- **Vector agent:** "couldn't find specific details… excluded by policy… check sources separately." Not useful.
- **Graph agent:** fired off a series of **Cypher queries** and ran a **graph traversal**, color-coded:
  - **Blue nodes** = **seed nodes** (from the vector lookup + ranking) — traversal doesn't stop here.
  - **Gray nodes** = **one-hop traversals** from the seeds.
  - **Green nodes** = the ones that **won** and made it **into context**.
  - **Answer:** guest name **Tinksterlin**, **OS version out of date**, flagged — precise and actionable.

### Query 2 — Exposed `0.0.0.0` management ports

Goal: find management ports bound to `0.0.0.0` and exposed to the outside world (a bad configuration).

- **Ground truth:** a newly set-up **Matrix server** and **HAProxy** were exposed to the internet (bad); other services (the Cognee demo, the OpenClaw instance) were **inside the LAN** and only reachable from within it (correct).
- **Vector agent:** returned some info but told the user to go **check the services configuration / expects a pfSense rule** — i.e., punted the work back to the human.
- **Graph agent:** found an **open port exposed to the WAN** on **HAProxy and OpenVPN** (the two expected). The **shape of this graph was entirely different** from Query 1: it located the **pfSense router** node and **followed it directly** to every result related to it, yielding a precise answer.
- **Aftermath:** all the identified security holes were **patched after the demo**.

## Scale argument

A 3–4 node home lab is trivial. But for a **large enterprise data center**, **financial services** (huge sets of companies and customer records), or **anything at a scale that doesn't fit into the ~1M-token context window** of modern models, throwing everything into markdown files stops working — you need a real memory system (graph-backed).

## Tools & technologies named

- **OpenClaw** — markdown-file memory; ships with **PGVector**.
- **Hermes agent** — reflect-and-write-back skill memory.
- **Goose** (Agentic AI Foundation) — MCP-based, 70+ extensions, memory as an MCP server.
- **PGVector**, **LanceDB** — vector stores used in the demo.
- **Cognee** — memory startup, Neo4j backend; powers the graph store.
- **Neo4j**, **Cypher** — graph DB and query language.
- **Proxmox**, **pfSense**, **HAProxy**, **OpenVPN**, **Matrix** — home-lab infrastructure in the digital twin.
- **Neo4j GraphAcademy** — free training (`dev.neo4j.com/ga-rag`), incl. agent-memory and context-graph courses.
