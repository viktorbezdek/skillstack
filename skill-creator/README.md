# Skill Creator

> **v1.1.19** | Development | 21 iterations

Comprehensive skill creation framework combining philosophy-first design, evidence-based prompting, progressive disclosure, anti-pattern prevention, and enterprise-grade workflows.

## What Problem Does This Solve

Most Claude Code skills are written as checklists or template dumps that activate too broadly, trigger on the wrong keywords, or give Claude procedures without the mental framework to apply them intelligently. Without explicit philosophy, anti-patterns, and precise activation descriptions, skills produce inconsistent results and false activations. The deeper problem is that skill creation itself has no methodology -- people write SKILL.md files the way they write documentation, not the way they should write expert knowledge transfer. This skill provides the 8-phase Skill Forge methodology, progressive disclosure architecture, shibboleth encoding, and validation tooling to create skills that activate precisely, encode genuine expertise, and guide Claude's thinking rather than just constraining its output.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Create a new skill from scratch for this domain" | 8-phase Skill Forge methodology from schema definition through adversarial testing, plus `init_skill.py` scaffold script |
| "Turn this API documentation into a skill" | Documentation-to-skill workflow: extract patterns, warnings, and best practices, then structure with progressive disclosure |
| "My skill activates when it shouldn't" | Description field engineering formula ([What] [Keywords] NOT for [Exclusions]) with Bad/Better/Good progression examples |
| "Review this skill for quality issues" | Skill Review Checklist with CRITICAL items (description, line limit, file refs, activation tests) and quality scoring |
| "How should I structure a skill that has a lot of content?" | Progressive disclosure architecture: core in SKILL.md (<500 lines), details in /references/, code in /scripts/ |
| "Score this skill's quality" | `analyze_skill.py` script producing a 0-100 quality score against ten heuristics |

## When NOT to Use This Skill

- General prompt engineering -- use [prompt-engineering](../prompt-engineering/) instead
- Building MCP servers -- use [mcp-server](../mcp-server/) instead
- Creating hosted agents without skill wrappers -- use [hosted-agents](../hosted-agents/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install skill-creator@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the skill-creator skill to create a new skill for Terraform infrastructure management
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `create skill`
- `build skill`
- `design skill`
- `skill quality`
- `skill review`

## What's Inside

This is a large single-skill plugin with extensive references, examples, scripts, and templates organized for progressive disclosure.

### Core Skill

| Component | Purpose |
|---|---|
| `SKILL.md` | Philosophy (Skills as Mental Frameworks), four pillars, Quick Start (Minimal + Full workflow), SKILL.md template, description field engineering, five named anti-patterns, quality heuristics, and decision trees |

### Scripts (16 tools)

| Script | Purpose |
|---|---|
| `init_skill.py` | Initialize skill directory structure with required files |
| `quick_validate.py` | Fast validation checks for common issues |
| `validate_skill.py` | Full structural and content validation |
| `analyze_skill.py` | Quality scoring (0-100) against ten heuristics |
| `package_skill.py` | Validate and package skill to zip for distribution |
| `upgrade_skill.py` | Generate improvement suggestions for an existing skill |
| `test_activation.py` | Test whether a skill triggers on expected inputs |
| `check_self_contained.py` | Verify all referenced files actually exist |
| `extract_structure.py` | Parse documentation into JSON structure |
| `doc_analyzer.py` | Analyze documentation for skill-worthy patterns |
| `doc_extractor.py` | Extract documentation from URLs |
| `create_skill.py` | End-to-end skill generation |
| `skill_md_generator.py` | Generate SKILL.md from structured input |
| `generate_boilerplate.py` | Generate boilerplate for skill components |
| `skill-generator.py` | Alternative skill generator |
| `validate_flowchart.sh` | Validate flowchart syntax in skill documents |

### References (30+ documents)

| Category | Key References |
|---|---|
| **Methodology** | `skill-forge.md` (8-phase methodology), `skill_creation.md` (6-step workflow), `detailed_process_steps.md` |
| **Architecture** | `progressive_disclosure.md` (loading phases), `file-structure-standards.md`, `composability.md` (skill composition) |
| **Quality** | `anti-patterns.md`, `antipatterns.md`, `best_practices_checklist.md`, `comprehensive_checklist.md`, `validation.md`, `scoring-rubric.md` |
| **Expertise** | `shibboleths.md` (expert vs. novice knowledge), `evidence-based-prompting.md`, `prompting-principles.md`, `core_principles.md` |
| **Enterprise** | `skill-factory-workflow.md`, `SKILL-AUDIT-PROTOCOL.md`, `REQUIRED-SECTIONS.md`, `enterprise-checklist.md` |
| **Advanced** | `variation-patterns.md` (output diversity), `optimization.md`, `token_efficiency.md`, `skill-lifecycle.md` |

### Templates

| Template | Purpose |
|---|---|
| `SKILL_TEMPLATE.md` / `SKILL-template.md` | Full-featured SKILL.md templates |
| `minimal-skeleton/` | Minimal starter with just SKILL.md and README |
| `skill-skeleton/` | Standard skeleton with references and scripts directories |
| `skill-schema.json` | JSON schema for validating skill contracts |
| `adversarial-testing-protocol.md` | Red-team testing protocol for skills |
| `cov-protocol.md` | Chain-of-Verification protocol |

### Examples

| Example | Purpose |
|---|---|
| `document-skills/` | Complete PDF, DOCX, PPTX, XLSX skill examples |
| `good-skills/clip-aware-embeddings/` | Exemplary skill showing best practices |
| `before-after/` | Transformation examples: basic-to-effective, procedural-to-philosophical |
| `annotated/frontend-design-analysis.md` | Line-by-line analysis of an existing skill |

## Usage Scenarios

**Scenario 1 -- Creating a skill from domain expertise.** You are an expert in Terraform and want to encode that knowledge. The skill walks through the 8-phase Skill Forge: define the schema (inputs/outputs), establish cognitive frames, do intent archaeology (what does the user really need?), crystallize use cases, design the progressive disclosure architecture, engineer the activation description, craft instructions, and run adversarial testing.

**Scenario 2 -- Converting API docs into a skill.** You have extensive documentation for a CLI tool. The `doc_extractor.py` pulls content from URLs, `doc_analyzer.py` identifies patterns, warnings, and best practices worth encoding, and the methodology guides you to structure findings as decision trees and anti-patterns rather than template copies.

**Scenario 3 -- Debugging activation failures.** Your skill triggers on unrelated queries or misses queries it should handle. The skill diagnoses the description field, applies the [What] [Keywords] NOT for [Exclusions] formula, and `test_activation.py` verifies the fix by running both positive and negative test inputs.

**Scenario 4 -- Auditing skill quality.** You have an existing skill that feels "off" but you cannot pinpoint why. `analyze_skill.py` scores it 0-100 against ten heuristics (philosophy before procedure, description quality, line count, file refs, anti-patterns, variation guidance, shibboleth encoding, When to Use/NOT to Use sections, minimal allowed-tools, activation testing). The Skill Review Checklist then guides fixes ordered by priority.

**Scenario 5 -- Enterprise skill factory.** Your team produces skills regularly and needs consistency. The enterprise references provide the factory workflow, audit protocol, required sections specification, and the scoring rubric that makes quality gates objective rather than subjective.

## Related Skills

- **[Prompt Engineering](../prompt-engineering/)** -- Optimize the prompts within your skills using systematic prompt design methodology.
- **[Agent Evaluation](../agent-evaluation/)** -- Build test frameworks and benchmarks to measure whether your skills actually improve Claude's output.
- **[Hosted Agents](../hosted-agents/)** -- Create background agents when your use case needs runtime orchestration rather than skill-based knowledge transfer.
- **[Example Design](../example-design/)** -- Design effective examples for the few-shot demonstrations inside your skills.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 52 production-grade plugins for Claude Code.
