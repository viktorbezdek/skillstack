# Context Fundamentals

> **v1.0.5** | Context Engineering | 6 iterations

Foundational understanding of context engineering for AI agent systems. Covers context anatomy, attention mechanics, progressive disclosure, context budgeting, and the quality-vs-quantity principle.

## What Problem Does This Solve

Engineers building AI agent systems routinely run into unpredictable behavior, ballooning costs, and degraded outputs without understanding the underlying cause: context is a finite, attention-constrained resource, not an unlimited memory store. Without a mental model of how context components (system prompts, tool definitions, retrieved documents, message history, tool outputs) compete for attention budget, every architectural decision is guesswork. This skill provides the foundational theory needed before tackling compression, optimization, or degradation.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "I'm new to context engineering — where do I start?" | Anatomy of context: the five component types, how they interact, and which dominates token usage in typical agent trajectories |
| "Why does my agent perform worse as conversations get longer?" | Attention budget mechanics: n² relationship growth, position encoding degradation, and effective context limits versus nominal window sizes |
| "How should I structure my system prompt?" | System prompt organization principles: optimal altitude, XML/Markdown sectioning, and the two failure modes (brittle over-specification vs. vague under-specification) |
| "My agent is loading all documents upfront and running out of context" | Progressive disclosure principle: loading only skill names at startup, retrieving full content on demand with filesystem-based just-in-time access |
| "Adding more context is making my agent slower and more expensive" | Quality-vs-quantity principle: why larger contexts have exponentially growing costs and diminishing returns beyond threshold |
| "How do I design a context budget for my agent system?" | Context budgeting guidance: category allocation, utilization monitoring, compaction trigger thresholds, and attention-favored placement |

## When NOT to Use This Skill

- fixing broken context or diagnosing failures -- use [context-degradation](../context-degradation/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/context-fundamentals
```

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

- **When to Activate** -- Scenarios where foundational context knowledge is the right starting point: new agent design, unexpected behavior debugging, cost optimization, and onboarding.
- **Core Concepts** -- The five context components (system prompts, tool definitions, retrieved documents, message history, tool outputs), the attention budget constraint, and the progressive disclosure principle.
- **Detailed Topics** -- Deep coverage of context window anatomy, attention mechanics and position encoding, context quality versus quantity, and treating context as a finite resource with diminishing returns.
- **Practical Guidance** -- Filesystem-based access patterns, hybrid preload-plus-exploration strategies, and explicit context budgeting with threshold-based compaction triggers.
- **Examples** -- Structured system prompt with XML sections, and a two-step progressive document loading pattern.
- **Guidelines** -- Eight prioritized rules for treating context as a finite resource, from placement to progressive disclosure to compaction timing.
- **Integration** -- How this skill feeds into context-degradation (failures), context-optimization (techniques), multi-agent-patterns (isolation), and tool-design (tool definition quality).
- **References** -- Internal reference to the context components technical reference and external research on transformer attention mechanisms.

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

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
