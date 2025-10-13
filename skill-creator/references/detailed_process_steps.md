# Detailed Process Steps

This document provides in-depth guidance for each step of the skill creation process.

---

## Step 1.2: Plan Skill Structure and Draft

Before implementing, plan the skill's structure and create a rough draft to guide development.

### 1.2.1 Identify Utility Scripts Needed

Use this decision tree to determine which scripts to include:

```
User task → Is it a repetitive, deterministic operation?
    ├─ Yes → Does it require complex logic or error handling?
    │         ├─ Yes → Create utility script (use self-contained-script-template.py)
    │         └─ No  → Simple one-liner? → Use bash directly in SKILL.md
    │
    └─ No  → Is it a validation task?
        ├─ Yes → Create validation script (use validate-skill-template.py)
        └─ No  → Is it a static file for output? → Place in assets/
```

**Script Planning Questions:**
- What operations will be repeated across multiple skill uses?
- Which tasks require deterministic reliability (file processing, API calls)?
- What validation or checking is needed?
- Which operations benefit from error handling and user feedback?

**Document planned scripts:**
```markdown
Planned Scripts:
- scripts/process-files.py - Handle file operations with error handling
- scripts/validate-input.py - Check input format and requirements
- scripts/generate-report.py - Create standardized outputs
```

### 1.2.2 Plan Reference Documentation

Use this decision tree to determine reference needs:

```
Skill complexity → Will SKILL.md exceed ~300 lines?
    ├─ Yes → What detailed information is needed?
    │         ├─ API documentation → references/api-reference.md
    │         ├─ Extended examples → references/examples.md
    │         ├─ Technical deep-dives → references/implementation.md
    │         └─ Advanced patterns → references/advanced-usage.md
    │
    └─ No  → Keep all content in SKILL.md
```

**Reference Planning Questions:**
- What detailed information would Claude need to reference?
- Are there API docs, schemas, or technical specifications?
- Do you have more than 5 examples to include?
- Is there advanced usage that most users won't need?

**Document planned references:**
```markdown
Planned References:
- references/api-reference.md - Complete API documentation
- references/examples.md - Extended usage examples
- references/troubleshooting.md - Common issues and solutions
```

### 1.2.3 Plan Assets and Templates

Use this decision tree to determine asset needs:

```
Output requirements → What files will Claude produce?
    ├─ Templates needed → assets/templates/
    │   ├─ Document templates → assets/templates/document-templates/
    │   ├─ Code templates → assets/templates/code-templates/
    │   └─ Configuration files → assets/templates/config-templates/
    │
    ├─ Static resources → assets/static/
    │   ├─ Images, logos → assets/static/images/
    │   ├─ Sample data → assets/static/samples/
    │   └─ Reference files → assets/static/references/
    │
    └─ No assets needed → Skip assets/ directory
```

**Asset Planning Questions:**
- What templates will users need for outputs?
- Are there sample files or reference materials?
- Do you need images, logos, or other static resources?
- What boilerplate code or configurations are commonly needed?

**Document planned assets:**
```markdown
Planned Assets:
- assets/templates/report-template.docx - Standard report format
- assets/static/samples/sample-data.json - Example data structure
- assets/templates/config-templates/ - Configuration file examples
```

### 1.2.4 Sketch Draft SKILL.md Structure

Create a rough outline of your SKILL.md:

```markdown
# [Skill Name]

## Overview
- Purpose: [What the skill does]
- When to use: [Trigger scenarios]
- Key capabilities: [Main features]

## Helper Scripts Available
- scripts/[script1].py - [Purpose and usage]
- scripts/[script2].py - [Purpose and usage]

## Core Workflow
1. [Main step 1]
2. [Main step 2]
3. [Main step 3]

## Common Scenarios
- Scenario 1: [Example use case]
- Scenario 2: [Example use case]

## Reference Files
- [references/file1.md] - [What it contains]
- [references/file2.md] - [What it contains]

## Assets
- [assets/template1] - [What it provides]
- [assets/static1] - [What it contains]
```

### 1.2.5 Create Draft Plan Document

Create a `draft-plan.md` file to document your planning:

```markdown
# [Skill Name] - Draft Plan

## Skill Overview
**Purpose:** [Brief description of what the skill does]
**Target Users:** [Who will use this skill]
**Key Triggers:** [When users would activate this skill]

## Identified Gaps (from Step 1.1)
- Information Gap: [What Claude doesn't know]
- Efficiency Gap: [What Claude rewrites repeatedly]
- Quality Gap: [What Claude skips or does poorly]

## Planned Resources

### Scripts
- `scripts/[name].py` - [Purpose, when to use, key parameters]
- `scripts/[name].py` - [Purpose, when to use, key parameters]

### References
- `references/[name].md` - [Content, when Claude needs it]
- `references/[name].md` - [Content, when Claude needs it]

### Assets
- `assets/[path]` - [What it provides, when to use]
- `assets/[path]` - [What it provides, when to use]

## SKILL.md Structure Draft
[Include your sketched structure from 1.2.4]

## Implementation Notes
- Key challenges: [What might be difficult]
- Dependencies: [What external resources are needed]
- Testing approach: [How to validate the skill works]
```

---

## Step 1.3: Extract Patterns from Examples

Before planning resources, search the examples/ folder for similar skills to identify proven patterns.

### Search Strategy

1. **Identify skill type**: Document processor, API integration, analysis workflow, or reference/guidelines
2. **Search examples/**: Look for similar skills in the examples/ directory
3. **Extract patterns**: Note which patterns apply to your skill
4. **Document findings**: Reference specific example files

### Example Searches

**For document processing skills:**
```bash
# Look for PDF, Excel, PowerPoint examples
ls examples/document-skills/
# Review: examples/document-skills/pdf/, examples/document-skills/xlsx/
```

**For API integration skills:**
```bash
# Look for MCP, API examples
ls examples/
# Review: examples/mcp-builder/
```

**For analysis workflows:**
```bash
# Look for analysis, calculation examples
ls examples/document-skills/
# Review: examples/document-skills/analyzing-financial-statements/
```

### Pattern Documentation

Document which patterns you found:
- **Script patterns**: How similar skills handle file processing
- **Reference patterns**: How they organize documentation
- **Asset patterns**: What templates or examples they provide
- **Workflow patterns**: How they structure the main process

**Example pattern extraction:**
```
Found in examples/document-skills/pdf/:
- Script pattern: Bundled scripts for deterministic operations
- Reference pattern: API docs in references/ folder
- Workflow pattern: Black box CLI with --help first

Found in examples/mcp-builder/:
- Progressive disclosure: Main workflow in SKILL.md, details in references/
- Script pattern: Validation and generation scripts
- Asset pattern: Template files for common patterns
```

---

## Step 2: Planning Resources - Extended Analysis

### Analysis Examples

**Example 1: PDF Editor**
- Query: "Help me rotate this PDF"
- Analysis: Rotating a PDF requires re-writing the same code each time
- **Solution**: `scripts/rotate_pdf.py` script stored in the skill

**Example 2: Frontend Webapp Builder**
- Queries: "Build me a todo app" or "Build me a dashboard to track my steps"
- Analysis: Writing a frontend webapp requires the same boilerplate HTML/React each time
- **Solution**: `assets/hello-world/` template containing boilerplate HTML/React project files

**Example 3: BigQuery Database Skill**
- Query: "How many users have logged in today?"
- Analysis: Querying BigQuery requires re-discovering table schemas and relationships each time
- **Solution**: `references/schema.md` file documenting table schemas

### Pattern Library Reference

**Consult the pattern library to guide your decisions:**

**For Document Processors:**
- See `references/patterns.md` - "Bundled Scripts Pattern"
- Example: `examples/document-skills/pdf/`
- When: Deterministic operations on files (rotate, merge, extract)

**For API Integrations:**
- See `references/patterns.md` - "Progressive Disclosure Pattern"
- Example: `examples/mcp-builder/`
- When: Complex API with extensive documentation

**For Analysis Workflows:**
- See `references/patterns.md` - "Validation Loop Pattern"
- Example: `examples/document-skills/analyzing-financial-statements/`
- When: Multi-step calculations with validation

**For Reference/Guidelines:**
- See `references/patterns.md` - "Template Asset Pattern"
- Example: `examples/document-skills/applying-brand-guidelines/`
- When: Organizational standards and branding

---

## Step 4: Extended Editing Guidance

### Start with Reusable Skill Contents

Begin implementation with the reusable resources identified in Step 2:

1. **Create scripts/** - Executable code for repeated operations
2. **Create references/** - Detailed documentation for Claude to reference
3. **Add assets/** - Templates, images, or files used in outputs

**Note:** This step may require user input. For example:
- Brand-guidelines skill: User provides brand assets and documentation
- Database skill: User provides schema definitions and access patterns
- API integration: User provides API credentials, endpoint documentation

**Important:** Delete example files and directories not needed for your skill. The template creates examples to demonstrate structure, but most skills won't need all of them.

### Update SKILL.md

Answer these questions to complete SKILL.md:

1. **What is the purpose of the skill?** (2-3 sentences)
2. **When should the skill be used?** (Include trigger terms)
3. **How should Claude use the skill?** (Reference all scripts/, references/, assets/)

### Best Practices Checklist

**Frontmatter Quality:**
- [ ] Name uses gerund form: "Processing PDFs" not "PDF Processor"
- [ ] Description is specific AND includes key trigger terms (< 1024 chars)
- [ ] Description states both WHAT the skill does and WHEN to use it
- [ ] Third-person voice: "This skill should be used when..." not "Use this skill when..."

**Writing Style:**
- [ ] Use imperative/infinitive form throughout (verb-first instructions)
- [ ] Example: "To accomplish X, do Y" not "You should do X"
- [ ] Objective, instructional tone
- [ ] Consistent terminology throughout

**Progressive Disclosure:**
- [ ] SKILL.md body < 500 lines (use references/ if larger)
- [ ] Main workflow in SKILL.md, details in references/
- [ ] Clear references to bundled resources with usage examples
- [ ] Scripts in scripts/ with documented usage
- [ ] Assets in assets/ (not loaded into context)

**Content Quality:**
- [ ] Examples provided for complex operations
- [ ] Clear, actionable guidance for Claude
- [ ] All placeholders from template replaced with real content
- [ ] References to bundled resources include file paths and usage

---

## Step 6: Extended Iteration Guidance

### Evaluation-Driven Iteration

Follow this systematic approach:
1. **Create Test Scenarios** - Use concrete examples from Step 1
2. **Test the Skill** - Load skill in fresh Claude instance
3. **Observe Patterns** - Where does Claude struggle or hesitate?
4. **Improve Systematically** - Address issues one at a time
5. **Re-validate** - Run full validation after improvements

### Multi-Model Testing Protocol

Test skill with all Claude models to ensure broad compatibility:

**Claude Haiku Testing:**
- Does the skill provide enough guidance?
- Are instructions clear without over-explaining?
- Does Haiku successfully complete basic tasks?
- Document any gaps in guidance

**Claude Sonnet Testing:**
- Is the skill clear and efficient?
- Does it provide appropriate detail without verbosity?
- Does Sonnet handle edge cases well?
- Note any confusion or hesitation

**Claude Opus Testing:**
- Does the skill avoid over-explaining?
- Is Opus able to infer unstated details?
- Does it handle complex scenarios well?
- Identify any unnecessary verbosity

### Iteration Checklist

After each iteration:
- [ ] Tested skill with 3+ realistic scenarios
- [ ] Validated all feedback from testing
- [ ] Re-ran validation after improvements
- [ ] Documented learnings (in README or changelog)
- [ ] Verified improvements don't introduce new issues
- [ ] Tested with at least 2 different Claude models
- [ ] Checked token count remains under target
- [ ] Confirmed all scripts execute successfully
