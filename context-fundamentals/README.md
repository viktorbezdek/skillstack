> **v1.0.6** | Context Engineering | 6 iterations

# Context Fundamentals

> The foundational theory of context engineering -- what context is, how attention works, progressive disclosure principles, and why the smallest high-signal token set outperforms dumping everything into the window.
> Single skill + 2 reference documents | 13 trigger evals, 3 output evals

## The Problem

Context engineering is the most important skill in building effective AI agents, yet most teams approach it without a mental model. They treat the context window as a bucket: throw in the system prompt, tool definitions, retrieved documents, and message history, hope the model sorts it out. When the agent produces poor results, they add more context. When the window fills up, they get a bigger model. Neither approach works reliably, and teams waste months on symptoms because they do not understand the underlying mechanics.

The fundamental misconception is that more context equals better performance. Research consistently shows the opposite: larger context windows create diminishing returns and active degradation. Processing cost grows disproportionately -- not double the cost for double the tokens, but exponentially more in time and computing resources. Attention mechanisms create finite budgets that deplete as context grows. Models develop attention patterns from training data where shorter sequences predominate, meaning they have less specialized capacity for long-range dependencies. Without understanding these mechanics, teams cannot make rational decisions about what goes into context and what stays out.

The practical cost is enormous. Tool outputs alone can comprise 83.9% of total context usage in typical agent trajectories. Teams that do not understand this pay for context they do not need, get worse results from context that competes for attention, and have no framework for deciding what to include, exclude, or load on demand.

## The Solution

This plugin provides the foundational theory that all context engineering skills build upon. It covers the five components of context (system prompts, tool definitions, retrieved documents, message history, and tool outputs), attention mechanics and the budget constraint, progressive disclosure as the core management principle, and context budgeting as an engineering discipline. The skill does not fix specific problems -- it builds the mental model needed to diagnose and fix any context problem.

The core principle is informativity over exhaustiveness: include what matters for the decision at hand, exclude what does not, and design systems that can access additional information on demand. This applies at every level -- from system prompt organization to tool definition design to retrieval strategy. The plugin teaches you to think about context as a finite resource with diminishing returns, not an infinite bucket to fill.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Treat context as a bucket: add everything, hope the model sorts it out | Understand context as a finite resource with an attention budget that depletes as it grows |
| Assume bigger context windows solve quality problems | Know that larger contexts create diminishing returns and active degradation beyond model-specific thresholds |
| No framework for deciding what goes in context vs. what stays out | Progressive disclosure principle: load information only as needed, keep agents fast with on-demand access |
| Tool outputs fill 80%+ of context unnoticed | Understand that observations dominate context and require strategies like masking and selective retention |
| System prompts are written once and never structured | Organize prompts with clear section boundaries at the right altitude: specific enough to guide, flexible enough to generalize |
| No context budget -- discover limits only when things break | Design with explicit context budgets, monitoring usage and triggering optimization at 70-80% utilization |

## Context to Provide

This skill provides foundational theory, so prompts work best when they describe the design decision or architectural choice you are facing rather than asking about theory in the abstract. The skill generates the most useful output when it understands what you are building, not just what you want to learn.

**What to include in your prompt:**
- **What you are building** (agent type, tool count, document access pattern, expected conversation length)
- **Your context window size** -- actual token budget forces concrete allocation guidance
- **What is going wrong or unclear** (agent gets worse over time, not sure what to include, unsure how to structure the system prompt)
- **Your current approach** -- describe what you have now so the skill can identify the gap

**What makes results better:**
- Describing the information your agent needs to access (number of documents, how often they change, how much is relevant per task)
- Saying how many tools are defined and whether they are long or short descriptions
- Specifying whether conversations are short (10 turns) or long (50+ turns)
- Asking about a specific trade-off ("should I pre-load docs or use progressive disclosure?")

**What makes results worse:**
- Asking "explain context" without any agent design context -- produces textbook explanation rather than actionable guidance
- Asking how LLMs work in general -- this skill teaches context engineering for agent design, not LLM internals
- Skipping directly to "optimize my cache" or "compress my context" without understanding the fundamentals these techniques build on

**Template prompt:**
```
I am building a [agent type] with [N] tools, access to [describe document set], and expected conversations of [length]. My model has a [N]-token context window. Help me understand [specific aspect: how to budget, whether to use progressive disclosure, how to structure the system prompt, why adding more context hurts performance].
```

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-fundamentals@skillstack
```

### Prerequisites

No additional dependencies. This is the starting point for the context engineering plugin family. After installing, consider `context-degradation` (failure patterns), `context-compression` (reduction strategies), and `context-optimization` (extending capacity).

### Verify installation

After installing, test with:

```
Explain how context works in LLM agents -- what are the components, how does the attention budget work, and what's the progressive disclosure principle?
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `"What are the five components of LLM context and how do they interact?"`
3. The skill provides a structured breakdown of system prompts, tool definitions, retrieved documents, message history, and tool outputs with their attention implications
4. Follow up with: `"How should I budget context for a coding agent with a 200K token window?"`
5. The skill walks you through budget allocation, progressive disclosure, and monitoring strategies

---

## System Overview

```
context-fundamentals (plugin)
└── context-fundamentals (skill)
    ├── Context anatomy (5 components)
    │   ├── System prompts (identity, constraints, guidelines)
    │   ├── Tool definitions (actions, descriptions, parameters)
    │   ├── Retrieved documents (domain knowledge, RAG)
    │   ├── Message history (conversation, scratchpad)
    │   └── Tool outputs (observations, 80%+ of typical context)
    ├── Attention mechanics & budget constraint
    ├── Progressive disclosure principle
    ├── Context quality vs quantity
    └── references/
        ├── context-components.md (system prompt engineering, technical detail)
        └── latest-research-2026.md (current LLM context engineering research)
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `context-fundamentals` | Skill | Context anatomy, attention mechanics, progressive disclosure, context budgeting |
| `context-components.md` | Reference | System prompt engineering detail, technical depth on each component |
| `latest-research-2026.md` | Reference | Current research findings on LLM context engineering (2025-2026) |
| Trigger evals | Test suite | 13 trigger evaluation cases |
| Output evals | Test suite | 3 output quality evaluation cases |

### Component Spotlights

#### context-fundamentals (skill)

**What it does:** Activates when users need to understand context engineering theory. Provides the foundational mental model for how LLM context works -- the five components, attention budget mechanics, progressive disclosure, and context budgeting principles. This is the prerequisite skill for all other context engineering plugins.

**Input -> Output:** Questions about context mechanics, agent architecture decisions, or context-related design trade-offs -> Foundational understanding of context components, attention constraints, progressive disclosure strategies, and budget allocation guidance.

**When to use:**
- Designing new agent systems or modifying existing architectures
- Debugging unexpected agent behavior that may relate to context
- Optimizing context usage to reduce token costs or improve performance
- Onboarding new team members to context engineering concepts
- Reviewing context-related design decisions

**When NOT to use:**
- Diagnosing specific context failures or degradation (use `context-degradation`)
- Compressing or summarizing context (use `context-compression`)
- KV-cache optimization or partitioning (use `context-optimization`)
- File-based context patterns or scratch pads (use `filesystem-context`)

**Try these prompts:**

```
I'm designing a coding agent with 20 tools and access to a 200-file documentation set. My model has a 200K token window. What should I know about context engineering before I finalize the architecture? What are the key constraints I'll hit?
```

```
I added our entire API documentation (about 50 markdown files) to my agent's context and it got worse, not better. It was more accurate with just the top 10 docs. Why does more information hurt performance?
```

```
How should I structure the system prompt for a customer support agent with 15 tools? It needs to stay consistent across a 60-turn conversation. What's the right level of specificity?
```

```
My agent needs access to 300 documentation pages but only 3-5 are relevant to any single task. What is progressive disclosure and how do I implement it so context stays lean while the agent can still access anything it needs?
```

**Key references:**

| Reference | Topic |
|---|---|
| `context-components.md` | Detailed system prompt engineering, tool definition design, and technical depth on each context component |
| `latest-research-2026.md` | Current research findings on LLM context engineering, attention mechanisms, and production patterns |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate) | Good (specific, activates reliably) |
|---|---|
| "How do LLMs work?" | "How does the attention budget constraint work in LLM context windows, and what does it mean for agent design?" |
| "Help with my prompt" | "How should I structure a system prompt for a coding agent? What sections should it have and at what altitude?" |
| "Explain context" | "What are the five components of LLM context and how much of the budget does each typically consume?" |
| "Make my agent better" | "My agent loads 50 documents at startup. Should I use progressive disclosure instead? What's the trade-off?" |

### Structured Prompt Templates

**For understanding context anatomy:**
```
I'm building a [type of agent] with [tool count] tools and access to [document count/type] documents. Walk me through how these components interact in context and where I should expect bottlenecks.
```

**For context budget design:**
```
My model has a [N]-token context window. I need to allocate budget for [system prompt / tools / docs / history / buffer]. What's a reasonable allocation and how should I monitor it?
```

**For progressive disclosure design:**
```
My agent needs access to [large information set] but most of it is irrelevant to any single task. How do I implement progressive disclosure to keep context lean while maintaining access?
```

### Prompt Anti-Patterns

- **Asking about specific failures:** "Why does my agent hallucinate?" is a degradation question, not a fundamentals question. The skill provides theory, not diagnosis. Use `context-degradation` for failure analysis.
- **Requesting implementation code:** "Write me a context management system" goes beyond fundamentals. The skill teaches the principles; implementation details come from `context-optimization` and `context-compression`.
- **Skipping to optimization:** "How do I optimize KV-cache?" assumes fundamentals are understood. If you are asking about cache optimization without understanding the attention budget, start here first.

## Real-World Walkthrough

**Starting situation:** You are a senior engineer tasked with building your company's first AI coding agent. You have experience with LLM APIs but have never designed an agent architecture. You need to understand context engineering before making design decisions that will be expensive to change later.

**Step 1: Understand the five components.** You ask: "I'm designing a coding agent. What should I know about context engineering fundamentals before I start?"

The skill walks you through the five context components. System prompts establish identity and constraints -- they load once and persist. Tool definitions specify available actions -- each one consumes context proportional to its description length. Retrieved documents provide domain knowledge -- they are the most variable component. Message history tracks the conversation -- it grows with every turn. Tool outputs are the results of actions -- and they consume the most context, reaching 83.9% in typical agent trajectories.

**Step 2: Learn the attention budget constraint.** You ask: "How does the attention budget work? Why can't I just fill the context window?"

The skill explains that attention creates pairwise relationships between all tokens (n-squared relationships for n tokens). As context grows, the model's ability to capture these relationships stretches thin. Models develop attention patterns from training data where shorter sequences predominate. The result: a finite attention budget that depletes as context grows. This is why adding more context often makes results worse, not better. The critical insight is that context engineering means finding the smallest possible set of high-signal tokens, not filling the window.

**Step 3: Apply progressive disclosure.** You realize your agent will need access to project documentation, API references, and code context. You ask: "How do I give my agent access to 200 files of documentation without loading them all into context?"

The skill introduces progressive disclosure: at startup, load only skill names and descriptions -- enough to know when something might be relevant. Full content loads only when activated for a specific task. For documentation, maintain lightweight identifiers (file paths, summaries, search indices) and load full documents on demand. This mirrors human cognition -- we do not memorize entire libraries, we use indexing systems to retrieve what we need.

**Step 4: Design the system prompt.** You ask: "How should I structure my system prompt? How specific should it be?"

The skill explains the altitude problem. Too specific (hardcoded brittle logic) creates fragility. Too vague (high-level platitudes) fails to guide behavior. The right altitude: specific enough to give concrete signals, flexible enough to provide strong heuristics. Structure the prompt with clear sections using XML tags or Markdown headers: background information, instructions, tool guidance, and output description. The exact formatting matters less than structural clarity.

**Step 5: Plan the context budget.** You ask: "My model has a 200K token context window. How should I budget it?"

The skill helps you allocate: system prompt (2-5K tokens, stable), tool definitions (5-15K depending on tool count, stable), retrieved documents (variable, budget 20-30K), message history (grows continuously, budget 50-80K), buffer for tool outputs (remainder). Set monitoring at these thresholds and trigger compaction at 70-80% utilization. Design assuming context will degrade rather than hoping it will not.

**Step 6: Connect to hybrid strategies.** The skill introduces hybrid context loading: pre-load stable content (CLAUDE.md files, project rules) for speed, but enable autonomous exploration for additional context. For contexts with less dynamic content, pre-load more. For rapidly changing or highly specific information, use just-in-time loading. This completes your foundational understanding.

**Gotchas discovered:** The biggest insight was that tool outputs dominate context (83.9%) and most teams never measure this. The second was that the file system itself provides navigational structure -- file sizes suggest complexity, naming conventions hint at purpose, timestamps serve as relevance proxies. Using the filesystem as a context index is often better than loading everything into the window.

## Usage Scenarios

### Scenario 1: Onboarding a team to context engineering

**Context:** You are leading a team building AI agents. Nobody has a shared mental model of how context works.

**You say:** "Explain context engineering fundamentals for a team of senior engineers who are new to agent development. Cover the key components, constraints, and design principles."

**The skill provides:**
- Structured breakdown of five context components with relative size data
- Attention budget explanation with practical implications
- Progressive disclosure as the core management principle
- Context budgeting framework with monitoring thresholds

**You end up with:** A shared vocabulary and mental model the team can use to make consistent context design decisions.

### Scenario 2: Debugging why more context makes results worse

**Context:** You added comprehensive API documentation to your agent's context and quality dropped instead of improving.

**You say:** "I added more documentation to my agent's context and it got worse. Why would more information hurt performance?"

**The skill provides:**
- Explanation of the attention budget constraint and why it depletes with more tokens
- Quality vs. quantity principle: smaller high-signal context outperforms larger low-signal context
- Concrete recommendation to switch from pre-loading to progressive disclosure

**You end up with:** Understanding of why more is not better, and a design pattern to provide access without overloading context.

### Scenario 3: Designing context for a multi-tool agent

**Context:** Your agent has 25 tools and you are not sure how tool definitions interact with the rest of context.

**You say:** "I have 25 tools defined for my agent. How do tool definitions affect context usage and how should I manage them?"

**The skill provides:**
- Explanation that tool definitions live near the front of context and consume tokens proportional to description length
- The consolidation principle: if a human cannot tell which tool to use, the agent cannot either
- Strategies for reducing tool description overhead while maintaining activation quality

**You end up with:** A redesigned tool set with clearer descriptions and possibly fewer, better-designed tools.

---

## Decision Logic

**When should I use context-fundamentals vs. the other context engineering plugins?**

Start here. This plugin provides the mental model. Once you understand the fundamentals:
- Seeing degradation symptoms? -> `context-degradation` for diagnosis
- Need to reduce context size? -> `context-compression` for strategies
- Need to extend effective capacity? -> `context-optimization` for techniques
- Need file-based context patterns? -> `filesystem-context` for scratch pads and offloading

**How does attention budget interact with context placement?**

The attention budget creates a U-shaped curve: information at the beginning and end of context receives more attention than information in the middle. This means placement matters -- critical information should go at the beginning (system prompt, current task) or end (recent conversation, active constraints). This insight comes from the fundamentals but the specific degradation pattern (lost-in-middle) is covered in `context-degradation`.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Applying fundamentals without measuring | Designing context budgets based on theory alone, missing actual usage patterns | Instrument your agent to log actual token usage per component; compare against theoretical budget |
| Over-applying progressive disclosure | Agent spends too many turns retrieving information it needs frequently | Pre-load frequently-needed context (stable references, common patterns); progressive disclosure is for infrequent needs |
| Ignoring tool output dominance | System prompt and docs are optimized but tool outputs still consume 80%+ of context | Measure tool output sizes; implement observation masking for outputs that have served their purpose |

## Ideal For

- **Agent architects** designing new systems who need the foundational mental model before making context-related design decisions
- **Engineering leads** onboarding teams to context engineering who need a structured curriculum starting from first principles
- **Developers debugging unexpected agent behavior** who need to understand whether the issue is context-related before diving into specific diagnosis tools
- **Cost-conscious teams** who are spending too much on LLM tokens and need to understand why context efficiency matters before applying optimization techniques

## Not For

- **Diagnosing specific context failures** -- if you already know your context is degrading and need to identify the pattern, use `context-degradation`
- **Implementing compression** -- if you need specific summarization strategies and evaluation, use `context-compression`
- **Performance optimization** -- if you need KV-cache, observation masking, or partitioning techniques, use `context-optimization`

## Related Plugins

- **context-degradation** -- Understanding how context fails; builds directly on the attention mechanics taught here
- **context-compression** -- Practical compression strategies grounded in the quality-vs-quantity principle
- **context-optimization** -- Advanced optimization techniques for extending effective context capacity
- **filesystem-context** -- File-based context patterns (scratch pads, external storage) for the "Write" strategy
- **tool-design** -- How tool definitions interact with context; applies the consolidation principle taught here
- **multi-agent-patterns** -- Context isolation through multi-agent architectures; applies the partitioning concept

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
