# Skill Design Patterns

This document describes common patterns extracted from high-quality Claude Code skills. Use these patterns to guide your skill design decisions.

---

## Pattern 1: Progressive Disclosure

**When to use:** Skills with extensive documentation (> 500 lines)

**Problem:** Large SKILL.md files consume too many tokens and reduce context efficiency.

**Solution:** Keep SKILL.md lean with overview and workflow, move detailed documentation to reference files.

### Structure

```
skill-name/
├── SKILL.md              # Overview and main workflow (< 500 lines)
├── REFERENCE.md          # Detailed API reference
├── EXAMPLES.md           # Usage examples
└── references/           # Domain-specific documentation
    ├── domain_a.md
    ├── domain_b.md
    └── domain_c.md
```

### SKILL.md Pattern

````markdown
# Main Skill

## Quick Start
Brief getting started guide

## Features
- Feature 1 → See [REFERENCE.md](REFERENCE.md#feature-1)
- Feature 2 → See [REFERENCE.md](REFERENCE.md#feature-2)

## Examples
See [EXAMPLES.md](EXAMPLES.md) for usage examples
````

### Benefits

- **Token efficiency**: Only load what's needed
- **Better organization**: Clear separation of concerns
- **Easier maintenance**: Update references without touching main workflow
- **Scalability**: Add domains without bloating SKILL.md

### Examples from Repository

- **document-skills/pdf/**: SKILL.md references FORMS.md and REFERENCE.md
- **mcp-builder/**: SKILL.md references extensive reference/ directory

---

## Pattern 2: Bundled Scripts

**When to use:** Deterministic operations that are repeatedly rewritten

**Problem:** Same code gets generated over and over, wasting tokens and introducing inconsistency.

**Solution:** Bundle pre-written, tested scripts in the skill.

### Structure

```
skill-name/
├── SKILL.md
└── scripts/
    ├── process.py        # Main processing script
    ├── validate.py       # Validation utility
    └── helpers.py        # Shared helper functions
```

### SKILL.md Pattern

````markdown
## Processing Workflow

1. Analyze input:
   ```bash
   python scripts/process.py input.pdf
   ```

2. Validate results:
   ```bash
   python scripts/validate.py output.json
   ```
````

### Script Design Principles

**1. Single Responsibility**: Each script does one thing well

**2. Clear Interfaces**: Well-defined inputs and outputs
```python
def process_file(input_path: str, output_path: str) -> dict:
    """Process file and return results."""
    pass
```

**3. Error Handling**: Graceful failures with clear messages
```python
try:
    result = process(file)
except FileNotFoundError:
    print(f"❌ File not found: {file}")
    print("💡 Verify file path is correct")
    sys.exit(1)
```

**4. Documentation**: Clear docstrings and usage examples

### Benefits

- **Reliability**: Tested code instead of AI-generated
- **Token efficiency**: Execute without loading into context
- **Consistency**: Same results every time
- **Speed**: No code generation time

### Examples from Repository

- **document-skills/pdf/**: Scripts for PDF rotation, merging
- **analyzing-financial-statements/**: Scripts for ratio calculations

---

## Pattern 3: Validation Loop

**When to use:** Multi-step workflows with potential errors

**Problem:** Errors in early steps cascade through the workflow.

**Solution:** Validate after each step before proceeding.

### Workflow Pattern

```markdown
## Workflow with Validation

1. **Step 1**: Execute operation
   ```bash
   python scripts/step1.py input.json > intermediate.json
   ```

2. **Validate Step 1**:
   ```bash
   python scripts/validate.py intermediate.json
   ```
   ⚠️ **Only proceed if validation passes**

3. **Step 2**: Next operation
   ```bash
   python scripts/step2.py intermediate.json > output.json
   ```

4. **Final Validation**:
   ```bash
   python scripts/validate.py output.json --final
   ```
```

### Validation Script Pattern

```python
def validate(data: dict) -> tuple[bool, list[str]]:
    """Validate data and return (is_valid, error_messages)."""
    errors = []

    # Check required fields
    if 'required_field' not in data:
        errors.append("Missing required field: required_field")

    # Check data types
    if not isinstance(data.get('value'), int):
        errors.append("Field 'value' must be an integer")

    # Check business rules
    if data.get('value', 0) < 0:
        errors.append("Field 'value' must be non-negative")

    return len(errors) == 0, errors
```

### Benefits

- **Early error detection**: Catch problems before they propagate
- **Clear error messages**: Know exactly what to fix
- **Safer workflows**: Validation gates prevent invalid states
- **Better debugging**: Isolate which step failed

### Examples from Repository

- **analyzing-financial-statements/**: Validates financial data before calculations
- **mcp-builder/**: Validates API responses before proceeding

---

## Pattern 4: Template Assets

**When to use:** Generating output with consistent formatting/structure

**Problem:** Starting from scratch every time leads to inconsistency.

**Solution:** Bundle template files that Claude can customize.

### Structure

```
skill-name/
├── SKILL.md
└── assets/
    ├── template.xlsx      # Excel template
    ├── slide-deck.pptx    # PowerPoint template
    └── boilerplate/       # Code boilerplate
        ├── index.html
        └── styles.css
```

### SKILL.md Pattern

```markdown
## Creating Output

Use the provided template as a starting point:

1. Copy template: `cp assets/template.xlsx output.xlsx`
2. Customize with user data
3. Apply formatting and calculations
4. Save final output

Template includes:
- Pre-formatted headers
- Standard color scheme
- Common formulas
- Chart templates
```

### Template Design Principles

**1. Minimal but Complete**: Include essential structure, not every detail

**2. Clearly Marked Placeholders**:
```
{{COMPANY_NAME}}
{{REPORT_DATE}}
{{DATA_TABLE}}
```

**3. Example Content**: Show what finished output looks like

**4. Documentation**: Include comments explaining customization points

### Benefits

- **Consistency**: All outputs follow same structure
- **Speed**: Start from working template vs. blank file
- **Quality**: Pre-formatted, tested templates
- **Branding**: Embed organizational standards

### Examples from Repository

- **applying-brand-guidelines/**: Corporate branding templates
- **document-skills/**: Document templates with standard formatting

---

## Pattern 5: Domain Organization

**When to use:** Skills covering multiple domains or subject areas

**Problem:** One giant reference file is hard to navigate and loads unnecessary context.

**Solution**: Organize references by domain, load only what's needed.

### Structure

```
skill-name/
├── SKILL.md
└── references/
    ├── finance.md       # Finance domain
    ├── sales.md         # Sales domain
    ├── product.md       # Product domain
    └── marketing.md     # Marketing domain
```

### SKILL.MD Pattern

```markdown
## Available Domains

**Finance**: Revenue, ARR, billing → See [references/finance.md](references/finance.md)
**Sales**: Opportunities, pipeline → See [references/sales.md](references/sales.md)
**Product**: Features, usage → See [references/product.md](references/product.md)
**Marketing**: Campaigns, attribution → See [references/marketing.md](references/marketing.md)

## Finding Information

Use grep to search across domains:
```bash
grep -i "revenue" references/finance.md
grep -i "pipeline" references/sales.md
```
````

### Reference File Pattern

Each domain file follows consistent structure:

```markdown
# Finance Domain

## Overview
Brief description of what this domain covers

## Key Concepts
- Concept 1: Definition
- Concept 2: Definition

## Data Models
### Revenue
- field1: description
- field2: description

## Common Queries
Examples of typical queries for this domain
```

### Benefits

- **Focused loading**: Load only relevant domain
- **Clear organization**: Easy to find information
- **Parallel development**: Different people can work on different domains
- **Scalability**: Add domains without affecting others

### Examples from Repository

- **mcp-builder/**: Organized by API functionality areas

---

## Pattern 6: Workflow Checklist

**When to use:** Complex multi-step workflows where steps might be missed

**Problem:** Users skip critical steps or do them out of order.

**Solution:** Provide copy-paste checklists Claude can track.

### SKILL.md Pattern

````markdown
## Workflow

Copy this checklist and check off items as you complete them:

```
Task Progress:
- [ ] Step 1: Analyze the input
- [ ] Step 2: Validate input format
- [ ] Step 3: Process data
- [ ] Step 4: Generate output
- [ ] Step 5: Verify results
```

**Step 1: Analyze the input**
Run: `python scripts/analyze.py input.json`
Review the output for any warnings

**Step 2: Validate input format**
Run: `python scripts/validate.py input.json`
Fix any errors before continuing

**Step 3: Process data**
Run: `python scripts/process.py input.json output.json`

**Step 4: Generate output**
Run: `python scripts/generate.py output.json final.xlsx`

**Step 5: Verify results**
Run: `python scripts/verify.py final.xlsx`
If verification fails, return to Step 3
````

### Benefits

- **Progress tracking**: Clear view of what's done
- **Order enforcement**: Steps numbered and sequential
- **Error prevention**: Explicit validation steps
- **Communication**: Easy to share status

### Examples from Repository

- Referenced in Anthropic's best practices for complex workflows

---

## Pattern Selection Guide

| Your Need | Recommended Pattern | Example |
|-----------|---------------------|---------|
| Large documentation | Progressive Disclosure | mcp-builder |
| Repeated code operations | Bundled Scripts | pdf processing |
| Multi-step with validation | Validation Loop | financial analysis |
| Consistent output format | Template Assets | brand guidelines |
| Multiple subject areas | Domain Organization | database skills |
| Complex workflow | Workflow Checklist | multi-step processes |

---

## Combining Patterns

Patterns work together. A typical high-quality skill might use:

1. **Progressive Disclosure** - Keep SKILL.md lean
2. **Bundled Scripts** - For deterministic operations
3. **Validation Loop** - In the workflow
4. **Template Assets** - For consistent output
5. **Domain Organization** - If covering multiple areas

Example combining all:

```
financial-analyzer/
├── SKILL.md                  # Progressive Disclosure: overview only
├── references/
│   ├── metrics.md            # Domain Organization: different domains
│   ├── ratios.md
│   └── valuation.md
├── scripts/
│   ├── calculate.py          # Bundled Scripts: tested calculations
│   ├── validate.py           # Validation Loop: validation script
│   └── helpers.py
└── assets/
    └── report_template.xlsx  # Template Assets: consistent output
```

---

## Anti-Patterns to Avoid

### ❌ Mega SKILL.md

**Problem**: Everything in one huge SKILL.md file

**Solution**: Use Progressive Disclosure

### ❌ No Scripts for Repeated Code

**Problem**: AI generates the same code every time

**Solution**: Bundle Scripts

### ❌ No Validation in Workflows

**Problem**: Errors cascade through steps

**Solution**: Validation Loop

### ❌ Inconsistent Output

**Problem**: Every output looks different

**Solution**: Template Assets

### ❌ One Giant Reference File

**Problem**: Load entire reference for small query

**Solution**: Domain Organization

---

## Next Steps

1. **Identify your patterns**: Which patterns fit your skill?
2. **Review examples**: Study similar skills in `examples/`
3. **Start simple**: Begin with one or two patterns
4. **Iterate**: Add patterns as skill grows
5. **Validate**: Use `validate_skill.py` to check quality
