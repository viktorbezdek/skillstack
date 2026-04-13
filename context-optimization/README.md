> **v1.0.4** | Context Engineering | 5 iterations

# Context Optimization

> Double or triple your agent's effective context capacity through compaction, observation masking, KV-cache optimization, and context partitioning -- without switching to a larger model.

## The Problem

Agent developers hit context limits and reach for a bigger model. They upgrade from 128K to 200K to 1M-token windows, paying exponentially more per request, and discover that the agent's performance is no better -- or worse. The problem was never the window size. The problem is that 80% of their context is noise: verbose tool outputs that have already served their purpose, accumulated message history from resolved sub-tasks, and retrieved documents that are no longer relevant to the current step.

Tool outputs alone can consume 83.9% of total context in typical agent trajectories. A single `git diff` output from 15 turns ago is still sitting in context, consuming attention budget, even though the agent already processed it and moved on. Every API response, every file read, every search result accumulates without any eviction strategy. By turn 30, the agent is spending most of its attention budget on stale data.

Meanwhile, costs scale non-linearly with context length. Processing 400K tokens is not twice as expensive as 200K -- it is significantly more in both compute time and API cost. Teams running agents at scale watch their bills climb while their agents degrade. They have no framework for deciding what to optimize, when to trigger optimization, or how to measure whether their optimization preserved the information the agent needs.

## The Solution

This plugin provides four optimization strategies that extend effective context capacity without requiring larger models. Compaction summarizes context near limits and reinitializes with high-fidelity summaries, achieving 50-70% token reduction with less than 5% quality degradation. Observation masking replaces verbose tool outputs with compact references, recovering 60-80% of the tokens that tool outputs consume. KV-cache optimization reorders context elements to maximize cache hits, cutting cost and latency for requests with shared prefixes. Context partitioning splits work across sub-agents with isolated contexts, preventing any single context from growing large enough to degrade.

The skill provides a decision framework for choosing which strategy to apply based on what is consuming your context: tool outputs dominating means observation masking, retrieved documents dominating means summarization or partitioning, message history dominating means compaction. For most production agents, the answer is a combination of strategies applied at measured trigger points.

You also get budget management guidance: how to allocate tokens across categories (system prompt, tool definitions, retrieved docs, message history, buffer), when to trigger optimization (70-80% utilization), and how to monitor effectiveness over time. The goal is not maximum compression but optimal signal-to-noise ratio.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Tool outputs from 15 turns ago consume 80%+ of context with zero current value | Observation masking replaces stale outputs with compact references, recovering 60-80% of those tokens |
| Upgrade to larger models hoping more context fixes quality, paying exponentially more | Optimize existing context to double or triple effective capacity on the same model |
| No eviction strategy -- everything accumulates until the window fills | Compaction triggers at 70-80% utilization, summarizing low-value content while preserving critical information |
| Every request recomputes the full context from scratch, wasting cost and latency | KV-cache optimization reorders context for maximum cache hits on stable prefixes |
| Single-context agents grind to a halt on complex multi-step tasks | Context partitioning splits work across sub-agents with clean, focused contexts |
| No framework for deciding what to optimize or when | Decision matrix maps context composition to the right optimization strategy |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-optimization@skillstack
```

### Verify installation

After installing, test with:

```
My agent's context fills up with tool outputs after 20 turns and quality drops -- how do I optimize this without losing important information?
```

## Quick Start

1. Install the plugin using the commands above
2. Describe your context problem: `My agent runs out of context on complex tasks -- tool outputs and old messages fill the window before the task is done`
3. The skill diagnoses what is consuming your context and recommends the right optimization strategy (compaction, masking, caching, or partitioning)
4. Implement the recommended approach -- start with observation masking for tool-heavy agents or compaction for message-heavy conversations
5. Set up monitoring: track token utilization per category and measure quality before and after optimization

## What's Inside

| Component | Description |
|---|---|
| `context-optimization` skill | Core skill covering compaction strategies, observation masking, KV-cache optimization, context partitioning, budget management, and the optimization decision framework |
| `optimization_techniques.md` reference | Technical reference with detailed compaction approaches, token budget allocation strategies, and implementation patterns |
| 13 trigger eval cases | Validates correct skill activation and near-miss rejection |
| 3 output eval cases | Tests optimization guidance, strategy selection, and implementation planning |

### context-optimization

**What it does:** Activates when your agent hits context limits, when you need to reduce token costs or latency for long conversations, when tool outputs dominate your context usage, or when you are building production agent systems that must handle extended sessions reliably. Provides four optimization strategies with a decision framework for choosing and combining them.

**Try these prompts:**

```
My agent's tool outputs consume most of the context window -- how do I implement observation masking without losing the information I might need later?
```

```
I need to optimize my agent for cost -- conversations are averaging 100K tokens and my API bill is growing fast. What's the highest-impact optimization?
```

```
How do I set up KV-cache optimization for my agent? I want to reduce latency on the system prompt and tool definitions that stay the same across requests
```

```
My agent handles complex multi-step tasks that exceed context limits -- should I use compaction or split the work across sub-agents?
```

```
Design a context budget for my production agent: 200K window, system prompt is 8K tokens, 15 tools, and conversations typically run 50+ messages
```

**Key references:**

| Reference | Topic |
|---|---|
| `optimization_techniques.md` | Detailed compaction approaches (summary-based, selective), token budget allocation strategies, implementation patterns for each optimization technique |

## Real-World Walkthrough

You are running a coding agent that helps developers with feature implementation. The agent reads source files, runs tests, modifies code, and iterates until the feature works. A typical task involves 40-60 tool calls: file reads, grep searches, test runs, and code edits. By turn 30, the agent's context is at 85% capacity and quality is noticeably degraded -- it re-reads files it already examined and forgets test results from 10 turns ago.

You open Claude Code to fix this:

```
My coding agent hits 85% context utilization by turn 30 and quality drops -- it re-reads files and forgets test results. Help me optimize the context usage.
```

The context-optimization skill activates and starts with diagnosis. It asks you to profile what is consuming your context. You check and find: system prompt takes 4K tokens (3%), tool definitions take 6K tokens (5%), and the remaining 92% is message history dominated by tool outputs -- file contents, test output, grep results.

The skill identifies observation masking as the highest-impact first step. Those file reads from turn 5 are still consuming 3K tokens each in context even though the agent processed them and moved on. Test output from turn 8 is still consuming 5K tokens even though the agent already analyzed the failures. The skill walks you through implementing a masking strategy:

**Never mask:** outputs from the current and previous turn, outputs the agent is actively reasoning about, test results from the most recent test run.

**Consider masking after 3 turns:** file reads where the key findings have been captured in the agent's response, grep results that have been synthesized into a decision.

**Always mask:** repeated file reads (the agent re-read the same file), boilerplate test output (full stack traces when only the failure message matters), verbose command output that has been summarized.

You implement masking with a simple reference system. When a tool output is masked, it is replaced with a compact reference: `[Obs:ref-12 elided. Key: auth.controller.ts -- 142 lines, JWT validation logic in handleLogin()]`. The full output is stored externally and can be re-loaded if the agent needs it.

After implementing masking, your average context at turn 30 drops from 85% to 35%. The agent stops re-reading files because the compact references remind it what each file contained. Quality improvement is immediate and measurable.

Next, you tackle compaction for the remaining message history. The skill recommends trigger-based compaction at 70% utilization rather than aggressive early compression. When the trigger fires, the compaction process summarizes old conversational turns (preserving decisions and task state) while leaving recent turns untouched. You implement compaction that summarizes messages older than 10 turns into a structured summary with sections for decisions made, files modified, test status, and current approach.

Finally, you optimize for KV-cache by reordering your context elements. You place the system prompt and tool definitions first (stable across requests), followed by any reusable templates, then the unique conversation content. This reordering achieves a 72% cache hit rate on the prefix, reducing latency by 40% on each request.

The combined effect: your agent now handles 80+ turn sessions without degradation. Token usage per session dropped 55%, translating directly to cost savings. Latency per request dropped 40% from cache optimization. And crucially, the agent's quality at turn 60 is indistinguishable from its quality at turn 10, because the context is clean and focused rather than bloated with stale outputs.

You did not upgrade the model. You did not increase the context window. You made better use of the capacity you already had.

## Usage Scenarios

### Scenario 1: Tool-output-heavy agent running out of context

**Context:** Your agent makes 50+ tool calls per task, and file reads and test outputs consume the entire context window by mid-task. The agent starts repeating work because it has lost track of what it already did.

**You say:** `My agent makes tons of tool calls and the outputs fill up context by turn 30 -- it starts re-reading files it already looked at. How do I fix this?`

**The skill provides:**
- Observation masking strategy: which outputs to mask, when to mask them, and what reference format to use
- Masking priority rules: never mask current-turn outputs, consider masking after 3 turns, always mask repeated outputs
- Reference system design for storing and retrieving masked observations
- Expected impact: 60-80% reduction in observation token usage

**You end up with:** An observation masking implementation that recovers most of your context budget from stale tool outputs while preserving the information the agent needs.

### Scenario 2: Reducing API costs for long conversations

**Context:** Your production agent handles customer support conversations that average 100K tokens. API costs are growing faster than revenue and you need to optimize without degrading quality.

**You say:** `My agent conversations average 100K tokens and costs are too high -- what's the most impactful optimization to reduce token usage?`

**The skill provides:**
- Context composition profiling to identify where tokens are being consumed
- Optimization decision framework: tool outputs dominating = masking, message history dominating = compaction, retrieved docs dominating = summarization
- KV-cache optimization for reducing per-request computation cost
- Budget allocation framework with monitoring and trigger points
- Expected cost reduction targets by strategy

**You end up with:** A prioritized optimization plan targeting the highest-impact changes first, with expected cost savings and quality preservation targets.

### Scenario 3: Partitioning complex tasks across sub-agents

**Context:** Your agent handles complex tasks that require analyzing multiple systems, running tests across services, and synthesizing results. No single context window is large enough to hold all the information.

**You say:** `My agent needs to analyze 5 different microservices for a cross-cutting change -- the context can't hold all the code and test results at once. Should I partition?`

**The skill provides:**
- Context partitioning strategy: split each service analysis into a sub-agent with isolated context
- Coordinator pattern: a parent agent manages sub-agents and aggregates results
- Result aggregation approach: validate completions, merge compatible results, summarize if too large
- Comparison with alternatives: partitioning vs compaction, when each is appropriate

**You end up with:** A multi-agent architecture where each service gets analyzed in a clean, focused context, with results aggregated by a coordinator.

### Scenario 4: Designing cache-friendly prompt architecture

**Context:** You are building an agent platform serving thousands of concurrent sessions. You want to minimize latency and compute costs through KV-cache optimization.

**You say:** `I'm building an agent platform -- how do I design the prompt architecture for maximum KV-cache hits across sessions?`

**The skill provides:**
- Cache-friendly ordering: stable elements first (system prompt, tool definitions), reusable elements next, unique content last
- Cache stability guidelines: avoid timestamps and dynamic content in cached prefix, use consistent formatting
- Expected cache hit rates: 70%+ for stable workloads with proper ordering
- Hash-based block matching explanation and how to maximize prefix sharing

**You end up with:** A prompt architecture that achieves high cache hit rates, reducing both latency and compute costs across your platform.

## Ideal For

- **Agent developers hitting context limits** on complex tasks -- the four strategies extend effective capacity without model upgrades
- **Teams optimizing API costs** at scale -- observation masking and caching directly reduce token consumption and compute time
- **Platform engineers** building agent infrastructure that serves many concurrent sessions with cache optimization
- **Anyone building long-running agents** (50+ turns) where accumulated context degrades performance
- **Architects designing multi-agent systems** who need to understand when and how to partition context across sub-agents

## Not For

- **Reducing context via summarization strategies** (anchored iterative summarization, structured summaries) -- use [context-compression](../context-compression/) instead
- **Diagnosing why context is failing** (lost-in-middle, poisoning, distraction) -- use [context-degradation](../context-degradation/) instead
- **Learning foundational context theory** (what context is, how attention works) -- use [context-fundamentals](../context-fundamentals/) instead
- **File-system-based context patterns** (scratch pads, plan persistence) -- use [filesystem-context](../filesystem-context/) instead

## How It Works Under the Hood

The plugin is a single-skill architecture with one technical reference document.

The **core skill** (`SKILL.md`) covers four optimization strategies in depth: compaction (summary-based context reinitializaton, priority rules for what to compress, effectiveness targets), observation masking (the observation problem, masking strategy selection with never/consider/always rules, reference system design), KV-cache optimization (prefix caching mechanics, hash-based block matching, cache-friendly prompt ordering, stability guidelines), and context partitioning (sub-agent isolation, coordinator patterns, result aggregation). It provides a decision framework for choosing strategies based on context composition, budget management guidance, and trigger-based optimization patterns.

The **optimization techniques reference** (`optimization_techniques.md`) provides the depth layer with detailed compaction approaches (summary-based vs selective), token budget allocation strategies for different agent types, and implementation patterns for each technique. This reference activates when you need to implement a specific optimization rather than understand the strategy landscape.

The skill builds on context-fundamentals (understanding context anatomy and attention mechanics) and context-degradation (knowing when optimization is needed). It routes to context-compression for summarization-specific strategies and filesystem-context for file-based offloading patterns.

## Related Plugins

- **[Context Compression](../context-compression/)** -- Summarization strategies: anchored iterative summarization, opaque compression, and probe-based evaluation
- **[Context Degradation](../context-degradation/)** -- Diagnosing context failures: lost-in-middle, poisoning, distraction, clash, and confusion patterns
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational theory: what context is, how attention works, progressive disclosure, and budgeting
- **[Filesystem Context](../filesystem-context/)** -- File-system-based context: scratch pads, plan persistence, and sub-agent file workspaces

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
