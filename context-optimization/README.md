# Context Optimization Techniques

> Techniques for extending effective context capacity through compaction, observation masking, KV-cache optimization, and context partitioning. Double or triple effective context without larger models.

## Overview

Context optimization extends the effective capacity of limited context windows through strategic compression, masking, caching, and partitioning. The goal is not to magically increase context windows but to make better use of available capacity. When applied systematically, these techniques can double or triple effective context capacity without requiring larger models or longer context windows, while also reducing cost and latency.

The skill covers four primary optimization strategies. Compaction summarizes context near limits and reinitializes with the summary. Observation masking replaces verbose tool outputs (which can comprise 80%+ of token usage) with compact references. KV-cache optimization reuses cached computations across requests with identical prefixes. Context partitioning splits work across sub-agents with isolated contexts. Each strategy addresses different aspects of context pressure and can be combined for maximum effect.

Within the SkillStack collection, Context Optimization builds on the foundational concepts in Context Fundamentals and the failure patterns described in Context Degradation. It connects to Multi-Agent Patterns (partitioning as isolation), Agent Evaluation (measuring optimization effectiveness), and Memory Systems (offloading context to persistent memory). Context Compression provides deeper coverage of the compression strategies introduced here.

## What's Included

### Skill

- `skills/context-optimization/SKILL.md` -- Core optimization techniques covering compaction strategies, observation masking, KV-cache optimization, context partitioning, budget management, and trigger-based optimization

### References

- **optimization_techniques.md** -- Detailed technical reference for each optimization technique with implementation patterns

## Key Features

- **Compaction strategies** with priority ordering: compress tool outputs first, then old turns, then retrieved docs, but never compress the system prompt
- **Observation masking** replacing verbose tool outputs with compact references, achieving 60-80% reduction while preserving information accessibility
- **KV-cache optimization** through prefix caching with hash-based block matching, plus cache-friendly context ordering that maximizes hit rates
- **Context partitioning** across sub-agents with isolated contexts, achieving separation of concerns without any single context bearing the full burden
- **Budget management** with explicit token allocation across categories and trigger-based optimization at 80% utilization
- **Summary generation guidelines** tailored by message type: preserve key findings from tool outputs, key decisions from conversation, key facts from documents
- **Optimization decision framework** matching strategies to context composition: masking for tool-output-heavy contexts, summarization for document-heavy, compaction for history-heavy
- **Performance targets**: 50-70% token reduction from compaction with less than 5% quality degradation, 70%+ cache hit rate for stable workloads

## Usage Examples

Reduce token costs for a long-running agent:
```
Our agent sessions average 120K tokens and costs are high. Help me implement observation masking for tool outputs and compaction for message history to bring context usage under control.
```

Optimize for KV-cache hits:
```
We're running many similar agent sessions with the same system prompt and tools. Help me reorder context elements for maximum KV-cache reuse and design cache-stable prompts.
```

Implement context partitioning:
```
Our research agent is hitting context limits because it searches 10 sources and accumulates findings. Design a partitioned architecture where each source gets its own sub-agent with isolated context.
```

Set up trigger-based optimization:
```
Help me implement automatic context optimization that triggers at 80% utilization. It should apply observation masking first for tool outputs, then compaction for old conversation turns.
```

## Quick Start

1. **Measure first**: Know your current context composition -- what percentage is system prompt, tool definitions, tool outputs, message history, and retrieved documents.
2. **Apply observation masking**: Replace tool outputs older than 3 turns with compact references containing key findings only.
3. **Implement compaction**: When context exceeds 80% utilization, summarize old turns while preserving key decisions and file modifications.
4. **Optimize cache ordering**: Place stable elements first (system prompt, tool definitions), then frequently reused elements, then unique content last.
5. **Consider partitioning**: If a single context still exceeds limits, split work across sub-agents with focused contexts and aggregate results.

## Related Skills

- **context-fundamentals** -- Foundational context concepts and the attention budget constraint
- **context-degradation** -- Understanding when optimization becomes necessary
- **context-compression** -- Deep dive into compression strategies (a specific optimization technique)
- **multi-agent-patterns** -- Context partitioning as a form of isolation across agents
- **memory-systems** -- Offloading context to memory as an optimization strategy
- **agent-evaluation** -- Measuring whether optimizations maintain output quality

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install context-optimization@skillstack` — 46 production-grade plugins for Claude Code.
