> **v1.0.4** | Context Engineering | 5 iterations

# Context Optimization

Double or triple your effective context capacity through compaction, observation masking, KV-cache optimization, and context partitioning -- without switching to a larger model.

## What Problem Does This Solve

Tool outputs alone consume 80%+ of a context window in typical agent trajectories, yet much of that content is verbose output that has already served its purpose. Paying full token cost to re-process stale tool results on every turn wastes budget and adds latency. Meanwhile, identical prefixes (system prompts, tool definitions) get recomputed on every request because prompts are not structured for cache hits. This skill covers four concrete techniques -- compaction, observation masking, KV-cache optimization, and context partitioning -- that together can double or triple effective context capacity. Each technique targets a different source of waste, and the skill provides a decision framework for knowing which one to apply based on what is dominating your context.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-optimization@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

This is a single-skill plugin with one reference document:

| Component | Description |
|---|---|
| `skills/context-optimization/SKILL.md` | Core skill covering four optimization strategies (compaction, observation masking, KV-cache optimization, context partitioning), summary generation by message type, masking selection rules (never/consider/always mask), prefix-stable prompt ordering for cache hits, sub-agent partitioning with result aggregation, budget management with trigger-based optimization, and a decision framework mapping context composition to the right technique |
| `references/optimization_techniques.md` | Technical reference with Python implementations: selective masking with relevance scoring, compaction threshold configuration (warning at 70%, trigger at 80%, aggressive at 90%), cache-friendly vs. cache-unfriendly prompt design, partition planning for multi-agent decomposition, an OptimizingAgent integration pattern, MemoryAwareOptimizer for memory system integration, performance benchmarks (50-70% compaction reduction, 60-80% masking reduction, 70%+ cache hit rates), monitoring metrics, and common pitfalls (over-aggressive compaction, masking critical observations, ignoring attention distribution) |
| `evals/trigger-evals.json` | Trigger scenarios validating correct activation and near-miss rejection |
| `evals/evals.json` | Output quality scenarios testing optimization guidance |

## Usage Scenarios

**1. Tool outputs dominate your context and latency is climbing**

Your agent's context is 85% tool outputs from earlier turns -- file contents, search results, command outputs -- most of which are no longer relevant. Apply observation masking: replace verbose outputs with compact references like `[Obs:ref_42 elided. Key: auth endpoint returns 401]`. The skill provides selection rules: never mask observations critical to the current task or from the most recent turn; always mask repeated outputs, boilerplate, and outputs already summarized in conversation.

**2. Paying high inference costs on every call despite identical prefixes**

Your system prompt and tool definitions are the same across every request, but you are paying full computation cost each time. The skill covers KV-cache optimization: order context for prefix stability (system prompt first, tool definitions second, reused templates third, unique content last). Avoid dynamic content like timestamps in stable prefixes. Target: 70%+ cache hit rate for stable workloads, translating to 50%+ cost reduction and 40%+ latency reduction.

**3. Response quality degrades as conversations extend past 50 turns**

Context is approaching the limit and quality is dropping. Apply compaction: summarize context when utilization exceeds 80%. Priority order for compression: tool outputs (replace with summaries preserving key findings and metrics), old conversation turns (preserve decisions and commitments, remove filler), retrieved documents (summarize if newer versions exist). Never compress the system prompt. Target: 50-70% token reduction with less than 5% quality degradation.

**4. Single task is too large for one context window**

Your task requires processing more information than fits in one context. Use context partitioning: decompose the task across sub-agents with isolated contexts, each focused on its subtask. Sub-agents operate with clean, focused context without carrying accumulated context from other subtasks. Aggregate results by validating all partitions completed, merging compatible results, and summarizing if still too large. This is the most aggressive optimization but often the most effective.

**5. Not sure which optimization to apply first**

The skill provides a decision framework: if tool outputs dominate, apply observation masking first. If retrieved documents dominate, apply summarization or partitioning. If message history dominates, apply compaction with summarization. If multiple components contribute, combine strategies. Always measure before optimizing -- know your current token distribution across context components.

## How to Use

**Direct invocation:**

```
Use the context-optimization skill to reduce my agent's context usage
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `context-optimization`
- `kv-cache`
- `observation-masking`
- `compaction`

## When to Use / When NOT to Use

**Use when:**
- Context limits constrain task complexity
- Optimizing for cost reduction (fewer tokens = lower costs)
- Reducing latency for long conversations
- Implementing long-running agent systems
- Handling larger documents or conversations
- Building production systems at scale

**Do NOT use when:**
- Reducing or compressing content via summarization techniques -- use [context-compression](../context-compression/) instead
- Diagnosing context failures or degradation patterns -- use [context-degradation](../context-degradation/) instead
- Learning context theory or fundamentals -- use [context-fundamentals](../context-fundamentals/) instead
- Working with file-based context offloading -- use [filesystem-context](../filesystem-context/) instead

## Related Plugins

- **[Context Compression](../context-compression/)** -- Reducing context size through summarization strategies, anchored iterative summarization, and probe-based evaluation
- **[Context Degradation](../context-degradation/)** -- Diagnosing context failures: lost-in-middle, poisoning, distraction, clash, and confusion patterns with model-specific thresholds
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational theory: what context is, how attention works, progressive disclosure, and context budgeting
- **[Filesystem Context](../filesystem-context/)** -- Using the file system for context: scratch pads, plan persistence, and sub-agent file workspaces

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
