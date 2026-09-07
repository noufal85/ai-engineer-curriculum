# AI Application System Design Catalog

A catalog of 30 researched design studies. **The catalog remains unranked.** IDs are stable references for choosing what to study or build next; their order does not indicate priority. Technology names identify the options examined, not a predetermined choice for your application.

The [Amazon OpenSearch retrieval chapter](opensearch-retrieval.md) establishes the format for this collection. Each chapter explains the technology, compares alternatives, and works through two application architectures. These are design references, not deployed applications or measured benchmark results.

**Research snapshot: September 7, 2026 (UTC).** Read the source references and research-date notes in each chapter alongside its recommendations. Workload sizes and targets are illustrative unless explicitly attributed to measured evidence. Product capabilities and limitations can change; confirm them for the version and deployment you select.

## Retrieval, search, and knowledge

| ID | Design study | Example applications | Main decision to explore |
|---|---|---|---|
| R01 | [Retrieval with Amazon OpenSearch](opensearch-retrieval.md) | Enterprise knowledge assistant; product-discovery assistant | Combining lexical and semantic retrieval with filters and operational controls |
| R02 | [Retrieval with PostgreSQL and pgvector](postgres-pgvector.md) | SaaS knowledge assistant; customer-support copilot | Keeping relational data and vector retrieval together versus running a separate search service |
| R03 | [Retrieval with a dedicated vector database](vector-databases.md) | Semantic content discovery; recommendation retrieval | Comparing Pinecone, Qdrant, Weaviate, and Milvus for the actual workload |
| R04 | [Managed RAG with Amazon Bedrock Knowledge Bases](bedrock-knowledge-bases.md) | Internal document Q&A; policy assistant | Managed ingestion and retrieval versus a custom RAG pipeline |
| R05 | [Enterprise retrieval with Azure AI Search](azure-ai-search.md) | Employee knowledge portal; technical-support assistant | Search integration, identity, enrichment, and control over retrieval |
| R06 | [GraphRAG with Neo4j or Amazon Neptune](graphrag.md) | Dependency-impact assistant; relationship-based research | When explicit graph traversal adds value beyond text and vector similarity |
| R07 | [Permission-aware retrieval across multiple sources](federated-retrieval.md) | Company-wide search; customer-account research | Federated search versus a central index, with source-specific permissions and freshness |
| R08 | [Long-term memory for AI applications](long-term-memory.md) | Personal assistant; persistent customer-service assistant | What to remember, how to retrieve it, and how to correct or forget it |

## Agents, workflows, and tools

| ID | Design study | Example applications | Main decision to explore |
|---|---|---|---|
| A01 | [Durable AI workflows with Temporal or AWS Step Functions](durable-workflows.md) | Claims processing; document approval | Deterministic workflow steps versus model decisions, including retries and human review |
| A02 | [Tool-using agents with LangGraph or an agents SDK](tool-using-agents.md) | Research assistant; operations copilot | Agent loops versus bounded workflows, with explicit state and stopping conditions |
| A03 | [An MCP tool gateway for enterprise applications](mcp-tool-gateway.md) | Assistant accessing CRM, tickets, and internal APIs | Tool discovery, authentication, per-user authorization, and auditability |
| A04 | [Natural-language analytics over SQL](natural-language-sql.md) | Business metrics assistant; finance reporting copilot | Semantic definitions, validated query generation, and safe execution |
| A05 | [A coding agent with isolated execution](coding-agent-sandboxes.md) | Repository maintenance assistant; automated code repair | Sandboxes, repository context, test feedback, and approval boundaries |
| A06 | [A browser agent for business tasks](browser-agents.md) | Form-processing assistant; web research assistant | Browser automation versus direct APIs, with recovery and action verification |
| A07 | [Multi-agent task coordination](multi-agent-coordination.md) | Research-and-review workflow; complex support resolution | When specialization and parallel work justify coordination cost |

## Documents, audio, and multimodal applications

| ID | Design study | Example applications | Main decision to explore |
|---|---|---|---|
| D01 | [Document intelligence with Amazon Textract and LLMs](document-intelligence.md) | Invoice processing; insurance document intake | OCR, layout, structured extraction, validation, and human review |
| D02 | [Multimodal retrieval over text, tables, and images](multimodal-retrieval.md) | Engineering manual assistant; visual product search | Separate representations versus a shared retrieval model |
| D03 | [A real-time voice assistant](realtime-voice.md) | Voice customer service; appointment scheduling | Streaming audio, turn detection, interruptions, tool calls, and latency |
| D04 | [A meeting intelligence pipeline](meeting-intelligence.md) | Searchable meeting archive; action-item assistant | Transcription, speaker attribution, provenance, consent, and retention |
| D05 | [Video understanding and retrieval](video-retrieval.md) | Training-video assistant; media archive search | Frame sampling, transcripts, temporal indexing, and timestamped evidence |

## Model serving and inference

| ID | Design study | Example applications | Main decision to explore |
|---|---|---|---|
| S01 | [A multi-provider LLM gateway](llm-gateway.md) | Shared enterprise AI platform; resilient SaaS assistant | Routing, quotas, fallbacks, privacy boundaries, and cost attribution |
| S02 | [Self-hosted inference with vLLM or NVIDIA Triton](self-hosted-inference.md) | Private internal assistant; high-volume generation API | Managed model APIs versus GPU ownership, batching, and capacity planning |
| S03 | [An asynchronous batch inference platform](batch-inference.md) | Catalog enrichment; large-scale document classification | Queues, idempotency, throughput, backpressure, and recovery |
| S04 | [Caching for AI applications with Redis](ai-caching.md) | Repeated support queries; high-volume semantic search | Exact versus semantic caches, invalidation, tenant isolation, and stale answers |
| S05 | [Edge and on-device AI](edge-on-device-ai.md) | Offline field assistant; private personal assistant | Local models versus cloud inference, synchronization, and device constraints |

## Data pipelines, evaluation, and operations

| ID | Design study | Example applications | Main decision to explore |
|---|---|---|---|
| P01 | [Fresh retrieval indexes with Kafka or Amazon Kinesis](streaming-indexes.md) | Live catalog assistant; changing enterprise knowledge | CDC, event ordering, replay, deletions, and reindexing without stale resurrection |
| P02 | [An evaluation and observability platform for AI](evaluation-observability.md) | RAG quality dashboard; agent regression suite | Datasets, tracing, automated judges, human review, and release gates |
| P03 | [A feedback and model-adaptation pipeline](feedback-model-adaptation.md) | Domain-specific support model; specialized extraction model | Prompt changes versus retrieval improvements versus fine-tuning |
| P04 | [A secure multi-tenant AI platform](secure-multi-tenant-platform.md) | AI features shared across SaaS customers; enterprise AI workspace | Tenant isolation, model/tool access, budgets, audit trails, and data boundaries |
| P05 | [An AI incident-triage copilot](incident-triage-copilot.md) | On-call assistant; production incident investigation | Connecting telemetry, runbooks, and live tools while controlling actions |

## Choosing what to study or build next

Pick any IDs, names, or categories that interest you. We can prioritize deeper walkthroughs, experiments, and implementations based on your preferences. Writing the chapters does not assign an implementation priority.
