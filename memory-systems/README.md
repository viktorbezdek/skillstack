# Memory System Design

> Production memory architectures for LLM agents. Compares Mem0, Zep/Graphiti, Letta, Cognee, LangMem with benchmarks. Covers temporal knowledge graphs, memory consolidation, and retrieval strategies.

## Overview

Memory provides the persistence layer that allows agents to maintain continuity across sessions and reason over accumulated knowledge. Simple agents rely entirely on the context window for memory, losing all state when sessions end. Sophisticated agents implement layered memory architectures that balance immediate context needs with long-term knowledge retention. The evolution from vector stores to knowledge graphs to temporal knowledge graphs represents increasing investment in structured memory for improved retrieval and reasoning.

This skill provides a comprehensive comparison of production memory frameworks (Mem0, Zep/Graphiti, Letta, Cognee, LangMem) with benchmark data from LoCoMo, LongMemEval, DMR, and HotPotQA. A key finding: tool complexity matters less than reliable retrieval -- Letta's filesystem agents scored 74% on LoCoMo using basic file operations, beating Mem0's specialized tools at 68.5%. The skill covers memory layers from volatile working memory through cross-session temporal knowledge graphs, retrieval strategies from semantic similarity through hybrid graph-based approaches, and consolidation patterns that prevent unbounded growth.

Within the SkillStack collection, Memory Systems builds on Context Fundamentals and connects to Multi-Agent Patterns for shared memory across agents, Context Optimization for memory-based context loading, and Agent Evaluation for measuring memory quality. The Filesystem Context skill provides the simplest memory layer pattern that this skill extends with more sophisticated architectures.

## What's Included

### Skill

- `skills/memory-systems/SKILL.md` -- Core memory architecture covering framework comparison, memory layers, retrieval strategies, consolidation patterns, practical guidance for choosing architectures, and integration with context systems

### References

- **implementation.md** -- Detailed implementation patterns including working consolidation code, production framework configurations, and memory integration examples
- **latest-research-2026.md** -- Updated research findings on memory systems from 2025-2026

## Key Features

- **Production framework comparison** of Mem0 (vector store + graph, fastest to production), Zep/Graphiti (temporal knowledge graph with bi-temporal model), Letta (self-editing tiered storage), Cognee (multi-layer semantic graph with customizable ECL pipeline), and LangMem (LangGraph workflow tools)
- **Benchmark data** across DMR (Zep 94.8%), LoCoMo (Letta 74%, Mem0 68.5%), and HotPotQA (Cognee highest on EM, F1, correctness), with the insight that no single benchmark is definitive
- **Five memory layers** with clear decision criteria: working (context window), short-term (session-scoped), long-term (cross-session), entity (identity tracking), and temporal KG (time-travel queries)
- **Four retrieval strategies**: semantic (embedding similarity), entity-based (graph traversal), temporal (validity filter), and hybrid (90% latency reduction via relevant subgraph retrieval)
- **Memory consolidation** patterns that invalidate but do not discard, preserving history for temporal queries while preventing unbounded growth
- **Progressive architecture guidance**: start with filesystem, scale to Mem0/vector store, add Graphiti/Cognee for complex reasoning, use Letta for full agent self-management
- **Error recovery patterns** for empty retrieval, stale results, conflicting facts, and storage failures
- **Cognee's 14 search modes** combining graph, vector, and relational stores for query-type-specific retrieval

## Usage Examples

Choose a memory framework for your agent:
```
I'm building a customer support agent that needs to remember user preferences, past interactions, and product knowledge across sessions. Compare Mem0, Zep, and Cognee for my use case and recommend the best fit.
```

Implement temporal knowledge tracking:
```
Our agent needs to track facts that change over time -- user addresses, subscription plans, team memberships. Implement temporal validity so we can query what was true at any point in time and prevent stale information from poisoning context.
```

Design a memory consolidation strategy:
```
Our agent's memory store has grown to 50K entries and retrieval quality is degrading. Help me implement consolidation that merges redundant entries, invalidates outdated facts, and maintains history for audit.
```

Add memory to an existing agent:
```
I have a working coding agent but it forgets everything between sessions. Start with the simplest memory pattern (filesystem-based) and show me how to evolve to a more sophisticated architecture if needed.
```

## Quick Start

1. **Start simple**: Use filesystem memory -- store facts as structured JSON with timestamps. This is good enough to validate agent behavior.
2. **Scale to Mem0**: When you need semantic search and multi-tenant isolation, move to Mem0 or a vector store with metadata.
3. **Add graph structure**: When you need relationship traversal or temporal validity, add Zep/Graphiti (bi-temporal model) or Cognee (multi-layer semantic graph).
4. **Implement consolidation**: Set up periodic consolidation that invalidates outdated facts without discarding them, triggered by memory count thresholds or degraded retrieval quality.
5. **Monitor in production**: Track memory growth, retrieval latency, and retrieval quality. Benchmark against LoCoMo or LongMemEval before and after changes.

## Related Skills

- **context-fundamentals** -- Foundational context concepts that inform memory integration
- **multi-agent-patterns** -- Shared memory architectures across multiple agents
- **context-optimization** -- Memory-based context loading as an optimization strategy
- **filesystem-context** -- Filesystem-as-memory as the simplest persistent memory layer
- **agent-evaluation** -- Evaluating memory quality, recall accuracy, and retrieval effectiveness

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install memory-systems@skillstack` — 46 production-grade plugins for Claude Code.
