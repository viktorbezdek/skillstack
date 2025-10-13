# Degrees of Freedom: Matching Specificity to Task Fragility

Guide to calibrating how prescriptive your skill instructions should be.

## The Principle

**Match specificity to task fragility**:
- Fragile tasks = Low freedom (specific instructions)
- Robust tasks = High freedom (flexible guidance)
- Middle ground = Medium freedom (preferred patterns)

**Analogy**: Think of Claude as a robot exploring a path:
- **Narrow bridge with cliffs** (low freedom): One safe way forward
- **Open field** (high freedom): Many paths lead to success
- **Marked trail with options** (medium freedom): Recommended path, alternatives exist

## The Three Levels

### High Freedom: Text Instructions

**When to use**:
- Multiple valid approaches exist
- Decisions depend on context
- Heuristics guide the approach
- Judgment required
- Low risk if approach varies

**Language markers**:
- "Consider", "typically", "common approaches"
- Multiple examples showing variety
- Guidance on selection criteria
- No warnings or MUST statements
- Emphasis on principles over procedures

**Example - Data Analysis**:
```markdown
## Analyzing Data

Consider these approaches based on data type:
- **Numeric data**: Statistical methods (mean, median, std dev, distributions)
- **Categorical data**: Frequency analysis, cross-tabulation
- **Time series**: Trend analysis, seasonality detection
- **Mixed data**: Segment by category, then analyze numeric dimensions

Choose visualizations appropriate for insights:
- Distributions: histograms, box plots
- Relationships: scatter plots, correlation matrices
- Trends: line charts, area charts
- Comparisons: bar charts, grouped comparisons
```

**Why high freedom?**: Many valid ways to analyze data, depends on questions being asked and data characteristics. No single "correct" approach.

**Benefits**:
- Claude can apply judgment based on context
- Adapts to user's specific needs
- Encourages exploration and creativity
- Handles novel situations well

**Risks**:
- May be too vague for inexperienced users
- Could lead to inconsistent approaches
- Requires Claude to make judgment calls

### Medium Freedom: Scripts with Parameters

**When to use**:
- Preferred pattern exists
- Some variation acceptable
- Configuration affects behavior
- Standard approach with options
- Moderate risk if done incorrectly

**Language markers**:
- "Use X with these options"
- Documented parameters with defaults
- "For custom needs, modify Y"
- Escape hatches provided
- Recommended approach stated clearly

**Example - Report Generation**:
```markdown
## Generating Reports

Use the report generation script with configuration:

```bash
python scripts/generate_report.py \
  --data input.json \
  --template quarterly \
  --format pdf \
  --include-charts
```

**Parameters**:
- `--template`: quarterly, monthly, annual (required)
- `--format`: pdf, html, markdown (default: pdf)
- `--include-charts`: Add visualizations (optional)
- `--sections`: Comma-separated section list (optional)

**Template selection**:
- `quarterly`: Executive summary + KPIs + commentary
- `monthly`: Detailed metrics + charts
- `annual`: Comprehensive + comparisons + forecasts

For custom layouts, copy `assets/templates/custom_template.md` and modify.
```

**Why medium freedom?**: Standard tool exists with clear best practices, but parameters allow customization for different use cases.

**Benefits**:
- Clear recommended approach
- Flexibility for different scenarios
- Consistent baseline with room for variation
- Easy to follow for most cases

**Risks**:
- Users might not understand parameters
- Could choose suboptimal configuration
- Still requires some judgment

### Low Freedom: Specific Scripts

**When to use**:
- Operations are fragile/error-prone
- Consistency is critical
- Specific sequence required
- High risk of errors if varied
- Safety-critical operations

**Language markers**:
- ⚠️ Warning symbols
- "MUST", "Do not modify", "In exact order"
- Numbered sequential steps
- Explicit validation checkpoints
- No alternatives suggested
- Strict imperative voice

**Example - Database Migration**:
```markdown
## Database Migration Workflow

⚠️ **CRITICAL**: Execute steps in exact order. Do not skip validation.

```
Migration Checklist:
- [ ] Step 1: Backup database
- [ ] Step 2: Validate current schema
- [ ] Step 3: Run migration script
- [ ] Step 4: Verify migration success
- [ ] Step 5: Rollback if verification fails
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
python scripts/migrate.py --from v2 --to v3 --dry-run
```
Review output carefully. Then run actual migration:
```bash
python scripts/migrate.py --from v2 --to v3
```
⚠️ Do not modify command. Do not add flags.

**Step 4: Verify migration success**
```bash
python scripts/validate_schema.py --expected schema_v3.json
```
⚠️ **MUST return "OK"**. If validation fails, proceed immediately to Step 5.

**Step 5: Rollback if needed**
```bash
python scripts/restore_db.py --backup backup_YYYYMMDD.sql
```

⚠️ **Do NOT**:
- Skip validation steps
- Modify migration commands
- Proceed if validation fails
- Run migrations without backup
- Interrupt migration in progress
```

**Why low freedom?**: Database migrations are fragile, errors are costly, data loss risk is high. Must follow exact sequence with validation gates.

**Benefits**:
- Maximum safety and consistency
- Clear error prevention
- Explicit validation at each step
- Easy to audit and verify

**Risks**:
- Less flexible
- May feel overly restrictive
- Could be frustrating for experienced users
- Requires maintenance if process changes

## Calibration Examples

### Example 1: PDF Text Extraction

**Task fragility**: Low - well-established libraries, robust operation, low risk
**Freedom level**: High

```markdown
## Extracting Text

Use pdfplumber for text extraction:
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

For scanned PDFs requiring OCR, use pytesseract or cloud OCR services.
```

**Rationale**: Text extraction is straightforward, multiple approaches work, low risk of failure.

### Example 2: API Client Configuration

**Task fragility**: Medium - standard approach exists, some variation acceptable, moderate risk
**Freedom level**: Medium

```markdown
## Configuring API Client

Use the provided client with your API key:
```python
from api_client import APIClient

client = APIClient(
    api_key=os.environ['API_KEY'],
    timeout=30,  # Adjust for slow connections
    retry_count=3  # Standard for most cases
)
```

**Configuration options**:
- `timeout`: Request timeout in seconds (default: 30)
- `retry_count`: Number of retries (default: 3)
- `base_url`: Override API endpoint (rarely needed)

Most users should use defaults. Adjust timeout for slow networks.
```

**Rationale**: API configuration has best practices, but network conditions vary. Parameters allow customization while providing sensible defaults.

### Example 3: Production Deployment

**Task fragility**: High - errors impact users, rollback difficult, high risk
**Freedom level**: Low

```markdown
## Production Deployment

⚠️ **Follow exact sequence. Test in staging first.**

1. Run test suite: `make test-all`
   ⚠️ **ALL tests must pass**. Do not proceed if any fail.

2. Build production image: `make build-prod`
   ⚠️ **Verify build success**. Check for errors in output.

3. Deploy to production: `make deploy-prod`
   ⚠️ **Do not modify make targets**. Use exact command.

4. Health check: `make health-check-prod`
   ⚠️ **Must return 200 OK within 60 seconds**.

5. Monitor for 10 minutes: `make monitor-prod`
   ⚠️ **Watch for errors or anomalies**.

If ANY step fails: `make rollback-prod` immediately.
```

**Rationale**: Production deployments affect users, errors are costly, specific sequence required. No room for variation.

## Mixed Freedom in One Skill

Skills often need different levels for different tasks:

**Example - Data Processing Skill**:

### Data Exploration (High Freedom)
```markdown
## Exploring Data

Analyze data characteristics using appropriate methods:
- Statistical summaries for numeric columns (mean, median, distribution)
- Frequency analysis for categorical data
- Correlation analysis to find relationships
- Outlier detection (Z-score, IQR, or isolation forest)

Choose methods based on data type and analytical questions.
```

### Data Cleaning (Medium Freedom)
```markdown
## Cleaning Data

Use the cleaning pipeline with configuration:
```bash
python scripts/clean_data.py \
  --remove-duplicates \
  --handle-nulls mean \
  --outliers iqr
```

Options:
- `--handle-nulls`: mean, median, drop, forward-fill
- `--outliers`: iqr, zscore, none
- `--encoding`: utf-8, latin-1, auto (default: auto)

Recommended: Start with defaults, adjust based on data quality report.
```

### Data Export (Low Freedom)
```markdown
## Exporting Data

⚠️ Export to exact format required by downstream systems:
```bash
python scripts/export_data.py \
  --format warehouse \
  --validate
```
⚠️ Do not change format parameter. Validation must pass before export completes.

Downstream systems expect exact schema. Format variations will cause pipeline failures.
```

## Indicators for Each Level

### High Freedom Indicators
Use when instructions include:
- ✅ "Consider", "typically", "common approaches"
- ✅ Multiple examples showing variety
- ✅ Guidance on selection criteria
- ✅ No warnings or MUST statements
- ✅ Flexibility language ("adapt", "choose", "depending on")

### Medium Freedom Indicators
Use when instructions include:
- ✅ "Use X with these options"
- ✅ Documented parameters/configuration
- ✅ Recommended defaults stated
- ✅ Escape hatch: "For custom needs, modify Y"
- ✅ Options listed with explanations

### Low Freedom Indicators
Use when instructions include:
- ✅ ⚠️ Warning symbols
- ✅ "MUST", "Do not modify", "In exact order"
- ✅ Numbered sequential steps
- ✅ Explicit validation checkpoints
- ✅ No alternatives suggested
- ✅ Consequences stated ("will cause failure", "data loss risk")

## Anti-Patterns

### ❌ Wrong: Mixed Messages

```markdown
## Processing Data

⚠️ You MUST use this exact command, but feel free to adjust parameters as needed.
```

**Problem**: "MUST" (low freedom) contradicts "feel free" (high freedom). Confusing and inconsistent.

**Fix**: Choose one level:
```markdown
# Low freedom version:
⚠️ Use this exact command: `python process.py --strict`
Do not modify parameters.

# OR high freedom version:
Process data using approach appropriate for your data type.
Consider `python process.py` with parameters adjusted for your needs.
```

### ❌ Wrong: Low Freedom for Robust Tasks

```markdown
## Writing a Summary

⚠️ Follow exact structure:
1. First sentence must be exactly 20-25 words
2. Second paragraph must contain exactly 3 bullet points
3. Each bullet must be 10-15 words
4. Conclusion must be exactly 15 words
```

**Problem**: Summaries are robust tasks that don't need this level of specificity. Over-constrained.

**Fix**: Use high freedom:
```markdown
## Writing a Summary

Create a concise summary including:
- Key findings (2-4 sentences)
- Supporting evidence (bullet points or short paragraphs)
- Conclusion or recommendations

Adjust length and structure based on content complexity and audience needs.
```

### ❌ Wrong: High Freedom for Fragile Tasks

```markdown
## Database Migration

Generally speaking, migrations usually involve running some scripts and checking that things work. Consider backing up first if you think it's important. Then run whatever migration commands seem appropriate.
```

**Problem**: Migrations are fragile operations requiring specific sequence. Too much freedom leads to errors and data loss.

**Fix**: Use low freedom:
```markdown
## Database Migration

⚠️ **CRITICAL**: Follow exact sequence.

1. Backup: `python scripts/backup_db.py` (MUST complete)
2. Validate: `python scripts/validate.py` (MUST pass)
3. Migrate: `python scripts/migrate.py` (Do not modify)
4. Verify: `python scripts/verify.py` (MUST pass)

If verification fails, rollback immediately.
```

## Best Practices

### 1. Assess Fragility First

Ask yourself:
- **How badly can this go wrong?** (Low/Medium/High risk)
- **What's the cost of errors?** (Annoying / Costly / Catastrophic)
- **How many ways can it succeed?** (Many / Some / One)
- **Do variations matter?** (No / Sometimes / Always)

### 2. Match Specificity Appropriately

- **High fragility → Low freedom**: Specific steps, warnings, validation
- **Medium fragility → Medium freedom**: Recommended approach, options, defaults
- **Low fragility → High freedom**: Principles, examples, flexibility

### 3. Use Visual Markers Consistently

- **High freedom**: No special markers
- **Medium freedom**: "Recommended:", "Options:", defaults noted
- **Low freedom**: ⚠️ symbols, "MUST", numbered steps

### 4. Be Consistent Within Sections

Don't mix freedom levels within a single workflow. Each workflow section should maintain consistent freedom level.

### 5. Test Calibration

If Claude:
- **Hesitates or asks permission** → Too little freedom, increase flexibility
- **Makes errors or skips steps** → Too much freedom, add specificity
- **Follows perfectly** → Calibration is good

## Validation

The validation script checks for degrees of freedom consistency:

```bash
python scripts/validate_skill.py --full-check <skill-dir>
```

Checks for:
- ✅ Mixed messages (MUST + feel free)
- ✅ Missing warnings on low-freedom tasks
- ✅ Over-specification of high-freedom tasks
- ✅ Inconsistent freedom within sections

## Summary Table

| Aspect | High Freedom | Medium Freedom | Low Freedom |
|--------|-------------|----------------|-------------|
| **Risk** | Low | Medium | High |
| **Approaches** | Many valid | Preferred + alternatives | One correct way |
| **Language** | "Consider", "typically" | "Use X with options" | "MUST", "Do not modify" |
| **Examples** | Multiple varieties | Recommended + variations | Single exact example |
| **Warnings** | None | Optional | Required (⚠️) |
| **Validation** | User judgment | Recommended checks | Mandatory checkpoints |
| **Escape hatch** | Not needed (flexible) | Provided | None (strict) |

## Quick Decision Tree

```
Is the task fragile? (High error risk, costly mistakes, safety-critical)
├─ YES: Use LOW freedom
│   - Exact commands
│   - ⚠️ warnings
│   - Validation gates
│   - No alternatives
│
├─ SOMEWHAT: Use MEDIUM freedom
│   - Recommended approach
│   - Documented options
│   - Sensible defaults
│   - Escape hatch for custom needs
│
└─ NO: Use HIGH freedom
    - Principles and guidance
    - Multiple examples
    - Selection criteria
    - Flexibility emphasized
```

---

**Remember**: The goal is to give Claude the right amount of guidance—not too much (slow, rigid) and not too little (errors, inconsistency). Match specificity to task fragility.
