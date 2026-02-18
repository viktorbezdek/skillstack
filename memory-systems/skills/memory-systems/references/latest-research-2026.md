# Agent Memory Systems: Latest Research 2025-2026

**Last updated:** 2026-03-14
**Research scope:** Production frameworks, benchmarks, academic advances, and integration patterns

---

## Table of Contents

1. [Benchmark Landscape](#benchmark-landscape)
2. [Production Frameworks: Detailed State](#production-frameworks)
   - [Mem0](#mem0)
   - [Zep / Graphiti](#zep--graphiti)
   - [Letta](#letta)
   - [Cognee](#cognee)
   - [LangMem](#langmem)
3. [Emerging Frameworks & Research Systems](#emerging-frameworks)
4. [Temporal Knowledge Graph Advances](#temporal-knowledge-graph-advances)
5. [Benchmark Results: Head-to-Head Numbers](#benchmark-results)
6. [Production Patterns at Scale](#production-patterns-at-scale)
7. [Integration Patterns](#integration-patterns)
8. [Academic Survey: Memory Taxonomy](#academic-survey-memory-taxonomy)
9. [Sleep-Time Compute](#sleep-time-compute)
10. [Decision Matrix: Choosing a Framework](#decision-matrix)

---

## Benchmark Landscape

### Active Benchmarks (2025-2026)

| Benchmark | Description | Key Metrics |
|-----------|-------------|-------------|
| **LoCoMo** | Snap Research. 300-turn, 9K-token conversations over 35 sessions. Tests QA, event summarization, multimodal dialogue. | Exact Match, F1, BLEU-1 |
| **LongMemEval** | 500 manually-created questions testing: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, abstention. | LLM-as-a-Judge, Accuracy |
| **LongMemEval_S / _SS** | Shortened variants for faster iteration. | Same metrics, different scale |
| **DMR (Deep Memory Retrieval)** | Role-based conversation retrieval task from LoCoMo labels. | Accuracy % |
| **HotPotQA** | Multi-hop question answering. Used for graph memory evaluation. | EM, F1, Human-like Correctness |
| **AIME / GSM** | Math benchmarks used for sleep-time compute evaluation. | Accuracy |
| **Terminal-Bench** | AI coding benchmark; Letta Code is #1 model-agnostic open-source agent. | Score |

**Sources:**
- [LoCoMo](https://snap-research.github.io/locomo/)
- [LongMemEval ICLR 2025](https://arxiv.org/pdf/2410.10813)
- [MEMTRACK 2025](https://arxiv.org/pdf/2510.01353)

---

## Production Frameworks

### Mem0

**Status:** Most widely adopted. YC-backed. $24M total funding as of early 2026. 50,000+ developers.

**Architecture:** Triple-store design per memory: vector store (semantic search), key-value store (fast lookups), graph database (relational queries). Hierarchical memory at user, session, and agent levels.

**Key paper:** [arXiv:2504.19413](https://arxiv.org/abs/2504.19413) — "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory" (April 2025)

**LoCoMo Benchmark Results (from arXiv:2504.19413):**
- Mem0 overall LLM-as-a-Judge score: **66.9%** vs OpenAI Memory: **52.9%** — a **26% relative improvement**
- Mem0 with graph memory (Mem0g): ~**68.5%** (~2% above base)
- p95 latency: **1.44s** vs full-context **17.12s** — **91% lower latency**
- Token consumption: ~**1.8K tokens/conversation** vs full-context **26K** — **90% reduction**
- Outperforms across all four question types: single-hop, temporal, multi-hop, open-domain

**Graph Memory (January 2026):**
Graph memory is an optional add-on that captures entity-relationship structures alongside vector embeddings. Graph operations run concurrently via `ThreadPoolExecutor`. Available at Pro tier ($249/month cloud) or self-hosted with Neo4j.

**Pricing:** $0 (free tier) → $19/month → $249/month. Open-source self-hosted available.

**Integrations:** Python SDK, JavaScript SDK, OpenAI, LangGraph, CrewAI, Vercel AI SDK.

**Sources:**
- [Mem0 Research Page](https://mem0.ai/research)
- [Mem0 arXiv Paper](https://arxiv.org/abs/2504.19413)
- [Graph Memory Blog Jan 2026](https://mem0.ai/blog/graph-memory-solutions-ai-agents)
- [AI Memory Layer Guide Dec 2025](https://mem0.ai/blog/ai-memory-layer-guide)

---

### Zep / Graphiti

**Status:** Cloud-only managed service + open-source Graphiti engine. Credit-based pricing ($0 → $25/month+).

**Paper:** [arXiv:2501.13956](https://arxiv.org/abs/2501.13956) — "Zep: A Temporal Knowledge Graph Architecture for Agent Memory" (January 2025). Presented at KGC 2025.

**Core technology:** Graphiti — a temporally-aware knowledge graph engine that synthesizes unstructured conversational data and structured business data while maintaining historical relationships.

**Bi-Temporal Model:** Each graph edge carries four timestamps:
- `t_created` / `t_expired`: when the fact was recorded or invalidated in the system
- `t_valid` / `t_invalid`: when the fact was actually true in the real world

This enables non-lossy updates — historical states remain queryable.

**Hierarchical Graph Structure (mirrors human memory):**
1. **Episodic subgraph** — raw conversation data
2. **Semantic subgraph** — extracted entities and facts
3. **Community subgraph** — high-level domain summaries

**Retrieval:** Hybrid search combining semantic embeddings + BM25 keyword search + direct graph traversal. No LLM calls during retrieval. P95 latency: **300ms**.

**Benchmark Results:**
- DMR: **94.8%** accuracy (vs MemGPT 93.4%)
- LongMemEval: up to **18.5% accuracy improvement** over baseline, **90% latency reduction**

**Important caveat:** Zep's published LoCoMo score of 84% was challenged in [GitHub Issue #5 on zep-papers](https://github.com/getzep/zep-papers/issues/5), with a corrected evaluation producing **58.44%** accuracy. Treat headline numbers with caution.

**Sources:**
- [Zep arXiv Paper](https://arxiv.org/abs/2501.13956)
- [Graphiti GitHub](https://github.com/getzep/graphiti)
- [Neo4j Graphiti Blog](https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/)
- [KGC 2025 Talk](https://watch.knowledgegraph.tech/videos/zep-a-temporal-knowledge-graph-architecture-for-agent-memory-720p)

---

### Letta

**Status:** Formerly MemGPT. $10M raised. LLM-as-an-Operating-System paradigm. Most architecturally ambitious.

**Core concept:** Agents actively manage their own memory. Memory is a first-class component of agent state. Agents edit memory blocks using specialized tools rather than relying on passive retrieval.

**Key 2025-2026 Developments:**

| Feature | Date | Description |
|---------|------|-------------|
| New architecture for reasoning models | Oct 2025 | Optimized for Claude Sonnet 4.5's advanced memory tool capabilities |
| Letta Evals | Oct 2025 | Open-source evaluation framework for stateful agents |
| Conversations API | Jan 2026 | Shared memory across parallel user experiences |
| Context Repositories | Feb 12, 2026 | Git-backed memory filesystem (MemFS) for coding agents |
| Letta Code | 2026 | #1 model-agnostic open-source agent on Terminal-Bench |

**Context Repositories (Feb 2026):** A breakthrough for coding agents. Agent's context stored as git-tracked markdown files in MemFS. Each memory file has frontmatter (description, character limit, read-only flag). Multiple subagents can process memory concurrently using isolated git worktrees. Merges via git conflict resolution. Every memory change is versioned with commit messages.

**Benchmarking insight from Letta:** Their filesystem-based agent achieved **74.0% on LoCoMo** with GPT-4o mini, using only `grep`, `search_files`, `open`, `close` tools — outperforming Mem0's graph variant (68.5%). Key finding: "Memory effectiveness depends more on agent architecture, its tools, and the underlying model than on specific retrieval mechanisms."

**Sources:**
- [Letta Blog Research](https://www.letta.com/blog-categories/research)
- [Benchmarking AI Agent Memory](https://www.letta.com/blog/benchmarking-ai-agent-memory)
- [Context Repositories Blog](https://www.letta.com/blog/context-repositories)
- [Sleep-Time Compute](https://www.letta.com/blog/sleep-time-compute)
- [Stateful Agents Blog](https://www.letta.com/blog/stateful-agents)

---

### Cognee

**Status:** Open-source memory engine. $7.5M seed led by Pebblebed (backed by OpenAI and FAIR founders). Pipeline volume grew 500x in 2025 (2K → 1M+ runs).

**Core pipeline (6 stages):** classify → check permissions → extract chunks → LLM entity/relationship extraction → generate summaries → embed + commit to vector store and graph.

**"Memify" layer:** Post-ingestion graph refinement. Prunes stale nodes, strengthens frequent connections, reweights edges based on usage signals. Memory is an evolving structure, not static storage.

**HotPotQA Benchmark (Aug 2025, Cognee's own evaluation — 45 cycles, 24 questions):**
- Cognee 2025.1 Human-like Correctness: **0.93**
- Significantly outperformed: Mem0 2025.2, LightRAG 2025.0, Graphiti 2025.1
- With CoT retriever optimization: **+25% human-like correctness**, **+16-18% DeepEval EM**
- Note: Graphiti numbers were self-reported, not independently verified by Cognee team

**Recent integrations (2025-2026):**
- December 2025: Persistent memory for Claude Agent SDK via MCP
- March 2026: ScrapeGraphAI integration for live web data → knowledge graph
- OpenClaw AI memory plugin architecture

**Sources:**
- [Cognee GitHub](https://github.com/topoteretes/cognee)
- [Cognee Memory Benchmarks Aug 2025](https://www.cognee.ai/blog/deep-dives/ai-memory-evals-0825)
- [Cognee $7.5M Seed](https://www.cognee.ai/blog/cognee-news/cognee-raises-seven-million-five-hundred-thousand-dollars-seed)
- [Cognee September 2025 Updates](https://www.cognee.ai/blog/cognee-news/cognee-september-updates)

---

### LangMem

**Status:** LangChain's official memory library. Free open-source. Python-only. No knowledge graphs. Self-hosted only.

**SDK launch:** Early 2025. Native integration with LangGraph's Long-term Memory Store.

**Memory types:**
- **Semantic** — facts and knowledge
- **Episodic** — past experiences as few-shot examples
- **Procedural** — learned how-to knowledge, saved as updated agent prompt instructions

**Key components:**
- Memory management tools for in-conversation recording and search
- Background memory manager — auto-extracts, consolidates, and updates knowledge between sessions
- `ReflectionExecutor` — handles memory updates asynchronously in background
- Multiple prompt optimization algorithms: `metaprompt` (reflection + thinking time), `gradient` (critique + proposal), `prompt_memory` (simple)

**Storage backends:** Works with any store. Common production pattern: PostgreSQL + pgvector via `PostgresStore`.

**Framework dependency:** Requires LangGraph. Best for teams already on LangGraph stack.

**Sources:**
- [LangMem Docs](https://langchain-ai.github.io/langmem/)
- [LangMem SDK Launch Blog](https://blog.langchain.com/langmem-sdk-launch/)
- [LangMem GitHub](https://github.com/langchain-ai/langmem)
- [LangMem PyPI](https://pypi.org/project/langmem/)

---

## Emerging Frameworks

### A-MEM (arXiv:2502.12110) — NeurIPS 2025
Zettelkasten-inspired agentic memory. When a memory is added, generates a structured note with contextual descriptions, keywords, and tags. Analyzes historical memories to establish links. New memories trigger updates to existing memory representations. Empirically outperforms SOTA on six foundation models.
- [arXiv](https://arxiv.org/abs/2502.12110) | [GitHub (WujiangXu)](https://github.com/WujiangXu/A-mem) | [GitHub (agiresearch)](https://github.com/agiresearch/A-mem)

### ENGRAM (arXiv:2511.12960)
Lightweight memory orchestration using typed memories, minimal routing, dense-only retrieval with set aggregation.

**LongMemEval_S results:**
- Overall LLM-as-a-Judge: **71.40%** (vs full-context control 56.20%)
- Token reduction: **~99%** (~1.0K-1.2K tokens/query)

**ENGRAM-R (extended) on LongMemEval_SS:**
- Accuracy improvement: **+21.8 pp** overall (+30.1 pp multi-session, +13.5 pp temporal)
- Input token reduction: **95.5%**
- Reasoning token reduction: **77.8%**
- [arXiv](https://arxiv.org/abs/2511.12960)

### MemoryOS (arXiv:2506.06326) — EMNLP 2025 Oral
Memory Operating System for personalized AI agents. Three-tier storage: short-term → mid-term → long-term personal memory.

**LoCoMo benchmark (GPT-4o-mini):**
- F1 improvement: **+49.11%** over baselines
- BLEU-1 improvement: **+46.18%** over baselines
- [arXiv](https://arxiv.org/abs/2506.06326) | [GitHub](https://github.com/BAI-LAB/MemoryOS)

### EverMemOS (EverMind, Dec 2025)
Brain-inspired four-layer architecture: Agentic (prefrontal cortex) → Memory (cortical networks) → Index (hippocampus) → API/MCP Interface. Converts raw text to semantic MemUnits organized in adaptive memory graphs.

**Benchmark results:**
- LoCoMo: **92.3% accuracy**
- LongMemEval-S: **82% accuracy**

"Surpassing LLM full-context performances with far fewer tokens."
- [EverMind](https://evermind.ai/) | [EverMemOS GitHub](https://github.com/EverMind-AI/EverMemOS) | [PR Newswire announcement](https://www.prnewswire.com/news-releases/evermemos-redefines-efficiency-in-ai-memory-surpassing-llm-full-context-perfomances-with-far-fewer-tokens-in-open-evaluation-302645884.html)

### U-Mem / Autonomous Memory Agents (arXiv:2602.22406)
- HotpotQA improvement: **+14.6 points** (Qwen2.5-7B)
- AIME25 improvement: **+7.33 points** (Gemini-2.5-flash)
- [arXiv](https://arxiv.org/html/2602.22406)

### E-mem (arXiv:2601.21714)
Multi-agent episodic context reconstruction for ultra-long contexts.
- HotPotQA: highest F1 scores across all baselines in 1600-doc setting
- E-mem vs RAG: **+7.29% F1** (1600-doc setting)
- [arXiv](https://arxiv.org/html/2601.21714)

### LiCoMemory
- LongMemEval: **73.8% accuracy / 76.6% recall** with GPT-4o-mini
- Latency reduction: **10-40%** consistently

### SimpleMem (March 2026)
New lightweight memory framework announced March 3, 2026. Positions as low-overhead alternative to full graph systems.
- [BrightCoding Blog](https://www.blog.brightcoding.dev/2026/03/03/simplemem-the-revolutionary-memory-system-every-ai-agent-needs)

### MemoClaw
- Memory-as-a-Service with crypto wallet authentication (no API keys)
- Pay-per-use: $0.001/operation
- Importance scoring for memory ranking
- No entity modeling, no self-hosting

---

## Temporal Knowledge Graph Advances

The most significant architectural advance of 2025 is the **bi-temporal model** for knowledge graphs, pioneered primarily by Zep/Graphiti and adopted widely.

### Bi-Temporal Pattern

```
Fact: "User works at Acme Corp"
  t_valid:   2024-01-01  (when it became true)
  t_invalid: 2025-06-15  (when it was superseded)
  t_created: 2024-01-05  (when system learned it)
  t_expired: 2025-06-20  (when system recorded the change)
```

This enables:
- Querying the world state at any past point in time
- Distinguishing when something happened from when we learned about it
- Non-lossy updates — no information is ever deleted, only superseded

### Community Subgraphs / Hierarchical Organization
Emerging pattern in 2025: three-tier graph hierarchies:
1. **Episodic** — raw conversation events with timestamps
2. **Semantic** — extracted entities, facts, relationships
3. **Community** — high-level domain summaries built via graph clustering

This mirrors the cognitive science hierarchy of human memory and enables different retrieval strategies at each level.

### Hybrid Retrieval (2025 Standard)
All competitive systems now implement hybrid retrieval combining:
- **Vector similarity** (dense embeddings, cosine/dot product)
- **BM25 keyword search** (sparse, exact term matching)
- **Graph traversal** (entity relationship paths)

Zep Graphiti's hybrid retrieval achieves **P95 = 300ms** with no LLM calls during retrieval.

### Dynamic Graph Updates
2025 introduced "memify" patterns (Cognee's term) where graphs are continuously refined:
- Prune stale nodes based on staleness + usage signals
- Strengthen frequently-accessed connections
- Reweight edges based on interaction traces
- Self-improving memory graphs vs static storage

### KuzuDB as Embedded Graph Backend
For production systems needing embedded graph storage (vs cloud Neo4j), KuzuDB has emerged as a high-performance alternative:
- **374x faster** on 2nd-degree path queries vs Neo4j (0.009s vs 3.22s)
- **40.8x faster** on filtered path-finding
- **53x faster** on ingestion (100K nodes, 2.4M edges)
- Vela Partners maintains a fork with concurrent write support for multi-agent workloads
- [KuzuDB GitHub](https://github.com/kuzudb/kuzu) | [Vela Partners benchmark blog](https://www.vela.partners/blog/kuzudb-ai-agent-memory-graph-database)

**Sources:**
- [Zep Temporal KG Paper](https://arxiv.org/abs/2501.13956)
- [Cognee Architecture](https://www.cognee.ai/blog/fundamentals/how-cognee-builds-ai-memory)
- [Neo4j Temporal KG at Nodes 2025](https://neo4j.com/nodes-2025/agenda/building-evolving-ai-agents-via-dynamic-memory-representations-using-temporal-knowledge-graphs/)

---

## Benchmark Results: Head-to-Head Numbers

### LoCoMo Benchmark Summary

| System | Score | Notes |
|--------|-------|-------|
| EverMemOS | 92.3% accuracy | Self-reported, Dec 2025 |
| Letta Filesystem (GPT-4o mini) | 74.0% accuracy | Independent Letta evaluation |
| Mem0 (base) | 66.9% LLM-as-Judge | arXiv:2504.19413 |
| Mem0 with graph (Mem0g) | ~68.5% | ~2% above base |
| OpenAI Memory | 52.9% LLM-as-Judge | arXiv:2504.19413 comparison |
| MemoryOS (GPT-4o-mini) | +49% F1 over baselines | EMNLP 2025 |
| Zep (claimed) | 84% | Disputed; corrected eval: 58.44% |

### LongMemEval Results

| System | Score | Token Efficiency |
|--------|-------|-----------------|
| EverMemOS | 82% (LongMemEval-S) | Far fewer tokens than full-context |
| ENGRAM-R (LongMemEval_SS) | +21.8 pp overall | 95.5% input token reduction |
| ENGRAM (LongMemEval_S) | 71.40% LLM-as-Judge | ~99% token reduction (1K-1.2K tokens/query) |
| Full-context baseline | 56.20% | 26K tokens/conversation |
| LiCoMemory | 73.8% accuracy, 76.6% recall | 10-40% latency reduction |
| Zep | +18.5% over baseline | 90% latency reduction |

### DMR Benchmark

| System | Accuracy |
|--------|----------|
| Zep/Graphiti | 94.8% |
| MemGPT | 93.4% |

### HotPotQA (Cognee eval, 45 cycles, 24 questions)

| System | Human-like Correctness |
|--------|----------------------|
| Cognee 2025.1 (with CoT) | 0.93 + 25% improvement |
| Cognee 2025.1 (baseline) | 0.93 |
| LightRAG 2025.0 | Lower (close on Human-like C.) |
| Graphiti 2025.1 | Reliable mid-range |
| Mem0 2025.2 | Lowest across all metrics |

**Important methodology note:** Each organization uses different evaluation setups. Direct numerical comparison across benchmarks is unreliable. Prefer controlled experiments holding framework and tools constant (Letta's approach).

---

## Production Patterns at Scale

### The Memory Infrastructure Stack (2025 Standard)

**Tier 1 — Hot Working Memory**
- Technology: Redis
- Contents: Current task state, tool outputs, recent messages
- TTL: Session duration
- Characteristic: Sub-millisecond reads, ephemeral

**Tier 2 — Persistent Semantic Memory**
- Technology: pgvector, Pinecone, Weaviate, Qdrant
- Contents: Embedding vectors, semantic memories
- Operations: cosine similarity search, HNSW index
- Characteristic: 10-50ms reads at scale

**Tier 3 — Relational/Graph Memory**
- Technology: Neo4j, KuzuDB, Memgraph
- Contents: Entity relationships, temporal facts
- Operations: Multi-hop path queries, community detection
- Characteristic: 50-300ms for complex traversals

**Tier 4 — Decision Trace / Audit Logs**
- Technology: Structured logs (Postgres, S3)
- Contents: Every prompt, response, decision made
- Compliance: SOC2 CC6.3, ISO 27001 A.12.4.1 (PII masking required)

### Memory Compaction Pattern
Rather than "context stuffing," 2025 production systems use:
1. LLM-based summarization of older events (sliding window)
2. Write summaries back as new events
3. Gradual replacement of raw transcripts with semantic summaries
4. Mem0 reports **80% prompt token reduction** via this approach

### Multi-Agent Memory Architecture
Challenge: Multiple agents sharing and updating memory concurrently.

**Letta's approach (Feb 2026):** Git-based MemFS with isolated worktrees per subagent. Concurrent writes without locking. Merges via git conflict resolution. Informative commit messages on every change.

**Mem0's approach:** ThreadPoolExecutor for concurrent graph + vector operations. Hierarchical scoping: per-user, per-session, per-agent.

**Zep's approach:** Bi-temporal KG with append-only semantics. No destructive updates. Concurrent readers, controlled writers.

### Market Context (March 2026)
- Dedicated memory layer market: **$55M+ venture funding** total
- Mem0: $24M total
- Cognee: $7.5M seed
- Letta: $10M
- Most popular OSS: Mem0 (50K+ developers)

---

## Integration Patterns

### Claude Code + MCP Memory

Claude Code integrates memory via the Model Context Protocol (MCP). Available servers as of 2026:

| Server | Backend | Key Feature |
|--------|---------|-------------|
| Cognee MCP (Dec 2025) | Neo4j + vector | Persistent knowledge graph, semantic search |
| MCP Memory Keeper | SQLite | Context management across sessions |
| claude-mem | Claude Agent SDK | Auto-captures, compresses, re-injects session context |
| Neo4j Memory MCP | Neo4j | Intelligent memory, relationship mapping |
| Basic Memory | Markdown + SQLite | Searchable notes, semantic connections, spans projects |
| WhenMoon Memory MCP | SQLite + FTS5 | Lightweight, fully local, TypeScript |

**Configuration pattern:**
```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

**Sources:**
- [Claude Code MCP Docs](https://code.claude.com/docs/en/mcp)
- [Cognee Claude SDK Integration](https://www.cognee.ai/blog/integrations/what-is-openclaw-ai-and-how-we-give-it-memory-with-cognee)
- [Basic Memory for Claude Code](https://docs.basicmemory.com/integrations/claude-code/)
- [claude-mem GitHub](https://github.com/thedotmack/claude-mem)

---

### LangGraph Memory Integration

**Native memory store pattern:**
```python
# Development
store = InMemoryStore()

# Production
store = PostgresStore(connection_string="postgresql://...")

# Retrieval in pre-model hook
memories = store.search(query, namespace=("user", user_id))
system_prompt += f"\nRelevant memories: {memories}"

# Storage in post-model hook
store.put(namespace, key, {"content": memory, "timestamp": now})
```

**Background memory extraction with LangMem:**
```python
from langmem import ReflectionExecutor, create_memory_manager

manager = create_memory_manager(
    model="claude-3-5-sonnet",
    storage=PostgresStore(...)
)
executor = ReflectionExecutor(manager)
# Runs async after each conversation
```

**MongoDB integration (2025):** `langgraph-store-mongodb` package provides `MongoDBStore` with native JSON document storage and Atlas Vector Search for semantic retrieval.

**AWS Bedrock AgentCore (2025):** `Integrate AgentCore Memory with LangChain or LangGraph` — managed memory tier on AWS infrastructure.

**Sources:**
- [LangGraph Memory Docs](https://docs.langchain.com/oss/python/langgraph/add-memory)
- [MongoDB + LangGraph](https://www.mongodb.com/company/blog/product-release-announcements/powering-long-term-memory-for-agents-langgraph)
- [AWS Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-integrate-lang.html)
- [Infinite Memory with LangGraph + Postgres (Nov 2025)](https://medium.com/@alonjamanjeetsinh77/building-infinite-memory-agents-a-master-guide-to-langgraph-langmem-and-postgres-05b3cabd689b)

---

### CrewAI Memory Integration

CrewAI's built-in memory system provides: short-term, long-term, entity, and contextual memory.

**Cognee integration:**
```python
from crewai import Crew
from cognee.api.v1.cognify import cognify

crew = Crew(agents=[...], tasks=[...])
# Pre-task: load relevant memory from cognee knowledge graph
await cognify(conversation_history)
# Post-task: store outputs back
```

**Mem0 + CrewAI production pattern:**
```python
from mem0 import MemoryClient
from crewai import Agent

memory = MemoryClient(api_key="...")

class MemoryAgent(Agent):
    def execute(self, task):
        memories = memory.search(task.description, user_id=self.user_id)
        enriched_context = f"{task.description}\n\nRelevant history: {memories}"
        result = super().execute(Task(description=enriched_context))
        memory.add(result, user_id=self.user_id)
        return result
```

**Sources:**
- [CrewAI Memory Docs](https://docs.crewai.com/en/concepts/memory)
- [CrewAI Cognitive Memory Blog](https://blog.crewai.com/how-we-built-cognitive-memory-for-agentic-systems/)
- [Mem0 + CrewAI Production Setup](https://mem0.ai/blog/crewai-memory-production-setup-with-mem0)
- [Cognee + CrewAI Integration](https://www.cognee.ai/blog/deep-dives/crewai-memory-with-cognee)

---

## Academic Survey: Memory Taxonomy

**"Memory in the Age of AI Agents"** (arXiv:2512.13564, Dec 2025)

The most comprehensive 2025 survey. Proposes a three-dimensional taxonomy:

### Dimension 1: Forms of Memory
- **Token-level memory** — information within the context window
- **Parametric memory** — knowledge encoded in model weights
- **Latent memory** — hidden state representations

### Dimension 2: Functions of Memory
- **Factual memory** — stored knowledge and facts
- **Experiential memory** — learned from interactions
- **Working memory** — temporary active processing

### Dimension 3: Dynamics
How memory is formed, evolved, and retrieved over time.

**Key finding:** "Traditional taxonomies such as long/short-term memory have proven insufficient" for contemporary systems.

**Five emerging research frontiers:**
1. Memory automation — automated management processes
2. Reinforcement learning integration — combining RL with memory
3. Multimodal memory — handling images, audio, video
4. Multi-agent memory — coordination across agent networks
5. Trustworthiness — reliable and safe memory systems

Memory should be treated as "a first-class primitive in the design of future agentic intelligence."

**Supporting surveys:**
- [A Survey on Memory Mechanism of LLM-based Agents (ACM TOIS)](https://dl.acm.org/doi/10.1145/3748302)
- [Memory in LLM-based Multi-agent Systems (TechRxiv)](https://www.techrxiv.org/users/1007269/articles/1367390)
- [Agent Memory Paper List (GitHub)](https://github.com/Shichun-Liu/Agent-Memory-Paper-List)
- [ICLR 2026 Workshop: MemAgents: Memory for LLM-Based Agentic Systems](https://openreview.net/pdf?id=U51WxL382H)

---

## Sleep-Time Compute

A new memory paradigm introduced by Letta (with Databricks and Anyscale's Ion Stoica), published 2025.

**Core idea:** AI agents use idle time between tasks to reflect and improve their own memory state, rather than sitting idle.

**How it works:**
1. Agent receives original context (conversation history, files)
2. During idle period, a sleep-time agent reflects on that context
3. Iteratively derives a "learned context" — distilled, actionable memory
4. At next activation, agent uses learned context instead of raw history

**Results on math benchmarks (AIME, GSM):**
- Sleep-time compute reaches same accuracy with **~5x fewer test-time tokens** vs plain baseline
- Shifts computational load from high-latency user interactions to idle periods

**Architectural requirement:** Requires stateful agents with persistent memory — systems that maintain and can update their own context across time.

**Sources:**
- [Letta Sleep-Time Compute Blog](https://www.letta.com/blog/sleep-time-compute)
- [Letta Sleep-Time Agents Docs](https://docs.letta.com/guides/agents/architectures/sleeptime/)
- [Fast Company: Sleep-time compute](https://www.fastcompany.com/91368307/why-sleep-time-compute-is-the-next-big-leap-in-ai)
- [Arize AI Analysis](https://arize.com/blog/sleep-time-compute-beyond-inference-scaling-at-test-time/)

---

## Decision Matrix: Choosing a Framework

| Criterion | Mem0 | Zep/Graphiti | Letta | Cognee | LangMem |
|-----------|------|-------------|-------|--------|---------|
| **Setup speed** | Fast (managed) | Medium | Slow (full runtime) | Medium | Fast (library) |
| **Framework lock-in** | None | None | Letta runtime | None | LangGraph required |
| **Self-hosting** | Yes (OSS) | No (cloud-only) | Yes | Yes | Yes |
| **Knowledge graphs** | Pro tier+ | Core feature | Via tools | Core feature | No |
| **Temporal reasoning** | Good | Excellent | Good | Good | Fair |
| **Multi-agent** | Yes | Yes | Native | Yes | Via LangGraph |
| **Language support** | Python + JS | Python | Python | Python | Python only |
| **Production maturity** | Highest | High | Medium | Growing | Medium |
| **Best use case** | Managed SaaS, quick integration | Enterprise, CRM, temporal data | Coding agents, full control | Self-improving knowledge graphs | LangGraph-native agents |
| **Pricing model** | Tiered ($0-$249+/mo) | Credits ($0-$25+/mo) | $10M-funded, OSS + cloud | $0 OSS + cloud | Free OSS |

### Recommendation Summary

- **Fastest to production:** Mem0 managed
- **Best temporal accuracy:** Zep/Graphiti
- **Most architectural control:** Letta
- **Best knowledge graph reasoning:** Cognee or Zep
- **LangGraph ecosystem:** LangMem
- **Claude Code integration:** Cognee MCP or Basic Memory
- **High-performance embedded graph:** KuzuDB (Vela fork)
- **Token efficiency priority:** ENGRAM or Mem0's compaction

---

## Key Observations for 2026

1. **Benchmark inflation is real.** Self-reported numbers vary wildly. Prefer controlled evaluations with fixed framework+tools (Letta's methodology). The Zep 84% vs 58.44% discrepancy is a cautionary example.

2. **Graph memory is converging.** All major frameworks now offer some form of knowledge graph. The differentiator is now temporal modeling quality and retrieval strategy.

3. **Token efficiency is the new performance metric.** ENGRAM's 99% token reduction with higher accuracy challenges the assumption that "more context = better performance."

4. **Sleep-time compute changes the economics.** Shifting reasoning to idle periods reduces per-query cost and latency while improving quality. Requires stateful agents.

5. **The filesystem may be the killer app.** Letta's finding that simple filesystem tools beat specialized memory systems on LoCoMo suggests LLMs are optimized for file operations from training data — an underappreciated advantage of Letta Code's git-backed MemFS.

6. **MCP is the integration standard.** Nearly every memory framework now offers or plans an MCP server, making Claude Code the common interface layer.

7. **Multi-agent memory is the unsolved problem.** Concurrent writes, conflict resolution, and shared memory across agent networks remain research-level challenges. Git-based approaches (Letta) and bi-temporal append-only graphs (Zep) represent two competing solutions.

---

*Research compiled 2026-03-14. Sources verified as of this date. Framework versions and benchmark numbers change rapidly — always verify against official sources before production decisions.*
