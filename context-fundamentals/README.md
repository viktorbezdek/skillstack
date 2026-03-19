# Context Fundamentals

> **v1.0.5** | Context Engineering | 6 iterations

Foundational understanding of context engineering for AI agent systems. Covers context anatomy, attention mechanics, progressive disclosure, context budgeting, and the quality-vs-quantity principle.

## What Problem Does This Solve

Context is the complete state available to a language model at inference time. It includes everything the model can attend to when generating responses: system instructions, tool definitions, retrieved documents, message history, and tool outputs. Understanding context fundamentals is prerequisite to effective context engineering.

## When to Use This Skill

Foundational theory of context engineering — what context IS, how attention works, progressive disclosure principles, and context budgeting basics. Use when the user asks to "understand context", "explain context windows", "learn context engineering", or discusses context components, attention mechanics, or context budgets.

## When NOT to Use This Skill

- fixing broken context or diagnosing failures -- use [context-degradation](../context-degradation/) instead

## How to Use

**Direct invocation:**

```
Use the context-fundamentals skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `context-engineering`
- `attention`
- `progressive-disclosure`
- `context-window`

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

- `1.0.5` fix(context-engineering): optimize descriptions with cross-references and NOT clauses (7881054)
- `1.0.4` fix(context-fundamentals): add standard keywords and expand README to full format (ec23f4a)
- `1.0.3` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.2` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.1` docs: add 2025-2026 research references for context and memory plugins (8e815ba)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Context Compression](../context-compression/)** -- Production strategies for compressing LLM context windows. Anchored iterative summarization, opaque compression, tokens-...
- **[Context Degradation](../context-degradation/)** -- Patterns for recognizing and mitigating context failures in LLM agents. Covers lost-in-middle, context poisoning, distra...
- **[Context Optimization](../context-optimization/)** -- Techniques for extending effective context capacity through compaction, observation masking, KV-cache optimization, and ...
- **[Filesystem Context](../filesystem-context/)** -- Filesystem-based context engineering patterns for LLM agents. Scratch pads, plan persistence, sub-agent communication, d...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 46 production-grade plugins for Claude Code.
