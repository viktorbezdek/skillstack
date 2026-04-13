# Detailed Editing Guidance

## Best Practices Checklist

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

## Script Quality: "Solve, Don't Punt" Pattern

When creating scripts for your skill, follow the "solve, don't punt" principle: scripts must handle errors explicitly with fallbacks rather than punting to Claude.

**Core Principle**: Scripts should be robust enough to handle common errors gracefully, providing helpful feedback and sensible defaults rather than crashing and leaving Claude to figure out what went wrong.

**❌ Bad: Punt to Claude**
```python
def process_file(path):
    # Let Claude figure out what went wrong
    return open(path).read()
```

Problems with punting:
- Script crashes with cryptic error
- Claude has to generate error-handling code
- Inconsistent behavior across runs
- Wastes tokens on error recovery

**✅ Good: Solve with Explicit Handling**
```python
def process_file(path):
    """Process file with comprehensive error handling."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {path}")
        print("💡 Check the file path is correct")
        return ''  # Sensible default
    except PermissionError:
        print(f"❌ Cannot access: {path}")
        print("💡 Check file permissions")
        return ''
    except UnicodeDecodeError:
        print(f"❌ Encoding error: {path}")
        print("💡 Trying alternative encoding...")
        try:
            with open(path, 'r', encoding='latin-1') as f:
                return f.read()
        except Exception:
            return ''
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return ''
```

Benefits of solving:
- Clear error messages guide users
- Fallback behavior keeps workflow moving
- Consistent, predictable behavior
- No token waste on error handling

**Error Handling Checklist**:
- [ ] All file operations wrapped in try/except
- [ ] Specific exceptions caught (not bare `except:`)
- [ ] Helpful error messages for each exception
- [ ] Recovery guidance provided ("Check file path", "Verify permissions")
- [ ] Sensible fallback behavior (defaults, retries, alternatives)
- [ ] No silent failures

**Example Error Messages**:
```python
# ✅ Good: Helpful and actionable
print(f"❌ File not found: {path}")
print("💡 Check the file path is correct")

# ❌ Bad: Generic and unhelpful
print("Error occurred")

# ❌ Bad: Technical jargon
print(f"FileNotFoundError: [Errno 2] No such file or directory: '{path}'")
```

## Degrees of Freedom Calibration

Match the level of specificity in your instructions to the task's fragility:

### High Freedom - Text Instructions

When to use:
- Multiple valid approaches exist
- Decisions depend on context
- Heuristics guide the approach
- Judgment required

Language markers:
- "Consider", "typically", "common approaches"
- Multiple examples showing variety
- Guidance on selection criteria
- No warnings or MUST statements

Example:
```markdown
## Analyzing Data

Consider these approaches based on data type:
- **Numeric data**: Statistical methods (mean, median, distributions)
- **Categorical data**: Frequency analysis, cross-tabulation
- **Time series**: Trend analysis, seasonality detection

Choose visualizations appropriate for insights:
- Distributions: histograms, box plots
- Relationships: scatter plots, correlation matrices
- Trends: line charts, area charts
```

### Medium Freedom - Scripts with Parameters

When to use:
- Preferred pattern exists
- Some variation acceptable
- Configuration affects behavior
- Standard approach with options

Language markers:
- "Use X with these options"
- Documented parameters with defaults
- "For custom needs, modify Y"
- Escape hatches provided

Example:
```markdown
## Generating Reports

Use the report generation script with configuration:
```bash
python scripts/generate_report.py \
  --template quarterly \
  --format pdf \
  --include-charts
```

**Parameters**:
- `--template`: quarterly, monthly, annual (required)
- `--format`: pdf, html, markdown (default: pdf)
- `--include-charts`: Add visualizations (optional)

For custom layouts, copy `assets/templates/custom_template.md` and modify.
```

### Low Freedom - Specific Scripts

When to use:
- Operations are fragile/error-prone
- Consistency is critical
- Specific sequence required
- High risk of errors if varied

Language markers:
- ⚠️ Warning symbols
- "MUST", "Do not modify", "In exact order"
- Numbered sequential steps
- Explicit validation checkpoints
- No alternatives suggested

Example:
```markdown
## Database Migration Workflow

⚠️ **CRITICAL**: Execute steps in exact order. Do not skip validation.

```
Migration Checklist:
- [ ] Step 1: Backup database
- [ ] Step 2: Validate current schema
- [ ] Step 3: Run migration script
- [ ] Step 4: Verify migration success
```

**Step 1: Backup database**
```bash
python scripts/backup_db.py --output backup_$(date +%Y%m%d).sql
```
⚠️ **MUST complete before proceeding**. Verify backup file exists.

**Step 2: Validate current schema**
```bash
python scripts/validate_schema.py --expected schema_v2.json
```
⚠️ **MUST return "OK"**. If validation fails, DO NOT proceed.

**Step 3: Run migration script**
```bash
python scripts/migrate.py --from v2 --to v3
```
⚠️ Do not modify command. Do not add flags.
```

**Calibration Checklist**:
- [ ] Assessed task fragility (low/medium/high risk)
- [ ] Matched instruction specificity to fragility
- [ ] Used appropriate language markers (consider/use/MUST)
- [ ] Consistent freedom level within each workflow section
- [ ] Added ⚠️ warnings for low-freedom critical operations

## Navigation

- [Back to main SKILL.md](../SKILL.md)
- [Core Principles](core_principles.md)
- [Progressive Disclosure](progressive_disclosure.md)
