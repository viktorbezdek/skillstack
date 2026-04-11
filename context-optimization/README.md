# Context Optimization

> **v1.0.4** | Context Engineering | 5 iterations

Techniques for extending effective context capacity through compaction, observation masking, KV-cache optimization, and context partitioning. Double or triple effective context without larger models.

## What Problem Does This Solve

Tool outputs alone can consume 80%+ of a context window in typical agent trajectories, yet much of that content is verbose output that has already served its purpose. Paying full token cost to re-process stale tool results on every turn wastes budget and adds latency. This skill covers four concrete techniques — compaction, observation masking, KV-cache optimization, and context partitioning — that together can double or triple effective context capacity without switching to larger models.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "My agent's responses degrade and latency increases as conversations extend" | Compaction strategy: when to trigger (70-80% utilization), what to compress first (tool outputs then old turns), and how to preserve system prompts |
| "Tool outputs are dominating my context window" | Observation masking: strategy for replacing verbose outputs with compact references, with rules for what to always/never mask |
| "I'm paying high inference costs on every call even though most context is identical" | KV-cache optimization: prefix-stable prompt ordering (system prompt first, unique content last) to maximize cache hit rates |
| "I need to handle a task that's too large for a single context window" | Context partitioning: sub-agent isolation pattern that keeps each subtask's context clean, plus result aggregation strategies |
| "How do I know when to apply which optimization technique?" | Decision framework: what to apply based on which component dominates — tool outputs, retrieved docs, or message history |
| "What compression ratios and quality tradeoffs should I expect?" | Performance benchmarks: 50-70% reduction for compaction, 60-80% for masking, 70%+ cache hit rate targets for stable workloads |

## When NOT to Use This Skill

- reducing or compressing content via summarization -- use [context-compression](../context-compression/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-optimization@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the context-optimization skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `context-optimization`
- `kv-cache`
- `observation-masking`
- `compaction`

## What's Inside

- **When to Activate** -- Six conditions signaling optimization is needed: context limits, cost reduction goals, latency problems, long-running agents, large documents, and production scale.
- **Core Concepts** -- Four primary strategies (compaction, observation masking, KV-cache optimization, context partitioning) and the principle that context quality matters more than quantity.
- **Detailed Topics** -- Deep coverage of compaction implementation and summary generation by message type, observation masking selection rules, KV-cache prefix ordering patterns, sub-agent partitioning, and budget management with trigger-based optimization.
- **Practical Guidance** -- Decision framework mapping context composition to the right optimization technique, plus performance benchmarks for each strategy.
- **Examples** -- Code patterns for compaction triggers, observation masking with reference IDs, and cache-friendly context ordering.
- **Guidelines** -- Eight prioritized rules from measuring before optimizing through graceful degradation for edge cases.
- **Integration** -- How this skill connects to multi-agent-patterns (partitioning as isolation), evaluation (measuring optimization effectiveness), and memory-systems (offloading context).
- **References** -- Internal reference to the optimization techniques technical reference and external resources on KV-cache and context window research.

## Version History

- `1.0.4` fix(context-engineering): optimize descriptions with cross-references and NOT clauses (7881054)
- `1.0.3` fix(context-optimization): add standard keywords and expand README to full format (ed35eb2)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Context Compression](../context-compression/)** -- Production strategies for compressing LLM context windows. Anchored iterative summarization, opaque compression, tokens-...
- **[Context Degradation](../context-degradation/)** -- Patterns for recognizing and mitigating context failures in LLM agents. Covers lost-in-middle, context poisoning, distra...
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational understanding of context engineering for AI agent systems. Covers context anatomy, attention mechanics, pro...
- **[Filesystem Context](../filesystem-context/)** -- Filesystem-based context engineering patterns for LLM agents. Scratch pads, plan persistence, sub-agent communication, d...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
