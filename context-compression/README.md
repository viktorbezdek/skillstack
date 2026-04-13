> **v1.0.4** | Context Engineering | 5 iterations

# Context Compression

Production strategies for compressing LLM context windows without destroying the information agents need most.

## What Problem Does This Solve

When coding agents run long sessions, naive compression destroys the information they need most -- file paths, error messages, and decisions made earlier -- forcing expensive re-exploration that costs more tokens than the compression saved. Most teams optimize for tokens-per-request (how small can I make each call?) when the real optimization target is tokens-per-task (total tokens consumed from start to completion, including re-fetching). This skill provides three production-tested compression strategies -- anchored iterative summarization, opaque compression, and regenerative summaries -- along with probe-based evaluation to measure whether compression actually preserved the information that matters.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install context-compression@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

This is a single-skill plugin with one reference document:

| Component | Description |
|---|---|
| `skills/context-compression/SKILL.md` | Core skill covering three compression methods, tokens-per-task optimization, artifact trail preservation, structured summary sections, trigger strategies, and the three-phase compression workflow for large codebases |
| `references/evaluation-framework.md` | Complete evaluation framework: four probe types (recall, artifact, continuation, decision), six-dimension scoring rubrics (accuracy, context awareness, artifact trail, completeness, continuity, instruction following), LLM judge configuration, and benchmark results across 36,000+ messages |
| `evals/trigger-evals.json` | 13 trigger scenarios validating correct activation and near-miss rejection |
| `evals/evals.json` | 3 output quality scenarios testing compression guidance, approach review, and greenfield setup |

## Usage Scenarios

**1. Agent keeps forgetting which files it modified after compaction**

Your coding agent compacts context at 80% utilization, but afterward it re-reads files it already modified and proposes changes it already made. Use anchored iterative summarization with explicit `Files Modified` sections that survive repeated compression cycles. The structured sections act as checklists the summarizer must populate, preventing silent information drift.

**2. Choosing the right compression method for a long debugging session**

You have a 100+ message debugging session approaching the context limit. The skill provides a decision matrix: use anchored iterative summarization (98.6% compression, 3.70 quality score) for sessions where file tracking matters, opaque compression (99.3% compression, 3.35 quality) when maximum token savings are needed and re-fetching is cheap, or regenerative summaries (98.7% compression, 3.44 quality) when interpretability is critical.

**3. Measuring whether your compression is actually working**

Traditional metrics like ROUGE or embedding similarity fail for coding agents -- a summary can score high on lexical overlap while missing the one file path the agent needs. Use the probe-based evaluation framework: after compression, ask recall probes ("What was the original error message?"), artifact probes ("Which files have we modified?"), continuation probes ("What should we do next?"), and decision probes ("Why did we choose connection pooling?"). If the agent hallucinates answers, your compression is lossy in ways that matter.

**4. Compressing a 5M+ token codebase into a workable context**

A codebase exceeding the context window needs a three-phase compression workflow: (1) Research Phase -- produce a structured analysis of components and dependencies from architecture diagrams and key interfaces, (2) Planning Phase -- convert research into an implementation specification with function signatures and data flow (a 5M token codebase compresses to ~2,000 words of spec), (3) Implementation Phase -- execute against the spec rather than raw codebase exploration.

**5. Setting up compression triggers that fire at the right time**

The skill covers four trigger strategies with tradeoffs: fixed threshold (70-80% utilization, simple but may compress too early), sliding window (keep last N turns + summary, predictable), importance-based (compress low-relevance sections first, complex but preserves signal), and task-boundary (compress at logical completions, clean summaries but unpredictable timing).

## How to Use

**Direct invocation:**

```
Use the context-compression skill to design a compression strategy for my agent
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `context-compression`
- `summarization`
- `compaction`
- `token-optimization`

## When to Use / When NOT to Use

**Use when:**
- Agent sessions exceed context window limits
- Designing conversation summarization strategies
- Debugging cases where agents "forget" what files they modified
- Building evaluation frameworks for compression quality
- Codebases exceed context windows (5M+ token systems)

**Do NOT use when:**
- Diagnosing context failures or degradation patterns -- use [context-degradation](../context-degradation/) instead
- Optimizing KV-cache, observation masking, or context partitioning -- use [context-optimization](../context-optimization/) instead
- Learning context theory or fundamentals -- use [context-fundamentals](../context-fundamentals/) instead
- Offloading context to the file system via scratch pads -- use [filesystem-context](../filesystem-context/) instead

## Related Plugins

- **[Context Degradation](../context-degradation/)** -- Diagnosing context failures: lost-in-middle, poisoning, distraction, clash, and confusion patterns with empirical thresholds by model
- **[Context Fundamentals](../context-fundamentals/)** -- Foundational theory of context engineering: what context is, how attention works, progressive disclosure, and context budgeting
- **[Context Optimization](../context-optimization/)** -- Extending effective context capacity: KV-cache optimization, observation masking, context partitioning, and retrieval strategies
- **[Filesystem Context](../filesystem-context/)** -- Using the file system for context: scratch pads, plan persistence, dynamic skill loading, and sub-agent file workspaces

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
