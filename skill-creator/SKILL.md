---
name: skill-creator
description: >
  Comprehensive skill creation framework combining philosophy-first design, evidence-based
  prompting, progressive disclosure, anti-pattern prevention, and enterprise-grade workflows.
  Use when creating new skills, improving existing skills, reviewing skill quality, building
  agent-powered workflows, or transforming documentation into production-ready skills.
  Triggers: "create skill", "build skill", "design skill", "skill quality", "skill review",
  "turn docs into skill", "skill from documentation", "improve skill", "skill best practices".
  NOT for general coding advice, non-skill Claude Code features, or simple script writing.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, WebFetch, WebSearch]
---

# Skill Creator

A comprehensive framework for creating high-quality Claude Code skills that encode domain expertise, follow evidence-based prompting principles, and leverage progressive disclosure architecture.

## Philosophy: Skills as Mental Frameworks

Skills are not checklists or templates - they are **mental frameworks that guide creative problem-solving**.

**Core Principle: Unlock vs. Constrain**

| Constraining Approach | Unlocking Approach |
|-----------------------|-------------------|
| Rigid templates | Flexible frameworks |
| Strict rules | Guiding principles |
| Fixed outputs | Context-appropriate results |
| Limiting choices | Expanding possibilities |
| Checklists | Mental models |

### The Four Pillars of Effective Skills

1. **Philosophy Before Procedure**: Establish "how to think" before "what to do"
2. **Anti-Patterns as Guidance**: What NOT to do is as important as what to do
3. **Progressive Disclosure**: Core in SKILL.md (<500 lines), details in references/
4. **Shibboleths**: Encode expert knowledge that separates novices from experts

---

## When to Use This Skill

**Use for:**
- Creating new skills from scratch or documentation
- Reviewing/auditing existing skills for quality
- Improving skill activation rates and precision
- Adding domain expertise and shibboleths to skills
- Building agent-powered skill workflows
- Debugging why skills don't activate correctly
- Transforming CLI/API documentation into skills

**NOT for:**
- General Claude Code features (slash commands, MCPs)
- Non-skill coding advice
- Simple script writing without skill abstraction
- Debugging runtime errors (use domain-specific skills)

---

## Quick Start: Creating a Skill

### Minimal Workflow (Simple Skills)

1. **Define scope**: What expertise? What keywords? What NOT to handle?
2. **Initialize**: `python scripts/init_skill.py <skill-name> --path <output-dir>`
3. **Write description** with keywords AND NOT clause
4. **Add 1-3 anti-patterns** you've observed
5. **Test activation** - does it trigger when it should?
6. **Validate**: `python scripts/quick_validate.py <skill-path>`

### Full Workflow (Production Skills)

Use the 8-phase methodology for complex, shared, or enterprise skills:

| Phase | Name | Purpose | Time |
|-------|------|---------|------|
| 0 | Schema Definition | Define I/O contracts (Expert Track) | 5-10 min |
| 0.5 | Cognitive Frame | Design cognitive patterns | 5-10 min |
| 1 | Intent Archaeology | Deep analysis of true intent | 10-15 min |
| 1b | Intent Verification | Chain-of-Verification | 5-10 min |
| 2 | Use Case Crystallization | Concrete examples | 10-15 min |
| 3 | Structural Architecture | Progressive disclosure design | 10-15 min |
| 4 | Metadata Engineering | Name, description, triggers | 5-10 min |
| 5 | Instruction Crafting | Write actual content | 20-30 min |
| 5b | Instruction Verification | Adversarial testing | 10-15 min |
| 6 | Resource Development | Scripts, references, assets | 15-30 min |
| 7 | Validation & Iteration | Testing and refinement | 15-20 min |
| 7a | Adversarial Testing | Red-team vulnerabilities | 25-40 min |
| 8 | Metrics Tracking | Track revision gains | 10-15 min |

**See**: `references/skill-forge.md` for detailed phase descriptions.

---

## Skill Structure

### Mandatory
```
your-skill/
└── SKILL.md           # Core instructions (<500 lines)
```

### Optional (add only what's needed)
```
├── scripts/           # Working code (not templates)
├── references/        # Deep dives (referenced from SKILL.md)
├── templates/         # Config files, boilerplate
├── assets/            # Images, fonts, static files
└── examples/          # Concrete good/bad examples
```

**Anti-pattern**: Creating structure "just in case" - only add files that SKILL.md references.

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
[Philosophy section establishing mental model BEFORE procedures]

**Before [acting], ask**:
- Question 1
- Question 2
- Question 3

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

---

## Description Field Engineering

The description is your activation trigger. Formula: **[What] [Use for] [Keywords] NOT for [Exclusions]**

**Progression from Bad to Good:**

| Quality | Example | Issues |
|---------|---------|--------|
| Bad | `Helps with images` | Too vague, no keywords |
| Better | `Image processing with CLIP` | Has keyword but no exclusions |
| Good | `CLIP semantic search. Use for image-text matching, zero-shot classification. Activate on "CLIP", "embeddings", "image search". NOT for counting, fine-grained classification, spatial reasoning.` | Complete |

**Guidelines:**
- Use third-person voice ("Use when..." not "You should use...")
- Include specific trigger keywords/phrases
- State clear boundaries (what it does NOT do)
- 100-200 characters recommended for core description

---

## Core Principles

### 1. Progressive Disclosure Architecture

Skills load in three phases:
- **Phase 1 (~100 tokens)**: Metadata (name, description) - "Should I activate?"
- **Phase 2 (<5k tokens)**: Main instructions in SKILL.md - "How do I do this?"
- **Phase 3 (as needed)**: Scripts, references, assets - "Show me the details"

**Critical**: Keep SKILL.md under 500 lines. Split details into `/references`.

### 2. Anti-Pattern Detection

Great skills actively warn about common mistakes:

```markdown
## Common Anti-Patterns

### Pattern: [Name]
**What it looks like**: [Code example or description]
**Why it's wrong**: [Fundamental reason]
**What to do instead**: [Better approach]
**How to detect**: [Validation rule]
```

**See**: `references/anti-patterns.md` and `references/antipatterns.md` for comprehensive lists.

### 3. Shibboleth Encoding

Shibboleths = deep knowledge that separates novices from experts.

**Novice skill creator**:
- "I'll make a comprehensive skill that handles everything"
- Focuses on templates and examples
- Description: "Helps with many things"

**Expert skill creator**:
- "I'll encode THIS specific expertise about X"
- Focuses on decision trees and anti-patterns
- Description with keywords AND NOT clause
- Encodes temporal knowledge: "Pre-2024 pattern X, now use Y"

### 4. Temporal Knowledge

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

## Common Anti-Patterns in Skill Creation

### Anti-Pattern: The Reference Illusion
**What it looks like**: Skill references scripts/files that don't exist
**Why it's wrong**: Claude will try to use non-existent files
**Solution**: Only reference files that actually exist; use `find skill-dir/ -type f` to verify

### Anti-Pattern: Description Soup
**What it looks like**: `description: Helps with many things including X, Y, Z`
**Why it's wrong**: Causes false activations and missed activations
**Solution**: Specific trigger keywords + clear exclusions

### Anti-Pattern: Template Theater
**What it looks like**: Skill is 90% templates, 10% instructions
**Why it's wrong**: Claude needs expert knowledge and decision trees, not templates
**Solution**: Focus on WHEN to use patterns, encode decision logic

### Anti-Pattern: The Everything Skill
**What it looks like**: One skill handling entire domain
**Why it's wrong**: Too broad to activate correctly, mixes concerns
**Solution**: Create focused, composable skills

### Anti-Pattern: Orphaned Sections
**What it looks like**: Files in `/references/` never referenced in SKILL.md
**Why it's wrong**: Files exist but are never used
**Solution**: Explicit triggers in SKILL.md for each reference file

**See**: `references/anti-patterns.md` for complete list with examples.

---

## Scripts Reference

### Core Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `init_skill.py` | Initialize skill structure | `python scripts/init_skill.py <name> --path <dir>` |
| `quick_validate.py` | Fast validation checks | `python scripts/quick_validate.py <skill-path>` |
| `package_skill.py` | Validate + package to zip | `python scripts/package_skill.py <skill-path>` |
| `validate_skill.py` | Full validation | `python scripts/validate_skill.py <skill-path>` |
| `analyze_skill.py` | Quality scoring (0-100) | `python scripts/analyze_skill.py <skill-path>` |
| `upgrade_skill.py` | Generate improvements | `python scripts/upgrade_skill.py <skill-path>` |

### Documentation Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `extract_structure.py` | Parse document to JSON | `python scripts/extract_structure.py doc.md` |
| `doc_analyzer.py` | Analyze documentation | `python scripts/doc_analyzer.py <docs>` |
| `doc_extractor.py` | Extract from URLs | `python scripts/doc_extractor.py <url>` |

### Validation Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `test_activation.py` | Test skill triggers | `python scripts/test_activation.py <skill-path>` |
| `check_self_contained.py` | Verify all refs exist | `python scripts/check_self_contained.py <skill-path>` |
| `validate_flowchart.sh` | Validate flowcharts | `./scripts/validate_flowchart.sh <file>` |

---

## Quality Heuristics

An effective skill should:

- [ ] **Establish philosophy** before procedures
- [ ] **Description has keywords AND NOT clause**
- [ ] **SKILL.md under 500 lines**
- [ ] **All referenced files exist**
- [ ] **Prevent anti-patterns** with explicit examples
- [ ] **Encourage variation** to avoid convergence
- [ ] **Encode shibboleths** (expert vs novice knowledge)
- [ ] **Has "When to Use" and "When NOT to Use" sections**
- [ ] **allowed-tools is minimal**
- [ ] **Test activation**: triggers when it should, doesn't when it shouldn't

**Target score**: 70+/100 on `analyze_skill.py` for effective skills.

---

## Skill Review Checklist

### CRITICAL (must-have)
- [ ] Description has keywords AND NOT clause
- [ ] SKILL.md under 500 lines
- [ ] All referenced files exist (`find skill-dir/ -type f`)
- [ ] Test activation: triggers when appropriate
- [ ] Test non-activation: doesn't trigger when inappropriate

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

---

## Creating Skills from Documentation

### Workflow

1. **Gather documentation** (markdown or URLs via crawl4ai)
2. **Analyze** to extract tool overview, patterns, pitfalls, best practices
3. **Design** components: scripts, templates, guardrails, references
4. **Create** directory structure and artifacts
5. **Write** SKILL.md with progressive disclosure
6. **Test** activation and workflows
7. **Iterate** based on feedback

### What to Extract from Documentation

- Tool overview and primary use cases
- Command/API patterns and flag combinations
- Multi-step workflows
- Explicitly mentioned warnings and gotchas
- Prerequisites and setup requirements
- Best practices and security considerations

**See**: `references/skill_creation.md` for detailed workflow.

---

## Templates Available

### SKILL.md Templates
- `templates/SKILL_TEMPLATE.md` - Full featured template
- `templates/SKILL-template.md` - Alternative template
- `templates/minimal-skeleton/SKILL.md` - Minimal starter
- `templates/skill-skeleton/SKILL.md` - Standard skeleton

### Script Templates
- `templates/helper-script.py.template` - Python helper
- `templates/helper-script.sh.template` - Bash helper
- `templates/scripts-template.sh` - Script boilerplate

### Other Templates
- `templates/skill-schema.json` - JSON schema for skill contracts
- `templates/skill-metrics.yaml` - Metrics tracking template
- `templates/cov-protocol.md` - Chain-of-Verification protocol
- `templates/adversarial-testing-protocol.md` - Red-team testing

---

## Reference Documentation

### Core References
| Reference | Purpose |
|-----------|---------|
| `references/skill-forge.md` | 8-phase methodology |
| `references/skill_creation.md` | 6-step workflow |
| `references/progressive_disclosure.md` | Loading architecture |
| `references/core_principles.md` | Fundamental principles |

### Anti-Patterns & Best Practices
| Reference | Purpose |
|-----------|---------|
| `references/anti-patterns.md` | Comprehensive anti-pattern list |
| `references/antipatterns.md` | Additional anti-patterns |
| `references/best_practices_checklist.md` | Quality checklist |
| `references/shibboleths.md` | Expert vs novice knowledge |

### Advanced Topics
| Reference | Purpose |
|-----------|---------|
| `references/evidence-based-prompting.md` | Research-backed techniques |
| `references/prompting-principles.md` | Prompting patterns |
| `references/composability.md` | Skill composition patterns |
| `references/variation-patterns.md` | Output diversity techniques |

### Enterprise & Workflows
| Reference | Purpose |
|-----------|---------|
| `references/skill-factory-workflow.md` | Enterprise workflows |
| `references/SKILL-AUDIT-PROTOCOL.md` | Audit methodology |
| `references/REQUIRED-SECTIONS.md` | Section requirements |
| `references/validation.md` | Validation guidelines |

---

## Examples

### Example Skills
- `examples/document-skills/` - PDF, DOCX, PPTX, XLSX skills
- `examples/algorithmic-art/` - Creative coding skill
- `examples/internal-comms/` - Communication skill
- `examples/good-skills/clip-aware-embeddings/` - Exemplary skill

### Transformation Examples
- `examples/before-after/basic-to-effective.md` - Simple to effective
- `examples/before-after/procedural-to-philosophical.md` - Checklist to framework
- `examples/annotated/frontend-design-analysis.md` - Line-by-line analysis

### Test Cases
- `examples/tests/` - Validation test cases

---

## Decision Trees

### When to create a NEW skill?
- ✅ You have domain expertise not in existing skills
- ✅ Pattern repeats across 3+ projects
- ✅ Anti-patterns you want to prevent
- ❌ One-time task - just do it directly
- ❌ Existing skill could be extended - improve that one

### Skill vs Subagent vs MCP?
- **Skill**: Domain expertise, decision trees, anti-patterns (no runtime state)
- **Subagent**: Multi-step workflows needing tool orchestration
- **MCP**: External APIs, auth, stateful connections

### Quick Track vs Expert Track?
- **Quick Track** (Phases 1-7): Simple skills with clear I/O
- **Expert Track** (Phases 0-8): Complex skills, strict contracts, production use

---

## Success Metrics

- **Activation**: 90%+ when appropriate, <5% false positives
- **Token efficiency**: <5k tokens typical invocation
- **Error prevention**: Measurable reduction in common mistakes
- **Quality score**: 70+/100 on analyze_skill.py

---

## Remember

**Skills are mental frameworks, not checklists.**

The best skills:
- Establish philosophies that guide thinking
- Prevent mistakes through explicit anti-patterns
- Encourage context-appropriate variation
- Encode shibboleths (expert knowledge)
- Stay under 500 lines with progressive disclosure
- Empower Claude to do extraordinary work

**Claude is capable of extraordinary work in skill creation. These guidelines illuminate the path - they don't fence it.**

---

## Related Skills

- `prompt-architect` - Prompt optimization
- `agent-creator` - Agent creation without skill wrapper
- `eval-harness` - Benchmark testing
- `cognitive-lensing` - Cognitive frame design



