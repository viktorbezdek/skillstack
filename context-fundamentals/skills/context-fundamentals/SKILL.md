---
name: context-fundamentals
description: Foundational theory of context engineering — what context IS, how attention works, progressive disclosure principles, and context budgeting basics. Use when the user asks to "understand context", "explain context windows", "learn context engineering", or discusses context components, attention mechanics, or context budgets. NOT for fixing broken context or diagnosing failures (use context-degradation), NOT for compressing or summarizing context (use context-compression), NOT for KV-cache or partitioning performance optimization (use context-optimization), NOT for file-based context patterns or scratch pads (use filesystem-context).
---

# Context Engineering Fundamentals

Context is the complete state available to a language model at inference time: system instructions, tool definitions, retrieved documents, message history, and tool outputs. Understanding context fundamentals is prerequisite to all other context engineering skills.

## When to Use / Not Use

**Use when:**
- Designing new agent systems or modifying existing architectures
- Onboarding to context engineering concepts
- Reviewing context-related design decisions
- Debugging unexpected agent behavior that may relate to context structure

**Do NOT use when:**
- Diagnosing context failures or degradation -> use `context-degradation`
- Compressing or summarizing context -> use `context-compression`
- KV-cache optimization or context partitioning -> use `context-optimization`
- File-based context patterns or scratch pads -> use `filesystem-context`

## Decision Tree

```
What do you need to understand about context?
├── What goes INTO context
│   ├── System instructions / identity -> System Prompts (§Anatomy)
│   ├── Available actions -> Tool Definitions (§Anatomy)
│   ├── External knowledge -> Retrieved Documents (§Anatomy)
│   ├── Conversation so far -> Message History (§Anatomy)
│   └── Action results -> Tool Outputs (§Anatomy)
├── How context is CONSUMED
│   ├── Attention mechanics / budget -> Attention Budget (§Attention)
│   ├── Position encoding limits -> Position Encoding (§Attention)
│   └── Quality vs quantity trade-offs -> Quality vs Quantity (§Quality)
├── How to MANAGE context
│   ├── Load only when needed -> Progressive Disclosure (§Disclosure)
│   ├── Allocate token budget -> Context Budgeting (§Budgeting)
│   └── Mix pre-load + JIT -> Hybrid Strategies (§Hybrid)
└── Not about fundamentals? -> See related skills
```

## The Anatomy of Context

Five components, each with different characteristics:

| Component | Persistence | Typical Token Share | Key Risk |
|-----------|------------|---------------------|----------|
| System Prompts | Session-long | Low | Wrong altitude: too brittle or too vague |
| Tool Definitions | Session-long | Medium | Poor descriptions force agent guessing |
| Retrieved Documents | Dynamic | Medium | Pre-loading creates distraction |
| Message History | Growing | Medium-High | Dominates context in long sessions |
| Tool Outputs | Growing | **83.9%** of total | Verbose outputs consume budget |

### System Prompts

Establish agent identity, constraints, and behavioral guidelines. The right altitude balances two failure modes: hardcoded brittle logic (fragile, high maintenance) vs. vague high-level guidance (no concrete signals). Organize with XML tagging or Markdown headers for background, instructions, tool guidance, and output description.

### Tool Definitions

Specify actions: name, description, parameters, return format. **Consolidation principle:** If a human engineer cannot definitively say which tool to use in a given situation, the agent cannot either. Include usage context, examples, and defaults in descriptions.

### Retrieved Documents

Domain-specific knowledge loaded at runtime via RAG. Use JIT approach: maintain lightweight identifiers (file paths, queries, links) and load data dynamically. Mirrors human cognition — use external indexing systems rather than memorizing corpuses.

### Message History

Conversation between user and agent. Serves as scratchpad memory for tracking progress and preserving reasoning. Can dominate context in long-running tasks. Critical for long-horizon task completion.

### Tool Outputs

The majority of tokens in typical agent trajectories (83.9% research finding). Relevant or not, they consume context. Creates pressure for observation masking, compaction, and selective retention.

## Attention Mechanics

### The Attention Budget Constraint

For n tokens, attention creates n² pairwise relationships. As context grows, the model's ability to capture relationships gets stretched thin. Models develop attention patterns from training data where shorter sequences predominate — less experience with context-wide dependencies.

### Position Encoding and Context Extension

Position encoding interpolation adapts models to longer sequences but introduces degradation in position understanding. Models remain capable at longer contexts but show reduced precision for retrieval and long-range reasoning.

### Progressive Disclosure Principle

Load information only as needed. At startup, load skill names and descriptions — sufficient to know relevance. Full content loads only on activation. Applies at multiple levels: skill selection, document loading, tool result retrieval.

## Quality vs Quantity

The assumption that larger context windows solve memory problems is empirically debunked. Context engineering = finding the smallest high-signal token set that maximizes desired outcomes.

| Factor | Impact |
|--------|--------|
| Processing cost | Grows exponentially, not linearly, with context length |
| Model performance | Degrades beyond thresholds even when window supports more |
| Long input cost | Remains expensive even with prefix caching |
| Informativity principle | Include what matters for the decision at hand; exclude what does not |

## Context Budgeting

Design with explicit budgets:
1. Know the effective context limit for your model and task
2. Monitor context usage during development
3. Implement compaction triggers at 70-80% utilization
4. Design assuming context will degrade rather than hoping it won't
5. Understand attention distribution — middle receives less attention than edges

## Hybrid Strategies

Most effective agents mix pre-loading and JIT loading:

| Condition | Strategy |
|-----------|----------|
| Less dynamic content (project rules, CLAUDE.md) | Pre-load upfront for speed |
| Rapidly changing or highly specific information | JIT loading avoids stale context |
| Reference documentation | Summary first, detail on demand |

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Stuffing all context upfront | 83.9% of tokens are tool outputs; pre-loading docs creates distraction | Use progressive disclosure; load only when task requires it |
| Vague system prompts | No concrete signals for desired outputs | Balance specificity with flexibility; include examples and defaults |
| Equally vague tool descriptions | Agent must guess which tool to use | Include usage context, examples, defaults; apply consolidation principle |
| Assuming larger context = better | Cost grows exponentially; performance degrades past thresholds | Optimize for informativity over exhaustiveness; find smallest high-signal set |
| Ignoring position in context | Middle receives 10-40% less attention than edges | Place critical information at beginning or end of context |
| No compaction triggers | Context fills silently until severe degradation | Implement triggers at 70-80% utilization; monitor context usage |
| Monolithic context for all tasks | Different tasks need different information; mixing creates confusion | Isolate task contexts; use clear segmentation and transitions |
| Pre-loading all retrieved docs | Single irrelevant document measurably degrades performance | Apply relevance filtering; use JIT retrieval instead of pre-loading |

## Guidelines

1. Treat context as a finite resource with diminishing returns
2. Place critical information at attention-favored positions (beginning and end)
3. Use progressive disclosure to defer loading until needed
4. Organize system prompts with clear section boundaries
5. Monitor context usage during development
6. Implement compaction triggers at 70-80% utilization
7. Design for context degradation rather than hoping to avoid it
8. Prefer smaller high-signal context over larger low-signal context

## Integration

- context-degradation - Understanding how context fails (prerequisite: this skill)
- context-optimization - Techniques for extending context capacity
- context-compression - Summarization strategies
- multi-agent-patterns - Context isolation for multi-agent systems
- tool-design - How tool definitions interact with context

## References

Internal reference:
- [Context Components Reference](./references/context-components.md) - Detailed technical reference

External resources:
- Research on transformer attention mechanisms (Vaswani et al., 2017)
- Production engineering guides from leading AI labs
- Framework documentation on context window management
