# Agent Evaluation Framework

> Comprehensive evaluation framework for LLM agent systems. Multi-dimensional rubrics, LLM-as-judge with bias mitigation, pairwise comparison, direct scoring, confidence calibration, and continuous monitoring.

## Overview

Evaluating LLM agents requires fundamentally different approaches than traditional software testing or standard language model benchmarking. Agents make dynamic decisions, are non-deterministic between runs, and often lack single correct answers. This skill encodes a rigorous evaluation methodology that accounts for these characteristics while providing actionable, measurable feedback across multiple quality dimensions.

The Agent Evaluation skill covers the full spectrum from rubric design and test set construction through advanced techniques like LLM-as-judge, pairwise comparison with position bias mitigation, and confidence calibration. It is designed for teams building agent systems who need to validate context engineering choices, catch regressions, and measure improvements systematically rather than relying on ad-hoc "looks good" assessments.

Within the SkillStack collection, Agent Evaluation is a cross-cutting concern that connects to every other skill. Context optimization needs evaluation to prove it works. Multi-agent patterns need evaluation to verify coordination quality. Memory systems need evaluation to measure recall fidelity. This skill provides the measurement framework that makes all other improvements verifiable.

## What's Included

### Skill

- `skills/agent-evaluation/SKILL.md` -- Core evaluation methodology covering rubric design, bias mitigation, direct scoring, pairwise comparison, test set design, and production pipeline architecture

### References

- **bias-mitigation.md** -- Techniques for mitigating position bias, length bias, self-enhancement bias, and authority bias in LLM judges
- **implementation-patterns.md** -- Production implementation patterns for evaluation pipelines
- **metrics-guide.md** -- Guide to selecting evaluation metrics by task type
- **metrics.md** -- Detailed metric definitions and calculation methods

## Key Features

- **Multi-dimensional rubrics** with descriptive levels, edge case guidance, and domain-specific terminology that reduce evaluation variance by 40-60%
- **LLM-as-judge taxonomy** distinguishing direct scoring (for objective criteria) from pairwise comparison (for subjective preferences)
- **Position bias mitigation protocol** with dual-pass position swapping and consistency-based confidence calibration
- **The 95% finding** from BrowseComp research: token usage explains 80% of agent performance variance, informing evaluation design
- **Probe-based test sets** stratified by complexity from simple single-tool calls to extended multi-step reasoning
- **Production pipeline architecture** with criteria loading, primary scoring, bias mitigation, and confidence calibration stages
- **Scaling strategies** including Panel of LLMs (PoLL), hierarchical evaluation, and human-in-the-loop for high-stakes decisions
- **Anti-pattern detection** for scoring without justification, single-pass comparison, overloaded criteria, and single-metric obsession

## Usage Examples

Build an evaluation rubric for a coding assistant:
```
Create a multi-dimensional evaluation rubric for our coding agent. It should cover code correctness, completeness, readability, and efficiency. Include edge case guidance and a 1-5 scoring scale with clear level descriptions.
```

Implement LLM-as-judge for prompt comparison:
```
Set up a pairwise comparison evaluation to determine which of two system prompts produces better agent responses. Include position bias mitigation and confidence scoring.
```

Design a test set for an agent pipeline:
```
Help me create a stratified test set for our customer support agent. I need test cases spanning simple FAQ lookups through complex multi-step troubleshooting scenarios.
```

Set up continuous evaluation monitoring:
```
Design an automated evaluation pipeline that runs on every agent change, tracks quality metrics over time, and alerts on regressions. We need to compare versions and detect drift.
```

## Quick Start

1. **Define quality dimensions** relevant to your agent's use case (accuracy, completeness, tool efficiency, etc.).
2. **Choose evaluation approach** per dimension: direct scoring for objective criteria with ground truth, pairwise comparison for subjective quality judgments.
3. **Build rubrics** with clear level descriptions, observable characteristics, and edge case guidance.
4. **Create test sets** from real usage patterns, stratified by complexity (simple, medium, complex, very complex).
5. **Implement bias mitigation**: always swap positions in pairwise comparison, always require justification before scores.
6. **Run continuously** on agent changes and track metrics over time for trend detection.

## Related Skills

- **context-fundamentals** -- Evaluation prompts require effective context structure
- **context-degradation** -- Detecting and measuring degradation effects through evaluation
- **context-optimization** -- Measuring optimization effectiveness with evaluation metrics
- **multi-agent-patterns** -- Evaluating coordination quality across agents
- **memory-systems** -- Evaluating memory recall quality and retrieval accuracy
- **tool-design** -- Evaluating tool effectiveness and agent-tool interactions

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install agent-evaluation@skillstack` — 46 production-grade plugins for Claude Code.
