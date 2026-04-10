# Documentation Generator

> **v1.1.15** | Documentation | 17 iterations

Generate comprehensive documentation for repositories of any size - from small libraries to large monorepos. Creates both non-technical overviews and detailed technical references.

## What Problem Does This Solve

Writing documentation from scratch is slow and inconsistent: different team members structure READMEs differently, API docs miss edge cases, and architecture docs go stale because there is no systematic process. This skill provides a structured six-phase workflow — analysis, planning, structure, writing, coverage, and validation — that turns a repository into a complete, audience-aware documentation set. It orchestrates 24 templates and a suite of supporting skills so nothing falls through the cracks.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Write documentation for this repo" | Six-phase workflow: repo analysis script, audience planning, template selection, and coverage validation |
| "Generate an API reference for our REST endpoints" | REST endpoint template with example-design and edge-case-coverage baked in |
| "Create an architecture doc for the system" | System design, data flow, and ADR templates backed by systems-thinking and ontology-design skills |
| "Write a getting-started guide for new developers" | Quickstart and installation templates structured around user-journey-design |
| "Our docs are outdated — find what's missing" | `drift` and `validate` script commands that score coverage and flag gaps |
| "Create a runbook for the on-call team" | Operations runbook template with risk-management and edge-case-coverage applied |

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/documentation-generator
```

## How to Use

**Direct invocation:**

```
Use the documentation-generator skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `docs`
- `readme`
- `api-docs`
- `architecture-docs`

## What's Inside

- **Workflow Overview** -- Six-phase sequence (analysis → planning → structure → writing → coverage → validation) with the supporting skills to load at each phase.
- **Phase 1: Analysis** -- Python script that inspects repository structure and outputs a structured `analysis.json` to drive subsequent phases.
- **Phase 2: Planning - Load Supporting Skills** -- Persona definition, Power-Interest stakeholder mapping, and RICE/ICE prioritization to decide which docs to write first.
- **Phase 3: Structure - Load Supporting Skills** -- Systems-thinking for architecture mapping, ontology-design for domain concepts, and navigation-design for information architecture.
- **Phase 4: Writing - Load Supporting Skills** -- UX-writing for interface copy, example-design for code samples, and consistency-standards for terminology and style.
- **Phase 5: Coverage - Load Supporting Skills** -- Edge-case-coverage for boundary conditions and user-journey-design to validate that readers can flow from awareness to mastery.
- **Phase 6: Validation - Load Supporting Skills** -- Outcome-orientation to define success metrics and risk-management to identify and track documentation gaps.
- **Template Portfolio** -- 24 ready-to-fill templates across core docs, API reference, architecture, domain model, specs, integrations, and operations.

## Version History

- `1.1.15` fix(docs+quality): optimize descriptions for api-design, docs, edge-cases, examples, navigation, standards (6e315cf)
- `1.1.14` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.13` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.12` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.11` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.10` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.9` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.8` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.7` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.1.6` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)

## Related Skills

- **[Example Design](../example-design/)** -- Design effective code examples, tutorials, and runnable samples with progressive complexity.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
