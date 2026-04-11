# Filesystem Context

> **v1.0.4** | Context Engineering | 5 iterations

Filesystem-based context engineering patterns for LLM agents. Scratch pads, plan persistence, sub-agent communication, dynamic skill loading, terminal persistence, and self-modification patterns.

## What Problem Does This Solve

LLM agents operating on long-horizon tasks accumulate tool outputs, plans, and intermediate results in their context window until it fills up and performance degrades. The usual workarounds — summarisation and truncation — lose information. This skill addresses that constraint by treating the filesystem as an unlimited external memory layer: large outputs are written to files and referenced by pointer, plans are persisted and re-read on each turn, and sub-agents share state through a shared workspace rather than message chains.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Our agent's context window fills up with tool outputs" | Scratch pad pattern — write large tool outputs to files above a token threshold, return a summary + file reference |
| "The agent loses track of its plan halfway through a long task" | Plan persistence pattern with YAML schema for objective, steps, and statuses that the agent re-reads each turn |
| "Sub-agents are duplicating work because they can't share state" | Sub-agent workspace pattern with per-agent file directories that the coordinator reads directly |
| "We have dozens of skills but can't load them all into the system prompt" | Dynamic skill loading pattern — store skills as files, include only names and descriptions statically, load on demand |
| "Terminal output from long-running builds is swamping the context" | Terminal persistence pattern — sync stdout to dated files, agents grep for error patterns rather than loading full logs |
| "How do I keep agent token usage under control across sessions?" | Token accounting guidance and file organisation conventions for scratch, memory, skills, and agent workspaces |

## When NOT to Use This Skill

- in-context optimization like KV-cache or observation masking -- use [context-optimization](../context-optimization/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/filesystem-context
```

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

- **When to Activate** -- Decision criteria for when filesystem patterns are appropriate versus when to stay in-context.
- **Core Concepts** -- Explanation of the four ways context engineering fails and how filesystem-based dynamic discovery addresses each one.
- **Detailed Topics** -- Six implementation patterns: scratch pad, plan persistence, sub-agent communication, dynamic skill loading, terminal/log persistence, and self-modification through learned preferences.
- **Practical Guidance** -- Threshold guidance (2000-token rule), recommended directory structure for scratch/memory/skills/agents, and token accounting approach.
- **Examples** -- Three worked examples showing before/after token counts for tool output offloading, dynamic skill loading, and chat history as file reference.
- **Guidelines** -- Ten numbered rules for effective filesystem context engineering, from output threshold to cleanup for scratch files.
- **Integration** -- How this skill connects to context-optimization, memory-systems, multi-agent-patterns, context-compression, and tool-design.
- **References** -- Links to internal implementation patterns and related external resources (LangChain, Cursor, Anthropic).

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

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
