# Module 7 · The Forward-Deployed Craft

## 🔨 The build

**`builds/07-domain-twin`** _(planned)_ — pick a domain you *don't* know, run a **discovery interview**, model it as a **graph** (entities + ≥2 hierarchy lenses, stitched from ≥2 sources), serve it via **MCP**, and run an **A/B demo** answering a multi-hop question the owner cares about — your approach vs. a vector baseline. The [Gates Foundation "moat" talk](../notes/moat-is-your-data-model.md), reproduced at small scale. Dockerized (`docker compose up`).

Build it, then the sections below explain the craft around it.

## Why it matters

This is the FDE differentiator and, per the [Your Moat Is Your Data Model](../notes/moat-is-your-data-model.md) talk, the **durable** skill: models and UIs commoditize, but understanding a customer's real process — the tacit knowledge of how the work actually gets done — does not. An FDE turns that understanding into a deployed solution against messy, siloed, half-documented systems. The technical modules make you an AI engineer; this one makes you *deployable at a customer*.

## Understand in depth

- **Discovery** — sitting with domain owners to extract tacit knowledge: what each field *really* means, how systems join, the limitations/systematics of the data, safeguards, and **reporting conventions**. The goal isn't just a correct answer — it's the answer *the way it's always been given*.
- **Scoping** — finding the wedge: the narrow, high-value use case that's demoable in days, not the boil-the-ocean platform. Sequencing from wedge to platform.
- **Domain data modeling** — turning a messy org into entities, relationships, and hierarchies (funding vs. management vs. people lenses); **stitching siloed source systems** on shared entities. The modeling itself surfaces gaps in your understanding — that's a feature.
- **Demos that land** — showing the A/B contrast (naive vs. your approach) on a real question the customer cares about; the live "find the thing they didn't know" moment.
- **Integration reality** — dealing with legacy systems, dirty data, access controls, and change requests without owning the customer's whole stack. Fork-and-extend over rebuild.
- **Serving where they are** — MCP into Claude/ChatGPT/co-work surfaces instead of forcing another app; when the UI is deliberately *not* the deliverable.
- **Measuring impact & making it stick** — evals tied to the customer's reporting standards, a feedback loop with data owners, and handoff/change management so the thing survives after you leave.
- **Communication** — translating between the domain expert and the system; writing the doc that captures the tacit knowledge you extracted (this is the asset).

## Build

- [ ] Pick a domain you *don't* know (a friend's business, an open dataset with real structure). Run a **discovery interview** and produce a written tacit-knowledge doc.
- [ ] Model that domain as a graph (entities + ≥2 hierarchy lenses), stitching ≥2 separate data sources.
- [ ] Ship it as an MCP-served assistant and run a **demo** answering a multi-hop question the owner cares about; capture their reaction and the gaps it exposed.
- [ ] Write customer-facing eval questions in *their* language and run the feedback loop once.

## Checklist

- [ ] I can run a discovery interview and extract non-obvious tacit knowledge
- [ ] I can find the demoable wedge instead of scoping a platform
- [ ] I can model a real domain as entities/relationships and stitch siloed systems
- [ ] I can run an A/B demo that shows my approach beating the naive one on a real question
- [ ] I can serve into the customer's existing surface (MCP) instead of a new UI
- [ ] I produce the tacit-knowledge doc and eval set that make the work durable

## Resources

- [Your Moat Is Your Data Model](../notes/moat-is-your-data-model.md) (talk notes in this site).
- Palantir FDE writing/talks — the canonical framing of the role.
- Domain-modeling references (Neo4j graph modeling; event storming / domain-driven design basics).
