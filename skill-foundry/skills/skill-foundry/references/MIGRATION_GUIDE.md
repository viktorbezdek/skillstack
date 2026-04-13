# Migration Guide: Adopting Anthropic Best Practices

Guide for updating existing skills to latest best practices (October 2025).

## Overview

This guide helps you migrate existing skills to incorporate:
- Evaluation-Driven Development (EDD)
- Degrees of freedom calibration
- "Solve don't punt" error handling
- Multi-model testing
- Enhanced conciseness

## For Existing Skills

### Quick Assessment

Run these checks on your existing skill:

```bash
# 1. Check conciseness
python scripts/analyze_conciseness.py path/to/skill

# 2. Full validation
python scripts/validate_skill.py --full-check path/to/skill

# 3. Review token count
# Target: < 5000 tokens for SKILL.md
```

**Interpretation**:
- ✅ Concise: < 3000 tokens
- 🟡 Acceptable: 3000-5000 tokens
- ⚠️ Verbose: 5000-8000 tokens
- ❌ Excessive: > 8000 tokens

### Priority Updates

#### P0: Critical Quality Issues

These impact skill effectiveness significantly:

1. **Add error handling to scripts** (solve don't punt)
   - **Impact**: Prevents failures, improves reliability
   - **Time**: 1-2 hours
   - **Priority**: Do first

2. **Remove common concept definitions** (PDF, JSON, API)
   - **Impact**: Reduces token waste
   - **Time**: 15-30 minutes
   - **Priority**: Quick win

3. **Fix second-person voice** (use imperative form)
   - **Impact**: Improves instruction clarity
   - **Time**: 30-60 minutes
   - **Priority**: Quality improvement

#### P1: Significant Improvements

These improve skill quality and usability:

4. **Create test scenarios** (3-5 realistic examples)
   - **Impact**: Enables validation and iteration
   - **Time**: 1-2 hours
   - **Priority**: Foundation for EDD

5. **Add degrees of freedom markers** (⚠️ for low freedom)
   - **Impact**: Clarifies instruction specificity
   - **Time**: 30-60 minutes
   - **Priority**: Clarity improvement

6. **Implement progressive disclosure** (if > 500 lines)
   - **Impact**: Reduces cognitive load, improves token efficiency
   - **Time**: 2-3 hours
   - **Priority**: If skill is large

#### P2: Polish

These add final polish and completeness:

7. **Multi-model testing**
   - **Impact**: Ensures broad compatibility
   - **Time**: 1-2 hours
   - **Priority**: Before release

8. **Conciseness improvements**
   - **Impact**: Token efficiency
   - **Time**: 1-2 hours
   - **Priority**: Ongoing refinement

9. **Enhanced validation**
   - **Impact**: Catches quality issues early
   - **Time**: 15-30 minutes
   - **Priority**: Part of workflow

## Step-by-Step Migration

### 1. Create Test Scenarios

**From**: No explicit tests
**To**: 3-5 documented test scenarios

**Action**:

1. Review original examples from skill creation
2. Convert to concrete test scenarios with expected outcomes
3. Document in README or separate TEST_SCENARIOS.md
4. Run tests, measure baseline (success rate, time, questions)

**Example**:
```markdown
## Test Scenarios

### Scenario 1: Basic PDF Text Extraction
**Task**: "Extract all text from invoice.pdf"
**Expected**: Text extracted, formatted cleanly
**Success criteria**: Complete extraction, < 1 minute

### Scenario 2: Multi-page Processing
**Task**: "Extract text from all pages in report.pdf"
**Expected**: All pages processed, organized by page
**Success criteria**: All pages included, proper ordering

### Scenario 3: Error Handling
**Task**: "Extract text from nonexistent.pdf"
**Expected**: Helpful error message
**Success criteria**: Graceful failure, recovery guidance
```

**Validation**: Run scenarios, document baseline metrics

---

### 2. Trim Verbose Content

**From**: Explanatory content, excessive examples
**To**: Minimal, actionable guidance

**Action**:

1. Run `scripts/analyze_conciseness.py path/to/skill`
2. Review sections flagged as verbose
3. Remove common concept definitions (PDF, JSON, API, CSV, etc.)
4. Cut hedge words (basically, essentially, typically, generally)
5. Consolidate or remove excessive examples (keep 1-2 best)
6. Remove long parenthetical definitions
7. Target < 5000 tokens (ideally < 3000)

**Before**:
```markdown
## Extracting Text from PDFs

PDF (Portable Document Format) is a common file format for documents.
There are many libraries available for PDF processing in Python.
Typically, you can use pdfplumber for text extraction because it's
generally more reliable than other options, although PyPDF2 is also
basically good for simple cases. You should consider your use case...
```

**After**:
```markdown
## Extracting Text

Use pdfplumber for text extraction:
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
```

**Validation**: Re-run `scripts/analyze_conciseness.py`, verify token reduction

---

### 3. Update Scripts to Solve Not Punt

**From**: Basic or missing error handling
**To**: Comprehensive error handling with fallbacks

**Action**:

1. Add try/except to all file operations
2. Catch specific exceptions (not bare `except:`)
3. Provide helpful error messages with emojis (❌, 💡)
4. Include recovery guidance
5. Provide sensible fallback behavior (defaults, retries)
6. Test error scenarios

**Before**:
```python
def load_data(path):
    return json.load(open(path))
```

**After**:
```python
def load_data(path):
    """Load JSON data with comprehensive error handling."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ File not found: {path}")
        print("💡 Check the file path is correct")
        return {}  # Sensible default
    except PermissionError:
        print(f"❌ Cannot access: {path}")
        print("💡 Check file permissions")
        return {}
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in: {path}")
        print(f"💡 Error at line {e.lineno}: {e.msg}")
        return {}
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("💡 Contact support if issue persists")
        return {}
```

**Additional improvements**:
- Document "magic numbers" with comments explaining choices
- Single responsibility per script
- Clear usage examples

**Validation**: Test error scenarios, verify helpful messages

---

### 4. Add Degrees of Freedom Markers

**From**: Implicit specificity levels
**To**: Explicit freedom markers

**Action**:

1. Identify fragile operations (database migrations, deployments, data modifications)
2. Add ⚠️ warnings to low-freedom (fragile) tasks
3. Use "Consider" / "typically" language for high-freedom tasks
4. Document parameters and options for medium-freedom tasks
5. Ensure consistency within each workflow section

**Low Freedom Example** (fragile operations):
```markdown
## Database Migration

⚠️ **CRITICAL**: Execute steps in exact order.

1. Backup: `python scripts/backup_db.py`
   ⚠️ **MUST complete** before proceeding

2. Validate: `python scripts/validate_schema.py`
   ⚠️ **MUST return OK**

3. Migrate: `python scripts/migrate.py --from v2 --to v3`
   ⚠️ Do not modify command
```

**Medium Freedom Example** (scripts with parameters):
```markdown
## Generating Reports

Use the report script with configuration:
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
```

**High Freedom Example** (flexible guidance):
```markdown
## Analyzing Data

Consider these approaches based on data type:
- **Numeric data**: Statistical methods (mean, median, distributions)
- **Categorical data**: Frequency analysis, cross-tabulation
- **Time series**: Trend analysis, seasonality detection

Choose visualizations appropriate for insights.
```

**Validation**: Run `scripts/validate_skill.py`, check for mixed messages

---

### 5. Implement Progressive Disclosure

**From**: One large SKILL.md (> 500 lines)
**To**: SKILL.md (< 500 lines) + references/

**Action**:

1. Identify candidate content for extraction:
   - API reference documentation
   - Detailed technical specifications
   - Advanced usage patterns
   - Extensive examples

2. Create references/ directory structure:
   ```
   skill-name/
   ├── SKILL.md              # Main workflow (< 500 lines)
   ├── references/
   │   ├── api_reference.md  # API details
   │   ├── advanced.md       # Advanced patterns
   │   └── examples.md       # Extended examples
   ```

3. Move detailed content to references/

4. Add clear references from SKILL.md:
   ```markdown
   For complete API reference, see `references/api_reference.md`.
   ```

5. Keep workflow and common patterns in SKILL.md

**Before** (800 lines in SKILL.md):
```markdown
## API Endpoints

### GET /users
Returns list of users...
[50 lines of API docs]

### POST /users
Creates new user...
[50 lines of API docs]

[... 700 more lines ...]
```

**After** (250 lines in SKILL.md):
```markdown
## Using the API

Use the provided API client:
```python
from api_client import APIClient
client = APIClient(api_key=os.environ['API_KEY'])
users = client.get_users()
```

For complete API reference, see `references/api_reference.md`.
```

**Validation**: Check SKILL.md < 500 lines, references linked correctly

---

### 6. Multi-Model Testing

**From**: Single model testing or no testing
**To**: Testing with Haiku, Sonnet, and Opus

**Action**:

1. Test with Claude Haiku:
   - **Question**: Does the skill provide enough guidance?
   - **Look for**: Haiku asking unnecessary questions, struggling with tasks
   - **If issues**: Add more examples, clarify ambiguous instructions

2. Test with Claude Sonnet:
   - **Question**: Is the skill clear and efficient?
   - **Look for**: Smooth completion, reasonable token usage
   - **If issues**: Core skill problems (typical target model)

3. Test with Claude Opus:
   - **Question**: Does the skill avoid over-explaining?
   - **Look for**: Opus slowed by verbose instructions
   - **If issues**: Reduce verbosity, increase freedom

4. Document model-specific notes (if needed):
   ```markdown
   ## Model Compatibility

   - **Haiku**: May need explicit library reminder
   - **Sonnet**: Optimal performance
   - **Opus**: Can infer best approach, reminders optional
   ```

**Validation**: All models achieve >90% success rate

---

## Validation

After each update:

```bash
python scripts/validate_skill.py --full-check path/to/skill
```

**Check for**:
- ✅ Conciseness (< 5000 tokens)
- ✅ Degrees of freedom consistency
- ✅ Script error handling quality
- ✅ Evaluation references
- ✅ No verbosity patterns
- ✅ Imperative voice

---

## FAQ

### Q: Do I need to migrate all skills immediately?

**A**: No. Prioritize:
1. Heavily-used skills first
2. Skills with known quality issues
3. Skills being actively developed
4. New skills follow new practices from the start

### Q: What if my skill is working well?

**A**: If it passes validation with no warnings and has good test coverage, migration is optional. Focus on new skills following best practices.

### Q: How long does migration take?

**A**: Depends on skill size and current state:
- **Small skills** (<200 lines): 1-2 hours
- **Medium skills** (200-500 lines): 2-4 hours
- **Large skills** (>500 lines): 4-8 hours
- Add 1-2 hours for comprehensive testing

### Q: Can I migrate incrementally?

**A**: Yes! Recommended approach:
- **Week 1**: P0 items (error handling, verbosity, voice)
- **Week 2**: P1 items (test scenarios, degrees of freedom, progressive disclosure)
- **Week 3**: P2 items (multi-model testing, final polish)

Each phase improves quality independently.

### Q: What if validation shows many warnings?

**A**: Prioritize by impact:
1. Critical errors (must fix before use)
2. Quality warnings (P0 and P1 items)
3. Polish warnings (P2 items)

Focus on high-impact, low-effort improvements first.

### Q: Should I rewrite or incrementally update?

**A**:
- **Incremental**: If skill is generally good, just needs polish
- **Rewrite**: If skill has fundamental issues or is very verbose (>1000 lines)
- **Hybrid**: Rewrite problem sections, update the rest

### Q: How do I know when migration is complete?

**A**: When you achieve:
- ✅ `validate_skill.py --full-check` passes with no critical warnings
- ✅ 3-5 test scenarios documented and passing
- ✅ Success rate >90% across test scenarios
- ✅ Token count < 5000 (ideally < 3000)
- ✅ Multi-model testing passed

---

## Getting Help

### Resources

- **EDD Guide**: `references/evaluation_driven_development.md`
- **Degrees of Freedom**: `references/degrees_of_freedom.md`
- **Best Practices**: `references/best_practices_checklist.md`

### Validation Scripts

- **Conciseness**: `python scripts/analyze_conciseness.py <skill-dir>`
- **Full check**: `python scripts/validate_skill.py --full-check <skill-dir>`

### Common Issues

**Issue**: Skill has >8000 tokens
**Solution**: Use progressive disclosure, move details to references/

**Issue**: Tests failing after migration
**Solution**: Review test scenarios, may need to adjust skill or tests

**Issue**: Mixed freedom signals warning
**Solution**: Separate workflows by freedom level, be consistent within sections

**Issue**: Scripts punting to Claude
**Solution**: Add comprehensive try/except, provide fallback behavior

---

## Migration Checklist

Use this checklist to track migration progress:

```markdown
## Migration Progress

### P0: Critical Quality Issues
- [ ] Added error handling to all scripts
- [ ] Removed common concept definitions
- [ ] Fixed second-person voice instances
- [ ] Ran validation, addressed critical warnings

### P1: Significant Improvements
- [ ] Created 3-5 test scenarios
- [ ] Documented baseline metrics
- [ ] Added degrees of freedom markers (⚠️ for low freedom)
- [ ] Implemented progressive disclosure (if > 500 lines)
- [ ] Ran validation, addressed major warnings

### P2: Polish
- [ ] Tested with Haiku (sufficient guidance?)
- [ ] Tested with Sonnet (efficient?)
- [ ] Tested with Opus (not over-explained?)
- [ ] Applied conciseness improvements
- [ ] Ran final validation
- [ ] Documented model-specific notes (if needed)

### Final Validation
- [ ] All test scenarios pass (>90% success)
- [ ] Token count < 5000
- [ ] `validate_skill.py --full-check` passes
- [ ] Multi-model testing complete
```

---

## Next Steps

1. **Assess** your skill with validation scripts
2. **Prioritize** updates based on P0/P1/P2 framework
3. **Migrate** incrementally, validating after each change
4. **Test** with realistic scenarios across models
5. **Document** learnings for future skills

Good luck with your migration! Remember: incremental improvements are valuable. You don't need to achieve perfection immediately.
