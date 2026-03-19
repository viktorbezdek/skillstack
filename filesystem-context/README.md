# Filesystem Context

> **v1.0.4** | Context Engineering | 5 iterations

Filesystem-based context engineering patterns for LLM agents. Scratch pads, plan persistence, sub-agent communication, dynamic skill loading, terminal persistence, and self-modification patterns.

## What Problem Does This Solve

The filesystem provides a single interface through which agents can flexibly store, retrieve, and update an effectively unlimited amount of context. This pattern addresses the fundamental constraint that context windows are limited while tasks often require more information than fits in a single window.

## When to Use This Skill

Using the FILE SYSTEM for context — scratch pads, plan persistence, dynamic skill loading, sub-agent file workspaces, and terminal log persistence. Use when the user asks to "offload context to files", "implement scratch pads", "persist agent plans", "use filesystem for agent memory", or mentions file-based context management, tool output persistence, or just-in-time context loading.

## When NOT to Use This Skill

- in-context optimization like KV-cache or observation masking -- use [context-optimization](../context-optimization/) instead

## How to Use

**Direct invocation:**

```
Use the filesystem-context skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `filesystem`
- `context-management`
- `scratch-pad`
- `dynamic-loading`

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
- `1.0.3` fix(filesystem-context): add standard keywords and expand README to full format (994c529)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Context Compression](../context-compression/)** -- Production strategies for compressing LLM context windows. Anchored iterative summarization, opaque compression, tokens-...
- **[Context Degradation](../context-degradation/)** -- Patterns for recognizing and mitigating context failures in LLM agents. Covers lost-in-middle, context poisoning, distra...
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational understanding of context engineering for AI agent systems. Covers context anatomy, attention mechanics, pro...
- **[Context Optimization](../context-optimization/)** -- Techniques for extending effective context capacity through compaction, observation masking, KV-cache optimization, and ...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 46 production-grade plugins for Claude Code.
