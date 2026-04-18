---
name: context-degradation
description: Diagnosing context FAILURES — lost-in-middle, poisoning, distraction, confusion, and clash patterns with empirical thresholds by model. Use when the user asks to "diagnose context problems", "fix lost-in-middle issues", "debug agent failures", "understand context poisoning", or mentions context degradation, context clash, or agent performance degradation. NOT for learning context basics or theory (use context-fundamentals), NOT for compressing or summarizing context (use context-compression), NOT for KV-cache optimization or partitioning (use context-optimization), NOT for building isolated multi-agent architectures (use multi-agent-patterns).
---

# Context Degradation Patterns

Language models exhibit predictable degradation patterns as context length increases. These patterns are not random failures — they follow measurable thresholds and can be systematically diagnosed and mitigated.

## When to Use / Not Use

**Use when:**
- Agent performance degrades unexpectedly during long conversations
- Debugging cases where agents produce incorrect or irrelevant outputs
- Designing systems that must handle large contexts reliably
- Investigating "lost in middle" phenomena in agent outputs
- Evaluating model selection based on degradation thresholds

**Do NOT use when:**
- Learning context basics or theory -> use `context-fundamentals`
- Compressing or summarizing context -> use `context-compression`
- KV-cache optimization or context partitioning -> use `context-optimization`
- Building isolated multi-agent architectures -> use `multi-agent-patterns`

## Decision Tree

```
What degradation symptom are you seeing?
├── Agent ignores information from middle of context
│   └── Lost-in-Middle -> Place critical info at edges, use explicit headers
├── Agent keeps referencing wrong/incorrect facts
│   ├── Wrong facts came from tool output error -> Context Poisoning (truncate to before poison point)
│   ├── Wrong facts came from retrieved docs -> Context Poisoning (validate docs before loading)
│   └── Wrong facts came from model hallucination -> Context Poisoning (mark and re-evaluate)
├── Agent focuses on irrelevant information
│   └── Context Distraction -> Relevance filter before loading, namespacing, JIT context
├── Agent mixes requirements from different tasks
│   └── Context Confusion -> Task segmentation, clear transitions, state isolation
├── Agent receives contradictory information
│   ├── From different sources -> Context Clash (priority rules, conflict marking)
│   ├── From version conflicts -> Context Clash (version filtering)
│   └── From different perspectives -> Context Clash (explicit conflict marking)
└── Performance degrades as context grows
    └── See Empirical Thresholds -> Choose mitigation from Four-Bucket Approach
```

## Five Degradation Patterns

### Lost-in-Middle

U-shaped attention curves: information at start and end of context receives reliable attention; middle suffers 10-40% lower recall. Caused by attention sinks at BOS token and limited attention budget stretched across growing context.

**Mitigation:** Place critical information at edges. Use explicit section headers for navigation. Surface key information in summary structures at attention-favored positions.

### Context Poisoning

Errors/hallucinations enter context and compound through repeated reference. Three entry paths: erroneous tool outputs, incorrect retrieved documents, model-generated hallucinations persisting in context.

**Detection signals:** Quality degradation on previously-succeeded tasks, tool misalignment, persistent hallucinations despite correction.

**Recovery:** Truncate to before poisoning point, explicitly mark poisoned content and request re-evaluation, or restart with clean context preserving only verified information.

### Context Distraction

Irrelevant information competes for limited attention budget. Even a single irrelevant document reduces performance significantly. Models cannot "skip" context — they must attend to everything provided.

**Mitigation:** Relevance filtering before loading retrieved documents. Namespacing and structural organization. JIT context loading through tool calls instead of pre-loading.

### Context Confusion

Irrelevant information influences model behavior — wrong tool definitions applied, constraints from different contexts mixed. Distinct from distraction: confusion is about influence on behavior, not attention allocation.

**Detection:** Responses address wrong aspect, tool calls appropriate for different task, outputs mixing multiple source requirements.

**Mitigation:** Explicit task segmentation with different context windows. Clear transitions between task contexts. State management that isolates context for different objectives.

### Context Clash

Accumulated information directly conflicts — different sources contradict, outdated vs current versions coexist, valid but incompatible perspectives collide.

**Resolution:** Explicit conflict marking requesting clarification. Priority rules establishing source precedence. Version filtering excluding outdated information.

## Empirical Thresholds by Model

| Model | Degradation Onset | Severe Degradation | Notes |
|-------|-------------------|-------------------|-------|
| GPT-5.2 | ~64K tokens | ~200K tokens | Best degradation resistance with thinking mode |
| Claude Opus 4.5 | ~100K tokens | ~180K tokens | 200K context window, strong attention management |
| Claude Sonnet 4.5 | ~80K tokens | ~150K tokens | Optimized for agents and coding tasks |
| Gemini 3 Pro | ~500K tokens | ~800K tokens | 1M context window, native multimodality |
| Gemini 3 Flash | ~300K tokens | ~600K tokens | 3x speed improvement, 81.2% MMMU-Pro |

**Key finding:** Only 50% of models claiming 32K+ context maintain satisfactory performance at 32K tokens (RULER benchmark). Needle-in-haystack test scores do not predict real long-context understanding.

### Model-Specific Failure Modes

| Model | Failure Mode | Mitigation |
|-------|-------------|------------|
| Claude 4.5 series | Tends to refuse/ask clarification rather than fabricate | Lower hallucination risk; may stall on ambiguous tasks |
| GPT-5.2 | Thinking mode reduces hallucination but increases latency | Use thinking mode for high-stakes tasks, instant for speed |
| Gemini 3 Pro/Flash | Native multimodality across 1M context | Leverage for multi-modal reasoning; still degrades at scale |

## Counterintuitive Findings

| Finding | Implication |
|---------|-------------|
| Shuffled haystacks outperform coherent ones | Coherent context may create false associations; incoherent forces exact matching |
| Single distractors have outsized impact | Effect is step-function, not proportional — any distractor triggers degradation |
| Needle-question similarity correlation | Lower similarity → faster degradation; inference across dissimilar content is most vulnerable |

## The Four-Bucket Mitigation Approach

| Strategy | What It Does | When to Use |
|----------|-------------|-------------|
| Write | Save context outside window (scratchpads, filesystem) | Active context must stay lean |
| Select | Pull relevant context in (retrieval, filtering, prioritization) | Distraction is the primary concern |
| Compress | Reduce tokens while preserving information | Context growing toward degradation threshold |
| Isolate | Split context across sub-agents or sessions | Most aggressive; any single context would otherwise degrade |

### Architectural Patterns

- **JIT context loading**: Retrieve information only when needed
- **Observation masking**: Replace verbose tool outputs with compact references
- **Sub-agent architectures**: Isolate context for different tasks
- **Compaction triggers**: Summarize growing context before exceeding limits

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Assuming larger context = better performance | Larger contexts create new problems; degradation is non-linear | Monitor context length vs performance; find your model's degradation onset and compress before it |
| No degradation monitoring | Failures appear silently; no early warning before quality drops | Track context length and task success rate; set alerts at model-specific degradation thresholds |
| Loading all retrieved docs without filtering | Single irrelevant document causes measurable degradation | Apply relevance filtering before loading; use JIT retrieval instead of pre-loading |
| Ignoring context placement | Critical info buried in middle gets 10-40% lower recall | Place critical information at context edges; use headers for navigation |
| Keeping outdated information in context | Version conflicts cause context clash | Implement version filtering; explicitly mark and remove superseded information |
| No poisoning recovery plan | Once poisoned, errors compound with no escape path | Define truncation points, explicit marking protocols, and clean-restart procedures |
| Treating all models the same | Different models have different degradation thresholds and failure modes | Match model selection to task context length requirements; see empirical thresholds table |
| Pre-loading "just in case" | Pre-loaded context that isn't needed creates distraction | Use JIT loading; load context only when the task requires it |

## Guidelines

1. Monitor context length and performance correlation during development
2. Place critical information at beginning or end of context
3. Implement compaction triggers before degradation becomes severe
4. Validate retrieved documents for accuracy before adding to context
5. Use versioning to prevent outdated information from causing clash
6. Segment tasks to prevent context confusion across different objectives
7. Design for graceful degradation rather than assuming perfect conditions
8. Test with progressively larger contexts to find degradation thresholds

## Integration

- context-fundamentals - Prerequisite: basic context concepts
- context-optimization - Techniques for mitigating degradation
- context-compression - Compression as a degradation mitigation strategy
- multi-agent-patterns - Using isolation to prevent degradation
- evaluation - Measuring and detecting degradation in production

## References

Internal reference:
- [Degradation Patterns Reference](./references/patterns.md) - Detailed technical reference

External resources:
- RULER Benchmark: Only 50% of 32K+ models maintain performance at 32K tokens
- Research on attention sinks and BOS-token attention allocation
- Studies on the "lost-in-middle" phenomenon (Liu et al., 2023)
