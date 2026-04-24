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

# Skill Creator

Framework for creating Claude Code skills that encode domain expertise through philosophy-first design, anti-pattern prevention, and progressive disclosure.

## Philosophy: Skills as Mental Frameworks

Skills are not checklists — they are **mental frameworks that guide creative problem-solving**.

**Unlock vs. Constrain:**

| Constraining | Unlocking |
|---|---|
| Rigid templates | Flexible frameworks |
| Fixed outputs | Context-appropriate results |
| Limiting choices | Expanding possibilities |
| Checklists | Mental models |

### The Four Pillars

1. **Philosophy Before Procedure**: "How to think" before "what to do"
2. **Anti-Patterns as Guidance**: What NOT to do is as important as what to do
3. **Progressive Disclosure**: Core in SKILL.md (<500 lines), details in `references/`
4. **Shibboleths**: Encode expert knowledge that separates novices from experts

---

## When to Use

**Use for:**
- Creating new skills from scratch or documentation
- Reviewing/auditing existing skills for quality
- Improving skill activation rates and precision
- Adding domain expertise and shibboleths to skills
- Debugging why skills don't activate correctly
- Transforming CLI/API documentation into skills

**NOT for:**
- General prompt engineering (use prompt-engineering)
- Full plugin development with hooks/MCP (use plugin-dev)
- Non-skill coding advice or simple script writing

---

## Quick Start: Minimal Workflow (6 steps)

1. **Define scope**: What expertise? What keywords? What NOT to handle?
2. **Initialize**: `python scripts/init_skill.py <skill-name> --path <output-dir>`
3. **Write description** with keywords AND NOT clause (see Description Engineering below)
4. **Add 1-3 anti-patterns** you've observed
5. **Test activation** — does it trigger when it should?
6. **Validate**: `python scripts/quick_validate.py <skill-path>`

For complex/production skills, use the 8-phase methodology in `references/skill-foundry.md`.

---

## Skill Structure

### Mandatory
```
your-skill/
└── SKILL.md           # Core instructions (<500 lines)
```

### Optional (add only what SKILL.md references)
```
├── scripts/           # Working code (not templates)
├── references/        # Deep dives (referenced from SKILL.md)
├── templates/         # Config files, boilerplate
├── assets/            # Images, fonts, static files
└── examples/          # Concrete good/bad examples
```

**Anti-pattern**: Creating structure "just in case" — only add files that SKILL.md references.

---

## SKILL.md Template

```markdown
---
name: your-skill-name
description: [What] [When] [Triggers]. NOT for [Exclusions].
allowed-tools: Read,Write  # Minimal only
---

# Skill Name
[One sentence purpose]

## When to Use
✅ Use for: [A, B, C]
❌ NOT for: [D, E, F]

## Philosophy: [Core Mental Framework]
[Establish mental model BEFORE procedures]

**Before [acting], ask**:
- Question 1
- Question 2

## Core Instructions
[Step-by-step, decision trees, not templates]

## Common Anti-Patterns
### [Pattern Name]
**Symptom**: [Recognition]
**Problem**: [Why wrong]
**Solution**: [Better approach]

## Variation Guidance
**IMPORTANT**: Outputs should vary based on context.
- [Dimension 1 to vary]
- [Dimension 2 to vary]
```

Full templates: `templates/skill-template.md` (comprehensive), `templates/skill-skeleton/SKILL.md` (with TODO markers), `templates/tool-skill-SKILL.md.template` (tool-wrapper skills).

---

## Description Field Engineering

The description is your activation trigger. Formula: **[What] [Use for] [Keywords] NOT for [Exclusions]**

| Quality | Example | Issues |
|---|---|---|
| Bad | `Helps with images` | Too vague, no keywords |
| Better | `Image processing with CLIP` | Has keyword but no exclusions |
| Good | `CLIP semantic search. Use for image-text matching, zero-shot classification. Activate on "CLIP", "embeddings", "image search". NOT for counting, fine-grained classification, spatial reasoning.` | Complete |

**Guidelines:**
- Third-person voice ("Use when..." not "You should use...")
- Include specific trigger keywords/phrases
- State clear boundaries (what it does NOT do)
- 100-200 characters recommended

---

## Core Principles

### Progressive Disclosure Architecture

Skills load in three phases:
- **Phase 1 (~100 tokens)**: Metadata (name, description) — "Should I activate?"
- **Phase 2 (<5k tokens)**: Main instructions in SKILL.md — "How do I do this?"
- **Phase 3 (as needed)**: Scripts, references, assets — "Show me the details"

**Critical**: Keep SKILL.md under 500 lines. Split details into `references/`.

### Anti-Pattern Detection

```markdown
## Common Anti-Patterns

### Pattern: [Name]
**What it looks like**: [Code example or description]
**Why it's wrong**: [Fundamental reason]
**What to do instead**: [Better approach]
**How to detect**: [Validation rule]
```

See `references/skill-creation-anti-patterns.md` and `references/domain-shibboleths.md`.

### Shibboleth Encoding

Shibboleths = deep knowledge that separates novices from experts.

**Novice skill creator**: "I'll make a comprehensive skill that handles everything"
**Expert skill creator**: "I'll encode THIS specific expertise" — focused scope, decision trees, anti-patterns, temporal knowledge

### Temporal Knowledge

Technology evolves. Capture what changed and when:

```markdown
## Evolution Timeline
### Pre-2024: Old Approach
[What people used to do]
### 2024-Present: Current Best Practice
[What changed and why]
### Watch For
[Deprecated patterns LLMs might still suggest]
```

---

## Anti-Patterns in Skill Creation

### The Reference Illusion
Skill references scripts/files that don't exist → Claude tries to use non-existent files
**Solution**: Only reference files that exist; use `python scripts/check_self_contained.py <skill-path>` to verify

### Description Soup
`description: Helps with many things including X, Y, Z` → false activations and missed activations
**Solution**: Specific trigger keywords + clear exclusions

### Template Theater
Skill is 90% templates, 10% instructions → Claude needs expert knowledge and decision trees, not templates
**Solution**: Focus on WHEN to use patterns, encode decision logic

### The Everything Skill
One skill handling entire domain → too broad to activate correctly
**Solution**: Create focused, composable skills

### Orphaned Sections
Files in `references/` never referenced in SKILL.md → files exist but are never loaded
**Solution**: Explicit triggers in SKILL.md for each reference file

See `references/skill-creation-anti-patterns.md` for complete list.

---

## Scripts Reference

### Core Workflow

| Script | Purpose | Usage |
|---|---|---|
| `init_skill.py` | Initialize skill structure | `python scripts/init_skill.py <name> --path <dir>` |
| `quick_validate.py` | Fast frontmatter validation | `python scripts/quick_validate.py <skill-path>` |
| `validate_skill.py` | Full validation (structure, content, refs) | `python scripts/validate_skill.py <skill-path>` |
| `analyze_skill.py` | Quality scoring (0-100) | `python scripts/analyze_skill.py <skill-path>` |
| `upgrade_skill.py` | Generate improvement suggestions | `python scripts/upgrade_skill.py <skill-path>` |
| `package_skill.py` | Validate + package to zip | `python scripts/package_skill.py <skill-path>` |

### Doc-to-Skill Pipeline

| Script | Purpose | Usage |
|---|---|---|
| `doc_extractor.py` | Extract docs from URLs or local files | `python scripts/doc_extractor.py <url-or-path>` |
| `doc_analyzer.py` | Analyze doc structure for skill design | `python scripts/doc_analyzer.py <docs>` |
| `create_skill.py` | Full doc-to-skill pipeline orchestrator | `python scripts/create_skill.py <docs>` |

### Validation & Testing

| Script | Purpose | Usage |
|---|---|---|
| `test_activation.py` | Test skill trigger keywords | `python scripts/test_activation.py <skill-path>` |
| `check_self_contained.py` | Verify all refs exist, no phantom tools | `python scripts/check_self_contained.py <skill-path>` |
| `validate_flowchart.sh` | Validate markdown flowcharts | `./scripts/validate_flowchart.sh <file>` |
| `extract_structure.py` | Parse markdown to JSON structure | `python scripts/extract_structure.py doc.md` |
| `analyze_conciseness.py` | Token counting + verbosity analysis | `python scripts/analyze_conciseness.py <skill-path>` |

### Advanced

| Script | Purpose | Usage |
|---|---|---|
| `init_project.py` | Interactive project initialization | `python scripts/init_project.py` |
| `create_skill.py` | Full doc-to-skill pipeline orchestrator | `python scripts/create_skill.py <docs>` |
| `skill-generator.py` | Agent-based skill scaffolding | `python scripts/skill-generator.py <name>` |
| `generate_agent.sh` | Generate agent YAML spec | `./scripts/generate_agent.sh <name>` |
| `generate_boilerplate.py` | Generate project boilerplate (Node/Python/Go) | `python scripts/generate_boilerplate.py <type>` |
| `generate-structure.sh` | Skill directory with references/examples/scripts | `./scripts/generate-structure.sh <name>` |
| `validate_agent.py` | Validate agent YAML specs | `python scripts/validate_agent.py <spec>` |
| `validate_structure.sh` | Validate generated project templates | `./scripts/validate_structure.sh <path>` |

---

## Quality Checklist

### CRITICAL (must-have)
- [ ] Description has keywords AND NOT clause
- [ ] SKILL.md under 500 lines
- [ ] All referenced files exist
- [ ] Test activation: triggers when appropriate, doesn't when inappropriate

### HIGH PRIORITY (should-have)
- [ ] Has "When to Use" and "When NOT to Use" sections
- [ ] Includes 1-3 anti-patterns with "Why it's wrong"
- [ ] Encodes domain shibboleths
- [ ] `allowed-tools` is minimal

### NICE TO HAVE (polish)
- [ ] Temporal knowledge (what changed when)
- [ ] Working code examples (not just templates)
- [ ] References for deep dives
- [ ] Bash restrictions if applicable

**Target score**: 70+/100 on `analyze_skill.py`.

---

## Decision Trees

### When to create a NEW skill?
- ✅ You have domain expertise not in existing skills
- ✅ Pattern repeats across 3+ projects
- ✅ Anti-patterns you want to prevent
- ❌ One-time task — just do it directly
- ❌ Existing skill could be extended — improve that one

### Skill vs Subagent vs MCP?
- **Skill**: Domain expertise, decision trees, anti-patterns (no runtime state)
- **Subagent**: Multi-step workflows needing tool orchestration
- **MCP**: External APIs, auth, stateful connections

### Quick Track vs Expert Track?
- **Quick Track** (6 steps): Simple skills with clear I/O
- **Expert Track** (8 phases): Complex skills, strict contracts, production use

---

## Creating Skills from Documentation

1. **Gather documentation** (markdown or URLs via `doc_extractor.py`)
2. **Analyze** to extract tool overview, patterns, pitfalls, best practices (`doc_analyzer.py`)
3. **Design** components: scripts, templates, guardrails, references
4. **Create** directory structure and artifacts (`init_skill.py`)
5. **Write** SKILL.md with progressive disclosure
6. **Test** activation and workflows (`test_activation.py`)
7. **Iterate** based on feedback (`analyze_skill.py`, `upgrade_skill.py`)

See `references/skill-creation.md` for detailed workflow.

---

## Reference Dispatch

Load a reference **only when the situation calls for it** — do not preload the catalog. If none of these conditions match, stay in this file.

| When you are... | Load |
|---|---|
| Building a production skill needing strict I/O contracts and adversarial testing | `references/skill-foundry.md` (8-phase methodology) |
| Scoping a skill from scratch with unclear requirements | `references/skill-creation.md` (6-step workflow) + `references/interactive-discovery.md` |
| Diagnosing why a skill activates too broadly or too narrowly | `references/editing-guidance.md` + `references/auto-activation-patterns.md` |
| Auditing an existing skill for quality or scoring it | `references/skill-audit-protocol.md` + `references/scoring-rubric.md` |
| Splitting a 500+ line SKILL.md | `references/progressive-disclosure.md` |
| Writing anti-patterns or encoding expert-vs-novice knowledge | `references/skill-creation-anti-patterns.md` + `references/domain-shibboleths.md` |
| Deciding between skill / subagent / MCP / script | `references/mcp-vs-scripts.md` |
| Turning external documentation (URLs, PDFs, markdown) into a skill | `references/research-protocol.md` + `references/optimization.md` |
| Composing multiple skills with dependencies | `references/composability.md` + `references/agent-patterns.md` |
| Adding research-backed prompting techniques (CoT, few-shot, plan-and-solve) | `references/evidence-based-prompting.md` |

**Complete catalog of all 47 references** — including enterprise/lifecycle/cookbook material — lives in `references/README.md`. Consult it when the situation above doesn't match.

---

## Examples

- `examples/annotated/frontend-design-analysis.md` — Line-by-line skill analysis
- `examples/before-after/basic-to-effective.md` — Simple → effective transformation
- `examples/before-after/procedural-to-philosophical.md` — Checklist → framework transformation
- `examples/good-skills/clip-aware-embeddings/` — Exemplary skill with decision tree + validation script
- `examples/example-1-basic-skill.md` — Minimal skill creation walkthrough
- `examples/example-1-specialist.md` — Specialist agent creation (6 phases)
- `examples/example-2-coordinator.md` — Multi-agent coordinator creation
- `examples/example-3-multi-agent-orchestration.md` — Orchestration skill creation
- `examples/enterprise-examples.md` — Full pipeline walkthrough (pytest skill)
- `examples/example-analysis.md` — Research-to-skill workflow (jq skill from docs)
- `examples/document-skills/` — PDF, DOCX, PPTX, XLSX functional skill examples

---

## Templates

- `templates/skill-template.md` — Comprehensive skill template
- `templates/skill-skeleton/` — Full skeleton with TODO markers
- `templates/tool-skill-SKILL.md.template` — Tool-wrapper skill template
- `templates/helper-script.py.template` — Python helper boilerplate
- `templates/helper-script.sh.template` — Bash helper boilerplate
- `templates/scripts-template.sh` — Production-ready Bash script template
- `templates/instruction-template.md` — Step-by-step instruction pattern
- `templates/examples-template.md` — Examples section pattern
- `templates/reference-template.md` — Reference doc pattern
- `templates/skill-schema.json` — JSON schema for skill I/O contracts
- `templates/skill-metrics.yaml` — Revision tracking metrics
- `templates/intake-template.yaml` — Phase 1 skill intake form
- `templates/agent-spec.yaml` — Agent specification template
- `templates/capabilities.json` — Agent capabilities schema
- `templates/readme-template.md` — Project README template
- `templates/research-log-template.md` — Research log for doc analysis
- `templates/README.md` — Templates directory index

---

## Success Metrics

- **Activation**: 90%+ when appropriate, <5% false positives
- **Token efficiency**: <5k tokens typical invocation
- **Error prevention**: Measurable reduction in common mistakes
- **Quality score**: 70+/100 on `analyze_skill.py`

---

## Remember

The best skills establish philosophies that guide thinking, prevent mistakes through anti-patterns, encourage context-appropriate variation, encode shibboleths, stay under 500 lines with progressive disclosure, and empower Claude to do extraordinary work.

---

## Related Skills

- `prompt-engineering` — Prompt optimization
- `hosted-agents` — Agent creation without skill wrapper
- `agent-evaluation` — Benchmark testing
