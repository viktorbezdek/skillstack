# Context Degradation Patterns

> Patterns for recognizing and mitigating context failures in LLM agents. Covers lost-in-middle, context poisoning, distraction, confusion, clash, and empirical degradation thresholds by model.

## Overview

Language models exhibit predictable degradation patterns as context length increases, but most teams discover these patterns through painful production failures rather than systematic understanding. This skill encodes the complete taxonomy of context degradation: how it manifests, why it occurs, and what architectural patterns prevent it. Understanding degradation is prerequisite to building reliable agent systems that operate at scale.

Context degradation is not a binary state but a continuum that manifests through five distinct patterns. The lost-in-middle phenomenon causes information in the center of context to receive 10-40% lower recall accuracy. Context poisoning creates feedback loops where errors compound through repeated reference. Context distraction overwhelms relevant information with irrelevant content. Context confusion arises when models cannot determine which context applies. Context clash develops when accumulated information directly conflicts. Each pattern has different detection signals and mitigation strategies.

Within the SkillStack collection, Context Degradation builds on the foundational concepts in Context Fundamentals and feeds directly into Context Optimization and Context Compression, which provide the techniques to mitigate degradation. It also informs Multi-Agent Patterns, where context isolation is the primary architectural motivation for distributing work across agents.

## What's Included

### Skill

- `skills/context-degradation/SKILL.md` -- Core degradation patterns covering lost-in-middle, context poisoning, distraction, confusion, clash, empirical benchmarks, counterintuitive findings, and the four-bucket mitigation approach

### References

- **patterns.md** -- Detailed technical reference for all degradation patterns with detection heuristics and mitigation strategies

## Key Features

- **Five degradation patterns** with distinct detection signals: lost-in-middle (U-shaped attention), poisoning (error feedback loops), distraction (irrelevant content overwhelming signal), confusion (wrong context applied), and clash (contradictory information)
- **Empirical benchmarks by model** including degradation onset and severe degradation thresholds for GPT-5.2, Claude Opus 4.5, Claude Sonnet 4.5, Gemini 3 Pro, and Gemini 3 Flash
- **RULER benchmark findings** showing only 50% of models claiming 32K+ context maintain satisfactory performance at 32K tokens
- **Counterintuitive research findings**: shuffled haystacks outperform coherent ones, single distractors have outsized impact, and lower needle-question similarity correlates with faster degradation
- **The four-bucket mitigation approach**: Write (save context externally), Select (pull relevant context), Compress (reduce tokens), and Isolate (split across sub-agents)
- **Model-specific behavior patterns** informing selection: Claude 4.5 series for lowest hallucination with calibrated uncertainty, GPT-5.2 thinking mode for step-by-step verification, Gemini 3 for native multimodality with 1M context
- **Cost implications** of large contexts with non-linear processing cost growth and cognitive load bottlenecks
- **Architectural mitigation patterns** including just-in-time loading, observation masking, sub-agent isolation, and compaction

## Usage Examples

Diagnose why an agent is producing incorrect outputs:
```
Our agent works well for the first 20 messages but starts producing irrelevant responses after extended conversations. Help me diagnose which degradation pattern is occurring and how to fix it.
```

Design a system resilient to context degradation:
```
I'm building an agent that processes large documents (100K+ tokens). Help me design the architecture to avoid lost-in-middle problems and maintain quality across the full document.
```

Choose the right model for a long-context task:
```
I need to select a model for a task that requires reliable performance at 64K+ tokens of context. Compare the degradation thresholds of current models and recommend the best fit.
```

Investigate context poisoning in production:
```
Our agent's output quality has degraded and it keeps referencing an incorrect API endpoint that was mentioned early in the conversation. Help me identify if this is context poisoning and how to recover.
```

## Quick Start

1. **Monitor context length** and correlate it with output quality during development to find your degradation threshold.
2. **Place critical information** at the beginning or end of context (attention-favored positions), never buried in the middle.
3. **Watch for symptoms**: degraded output quality on previously working tasks, tool misalignment, persistent hallucinations despite correction.
4. **Apply the four buckets**: Write (offload to files), Select (filter for relevance), Compress (summarize growing context), Isolate (split across sub-agents).
5. **Test progressively**: run agents with increasing context sizes to find the specific threshold where degradation becomes severe for your model and task.

## Related Skills

- **context-fundamentals** -- Foundational concepts about context anatomy and attention mechanics
- **context-optimization** -- Techniques for mitigating the degradation patterns identified here
- **context-compression** -- Compression as a specific mitigation for context growth
- **multi-agent-patterns** -- Context isolation through multi-agent architectures
- **agent-evaluation** -- Measuring and detecting degradation in production systems

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install context-degradation@skillstack` — 46 production-grade plugins for Claude Code.
