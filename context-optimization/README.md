# Context Optimization

> **v1.0.4** | Context Engineering | 5 iterations

Techniques for extending effective context capacity through compaction, observation masking, KV-cache optimization, and context partitioning. Double or triple effective context without larger models.

## What Problem Does This Solve

Context optimization extends the effective capacity of limited context windows through strategic compression, masking, caching, and partitioning. The goal is not to magically increase context windows but to make better use of available capacity. Effective optimization can double or triple effective context capacity without requiring larger models or longer contexts.

## When to Use This Skill

EXTENDING effective context capacity — KV-cache optimization, observation masking, context partitioning, and retrieval strategies. Use when the user asks to "optimize context", "implement KV-cache", "partition context", "mask observations", or mentions extending context capacity or cache-friendly prompt design.

## When NOT to Use This Skill

- reducing or compressing content via summarization -- use [context-compression](../context-compression/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/context-optimization
```

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

- **When to Activate**
- **Core Concepts**
- **Detailed Topics**
- **Practical Guidance**
- **Examples**
- **Guidelines**
- **Integration**
- **References**

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

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
