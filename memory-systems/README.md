# Memory Systems

> **v1.0.5** | Agent Architecture | 6 iterations

---

## The Problem

LLM agents forget everything the moment a session ends. Every conversation starts from zero -- no recollection of user preferences, past decisions, accumulated domain knowledge, or entity relationships established in previous interactions. Teams building production agents discover this the hard way: a customer support agent that asks the same onboarding questions every session, a coding assistant that re-discovers project conventions daily, or a research agent that cannot build on yesterday's findings.

The pain compounds quickly. Without persistent memory, agents cannot maintain entity consistency ("John Doe" in session 1 becomes an unknown stranger in session 2), cannot reason over accumulated knowledge (connecting facts from multiple sessions to derive new insights), and cannot adapt to evolving information (a user's address changed three months ago, but the agent still references the old one). Teams attempt workarounds -- stuffing entire conversation histories into prompts, maintaining manual knowledge bases, or building custom persistence layers from scratch -- and discover that naive approaches either blow context limits, degrade retrieval quality, or both.

The framework landscape makes the problem worse. Mem0, Zep/Graphiti, Letta, LangMem, and Cognee each take fundamentally different architectural approaches. Without direct comparison data, teams spend weeks evaluating options only to choose a framework mismatched to their actual retrieval needs. A team needing temporal reasoning picks a vector-only solution. A team needing simple preference storage over-engineers with a full knowledge graph. The mismatch surfaces months later when the system fails under production load.

## The Solution

The Memory Systems plugin gives Claude deep expertise in production memory architectures for LLM agents. It provides framework-by-framework comparison with benchmark data (LoCoMo, LongMemEval, DMR, HotPotQA), layered memory design patterns (working, short-term, long-term, entity, temporal knowledge graph), retrieval strategy selection (semantic, entity-based, temporal, hybrid), and consolidation approaches that prevent unbounded growth.

The plugin delivers a single skill backed by two reference documents covering implementation patterns and the latest 2025-2026 research. It compares five production frameworks -- Mem0, Zep/Graphiti, Letta, LangMem, and Cognee -- with concrete benchmarks rather than marketing claims. It covers the full spectrum from file-system prototypes to temporal knowledge graphs, helping you choose the right complexity for your stage.

The practical guidance follows a "start simple, add complexity when retrieval fails" philosophy. You get decision trees for architecture selection, integration patterns for connecting memory to context systems, error recovery strategies for empty retrieval / stale results / conflicting facts, and anti-patterns that prevent common production failures.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Spend weeks evaluating memory frameworks without benchmark data to guide the choice | Framework comparison table with LoCoMo, LongMemEval, DMR, and HotPotQA scores for direct comparison |
| Over-engineer with a temporal knowledge graph when a file-system approach would suffice | Graduated complexity path: file-system -> vector store -> knowledge graph -> temporal KG, matched to retrieval needs |
| Agents forget user preferences and entity relationships across sessions | Layered memory architecture (working/short-term/long-term/entity/temporal) with persistence strategies |
| Retrieval quality degrades as memory grows without consolidation | Consolidation patterns that invalidate-but-don't-discard, preserving history for temporal queries |
| Naive vector search fails on multi-hop reasoning and time-sensitive facts | Hybrid retrieval strategy selection (semantic + keyword + graph) with framework-specific guidance |
| No error handling for empty retrieval, stale results, or conflicting facts | Explicit recovery patterns: broader search fallback, validity timestamp checks, recency-based conflict resolution |

## Installation

Add the marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install memory-systems@skillstack
```

### Prerequisites

None. This is a standalone knowledge plugin. For cross-agent memory patterns, also install `multi-agent-patterns`. For context integration strategies, also install `context-optimization`.

### Verify installation

After installing, test with:

```
Help me design a memory architecture for a customer support agent that needs to remember user preferences across sessions
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `I'm building an agent that needs to persist knowledge across sessions -- which memory framework should I use?`
3. The skill activates and walks you through framework selection based on your requirements (multi-tenant, temporal reasoning, graph traversal, etc.)
4. You receive a concrete architecture recommendation with implementation guidance
5. Next, try: `Show me how to implement memory consolidation so retrieval quality doesn't degrade over time`

---

## System Overview

```
memory-systems/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
└── skills/
    └── memory-systems/
        ├── SKILL.md             # Core skill (framework comparison, architecture patterns, retrieval strategies)
        ├── references/
        │   ├── implementation.md        # Implementation patterns: vector stores, Mem0, Graphiti, Cognee code
        │   └── latest-research-2026.md  # 2025-2026 research: benchmarks, academic advances, integration patterns
        └── evals/
            ├── trigger-evals.json   # 15 trigger evaluation cases
            └── evals.json           # 3 output evaluation cases
```

The plugin is a single skill with two deep-dive reference documents. The SKILL.md provides the decision framework and overview; the references provide implementation code and research data that the skill loads on demand when deeper context is needed.

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `memory-systems` | Skill | Framework comparison, architecture design, retrieval strategy selection |
| `implementation.md` | Reference | Working code for vector stores, Mem0, Graphiti, Cognee integration |
| `latest-research-2026.md` | Reference | Benchmark landscape, academic advances, production patterns from 2025-2026 |

### Component Spotlight

#### memory-systems (skill)

**What it does:** Activates when you need to design, implement, or evaluate memory systems for LLM agents. Provides framework comparison with benchmark data, layered memory architecture patterns, retrieval strategy selection, consolidation approaches, and error recovery guidance.

**Input -> Output:** A description of your agent's memory requirements (persistence needs, query patterns, scale) -> A concrete memory architecture recommendation with framework selection, layer design, retrieval strategy, and integration patterns.

**When to use:**
- Building agents that must persist knowledge across sessions
- Choosing between Mem0, Zep/Graphiti, Letta, LangMem, or Cognee
- Designing retrieval strategies (semantic, entity-based, temporal, hybrid)
- Implementing memory consolidation to prevent unbounded growth
- Evaluating memory systems against benchmarks

**When NOT to use:**
- Multi-agent coordination or agent handoffs (use `multi-agent-patterns`)
- Tool design or tool interfaces (use `tool-design`)
- Hosted agent infrastructure or sandboxed VMs (use `hosted-agents`)
- General context window optimization (use `context-optimization`)

**Try these prompts:**

```
I need to add long-term memory to my Python agent -- it should remember user preferences and past decisions across sessions
```

```
Compare Mem0 vs Zep/Graphiti vs Cognee for a multi-tenant SaaS where each user's agent needs isolated memory
```

```
My agent's memory retrieval is returning stale results -- facts changed weeks ago but old versions keep surfacing
```

```
Design a temporal knowledge graph for a legal research agent that needs to track how regulations change over time
```

```
Show me how to implement memory consolidation -- my agent has accumulated thousands of memories and retrieval quality is degrading
```

**Key references:**

| Reference | Topic |
|---|---|
| `implementation.md` | Vector store implementation, Mem0 integration, Graphiti temporal KG, Cognee ECL pipeline code |
| `latest-research-2026.md` | LoCoMo/LongMemEval/DMR benchmarks, MemBench framework, 2025-2026 academic advances |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "How do I save data?" | "Design a memory architecture for my coding assistant that needs to remember project conventions across sessions" |
| "Tell me about Mem0" | "Compare Mem0 vs Graphiti for a multi-tenant agent that needs temporal reasoning over user history" |
| "My agent forgets things" | "My agent retrieves outdated facts -- the user changed their address but the old one keeps appearing in responses" |
| "What's the best memory framework?" | "I need a memory framework for an agent that handles 10K users, each with isolated memory and cross-session entity tracking" |

### Structured Prompt Templates

**For framework selection:**
```
I'm building [agent type] that needs to [memory requirement]. Key constraints: [multi-tenant/single-user], [temporal reasoning needed/not needed], [expected memory volume]. Which memory framework fits best?
```

**For architecture design:**
```
Design a memory architecture for [use case]. The agent needs to persist [what data] across sessions and retrieve it when [trigger condition]. Current scale: [users/memories].
```

**For retrieval troubleshooting:**
```
My agent uses [framework] for memory but [specific problem: stale results / empty retrieval / conflicting facts / slow queries]. How do I fix this?
```

### Prompt Anti-Patterns

- **Asking for "the best" framework without constraints** -- there is no universally best framework; the skill needs your requirements (multi-tenant? temporal? graph traversal?) to make a recommendation
- **Requesting a full implementation before choosing an architecture** -- start with architecture selection, then ask for implementation details for the chosen approach
- **Treating memory as a single monolithic system** -- memory has layers (working, short-term, long-term, entity, temporal); ask about the specific layer you need
- **Ignoring retrieval strategy** -- storing memories is the easy part; ask specifically about how your agent will retrieve and use them

## Real-World Walkthrough

**Starting situation:** You are building a customer success agent for a SaaS product. The agent handles support conversations, tracks customer health metrics, and proactively suggests improvements. Currently, every session starts fresh -- the agent has no memory of previous interactions, customer context, or resolved issues.

**Step 1: Architecture assessment.** You ask: "I need to design a memory system for a customer success agent that handles 500 enterprise accounts. Each account has a dedicated agent instance. The agent needs to remember past conversations, track evolving customer health, and connect related issues across sessions."

The skill activates and maps your requirements to the memory layer framework. It identifies you need: working memory (current conversation context), long-term memory (customer preferences, product usage patterns), entity memory (contacts, accounts, products as distinct entities), and temporal memory (health scores that change over time, issue timelines).

**Step 2: Framework selection.** Based on your multi-tenant requirement (500 isolated accounts), temporal reasoning need (health scores over time), and entity tracking (contacts and accounts), the skill recommends Zep/Graphiti for the temporal knowledge graph layer and suggests evaluating Cognee if you need richer multi-hop reasoning across interconnected customer data. It explains the trade-off: Graphiti uses generic relations keeping graphs simple; Cognee builds denser multi-layer semantic graphs with detailed relationship edges.

**Step 3: Retrieval strategy design.** You ask about retrieval, and the skill recommends a hybrid approach: semantic search for natural language queries ("What issues has Acme Corp reported?"), entity-based graph traversal for relationship queries ("Who are the key stakeholders at Acme?"), and temporal filtering for time-sensitive queries ("How has Acme's health score changed this quarter?"). It cites Zep's benchmark: 90% latency reduction (2.58s vs 28.9s) by retrieving only relevant subgraphs instead of scanning all memories.

**Step 4: Consolidation planning.** The skill warns about unbounded growth -- 500 accounts generating memories daily will degrade retrieval. It recommends periodic consolidation triggered by memory count thresholds per account, with an invalidate-but-don't-discard approach so temporal queries still work. Stale facts get marked with `valid_until` timestamps rather than deleted.

**Step 5: Error recovery design.** The skill provides recovery patterns: empty retrieval falls back to broader search (remove entity filter, widen time range), stale results trigger validity timestamp checks and consolidation, conflicting facts prefer the most recent `valid_from` with low-confidence conflicts surfaced to the human operator.

**Step 6: Integration.** You connect memory to the agent's context system using just-in-time loading -- memories are retrieved at conversation start and injected at attention-favored positions (beginning/end of context). The skill notes that strategic injection placement matters more than memory volume.

**Final outcome:** A production-ready memory architecture with Graphiti temporal KG for relationship/temporal reasoning, hybrid retrieval across three strategies, consolidation scheduled nightly per account, and error recovery that handles the five most common failure modes. Total design time: one session instead of weeks of framework evaluation.

**Gotchas discovered:** The skill flagged that Letta's filesystem approach scored 74% on LoCoMo, beating Mem0's 68.5% -- tool complexity matters less than reliable retrieval. This prevented over-engineering the prototype phase before validating the architecture.

## Usage Scenarios

### Scenario 1: Choosing a memory framework for a prototype

**Context:** You are building an AI coding assistant MVP and need the agent to remember project conventions, past code reviews, and user preferences between sessions. You want the simplest viable approach.

**You say:** "I'm prototyping a coding assistant that needs to remember project conventions and user preferences across sessions. What's the simplest memory approach that actually works?"

**The skill provides:**
- Recommendation to start with file-system memory (structured JSON with timestamps)
- Validation that Letta's filesystem agents scored 74% on LoCoMo using basic file operations
- Graduation path: move to Mem0 when you need semantic search and multi-tenant isolation
- Working code example for file-based memory with timestamps

**You end up with:** A file-system memory implementation you can build in an afternoon, with a clear upgrade path when retrieval demands increase.

### Scenario 2: Debugging degraded retrieval quality

**Context:** Your production agent uses Mem0 for memory but users are reporting that the agent references outdated information -- a user changed their tech stack preference months ago, but the agent keeps suggesting the old stack.

**You say:** "My agent uses Mem0 but keeps retrieving outdated preferences. A user switched from React to Vue three months ago but the agent still recommends React patterns."

**The skill provides:**
- Diagnosis: missing temporal validity tracking on preference memories
- Recovery pattern: check `valid_until` timestamps, prefer most recent `valid_from`
- Consolidation strategy to mark outdated preferences as invalid without deleting them
- Migration path to Zep/Graphiti if temporal reasoning becomes a core requirement

**You end up with:** A fix for the immediate stale-data problem plus a consolidation schedule that prevents recurrence.

### Scenario 3: Designing cross-agent shared memory

**Context:** You are building a multi-agent research system where a search agent, analysis agent, and writing agent need to share accumulated knowledge without passing full context between them.

**You say:** "I have three specialized agents (search, analysis, writing) that need to share accumulated knowledge. How do I design shared memory without bloating each agent's context?"

**The skill provides:**
- File-system memory as the coordination mechanism (agents read/write to shared persistent storage)
- Entity registry pattern for maintaining consistent entity identity across agents
- Integration guidance connecting to `multi-agent-patterns` for context isolation strategies
- Warning about consistency challenges with shared memory and recommended mitigation

**You end up with:** A shared memory architecture where agents coordinate through persistent storage rather than context passing, maintaining entity consistency without context bloat.

### Scenario 4: Implementing a temporal knowledge graph

**Context:** You are building a legal research agent that must track how regulations, case law, and compliance requirements change over time, including the ability to answer "what was the rule on date X?"

**You say:** "Design a temporal knowledge graph for a legal research agent that needs to track regulation changes and answer time-travel queries like 'what was the GDPR interpretation in March 2024?'"

**The skill provides:**
- Graphiti's bi-temporal model (when events occurred vs when they were ingested)
- Temporal relationship creation with `valid_from` / `valid_until` intervals
- Time-travel query implementation using `query_at_time`
- Benchmark data: Zep achieves 94.8% DMR accuracy with 18.5% accuracy improvement on LongMemEval

**You end up with:** A temporal knowledge graph design with bi-temporal tracking, time-travel query capability, and confidence that the approach is backed by benchmark performance data.

---

## Decision Logic

**When does the skill recommend each framework?**

The skill follows a graduated complexity model:

1. **File-system memory** -- when you are prototyping, have a single agent, and need to validate behavior before investing in infrastructure. Benchmark support: Letta filesystem scored 74% on LoCoMo.
2. **Mem0** -- when you need multi-tenant isolation, managed infrastructure, and semantic search. Fastest path to production. Best for broad integrations without deep relationship modeling.
3. **Zep/Graphiti** -- when you need relationship traversal, temporal validity (bi-temporal model), or cross-session synthesis. Enterprise-grade but advanced features are cloud-locked.
4. **Cognee** -- when you need multi-hop reasoning, richer interconnected knowledge structures, or a customizable ECL pipeline. Highest HotPotQA scores but heavier ingest-time processing.
5. **Letta** -- when you need full agent self-management of memory with deep introspection and tiered storage (in-context/core/archival).
6. **LangMem** -- when you are already on LangGraph and need memory tools that integrate natively.

**When does the skill escalate complexity?**

Only when retrieval quality degrades. The skill will not recommend a temporal knowledge graph until you demonstrate that simpler approaches (vector search, entity lookup) fail for your query patterns.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Over-engineering early | Spent weeks setting up a temporal KG for an agent that only needs preference storage | Start with file-system memory; the skill's graduated path prevents this |
| Unbounded memory growth | Retrieval latency increases, irrelevant results surface more often | Implement consolidation on count thresholds; invalidate but don't discard |
| Stale retrieval | Agent references outdated facts (old address, old preferences) | Add `valid_until` timestamps; trigger consolidation when most results are expired |
| Empty retrieval | Memory lookup returns nothing for valid queries | Fall back to broader search: remove entity filter, widen time range, prompt user |
| Conflicting facts | Two contradictory memories for the same entity/property | Prefer most recent `valid_from`; surface conflict to user if confidence is low |
| Framework mismatch | Chose Mem0 but need temporal reasoning; chose Graphiti but only need simple preferences | Use the skill's framework comparison table before committing; re-evaluate when requirements change |

## Ideal For

- **Agent builders** who need persistent memory across sessions and want benchmark-backed framework selection instead of guessing
- **Platform engineers** designing multi-tenant memory architectures where each user's agent needs isolated, scalable memory
- **ML engineers** evaluating memory frameworks against LoCoMo, LongMemEval, DMR, or HotPotQA benchmarks for production readiness
- **Teams with existing agents** experiencing retrieval degradation, stale data, or conflicting facts and needing systematic fixes
- **Researchers** exploring temporal knowledge graphs, memory consolidation strategies, or hybrid retrieval approaches

## Not For

- **Multi-agent coordination** -- use `multi-agent-patterns` for agent handoffs, supervisor/swarm architectures, and context isolation
- **Tool design for agents** -- use `tool-design` for designing tool interfaces and function calling patterns
- **Hosted agent infrastructure** -- use `hosted-agents` for sandboxed execution environments and deployment patterns
- **General context optimization** -- use `context-optimization` for attention management and context partitioning without persistent memory

## Related Plugins

- **multi-agent-patterns** -- shared memory across agents, context isolation strategies for multi-agent systems
- **context-fundamentals** -- foundational context engineering that memory systems build upon
- **context-optimization** -- memory-based context loading and partitioning strategies
- **context-degradation** -- diagnosing retrieval failures that may originate from memory system issues

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
