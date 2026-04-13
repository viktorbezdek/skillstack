> **v1.0.5** | Context Engineering | 6 iterations

# Context Fundamentals

The foundational theory of context engineering -- what context is, how attention works, why larger contexts hurt, and how to budget tokens -- that you need before tackling compression, optimization, or degradation.

## What Problem Does This Solve

Engineers building AI agent systems routinely hit unpredictable behavior, ballooning costs, and degraded outputs without understanding the underlying cause: context is a finite, attention-constrained resource, not an unlimited memory store. Without a mental model of how the five context components (system prompts, tool definitions, retrieved documents, message history, tool outputs) compete for attention budget, every architectural decision is guesswork. Tool outputs alone consume 83.9% of total context in typical agent trajectories, yet most teams treat context as a simple append-only log. This skill provides the foundational theory that all the other context engineering skills build on.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-fundamentals@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

This is a single-skill plugin with two reference documents:

| Component | Description |
|---|---|
| `skills/context-fundamentals/SKILL.md` | Core skill covering context anatomy (five component types), attention budget mechanics (n-squared relationship growth), position encoding and context extension, the progressive disclosure principle, context quality vs. quantity, context as a finite resource, and practical guidance on file-system-based access, hybrid strategies, and context budgeting |
| `references/context-components.md` | Technical reference with system prompt engineering (section structure, altitude calibration with too-low/too-high/optimal examples), tool definition specification (schema structure, description engineering), retrieved document management (identifier design, semantic chunking), message history management (turn representation, summary injection), tool output optimization (response formats, observation masking), context budget estimation, and progressive disclosure implementation patterns |
| `references/latest-research-2026.md` | Comprehensive survey of 2025-2026 research: frontier model context windows (Gemini 3 Pro 10M, Llama 4 Scout 10M, Claude Opus 4.6 ~200K), attention sink phenomenon (ICLR 2025), iRoPE architecture, YaRN position interpolation, SWAT training, production compression techniques, KV-cache advances (EAGLE-3, LongSpec), RULER/HELM/LongBench Pro benchmarks, and patterns from Anthropic, Google DeepMind, and Meta |

## Usage Scenarios

**1. Starting a new agent system from scratch**

You are designing an agent system and need to understand what context even is before making architectural decisions. This skill explains the five context components, how they interact, which one dominates token usage (tool outputs at 83.9%), and provides the progressive disclosure principle: load only skill names at startup, retrieve full content on demand.

**2. Agent performance degrades as conversations get longer**

Your agent works well on short conversations but quality drops after 50+ turns. This skill explains the attention budget constraint: n-squared relationships between tokens must be computed, and models have less experience with long-range dependencies from training data distributions. This foundational understanding helps you decide whether you need compression, optimization, or architectural isolation.

**3. Designing a system prompt that actually works**

Your system prompt is either too brittle (complex if-else logic that breaks when anything changes) or too vague (the agent guesses what you want). The skill provides altitude calibration with concrete examples of too-low, too-high, and optimal instruction levels, plus structural organization using XML tags or Markdown headers for background information, instructions, tool guidance, and output description.

**4. Agent loads all documents upfront and runs out of context**

Instead of stuffing everything into context, use progressive disclosure: maintain lightweight identifiers (file paths, stored queries, web links) and load data dynamically. The file system provides natural structure -- file sizes suggest complexity, naming conventions hint at purpose, timestamps indicate relevance. The skill covers hybrid strategies: pre-load critical context (like CLAUDE.md files), enable autonomous exploration for the rest.

**5. Understanding the latest research before making architectural choices**

The research reference covers frontier developments through March 2026: Chroma Research testing 18 models and finding all degrade as context grows (not just near the limit), the attention sink phenomenon where first tokens receive disproportionate attention regardless of semantic relevance, and the key finding that context quality matters more than quantity -- a well-curated 10K-token context outperforms a noisy 100K-token context on most tasks.

## How to Use

**Direct invocation:**

```
Use the context-fundamentals skill to explain context budgeting for my agent system
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `context-engineering`
- `attention`
- `progressive-disclosure`
- `context-window`

## When to Use / When NOT to Use

**Use when:**
- Designing new agent systems or modifying existing architectures
- Onboarding team members to context engineering concepts
- Reviewing context-related design decisions
- Needing to understand context anatomy before diving into specific techniques

**Do NOT use when:**
- Fixing broken context or diagnosing failures -- use [context-degradation](../context-degradation/) instead
- Compressing or summarizing context -- use [context-compression](../context-compression/) instead
- Optimizing KV-cache or context partitioning -- use [context-optimization](../context-optimization/) instead
- Working with file-based context patterns or scratch pads -- use [filesystem-context](../filesystem-context/) instead

## Related Plugins

- **[Context Compression](../context-compression/)** -- Reducing context size through summarization strategies, anchored iterative summarization, and probe-based evaluation
- **[Context Degradation](../context-degradation/)** -- Diagnosing context failures: lost-in-middle, poisoning, distraction, clash, and confusion patterns with model-specific thresholds
- **[Context Optimization](../context-optimization/)** -- Extending effective context capacity: KV-cache optimization, observation masking, and context partitioning
- **[Filesystem Context](../filesystem-context/)** -- Using the file system for context: scratch pads, plan persistence, and sub-agent file workspaces

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
