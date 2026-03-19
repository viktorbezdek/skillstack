# Context Compression

> **v1.0.4** | Context Engineering | 5 iterations

Production strategies for compressing LLM context windows. Anchored iterative summarization, opaque compression, tokens-per-task optimization, and probe-based evaluation.

## What Problem Does This Solve

When agent sessions generate millions of tokens of conversation history, compression becomes mandatory. The naive approach is aggressive compression to minimize tokens per request. The correct optimization target is tokens per task: total tokens consumed to complete a task, including re-fetching costs when compression loses critical information.

## When to Use This Skill

REDUCING context size — summarization strategies, anchored iterative summarization, tokens-per-task optimization, compaction triggers, and probe-based evaluation. Use when the user asks to "compress context", "summarize conversation history", "implement compaction", "reduce token usage", or mentions structured summarization or long-running sessions exceeding context limits.

## When NOT to Use This Skill

- diagnosing context failures or degradation patterns -- use [context-degradation](../context-degradation/) instead

## How to Use

**Direct invocation:**

```
Use the context-compression skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `context-compression`
- `summarization`
- `compaction`
- `token-optimization`

## What's Inside

- **When to Activate**
- **Core Concepts**
- **Detailed Topics**
- **Session Intent**
- **Files Modified**
- **Decisions Made**
- **Current State**
- **Next Steps**

## Version History

- `1.0.4` fix(context-engineering): optimize descriptions with cross-references and NOT clauses (7881054)
- `1.0.3` fix(context-compression): add standard keywords and expand README to full format (4005434)
- `1.0.2` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.1` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.0` Initial release (697ea68)

## Related Skills

- **[Context Degradation](../context-degradation/)** -- Patterns for recognizing and mitigating context failures in LLM agents. Covers lost-in-middle, context poisoning, distra...
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational understanding of context engineering for AI agent systems. Covers context anatomy, attention mechanics, pro...
- **[Context Optimization](../context-optimization/)** -- Techniques for extending effective context capacity through compaction, observation masking, KV-cache optimization, and ...
- **[Filesystem Context](../filesystem-context/)** -- Filesystem-based context engineering patterns for LLM agents. Scratch pads, plan persistence, sub-agent communication, d...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 46 production-grade plugins for Claude Code.
