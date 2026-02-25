# Context Fundamentals

> Foundational understanding of context engineering for AI agent systems. Covers context anatomy, attention mechanics, progressive disclosure, context budgeting, and the quality-vs-quantity principle.

## Overview

Context is the complete state available to a language model at inference time -- system instructions, tool definitions, retrieved documents, message history, and tool outputs. Understanding how these components interact with the attention mechanism is prerequisite to building effective agent systems. This skill provides the foundational theory and practical patterns that all other context engineering skills build upon.

The core insight is that context engineering is not a one-time prompt writing exercise but an ongoing discipline of curating the smallest possible set of high-signal tokens that maximize the likelihood of desired outcomes. Larger context windows do not solve memory problems; they create new ones. Processing cost grows disproportionately, model performance degrades beyond certain thresholds, and the attention budget depletes as context grows. The engineering discipline is managing these constraints through progressive disclosure, budget allocation, and strategic placement.

Within the SkillStack collection, Context Fundamentals is the entry point for the context engineering skill tree. It should be studied before exploring Context Degradation (how context fails), Context Optimization (how to extend capacity), Context Compression (how to reduce token usage), and Filesystem Context (how to offload context to the file system). Every other skill in the collection depends on the concepts introduced here.

## What's Included

### Skill

- `skills/context-fundamentals/SKILL.md` -- Core fundamentals covering context anatomy (system prompts, tool definitions, retrieved documents, message history, tool outputs), attention mechanics, progressive disclosure, context budgeting, and quality-vs-quantity principles

### References

- **context-components.md** -- Detailed technical reference for each context component type
- **latest-research-2026.md** -- Updated research findings on context engineering from 2025-2026

## Key Features

- **Context anatomy** breaking down the five component types: system prompts, tool definitions, retrieved documents, message history, and tool outputs (which can reach 83.9% of total context)
- **Attention budget constraint** explaining how n-squared token relationships create a finite budget that depletes as context grows
- **Progressive disclosure principle** for loading information only when needed: skill names at startup, full content on activation
- **Quality over quantity** principle backed by empirical evidence that larger context windows create disproportionate cost and degradation
- **System prompt design** at the right altitude: specific enough to guide behavior, flexible enough to provide strong heuristics
- **Context budgeting** with explicit allocation across categories, monitoring during development, and compaction triggers at 70-80% utilization
- **File-system-based access** patterns for storing reference materials externally and loading files only when needed
- **Hybrid strategies** balancing pre-loaded context (speed) with autonomous exploration (freshness) based on content dynamics

## Usage Examples

Design context architecture for a new agent:
```
I'm building a customer support agent with access to 15 tools and a knowledge base of 500 articles. Help me design the context architecture: what goes in the system prompt, what loads dynamically, and how to budget tokens.
```

Debug unexpected agent behavior:
```
My agent keeps using the wrong tool even though the correct one is defined. Help me understand how tool definitions interact with context and why the agent might be confused.
```

Optimize context for cost reduction:
```
Our agent conversations average 50K tokens and cost is becoming a concern. Help me apply the quality-over-quantity principle to reduce context usage without degrading performance.
```

Understand attention mechanics for prompt design:
```
Explain how the attention mechanism affects where I should place critical information in my prompts. I have a 30-page reference document the agent needs to work with.
```

## Quick Start

1. **Audit your context**: Identify which components consume the most tokens -- typically tool outputs dominate at 80%+ of total usage.
2. **Apply progressive disclosure**: Load only skill names and descriptions at startup; load full content when activated for specific tasks.
3. **Place strategically**: Put critical information at the beginning or end of context where attention is strongest; avoid burying important content in the middle.
4. **Set budgets**: Allocate explicit token budgets for system prompt, tool definitions, retrieved docs, and message history, with a reserved buffer.
5. **Monitor and iterate**: Track context usage during development, implement compaction triggers at 70-80% utilization, and design for degradation rather than hoping to avoid it.

## Related Skills

- **context-degradation** -- How context fails: lost-in-middle, poisoning, distraction, confusion, and clash patterns
- **context-optimization** -- Techniques for extending effective context capacity through compaction, masking, and caching
- **context-compression** -- Production strategies for compressing growing conversation history
- **filesystem-context** -- Using the file system for dynamic context discovery and offloading
- **tool-design** -- How tool definitions interact with context and steer agent behavior
- **multi-agent-patterns** -- How context isolation motivates multi-agent architectures

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install context-fundamentals@skillstack` — 46 production-grade plugins for Claude Code.
