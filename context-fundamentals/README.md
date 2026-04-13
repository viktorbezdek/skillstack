> **v1.0.5** | Context Engineering | 6 iterations

# Context Fundamentals

> The foundational theory of context engineering -- what context is, how attention works, and why the smallest high-signal token set outperforms dumping everything into the window.

## The Problem

Most teams building LLM agents treat context like a bucket: pour in the system prompt, tool definitions, retrieved documents, message history, and tool outputs, then hope the model figures out what matters. When the agent produces poor results, they add more context -- longer system prompts, more retrieved documents, fuller tool descriptions -- making the problem worse. They have no mental model for why context quality matters more than context quantity, or why their 200K-token context window produces worse results than a carefully curated 20K-token one.

The consequences compound. Engineers write system prompts at the wrong altitude -- either so vague the model guesses at behavior, or so brittle that any deviation breaks the agent. Tool definitions lack usage context, forcing agents to guess which tool applies. Retrieved documents get dumped into context without relevance filtering, consuming attention budget on irrelevant content. Tool outputs -- which research shows can reach 83.9% of total context usage -- accumulate without any strategy for retention or masking. And nobody monitors context utilization during development, so degradation hits in production as a surprise.

Without foundational understanding of how attention works, what progressive disclosure means in practice, and why context is a finite resource with diminishing returns, every other context engineering skill builds on sand. Teams cannot diagnose degradation if they do not understand the attention budget. They cannot design compression strategies if they do not know what context components matter most. They cannot build effective multi-agent systems if they do not understand why context isolation works.

## The Solution

This plugin teaches the foundational theory of context engineering through five interconnected concepts: the anatomy of context (system prompts, tool definitions, retrieved documents, message history, tool outputs), attention mechanics (the finite budget, position encoding, the n-squared relationship constraint), progressive disclosure (load information only when needed, not upfront), context quality versus quantity (informativity over exhaustiveness), and context budgeting (explicit limits, monitoring, compaction triggers).

The skill provides concrete guidance on system prompt organization (section boundaries, the right altitude between brittle specificity and vague abstraction), tool definition design (descriptions that steer behavior, the consolidation principle), and progressive document loading (just-in-time retrieval, file-system-based access patterns). It explains why models allocate attention as they do and what this means for where you place information in context.

After working through this plugin, you have a mental model that makes every other context engineering decision -- compression, optimization, degradation diagnosis, filesystem offloading -- grounded in first principles rather than cargo-culted from blog posts.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Treat context as an unlimited bucket and dump everything in | Understand context as a finite resource with diminishing marginal returns and curate accordingly |
| System prompts are either too vague (model guesses) or too brittle (breaks on deviation) | System prompts hit the right altitude: specific enough to guide, flexible enough to provide strong heuristics |
| Tool definitions lack context and examples, forcing agents to guess | Tool descriptions include usage context, examples, and defaults following the consolidation principle |
| Load all documents upfront "just in case" they are needed | Progressive disclosure loads information only when activated, keeping active context lean |
| No awareness of where information gets attention in the window | Place critical information at attention-favored positions (beginning and end) based on the U-shaped attention curve |
| No context budget -- discover limits through production failures | Explicit context budgets with monitoring and compaction triggers at 70-80% utilization |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-fundamentals@skillstack
```

### Verify installation

After installing, test with:

```
Explain how context engineering works for LLM agents -- I'm building my first agent and need to understand the fundamentals
```

## Quick Start

1. Install the plugin using the commands above
2. Start with the big picture: `I'm designing a new coding agent -- what do I need to know about context engineering?`
3. The skill walks you through context anatomy (the five components), attention mechanics (why placement matters), and progressive disclosure (load only what you need)
4. Apply the principles: organize your system prompt with clear sections, add usage context to tool descriptions, and implement just-in-time document loading
5. Set up monitoring: establish context budgets and compaction triggers before deploying to production

## What's Inside

| Component | Description |
|---|---|
| `context-fundamentals` skill | Core skill covering context anatomy, attention mechanics, progressive disclosure, quality-vs-quantity, context budgeting, system prompt organization, tool definition design, and hybrid loading strategies |
| `context-components.md` reference | Technical reference with detailed system prompt engineering, section structure patterns, and component-specific design guidance |
| 13 trigger eval cases | Validates correct skill activation and near-miss rejection |
| 3 output eval cases | Tests fundamentals explanation, architecture guidance, and concept application |

### context-fundamentals

**What it does:** Activates when you need to understand context engineering from first principles -- what context is, how the attention mechanism constrains it, why quality beats quantity, and how to design context-aware agent architectures. This is the prerequisite skill for all other context engineering work.

**Try these prompts:**

```
I'm building my first LLM agent -- explain what context engineering is and why it matters for agent performance
```

```
How should I organize my agent's system prompt? Right now it's a wall of text and the agent ignores half of it
```

```
My agent has access to 200K tokens of context but performance gets worse when I use more than 30K -- why is bigger not better?
```

```
What's progressive disclosure in context engineering? I keep hearing the term but I don't understand how to apply it
```

```
I need to design a context budget for my agent system -- how do I decide what goes in context vs what gets loaded on demand?
```

**Key references:**

| Reference | Topic |
|---|---|
| `context-components.md` | Detailed technical reference for system prompt section structure, component engineering patterns, and design guidance for each context component type |

## Real-World Walkthrough

You are building a customer support agent that handles technical questions about your company's API. The agent has access to 150 documentation pages, a system prompt, 12 tool definitions, and message history from ongoing conversations. You have thrown everything into context and the agent is producing mediocre results: it sometimes answers from the wrong documentation page, ignores relevant tool definitions, and starts degrading noticeably after 20 messages.

You open Claude Code to get foundational guidance:

```
I'm building a support agent and the quality is bad -- it uses wrong docs, ignores tools, and degrades after 20 messages. I think my context setup is fundamentally wrong. Help me understand context engineering basics.
```

The context-fundamentals skill activates and starts with the anatomy of context. Your agent has five components competing for the same attention budget: system prompt, tool definitions, retrieved documents, message history, and tool outputs. The skill explains that attention is not evenly distributed -- it follows a U-shaped curve where the beginning and end of context receive disproportionate attention, and everything in the middle gets less.

You realize your first mistake: all 150 documentation pages are loaded at session start. That is roughly 120K tokens of documents, most of which are irrelevant to any individual question. The skill introduces progressive disclosure: instead of pre-loading everything, maintain lightweight identifiers (page titles, summaries) and load full pages only when a question matches. This mirrors how humans work -- you do not memorize an entire manual, you use the table of contents to find the right section.

You implement a two-stage retrieval system. Stage one loads a 500-token document index at session start. Stage two loads the full content of the top 3 relevant pages when a question arrives. Your active context drops from 120K to about 8K tokens of documentation per question. Immediately, the agent stops referencing wrong pages because irrelevant pages are no longer in context competing for attention.

Next, the skill addresses your system prompt. You show it to the skill:

```
You are a helpful customer support agent. Be professional and accurate. Use the tools available. Follow company policies.
```

The skill identifies this as too high an altitude -- vague instructions that fail to give the model concrete signals. It walks you through the recommended structure: background information (domain, customer types, product context), instructions (specific behavioral guidelines with examples), tool guidance (when to use each tool, with defaults and edge cases), and output description (response format, tone, escalation triggers). You restructure the prompt into four clearly delimited sections using XML tags.

Then you tackle tool definitions. Your 12 tools have one-line descriptions like "Search the knowledge base" and "Create a ticket." The skill explains the consolidation principle: if a human engineer cannot definitively say which tool should be used in a given situation, the agent cannot either. You rewrite descriptions with usage context: "Search the knowledge base -- use when the customer asks a question about API functionality, rate limits, or authentication. Returns top 5 matching articles with relevance scores. Default: search the most recent documentation version."

With tool descriptions improved, the agent stops ignoring relevant tools. It now selects the right tool 90% of the time versus 60% before, because the descriptions provide the usage context the model needs for disambiguation.

Finally, the skill addresses the degradation after 20 messages. Tool outputs -- API responses, search results, file contents -- accumulate in message history and consume attention budget. Research shows tool outputs can reach 83.9% of total context usage. After 20 messages of accumulated tool results, your agent's active context is dominated by old tool outputs that are no longer relevant. The skill recommends implementing observation masking (replacing verbose old tool outputs with compact summaries) and compaction triggers at 70-80% context utilization.

After these changes, your support agent handles 50+ message conversations without degradation, answers from the correct documentation 95% of the time, and selects the right tool on the first attempt. The model did not change. The total amount of information available to the agent did not change. What changed was how context is assembled, organized, and maintained -- the fundamentals.

## Usage Scenarios

### Scenario 1: Designing context architecture for a new agent

**Context:** You are starting a new agent project and want to set up the context architecture correctly from the beginning rather than debugging it later.

**You say:** `I'm designing a new coding agent from scratch -- walk me through how to set up the context architecture so I don't run into problems later`

**The skill provides:**
- Anatomy of the five context components and how they interact
- System prompt organization with section boundaries and the right altitude
- Progressive disclosure strategy for document loading
- Context budget framework with monitoring and compaction triggers
- Attention-aware placement guidelines

**You end up with:** A context architecture design that handles growth gracefully, with explicit budgets and loading strategies for each component type.

### Scenario 2: Fixing a vague or brittle system prompt

**Context:** Your agent ignores parts of its system prompt or follows instructions too literally, breaking when inputs vary slightly from the expected pattern.

**You say:** `My agent either ignores half its system prompt or follows it so literally that it breaks on edge cases -- how do I write a system prompt at the right level?`

**The skill provides:**
- The altitude concept: too vague vs too brittle, and the sweet spot between them
- Section structure with XML tags or Markdown headers for background, instructions, tool guidance, and output format
- The principle that structural clarity matters more than exact formatting
- Examples of well-organized system prompts with appropriate specificity

**You end up with:** A restructured system prompt that guides behavior effectively without creating brittleness.

### Scenario 3: Understanding why more context produces worse results

**Context:** You expanded your agent's context window and loaded more reference documents, but quality dropped instead of improving.

**You say:** `I upgraded to a model with 200K context and loaded all our docs into it, but the agent's answers are worse than before with 30K context -- what's going on?`

**The skill provides:**
- The attention budget constraint: n-squared relationships stretch the budget as context grows
- Quality versus quantity: the smallest high-signal token set outperforms exhaustive loading
- Empirical evidence that performance degrades beyond model-specific thresholds
- Cost implications of large-context processing (non-linear growth)
- Progressive disclosure as the alternative to pre-loading

**You end up with:** Understanding of why bigger is not better for context, and a strategy for loading only what the agent needs for each task.

### Scenario 4: Setting up context monitoring for production

**Context:** Your agent works in development but you want to prevent context-related failures in production before they happen.

**You say:** `How do I set up context budgeting and monitoring for my agent before it goes to production?`

**The skill provides:**
- Context budget framework: know the effective limit for your model and task type
- Monitoring strategy: track context utilization during sessions
- Compaction trigger placement at 70-80% utilization
- Design for degradation: assume context will degrade and plan accordingly
- Attention distribution awareness for critical information placement

**You end up with:** A monitoring and budgeting plan that catches context problems before they impact users.

## Ideal For

- **Teams building their first LLM agent** who need foundational understanding before making architectural decisions
- **Engineers debugging mysterious agent behavior** that might stem from context mismanagement rather than model limitations
- **Tech leads onboarding team members** to context engineering concepts before they start building
- **Anyone who has read about context windows** but does not understand why their 200K-token window performs worse than a curated 20K-token one
- **Architects evaluating context strategies** who need first-principles understanding to make informed decisions about compression, optimization, or multi-agent isolation

## Not For

- **Diagnosing specific context failures** (lost-in-middle, poisoning, distraction) -- use [context-degradation](../context-degradation/) instead
- **Compressing or summarizing context** to reduce token usage -- use [context-compression](../context-compression/) instead
- **KV-cache optimization, observation masking, or context partitioning** -- use [context-optimization](../context-optimization/) instead
- **File-based context patterns** like scratch pads and plan persistence -- use [filesystem-context](../filesystem-context/) instead

## How It Works Under the Hood

The plugin is a single-skill architecture with one technical reference document.

The **core skill** (`SKILL.md`) covers five foundational topics: context anatomy (the five component types and their characteristics), attention mechanics (the finite budget, n-squared constraint, position encoding), progressive disclosure (just-in-time loading, file-system-based access, hybrid strategies), quality versus quantity (informativity over exhaustiveness, the cost of large contexts), and context budgeting (explicit limits, monitoring, compaction triggers, attention-aware placement). It provides practical guidance on system prompt organization, tool definition design, and document loading strategies.

The **context-components reference** (`context-components.md`) provides the technical depth layer with detailed section structure patterns for system prompts, engineering guidelines for each component type, and design patterns for context-aware architectures. This reference activates when you need to implement specific component designs rather than understand general principles.

The skill serves as the prerequisite for all other context engineering plugins. It explicitly routes to context-degradation for failure diagnosis, context-compression for summarization strategies, context-optimization for performance techniques, and filesystem-context for file-based patterns.

## Related Plugins

- **[Context Degradation](../context-degradation/)** -- Diagnosing context failures: lost-in-middle, poisoning, distraction, clash, and confusion patterns with empirical thresholds
- **[Context Compression](../context-compression/)** -- Reducing context size: summarization strategies, anchored iterative summarization, and probe-based evaluation
- **[Context Optimization](../context-optimization/)** -- Extending effective context capacity: KV-cache optimization, observation masking, and retrieval strategies
- **[Filesystem Context](../filesystem-context/)** -- Using the file system for context: scratch pads, plan persistence, and sub-agent file workspaces

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
