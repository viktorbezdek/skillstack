> **v1.0.4** | Context Engineering | 5 iterations

# Context Optimization

> Double or triple your agent's effective context capacity through compaction, observation masking, KV-cache optimization, and context partitioning -- without switching to a larger model.
> Single skill + 1 reference document | 13 trigger evals, 3 output evals

## The Problem

AI agent systems hit context limits long before their context windows technically fill up. An agent with a 200K-token window starts degrading at 80K tokens. Tool outputs silently consume 80%+ of the available space. Repeated prompts with identical prefixes waste computation that could be cached. The result: agents that could handle 3x more complex tasks if their context were managed efficiently.

Most teams respond to context limits by upgrading to larger-window models -- a solution that costs more, often degrades quality (larger windows have their own failure modes), and does not address the fundamental efficiency problem. A 200K-token window used at 30% efficiency gives you 60K tokens of effective capacity. The same window used at 80% efficiency gives you 160K tokens. Optimization yields more effective capacity than model upgrades at a fraction of the cost.

The specific waste patterns are well-understood but poorly addressed. Tool outputs from completed tasks linger in context consuming attention budget. Identical system prompts and tool definitions are recomputed from scratch on every request despite being unchanged. Growing message history is carried in full when most of it could be summarized. Monolithic contexts force a single agent to juggle multiple concerns when partitioned sub-agents would each operate in a clean, focused window.

## The Solution

This plugin provides four production-tested optimization techniques -- compaction (summarizing context near limits), observation masking (replacing verbose tool outputs with compact references), KV-cache optimization (reusing cached computations for stable prefixes), and context partitioning (splitting work across isolated sub-agent contexts). Each technique targets a different source of waste, and they compose: applying all four can double or triple effective context capacity without changing models.

The skill includes a decision framework for selecting which technique to apply based on context composition (which component dominates usage), trigger-based optimization (monitoring signals that indicate when to optimize), and performance benchmarks (compaction achieves 50-70% reduction, masking achieves 60-80% reduction on masked observations, cache optimization achieves 70%+ hit rates for stable workloads).

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Tool outputs from 20 turns ago still consume context despite being irrelevant | Observation masking replaces completed tool outputs with compact references (60-80% reduction) |
| Every API request recomputes the system prompt and tool definitions from scratch | KV-cache optimization reuses cached computations for stable prefixes (70%+ cache hit rate) |
| Context hits limits; response is to upgrade to a more expensive model | Compaction and masking double effective capacity on the existing model at no additional cost |
| Single agent juggles 5 different tasks in one growing context | Context partitioning isolates tasks in sub-agent windows, each operating in clean focused context |
| No framework for deciding when to optimize or which technique to apply | Trigger-based optimization monitors utilization and applies techniques based on context composition |
| Context optimization is ad hoc -- each developer invents their own approach | Systematic framework: measure, diagnose what dominates, apply the matching technique, verify improvement |

## Context to Provide

Optimization decisions depend heavily on what fills the context and at what utilization level quality degrades. Generic "make it faster" requests produce generic guidance. Providing your context composition breakdown unlocks targeted recommendations that match the specific waste pattern.

**What to include in your prompt:**
- **Current context utilization** (percentage or absolute tokens) and where quality starts to drop
- **Context composition breakdown** -- what percentage is system prompt, tool definitions, retrieved documents, message history, and tool outputs; this determines which technique to apply
- **Model and window size** -- thresholds differ by model
- **Cost or latency constraints** -- whether you are optimizing for token cost, response latency, or quality at scale
- **Workload characteristics** -- single long conversations vs. many short requests; stable prefix vs. dynamic content

**What makes results better:**
- Providing the actual percentage breakdown (e.g., "tool outputs are 52%, history is 20%, docs are 23%")
- Describing whether the system prompt and tool definitions change between requests (stable = cacheable)
- Saying whether tasks are coupled or independent (affects partitioning decisions)
- Mentioning the scale (10 requests/day vs. 10,000 requests/day changes cost optimization priority)

**What makes results worse:**
- Requesting all four techniques at once without knowing which component dominates -- each technique targets a specific waste source and has its own overhead
- Optimizing before measuring -- "make my agent better" without knowing current utilization leads to premature optimization
- Framing it as "I need a bigger context window" -- the skill will redirect you to efficiency first

**Template prompt:**
```
My [agent type] uses [N]% of its [M]-token context window. Composition: system prompt [X%], tool definitions [Y%], retrieved docs [Z%], message history [W%], tool outputs [V%]. Quality drops at [threshold]. I need to [reduce cost / handle longer sessions / improve quality]. What optimization techniques should I apply?
```

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-optimization@skillstack
```

### Prerequisites

No additional dependencies. Works best after installing `context-fundamentals` (understand the mechanics being optimized) and alongside `context-compression` (specific summarization strategies) and `context-degradation` (understanding when optimization is needed).

### Verify installation

After installing, test with:

```
My agent's context is hitting 80% utilization and quality is dropping. What optimization techniques should I apply to extend its effective capacity?
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `"My agent uses 120K of its 200K token window. Tool outputs dominate. How do I optimize?"`
3. The skill identifies observation masking as the primary technique and walks you through implementation
4. Follow up with: `"How do I set up KV-cache optimization for the stable parts of my prompt?"`
5. The skill provides cache-friendly prompt ordering and design patterns

---

## System Overview

```
context-optimization (plugin)
└── context-optimization (skill)
    ├── Four optimization techniques
    │   ├── Compaction (summarize near limits, 50-70% reduction)
    │   ├── Observation masking (replace tool outputs, 60-80% reduction)
    │   ├── KV-cache optimization (reuse stable prefixes, 70%+ hit rate)
    │   └── Context partitioning (isolate in sub-agent windows)
    ├── Budget management & trigger-based optimization
    ├── Optimization decision framework
    └── references/
        └── optimization_techniques.md (detailed technical strategies)
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `context-optimization` | Skill | Four optimization techniques, decision framework, budget management |
| `optimization_techniques.md` | Reference | Detailed compaction strategies, masking implementation, cache patterns, partitioning architectures |
| Trigger evals | Test suite | 13 trigger evaluation cases |
| Output evals | Test suite | 3 output quality evaluation cases |

### Component Spotlights

#### context-optimization (skill)

**What it does:** Activates when users need to extend effective context capacity. Provides four optimization techniques with a decision framework for selecting which to apply based on what component dominates context usage, trigger-based monitoring for when to optimize, and performance benchmarks for each technique.

**Input -> Output:** Description of context capacity problems (what fills the window, when quality drops, cost pressures) -> Specific optimization strategy combining the right techniques for your context composition, with implementation guidance and expected improvements.

**When to use:**
- Context limits constrain task complexity
- Optimizing for cost reduction (fewer tokens = lower costs)
- Reducing latency for long conversations
- Implementing long-running agent systems
- Needing to handle larger documents or conversations

**When NOT to use:**
- Reducing content via summarization specifically (use `context-compression`)
- Diagnosing context failures (use `context-degradation`)
- Learning context theory (use `context-fundamentals`)
- File-based context patterns (use `filesystem-context`)

**Try these prompts:**

```
My code review agent's context is 80% tool outputs from grep, file reads, and earlier file reviews. Most of those outputs are from files reviewed 20 turns ago. How do I implement observation masking to free up space without losing the ability to reference earlier reviews?
```

```
I'm running a production agent with 20,000 requests/day. My system prompt is 3K tokens and 15 tool definitions are 6K tokens -- identical across every request. I'm spending significant money recomputing these on every call. How do I structure the prompt for maximum KV-cache efficiency?
```

```
My customer support agent handles both account lookups and billing issues in one session. When both are active, it confuses context from one task with the other and quality drops. Should I split into sub-agents? What does partitioning look like and when does the coordination overhead outweigh the benefit?
```

```
My agent hits 80% context utilization around turn 35 and quality visibly degrades. I haven't implemented any optimization yet. What's the right order to apply compaction, masking, and caching -- and at what utilization percentage should each trigger?
```

**Key references:**

| Reference | Topic |
|---|---|
| `optimization_techniques.md` | Detailed compaction strategies, observation masking implementation, KV-cache patterns, partitioning architecture, result aggregation |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate) | Good (specific, activates reliably) |
|---|---|
| "Make context faster" | "My agent's context is 80% tool outputs. How do I apply observation masking to free up capacity?" |
| "Optimize my agent" | "I want to implement KV-cache optimization for my system prompt and tool definitions. How should I order context elements?" |
| "Use bigger context" | "My 200K window fills up too fast. What combination of compaction and masking would double effective capacity?" |
| "Context is expensive" | "How do I partition a multi-task agent into sub-agents so each operates in a clean context? What's the result aggregation pattern?" |

### Structured Prompt Templates

**For diagnosing context composition:**
```
My agent uses [N tokens] of its [M token] window. Breakdown: system prompt [X], tool definitions [Y], retrieved docs [Z], message history [W], tool outputs [V]. What optimization techniques should I apply and in what order?
```

**For implementing a specific technique:**
```
I need to implement [observation masking / KV-cache optimization / compaction / partitioning] for my [agent type]. My constraint is [cost / latency / complexity]. Walk me through the implementation.
```

**For trigger-based optimization:**
```
At what utilization percentage should I trigger [optimization technique]? My agent runs [workload type] and quality matters more than [cost / speed].
```

### Prompt Anti-Patterns

- **Requesting optimization without measurement:** "My agent is slow" does not give the skill enough to work with. Measure context utilization and identify which component dominates before optimizing.
- **Applying all techniques at once:** Each technique has overhead and trade-offs. The skill recommends based on context composition -- let it guide the selection rather than requesting everything.
- **Optimizing prematurely:** If your agent uses 30% of its context window and quality is fine, optimization adds complexity without benefit. Wait until utilization creates actual pressure.

## Real-World Walkthrough

**Starting situation:** You are running a production coding agent that helps developers with code review and refactoring tasks. The agent uses Claude Sonnet 4.5 with a 200K-token context window. As code review sessions extend to 30+ files, the context fills up and quality drops. Your monitoring shows context reaching 85% utilization with the following breakdown: system prompt (3%), tool definitions (5%), code files (25%), message history (15%), and tool outputs from earlier reviews (52%).

**Step 1: Diagnose context composition.** You ask: "My agent's context is 85% full. Tool outputs from earlier file reviews are 52% of usage. Code files are 25%. How do I optimize?"

The skill immediately identifies the primary waste: tool outputs from completed reviews. When the agent reviewed file #3 twenty turns ago, the full diff output, analysis, and suggestions are still in context despite being irrelevant to the current file. This is the textbook case for observation masking.

**Step 2: Implement observation masking.** The skill provides the masking strategy: for tool outputs older than 3 turns, replace the full content with a compact reference -- the file name, key findings (2-3 bullet points), and a reference ID to retrieve the full output if needed. Never mask observations from the most recent turn, observations critical to the current task, or observations being actively referenced in reasoning.

You implement this and measure: tool output share drops from 52% to 15%. Total context utilization drops from 85% to 48%. The agent can now review 2-3x as many files in a single session.

**Step 3: Optimize for KV-cache.** You notice that your system prompt and 15 tool definitions (8% combined) are identical across every request. You ask: "How do I optimize the stable parts of my context for KV-cache?"

The skill walks you through cache-friendly ordering: place stable elements first (system prompt, then tool definitions), then frequently reused elements (common code patterns, project conventions), then unique elements last (specific file under review, current conversation). Avoid dynamic content like timestamps early in context -- they invalidate cache for everything after them. You restructure and measure: cache hit rate goes from near-zero to 72%, reducing latency and cost for the prefix computation.

**Step 4: Add compaction for long sessions.** Some sessions still extend to 50+ turns with message history growing. You ask: "How should I compact message history when it grows beyond my budget allocation?"

The skill recommends monitoring message history against a 50K-token budget. When history exceeds 80% of budget (40K tokens), trigger compaction: summarize turns older than the last 10 into a structured summary preserving key decisions, reviewed files, and outstanding issues. Replace the old turns with the summary. This keeps message history within budget while preserving essential continuity.

**Step 5: Evaluate partitioning.** You mention that some sessions involve both code review and refactoring tasks. You ask: "Should I partition code review and refactoring into separate sub-agents?"

The skill walks through the trade-off. Partitioning gives each sub-agent a clean context focused on its specific task -- the review agent only carries review-related context, the refactoring agent only carries refactoring context. But it adds coordination overhead: the coordinator must manage sub-agent results and maintain overall task state. For your case (two clearly separable task types that rarely need shared context), partitioning is recommended. For tightly coupled tasks where shared context is critical, the overhead outweighs the benefit.

**Step 6: Measure combined improvement.** After applying masking, cache optimization, and compaction: effective capacity increased from 85% utilization with quality degradation to 45% utilization with full quality. The agent handles 3x more files per session. Cost per session dropped 40% from cache optimization alone.

**Gotchas discovered:** The most important lesson was the order of operations. Apply observation masking first (biggest impact, lowest risk), then cache optimization (free performance), then compaction (moderate complexity), then partitioning (highest complexity, only when needed). Starting with partitioning would have been over-engineering.

## Usage Scenarios

### Scenario 1: Tool-output-dominated context

**Context:** Your agent's context is 70% tool outputs from grep, file reads, and command execution. Most are from tasks already completed.

**You say:** "My agent's context is dominated by tool outputs from completed tasks. How do I free up that space?"

**The skill provides:**
- Observation masking strategy with rules for what to mask vs. preserve
- Compact reference format for masked observations
- Re-retrieval pattern for when masked content is needed again
- Expected 60-80% reduction in tool output token usage

**You end up with:** An observation masking system that recovers 40-60% of your context window.

### Scenario 2: High-cost production deployment

**Context:** You are running an agent system at scale and LLM costs are a major concern. Most requests share the same system prompt and tools.

**You say:** "I'm spending too much on LLM tokens. My system prompt and 20 tool definitions are identical across all requests. How do I optimize for caching?"

**The skill provides:**
- Cache-friendly prompt ordering (stable first, dynamic last)
- Guidelines for avoiding cache invalidation (no timestamps, consistent formatting)
- Expected 70%+ cache hit rate for stable workloads
- Cost reduction estimates

**You end up with:** A restructured prompt design that cuts prefix computation costs significantly.

### Scenario 3: Multi-task agent losing coherence

**Context:** Your agent handles both customer data analysis and report generation in one session. Quality drops when both tasks are active.

**You say:** "My agent does data analysis and report generation. It gets confused when both tasks are active in one session. Should I split into sub-agents?"

**The skill provides:**
- Context partitioning architecture with coordinator and sub-agents
- Result aggregation patterns for merging sub-agent outputs
- Analysis of when partitioning helps vs. adds unnecessary complexity
- Clean-context benefits: each sub-agent gets a focused window

**You end up with:** A sub-agent architecture where analysis and reporting each operate in clean, task-specific contexts.

---

## Decision Logic

**Which optimization technique should I apply?**

The skill selects based on what dominates context:
- Tool outputs dominate (50%+) -> Observation masking first
- Stable prefix repeated across requests -> KV-cache optimization
- Message history grows unbounded -> Compaction with structured summaries
- Multiple unrelated tasks in one context -> Partitioning into sub-agents
- Multiple components contribute -> Combine techniques in order: masking -> caching -> compaction -> partitioning

**When should I trigger optimization?**

Monitor these signals:
- Token utilization above 70%: start with masking
- Token utilization above 80%: apply compaction
- Quality degradation visible: apply whatever reduces the dominant component
- Performance drops with conversation length: likely needs partitioning

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Over-aggressive observation masking | Agent cannot reference earlier tool outputs when needed; quality drops on follow-up questions | Adjust masking rules: never mask outputs from the last 3 turns; implement re-retrieval for masked content |
| Cache invalidation from dynamic content | KV-cache hit rate drops to near-zero; costs do not decrease as expected | Audit prompt for dynamic elements (timestamps, random IDs, variable-order tools); move all dynamic content after stable prefix |
| Compaction destroys essential history | Agent loses track of decisions and context after compaction | Switch from aggressive compaction to structured summaries with explicit sections for decisions, files, and state |
| Premature partitioning | Sub-agent coordination overhead exceeds savings from context isolation | Partitioning is the last technique to apply; verify that masking and compaction are insufficient first |

## Ideal For

- **Agent platform teams** managing production systems that need to handle longer sessions without upgrading to more expensive models
- **Cost-conscious AI teams** who need to reduce per-request and per-session token costs through caching and context efficiency
- **Engineers building multi-step agents** whose tool outputs accumulate and degrade quality over extended interactions
- **Architects designing multi-agent systems** who need partitioning strategies for isolating task-specific contexts

## Not For

- **Reducing content through summarization** -- if you specifically need compression strategies (anchored iterative, opaque, regenerative), use `context-compression`
- **Diagnosing why context is failing** -- if you see degradation but do not know the cause, use `context-degradation` to identify the pattern first
- **Learning context basics** -- if you do not understand context components or attention mechanics, start with `context-fundamentals`

## Related Plugins

- **context-fundamentals** -- Foundational theory this skill builds on; understand the mechanics before optimizing them
- **context-degradation** -- Understand the failure patterns that optimization prevents
- **context-compression** -- Specific summarization strategies (one optimization technique explored in depth)
- **multi-agent-patterns** -- Context partitioning as part of broader multi-agent architecture
- **memory-systems** -- External memory as an optimization technique for offloading context

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
