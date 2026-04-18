---
name: context-optimization
description: EXTENDING effective context capacity — KV-cache optimization, observation masking, context partitioning, and retrieval strategies. Use when the user asks to "optimize context", "implement KV-cache", "partition context", "mask observations", or mentions extending context capacity or cache-friendly prompt design. NOT for reducing or compressing content via summarization (use context-compression), NOT for diagnosing context failures or degradation patterns (use context-degradation), NOT for file-based context patterns or scratch pads (use filesystem-context), NOT for learning context basics (use context-fundamentals).
---

# Context Optimization Techniques

Context optimization extends effective capacity through strategic compression, masking, caching, and partitioning. The goal is making better use of available capacity — not magically increasing windows. Effective optimization can double or triple effective context without larger models.

## When to Use / Not Use

**Use when:**
- Context limits constrain task complexity
- Optimizing for cost reduction (fewer tokens = lower costs)
- Reducing latency for long conversations
- Implementing long-running agent systems
- Building production systems at scale

**Do NOT use when:**
- Compressing or summarizing context -> use `context-compression`
- Diagnosing context failures or degradation -> use `context-degradation`
- Learning context basics -> use `context-fundamentals`
- File-based context patterns or scratch pads -> use `filesystem-context`

## Decision Tree

```
What optimization problem are you solving?
├── Tool outputs dominate token usage (>80%)
│   └── Observation Masking -> Replace verbose outputs with references
├── Context approaching limits (>70% utilization)
│   ├── Message history dominates -> Compaction + Summarization
│   ├── Retrieved docs dominate -> Summarization or Partitioning
│   └── Multiple components -> Combine strategies
├── Repeated requests with common prefixes
│   └── KV-Cache Optimization -> Stable prefix ordering
├── Single context too large for one agent
│   └── Context Partitioning -> Sub-agent isolation
├── Need to measure if optimization is working
│   └── See §Performance Targets
└── Not about extending capacity? -> See related skills
```

## Four Primary Strategies

| Strategy | Mechanism | Best For | Expected Savings |
|----------|-----------|----------|-----------------|
| Compaction | Summarize context near limits, reinitialize with summary | Message history dominating | 50-70% token reduction |
| Observation Masking | Replace verbose tool outputs with compact references | Tool output dominance (80%+ of tokens) | 60-80% reduction in masked obs |
| KV-Cache Optimization | Reuse cached KV computations across shared prefixes | Repeated requests with stable prefixes | 70%+ cache hit rate |
| Context Partitioning | Split work across sub-agents with isolated contexts | Single context too large | Isolation + clean focus |

### Compaction

Summarize context sections when approaching limits, then reinitialize with the summary. Priority order for compression:

1. **Tool outputs** — Replace with summaries of key findings, metrics, conclusions
2. **Old turns** — Summarize early conversation, preserve decisions and context shifts
3. **Retrieved docs** — Summarize if recent versions exist
4. **Never compress** — System prompt

Target: 50-70% token reduction with less than 5% quality degradation.

### Observation Masking

Replace verbose tool outputs with compact references once the output has served its purpose.

| Category | Action | Examples |
|----------|--------|---------|
| Never mask | Critical to current task, most recent turn, active reasoning | Current file being edited, error being debugged |
| Consider masking | 3+ turns old, verbose with extractable key points, purpose served | Large file reads, search results already acted on |
| Always mask | Repeated outputs, boilerplate headers/footers, already summarized | Help text, version banners, duplicate reads |

```python
if len(observation) > max_length:
    ref_id = store_observation(observation)
    return f"[Obs:{ref_id} elided. Key: {extract_key(observation)}]"
```

### KV-Cache Optimization

KV-cache stores Key and Value tensors from inference, growing linearly with sequence length. Prefix caching reuses KV blocks across requests with identical prefixes via hash-based block matching.

**Cache-friendly ordering principle:** Stable elements first, unique elements last.

```python
context = [system_prompt, tool_definitions]  # Cacheable (stable)
context += [reused_templates]                 # Reusable (semi-stable)
context += [unique_content]                   # Unique (never cached)
```

**Cache stability design:**
- Avoid dynamic content (timestamps, random IDs) in prefixes
- Use consistent formatting across sessions
- Keep structure stable even when content changes

### Context Partitioning

Most aggressive optimization: partition work across sub-agents with isolated contexts. Each sub-agent operates in a clean context focused on its subtask.

**When to partition:**
- Single context would exceed limits
- Independent subtasks with minimal dependencies
- Need separation of concerns (search context vs. synthesis context)

**Result aggregation:** Validate all partitions completed → merge compatible results → summarize if still too large.

## Context Budget Management

| Budget Category | Typical Allocation | Notes |
|----------------|-------------------|-------|
| System prompt | 5-10% | Never compress |
| Tool definitions | 10-15% | Semi-stable, cacheable |
| Retrieved documents | 15-30% | Dynamic, filterable |
| Message history | 20-40% | Growing, compactable |
| Tool outputs | 30-50% | Dominant, maskable |
| Reserved buffer | 10% | Headroom for responses |

**Trigger signals for optimization:**
- Token utilization above 80%
- Degradation indicators (quality dropping)
- Performance drops (latency increasing)
- Cost thresholds exceeded

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Optimizing without measuring | Cannot distinguish effective optimization from harmful compression | Measure before and after: token counts, quality metrics, cache hit rates |
| Masking too aggressively | Masking recent or critical observations causes agent to lose context mid-task | Follow masking categories: never mask current-turn or active-reasoning outputs |
| Ignoring cache stability | Dynamic content in prefixes (timestamps, random IDs) breaks cache hits | Place stable content first; push dynamic content to end of context |
| Partitioning too early | Isolation overhead exceeds savings for moderately-sized contexts | Partition only when single context would exceed limits or subtasks are genuinely independent |
| Compressing system prompt | System prompt establishes identity; compression loses behavioral constraints | Never compress system prompt; always include in cacheable prefix |
| No compaction triggers | Context fills silently until severe degradation | Implement triggers at 70-80% utilization; monitor usage against budget |
| Applying single strategy | Different context components need different optimization techniques | Combine strategies based on context composition (see Decision Tree) |
| Assuming optimization is free | Each strategy has quality cost; aggressive targets degrade output | Target 50-70% compaction with <5% quality loss; measure, don't assume |

## Guidelines

1. Measure before optimizing — know your current state
2. Apply compaction before masking when possible
3. Design for cache stability with consistent prompts
4. Partition before context becomes problematic
5. Monitor optimization effectiveness over time
6. Balance token savings against quality preservation
7. Test optimization at production scale
8. Implement graceful degradation for edge cases

## Integration

- context-fundamentals - Prerequisite: basic context concepts
- context-degradation - Understanding when optimization is needed
- context-compression - Compression as one optimization technique
- multi-agent-patterns - Partitioning as isolation
- evaluation - Measuring optimization effectiveness
- memory-systems - Offloading context to memory

## References

Internal reference:
- [Optimization Techniques Reference](./references/optimization_techniques.md) - Detailed technical reference

External resources:
- Research on context window limitations and KV-cache optimization
- Production engineering guides from leading AI labs
