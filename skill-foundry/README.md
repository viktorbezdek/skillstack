---
name: skill-foundry
description: >-
  Author high-quality Claude Code SKILL.md files using philosophy-first design, evidence-based
  prompting, progressive disclosure, and anti-pattern prevention. Use when the user asks to
  write a skill file, create a new Claude Code skill, design a SKILL.md, review whether a
  skill's description will trigger correctly, or convert a workflow into a reusable skill.
  NOT for optimizing standalone prompts or system prompts (use prompt-engineering). NOT for
  full plugin development with hooks and MCP (use plugin-architecture). NOT for generating
  code documentation (use documentation-generator).
allowed-tools:
- Read
- Write
- Edit
- Bash
- Glob
- Grep
- WebFetch
- WebSearch
---

# Skill Foundry

> **v2.1.0** | Production

Framework for creating Claude Code skills that encode domain expertise through philosophy-first design, anti-pattern prevention, and progressive disclosure.

## The Problem

Most Claude Code skills are checklists dressed up as expertise. They list steps to follow, templates to fill in, and rules to obey — and the output converges to the same generic pattern regardless of context. The skill activates when it shouldn't, stays silent when it should trigger, and produces rigid, templated responses that don't adapt.

The deeper problem: skill creators focus on procedure before philosophy. They write "Step 1: Do X, Step 2: Do Y" without establishing the mental framework that guides judgment when the steps don't apply. They stuff 800+ lines into SKILL.md without progressive disclosure. They reference files that don't exist, causing silent failures. They write descriptions that are too vague or too narrow, missing the activation window entirely.

## The Solution

Four pillars: **Philosophy Before Procedure** (establish "how to think" before "what to do"), **Anti-Patterns as Guidance** (what NOT to do is as important as what to do), **Progressive Disclosure** (SKILL.md under 500 lines, details in references), and **Shibboleths** (encode deep expert knowledge that separates novices from experts).

Two tracks: **Minimal Workflow** (6 steps for simple skills) and **Full 8-Phase Methodology** (for production-grade skills needing rigorous I/O contracts, adversarial testing, and enterprise validation).

## Context to Provide

- **The domain expertise to encode** — "PostgreSQL query optimization for Django ORM with N+1 detection" is better than "database help"
- **Top 3-5 mistakes to prevent** — anti-patterns are the highest-value content
- **The target users** — their experience level determines vocabulary and assumption depth
- **What the skill should NOT handle** — exclusions are as important as inclusions for activation precision
- **Existing skill to review** — paste it or provide the path for diagnosis

## Quick Start

1. **Install** the plugin: `/plugin install skill-foundry@skillstack`
2. **Describe expertise**: `Create a skill for PostgreSQL query optimization`
3. The skill **asks scope questions**: What specific expertise? What should it NOT handle?
4. It **generates the skill structure** with `init_skill.py`, writes description with keywords and NOT clause
5. **Validate and iterate**: `quick_validate.py` checks structure, `analyze_skill.py` scores quality 0-100

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Skills are checklists producing rigid output | Philosophy-first design produces context-appropriate variation |
| Description too vague/narrow — incorrect activation | Formula: [What] [Use for] [Keywords] NOT for [Exclusions] — precise activation |
| SKILL.md is 800+ lines, burning context | Progressive disclosure: under 500 lines, details loaded on demand |
| Skills reference non-existent files — silent failures | `check_self_contained.py` validates every reference |
| Common mistakes go uncaught | Anti-pattern sections teach the model to avoid them |
| No quality measurement | `analyze_skill.py` scores 0-100, `skill-metrics.yaml` tracks gains |

## What's Inside

| Component | Count | Purpose |
|---|---|---|
| Core skill | 1 | Four pillars, description engineering, two workflow tracks, quality heuristics |
| Reference files | 47 | Methodology, anti-patterns, quality, composability, enterprise, agents |
| Utility scripts | 25 | Init, validation, analysis, doc extraction, packaging, activation testing |
| Templates | 19 | SKILL.md starters, script boilerplate, config, metrics, intake forms |
| Examples | 18 | Annotated analysis, before/after, good skills, pipeline walkthroughs |
| Flowcharts | 6 | Decision tree, approval workflow, parallel execution, swimlane, onboarding |
| Evals | 2 | Trigger evaluation + output evaluation cases |

## Key Scripts

| Script | Purpose |
|---|---|
| `init_skill.py` | Initialize skill directory structure |
| `quick_validate.py` | Fast frontmatter validation |
| `validate_skill.py` | Full validation (structure, content, refs) |
| `analyze_skill.py` | Quality scoring (0-100) |
| `upgrade_skill.py` | Generate improvement suggestions |
| `test_activation.py` | Test skill trigger keywords |
| `check_self_contained.py` | Verify all refs exist |
| `doc_extractor.py` | Extract docs from URLs/local files |
| `create_skill.py` | Full doc-to-skill pipeline |

## Key References

| Reference | Topic |
|---|---|
| `skill-foundry.md` | Complete 8-phase methodology |
| `skill_creation.md` | 6-step creation workflow |
| `skill-creation-anti-patterns.md` | Skill creation anti-pattern catalog |
| `domain-shibboleths.md` | Expert vs novice knowledge encoding |
| `evidence-based-prompting.md` | Research-backed prompting techniques |
| `composability.md` | Skill composition + dependency patterns |
| `troubleshooting.md` | Common issues and solutions |

## Installation

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install skill-foundry@skillstack
```

## Prompt Patterns

**For creating a new skill:**
```
Create a Claude Code skill for [domain expertise]. The skill should encode
[specific knowledge: patterns, anti-patterns, decision trees]. Target users
are [who]. It should NOT handle [exclusions]. Top mistakes to prevent:
[list 2-3 common mistakes].
```

**For improving activation:**
```
My skill [name] triggers too broadly. It should activate for [target queries]
but currently [what happens instead]. Fix the activation with proper keywords
and NOT clauses.
```

**For refactoring an oversized skill:**
```
My SKILL.md is [N] lines. Split it using progressive disclosure.
Keep [decision trees, anti-patterns, philosophy] in SKILL.md and move
[detailed patterns, examples, deep dives] to reference files.
```

## Not For

- **General prompt engineering** — use [prompt-engineering](../prompt-engineering/)
- **Building Claude Code plugins** — use [plugin-dev](https://github.com/viktorbezdek/skillstack/tree/main/plugin-dev)
- **Agent runtime and orchestration** — use [multi-agent-patterns](../multi-agent-patterns/)

## Related Plugins

- **[Prompt Engineering](../prompt-engineering/)** — Optimize prompts for LLMs
- **[Agent Evaluation](../agent-evaluation/)** — Build evaluation frameworks
- **[Hosted Agents](../hosted-agents/)** — Create hosted coding agents
- **[Multi-Agent Patterns](../multi-agent-patterns/)** — Design multi-agent systems

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — production-grade plugins for Claude Code.
