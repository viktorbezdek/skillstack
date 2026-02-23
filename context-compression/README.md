# Context Compression Strategies

> Production strategies for compressing LLM context windows. Anchored iterative summarization, opaque compression, tokens-per-task optimization, and probe-based evaluation.

## Overview

When agent sessions generate millions of tokens of conversation history, compression becomes mandatory. The naive approach targets tokens-per-request, but the correct optimization target is tokens-per-task: the total tokens consumed to complete a task, including re-fetching costs when compression loses critical information. This skill provides production-ready compression strategies that minimize total token cost while preserving the information agents actually need.

The skill covers three distinct compression approaches: anchored iterative summarization (best quality, structured sections force preservation), opaque compression (highest compression ratio, sacrifices interpretability), and regenerative full summaries (readable but loses details across cycles). It also provides a probe-based evaluation framework that directly measures whether compression preserved the right information, replacing traditional metrics like ROUGE that fail to capture functional quality.

Within the SkillStack collection, Context Compression is a mitigation strategy for the problems described in Context Degradation and one of the optimization techniques covered in Context Optimization. It pairs with the Memory Systems skill for offloading compressed state to persistent storage and the Agent Evaluation skill for probe-based quality measurement.

## What's Included

### Skill

- `skills/context-compression/SKILL.md` -- Core compression methodology covering anchored iterative summarization, opaque compression, tokens-per-task optimization, three-phase compression workflow, and probe-based evaluation

### References

- **evaluation-framework.md** -- Detailed probe types, scoring rubrics, and evaluation dimensions for measuring compression quality

## Key Features

- **Tokens-per-task optimization** replacing the misleading tokens-per-request metric, accounting for re-fetching costs when compression loses critical details
- **Anchored iterative summarization** with explicit sections (session intent, files modified, decisions, next steps) that force preservation of critical information
- **Three compression approaches** compared with benchmarks: anchored iterative (98.6% compression, 3.70 quality), regenerative (98.7%, 3.44), and opaque (99.3%, 3.35)
- **Artifact trail tracking** addressing the weakest dimension across all methods (scoring 2.2-2.5/5.0), with specialized handling recommendations for file tracking
- **Probe-based evaluation** using recall, artifact, continuation, and decision probes to directly measure functional compression quality
- **Six evaluation dimensions**: accuracy, context awareness, artifact trail, completeness, continuity, and instruction following
- **Three-phase workflow** for large codebases: research phase, planning phase, and implementation phase that compresses 5M+ token systems to ~2,000 words of specification
- **Compression trigger strategies** including fixed threshold, sliding window, importance-based, and task-boundary approaches

## Usage Examples

Implement compression for a long coding session:
```
My debugging session has reached 89,000 tokens over 178 messages. Implement anchored iterative summarization that preserves which files I modified, what decisions I made, and what steps remain.
```

Evaluate compression quality:
```
I implemented context compression for our agent. Design a probe-based evaluation that tests whether the agent can still answer questions about file paths, error messages, and next steps after compression.
```

Handle a codebase exceeding the context window:
```
Our codebase is 5 million tokens. Help me apply the three-phase compression workflow: research the architecture, plan the implementation with function signatures, then execute against the spec.
```

Choose between compression strategies:
```
We have a long-running agent that processes customer tickets over hundreds of messages. Which compression approach should we use -- anchored iterative, opaque, or regenerative? Our priority is maintaining file tracking accuracy.
```

## Quick Start

1. **Define summary sections** matching your agent's needs: session intent, files modified, decisions made, current state, and next steps.
2. **Set compression trigger** at 70-80% context utilization using a sliding window approach.
3. **On first trigger**, summarize the truncated history into your defined sections.
4. **On subsequent triggers**, summarize only the newly truncated content and merge into existing sections (incremental, not regenerative).
5. **Evaluate with probes**: after compression, ask the agent about specific file paths, error messages, and decisions to verify preservation.

## Related Skills

- **context-degradation** -- Understanding the degradation patterns that compression mitigates
- **context-optimization** -- Compression as one technique within the broader optimization toolkit
- **context-fundamentals** -- Foundational context concepts that inform compression design
- **memory-systems** -- Offloading compressed state to persistent memory layers
- **agent-evaluation** -- Probe-based evaluation methodology applicable to compression testing

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install context-compression@skillstack` — 46 production-grade plugins for Claude Code.
