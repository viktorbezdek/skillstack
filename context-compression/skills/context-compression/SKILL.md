---
name: context-compression
description: REDUCING context size — summarization strategies, anchored iterative summarization, tokens-per-task optimization, compaction triggers, and probe-based evaluation. Use when the user asks to "compress context", "summarize conversation history", "implement compaction", "reduce token usage", or mentions structured summarization or long-running sessions exceeding context limits. NOT for diagnosing context failures or degradation patterns (use context-degradation), NOT for KV-cache optimization or context partitioning (use context-optimization), NOT for learning context theory or basics (use context-fundamentals), NOT for file-based offloading or scratch pads (use filesystem-context).
---

# Context Compression Strategies

When agent sessions generate millions of tokens of conversation history, compression becomes mandatory. The naive approach is aggressive compression to minimize tokens per request. The correct optimization target is tokens per task: total tokens consumed to complete a task, including re-fetching costs when compression loses critical information.

## When to Use / Not Use

**Use when:**
- Agent sessions exceed context window limits
- Codebases exceed context windows (5M+ token systems)
- Designing conversation summarization strategies
- Debugging cases where agents "forget" what files they modified
- Building evaluation frameworks for compression quality

**Do NOT use when:**
- Diagnosing why context is degrading -> use `context-degradation`
- KV-cache optimization or context partitioning -> use `context-optimization`
- Learning foundational context theory -> use `context-fundamentals`
- File-based offloading or scratch pads -> use `filesystem-context`

## Decision Tree

```
Why do you need compression?
├── Agent sessions hitting context limits
│   ├── What matters most?
│   │   ├── File tracking + decision history (long sessions) -> Anchored Iterative Summarization
│   │   ├── Maximum token savings (short sessions, low re-fetch cost) -> Opaque Compression
│   │   └── Readability + phase boundaries -> Regenerative Full Summary
│   └── Not sure? -> Start with Anchored Iterative (best quality trade-off)
├── Need to measure if compression is working
│   └── Probe-based evaluation (§Probe-Based Evaluation)
├── When to trigger compression?
│   └── See §Compression Trigger Strategies
└── Not about reducing size? -> See related skills
```

## Core Compression Approaches

| Method | Ratio | Quality | Best For |
|--------|-------|---------|----------|
| Anchored Iterative | 98.6% | 3.70 | Long sessions where file tracking matters (coding, debugging) |
| Opaque | 99.3% | 3.35 | Short sessions, maximum token savings, low re-fetch costs |
| Regenerative Full | 98.7% | 3.44 | Sessions with clear phase boundaries, readability critical |

**Key insight:** Structure forces preservation. Dedicated summary sections act as checklists the summarizer must populate, preventing silent information drift.

### Anchored Iterative Summarization

1. Define explicit summary sections matching your agent's needs
2. On first compression trigger, summarize truncated history into sections
3. On subsequent compressions, summarize only new truncated content
4. Merge new summary into existing sections (not full regeneration)
5. Track which information came from which compression cycle

### When to Use Each Approach

| Condition | Recommended Approach |
|-----------|---------------------|
| Sessions 100+ messages, file tracking critical | Anchored Iterative |
| Maximum token savings, short sessions, low re-fetch cost | Opaque |
| Clear phase boundaries, readability critical | Regenerative |
| Need to audit what was preserved | Anchored Iterative |

## Structured Summary Sections

```markdown
## Session Intent
[What the user is trying to accomplish]

## Files Modified
- auth.controller.ts: Fixed JWT token generation
- config/redis.ts: Updated connection pooling
- tests/auth.test.ts: Added mock setup for new config

## Decisions Made
- Using Redis connection pool instead of per-request connections
- Retry logic with exponential backoff for transient failures

## Current State
- 14 tests passing, 2 failing
- Remaining: mock setup for session service tests

## Next Steps
1. Fix remaining test failures
2. Run full test suite
3. Update documentation
```

## Compression Trigger Strategies

| Strategy | Trigger Point | Trade-off |
|----------|---------------|-----------|
| Fixed threshold | 70-80% context utilization | Simple but may compress too early |
| Sliding window | Keep last N turns + summary | Predictable context size |
| Importance-based | Compress low-relevance sections first | Complex but preserves signal |
| Task-boundary | Compress at logical task completions | Clean summaries but unpredictable timing |

**Recommendation:** Sliding window + structured summaries for most coding agent use cases.

## The Artifact Trail Problem

Artifact trail integrity is the weakest dimension across all compression methods (2.2-2.5/5.0 in evaluations). Coding agents need to track:
- Which files were created, modified, or read-only
- Function names, variable names, error messages

**Solution:** Supplement structured summaries with a separate artifact index or dedicated file-state tracking in agent scaffolding.

## Tokens-Per-Task vs Tokens-Per-Request

Traditional metrics target tokens-per-request. This is the wrong optimization. When compression loses critical details, the agent must re-fetch information, re-explore approaches, and waste tokens recovering context.

The right metric is **tokens-per-task**: total tokens consumed from task start to completion. A compression strategy saving 0.5% more tokens per request but causing 20% more re-fetching costs more overall.

## Probe-Based Evaluation

Traditional metrics (ROUGE, embedding similarity) fail for functional quality. Probe-based evaluation directly measures functional quality by asking questions after compression:

| Probe Type | What It Tests | Example Question |
|------------|---------------|------------------|
| Recall | Factual retention | "What was the original error message?" |
| Artifact | File tracking | "Which files have we modified?" |
| Continuation | Task planning | "What should we do next?" |
| Decision | Reasoning chain | "What did we decide about the Redis issue?" |

### Six Evaluation Dimensions

1. **Accuracy**: Are technical details correct? (largest variation between methods)
2. **Context Awareness**: Does response reflect current conversation state?
3. **Artifact Trail**: Does agent know which files were read or modified? (universally weak)
4. **Completeness**: Does response address all parts of the question?
5. **Continuity**: Can work continue without re-fetching?
6. **Instruction Following**: Does response respect stated constraints?

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Optimizing tokens-per-request | Re-fetch costs exceed savings; agent re-explores already-tried approaches | Optimize for tokens-per-task instead; measure total cost including recovery |
| Generic summarization | "Summarize this conversation" loses structured information | Use anchored iterative summarization with explicit sections for files, decisions, next steps |
| Full regeneration each cycle | Repeated regeneration introduces subtle drift; each cycle loses a few details | Use incremental merging: summarize only new truncated content, merge into existing sections |
| Ignoring artifact trail | File tracking degrades across long sessions (2.2-2.5/5.0 quality) | Implement separate artifact index outside the summary; dedicated file-state tracking |
| Compressing during active reasoning | Agent loses thread of current investigation mid-compression | Switch from fixed-threshold triggers to task-boundary triggers; compress only at logical completion points |
| No quality measurement | Cannot distinguish good compression from bad | Implement probe-based evaluation; run recall/artifact/continuation/decision probes after each compression |
| Over-aggressive compression ratio | 99.3% compression (opaque) loses 0.35 quality points vs 98.6% (anchored) | Accept slightly lower compression ratios for better quality; the 0.7% tokens retained buy 40% fewer re-fetch cycles |

## Guidelines

1. Optimize for tokens-per-task, not tokens-per-request
2. Use structured summaries with explicit sections for file tracking
3. Trigger compression at 70-80% context utilization
4. Implement incremental merging rather than full regeneration
5. Test compression quality with probe-based evaluation
6. Track artifact trail separately if file tracking is critical
7. Accept slightly lower compression ratios for better quality retention
8. Monitor re-fetching frequency as a compression quality signal

## Integration

- context-degradation - Compression is a mitigation strategy for degradation
- context-optimization - Compression is one optimization technique among many
- memory-systems - Compression relates to scratchpad and summary memory patterns

## References

Internal reference:
- [Evaluation Framework Reference](./references/evaluation-framework.md) - Detailed probe types and scoring rubrics

External resources:
- Factory Research: Evaluating Context Compression for AI Agents (December 2025)
- Research on LLM-as-judge evaluation methodology (Zheng et al., 2023)
