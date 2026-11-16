"""Attach topic and learning-mode navigation without changing published URLs."""

TOPICS = [
    {"id": key, "label": label, "url": f"topics/{key}/", "source": f"topics/{key}.md"}
    for key, label in (
        ("models", "Models & foundations"),
        ("prompting", "Prompting & context"),
        ("retrieval", "Retrieval & knowledge"),
        ("agents", "Agents & workflows"),
        ("evaluation", "Evaluation & quality"),
        ("production", "Production & delivery"),
    )
]

TOPIC_PAGES = {
    "models": (
        "curriculum/00-foundations.md", "curriculum/01-llm-internals.md",
        "labs/00-foundations.md", "labs/setup.md",
        "concepts/foundations.md", "concepts/models-and-providers.md",
        "concepts/developer-environment.md", "concepts/engineering-core.md",
        "notes/intro-to-large-language-models.md",
    ),
    "prompting": ("curriculum/02-prompting-context.md", "concepts/prompting.md"),
    "retrieval": (
        "curriculum/03-embeddings.md", "curriculum/03-rag-memory.md",
        "labs/03-embeddings.md", "concepts/retrieval-and-data.md",
        "notes/crabrag-graph-memory.md", "notes/moat-is-your-data-model.md",
        "system-design/opensearch-retrieval.md", "system-design/postgres-pgvector.md",
        "system-design/vector-databases.md", "system-design/bedrock-knowledge-bases.md",
        "system-design/azure-ai-search.md", "system-design/graphrag.md",
        "system-design/federated-retrieval.md", "system-design/long-term-memory.md",
        "system-design/document-intelligence.md", "system-design/multimodal-retrieval.md",
        "system-design/meeting-intelligence.md", "system-design/video-retrieval.md",
        "system-design/streaming-indexes.md",
    ),
    "agents": (
        "curriculum/04-agents-tools-mcp.md", "concepts/agents-and-protocols.md",
        "system-design/durable-workflows.md", "system-design/tool-using-agents.md",
        "system-design/mcp-tool-gateway.md", "system-design/natural-language-sql.md",
        "system-design/coding-agent-sandboxes.md", "system-design/browser-agents.md",
        "system-design/multi-agent-coordination.md", "system-design/realtime-voice.md",
    ),
    "evaluation": (
        "curriculum/05-evals-observability.md", "concepts/evals-and-observability.md",
        "system-design/evaluation-observability.md", "system-design/feedback-model-adaptation.md",
    ),
    "production": (
        "curriculum/06-production-systems.md", "curriculum/07-forward-deployed.md",
        "curriculum/08-capstones.md", "curriculum/specializations.md",
        "concepts/serving-and-ops.md", "concepts/platform-and-sre.md",
        "concepts/product-and-adoption.md", "concepts/safety-and-security.md",
        "system-design/llm-gateway.md", "system-design/self-hosted-inference.md",
        "system-design/batch-inference.md", "system-design/ai-caching.md",
        "system-design/edge-on-device-ai.md", "system-design/secure-multi-tenant-platform.md",
        "system-design/incident-triage-copilot.md", "career.md",
    ),
}

PAIRS = {
    "curriculum/00-foundations.md": "labs/00-foundations.md",
    "curriculum/03-embeddings.md": "labs/03-embeddings.md",
}

COURSE_STAGES = [
    ("Foundations", "stage-1-foundations", (
        ("curriculum/00-foundations.md", "Foundations & environment"),
        ("labs/00-foundations.md", "Foundations lab"),
        ("curriculum/01-llm-internals.md", "LLM internals"),
    )),
    ("Prompting & context", "stage-2-prompting", (
        ("curriculum/02-prompting-context.md", "Prompting & context engineering"),
    )),
    ("Retrieval & knowledge", "stage-3-retrieval", (
        ("curriculum/03-embeddings.md", "Embeddings"),
        ("labs/03-embeddings.md", "Embeddings lab"),
        ("curriculum/03-rag-memory.md", "Retrieval, RAG & memory"),
    )),
    ("Agents & workflows", "stage-4-agents", (
        ("curriculum/04-agents-tools-mcp.md", "Agents, workflows, tools & MCP"),
    )),
    ("Evaluation & production", "stage-5-evaluation-and-production", (
        ("curriculum/05-evals-observability.md", "Evals & observability"),
        ("curriculum/06-production-systems.md", "Production systems, platform & security"),
    )),
    ("Delivery & capstone", "stage-6-delivery-and-capstone", (
        ("curriculum/07-forward-deployed.md", "Forward-deployed craft"),
        ("curriculum/08-capstones.md", "Capstones"),
    )),
]
COURSE = [source for _, _, steps in COURSE_STAGES for source, _ in steps]

INLINE_LABS = set(COURSE) - set(PAIRS) - set(PAIRS.values()) - {"curriculum/08-capstones.md"}


def page_url(source):
    if source == "index.md":
        return "./"
    if source.endswith("/index.md"):
        return source[:-8]
    return source[:-3] + "/"


def course_for(source, available):
    steps = [
        (target, label, number, title, anchor)
        for number, (title, anchor, group) in enumerate(COURSE_STAGES, start=1)
        for target, label in group
        if target in available
    ]
    current = next((i for i, step in enumerate(steps) if step[0] == source), None)
    if current is None:
        return None

    def link(index):
        if not 0 <= index < len(steps):
            return None
        target, label, *_ = steps[index]
        return {"source": target, "label": label, "url": page_url(target)}

    _, label, stage_number, title, anchor = steps[current]
    return {
        "position": current + 1,
        "total": len(steps),
        "label": label,
        "stage": {
            "number": stage_number, "total": len(COURSE_STAGES),
            "title": title, "url": "curriculum/#" + anchor,
        },
        "plan_url": "curriculum/",
        "previous": link(current - 1),
        "next": link(current + 1),
    }


def workspace_for(source, available):
    topic = next((item for item in TOPICS if source == item["source"] or source in TOPIC_PAGES[item["id"]]), None)
    if source.startswith("papers/"):
        topic = TOPICS[0]
    kind = {
        "curriculum": "Explanation", "labs": "Practice", "concepts": "Reference",
        "system-design": "Design study", "papers": "Paper guide", "notes": "Talk notes",
        "topics": "Topic guide",
    }.get(source.split("/")[0], "Reference")
    if source.endswith("index.md") or source == "system-design/catalog.md":
        kind = "Explore"
    tabs = []
    for explanation, practice in PAIRS.items():
        if source in (explanation, practice):
            tabs = [
                {"label": label, "source": target, "url": page_url(target), "active": source == target}
                for label, target in (("Understand", explanation), ("Practice", practice))
                if target in available
            ]
            break
    if source in INLINE_LABS:
        anchor = "lab-build-tasks" if source == "curriculum/01-llm-internals.md" else "lab"
        tabs = [
            {"label": "Understand", "source": source, "url": page_url(source), "active": True},
            {"label": "Practice", "source": source, "url": page_url(source) + "#" + anchor, "active": False},
        ]
    return {
        "topic": topic,
        "kind": kind,
        "tabs": tabs,
        "course": course_for(source, available),
        "is_hub": source == "index.md" or source.startswith("topics/"),
    }


def on_config(config):
    config.extra["workspace_topics"] = TOPICS
    return config


def on_page_markdown(markdown, page, config, files):
    available = {file.src_uri for file in files.documentation_pages()}
    page.meta["workspace"] = workspace_for(page.file.src_uri, available)
    return markdown
