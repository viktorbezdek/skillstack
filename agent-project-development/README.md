# Agent Project Development Methodology

> Methodology for LLM-powered project development. Task-model fit analysis, pipeline architecture (acquire-prepare-process-parse-render), file system state machines, cost estimation, and architectural reduction.

## Overview

Not every problem benefits from LLM processing, and the first step in any agent-powered project is evaluating whether the task characteristics align with LLM strengths. This skill encodes a complete methodology for identifying suitable tasks, designing effective pipeline architectures, and iterating rapidly using agent-assisted development. It prevents the most common mistake in LLM projects: building automation before validating that the model can actually do the task.

The methodology applies whether building a batch processing pipeline, a multi-agent research system, or an interactive agent application. It covers the full lifecycle from manual prototype validation through staged pipeline architecture, structured output design, cost estimation, and architectural iteration. The pipeline pattern (acquire, prepare, process, parse, render) separates deterministic stages from the expensive non-deterministic LLM stage, enabling rapid iteration without re-running costly model calls.

Within the SkillStack collection, Agent Project Development provides the high-level methodology that other skills implement at the detail level. It pairs with the Tool Design skill for architectural reduction decisions, the Multi-Agent Patterns skill for scaling beyond single-agent limits, and the Context Compression skill for managing context when pipelines exceed window limits.

## What's Included

### Skill

- `skills/agent-project-development/SKILL.md` -- Core methodology covering task-model fit, pipeline architecture, file system state machines, structured output design, cost estimation, and agent-assisted development

### References

- **case-studies.md** -- Detailed analysis of production projects including Karpathy's HN Time Capsule, Vercel d0 architectural reduction, and Manus agent patterns
- **pipeline-patterns.md** -- Detailed pipeline architecture guidance and implementation patterns

## Key Features

- **Task-model fit recognition** with clear criteria for LLM-suited vs LLM-unsuited tasks, validated through manual prototyping before any automation
- **Five-stage pipeline architecture** (acquire, prepare, process, parse, render) with discrete, idempotent, cacheable stages that separate deterministic work from expensive LLM calls
- **File system as state machine** using directory structures and file existence to track pipeline progress, enable debugging, and provide natural idempotency
- **Structured output design** with section markers, format examples, and robust parsers that handle LLM output variations gracefully
- **Cost and scale estimation** formulas with 20-30% buffer for retries, plus strategies for reducing context length, using smaller models, and caching partial results
- **Architectural reduction** principle backed by production evidence (Vercel d0 went from 17 tools to 2, achieving 100% success rate up from 80%)
- **Agent-assisted development** patterns for rapid iteration: generate, test, fix, repeat

## Usage Examples

Evaluate whether a task suits LLM processing:
```
I want to analyze 500 customer support tickets and categorize them by topic, sentiment, and urgency. Is this a good fit for LLM processing? Help me validate with a manual prototype.
```

Design a batch processing pipeline:
```
Build a pipeline that processes academic papers: fetch from arXiv, extract key findings, grade novelty on a 1-10 scale, and generate a weekly digest. Use the acquire-prepare-process-parse-render pattern.
```

Estimate costs for an LLM project:
```
I need to process 10,000 product reviews through an LLM for sentiment analysis and feature extraction. Help me estimate the total token cost and suggest optimizations.
```

Choose between single and multi-agent architecture:
```
I'm building a research tool that needs to search multiple databases, cross-reference findings, and write a synthesis report. Should I use a single agent or multi-agent approach?
```

## Quick Start

1. **Validate task-model fit**: Take one representative input, test it directly with your target model, and evaluate output quality before building any automation.
2. **Design the pipeline**: Structure as acquire -> prepare -> process -> parse -> render with persistent intermediate files at each stage.
3. **Use file system state**: Create `data/{id}/` directories where each stage completion is marked by file existence (raw.json, prompt.md, response.md, parsed.json).
4. **Estimate costs**: Calculate `items x tokens_per_item x price_per_token` plus 20-30% buffer for retries.
5. **Start minimal**: Begin with the simplest architecture that works, then add complexity only when proven necessary.

## Related Skills

- **tool-design** -- Tool architecture and the architectural reduction principle
- **multi-agent-patterns** -- When to scale beyond single-agent pipelines
- **context-compression** -- Managing context when pipelines exceed window limits
- **agent-evaluation** -- Evaluating pipeline outputs and agent performance
- **context-fundamentals** -- Understanding context constraints for prompt design

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install agent-project-development@skillstack` — 46 production-grade plugins for Claude Code.
