# Context Degradation

> **v1.0.4** | Context Engineering | 5 iterations

Patterns for recognizing and mitigating context failures in LLM agents. Covers lost-in-middle, context poisoning, distraction, confusion, clash, and empirical degradation thresholds by model.

## What Problem Does This Solve

Language models exhibit predictable degradation patterns as context length increases. Understanding these patterns is essential for diagnosing failures and designing resilient systems. Context degradation is not a binary state but a continuum of performance degradation that manifests in several distinct ways.

## When to Use This Skill

Diagnosing context FAILURES — lost-in-middle, poisoning, distraction, clash, and confusion patterns with empirical thresholds by model. Use when the user asks to "diagnose context problems", "fix lost-in-middle issues", "debug agent failures", "understand context poisoning", or mentions context degradation, context clash, or agent performance degradation.

## When NOT to Use This Skill

- learning context basics or theory -- use [context-fundamentals](../context-fundamentals/) instead

## How to Use

**Direct invocation:**

```
Use the context-degradation skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `context-degradation`
- `lost-in-middle`
- `context-poisoning`
- `attention-patterns`

## What's Inside

- **When to Activate**
- **Core Concepts**
- **Detailed Topics**
- **Practical Guidance**
- **Examples**
- **Guidelines**
- **Integration**
- **References**

## Key Capabilities

- **Claude 4.5 series**
- **GPT-5.2**
- **Gemini 3 Pro/Flash**

## Version History

- `1.0.4` fix(context-engineering): optimize descriptions with cross-references and NOT clauses (7881054)
- `1.0.3` fix(context-degradation): add standard keywords and expand README to full format (39ba542)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Context Compression](../context-compression/)** -- Production strategies for compressing LLM context windows. Anchored iterative summarization, opaque compression, tokens-...
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational understanding of context engineering for AI agent systems. Covers context anatomy, attention mechanics, pro...
- **[Context Optimization](../context-optimization/)** -- Techniques for extending effective context capacity through compaction, observation masking, KV-cache optimization, and ...
- **[Filesystem Context](../filesystem-context/)** -- Filesystem-based context engineering patterns for LLM agents. Scratch pads, plan persistence, sub-agent communication, d...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 48 production-grade plugins for Claude Code.
