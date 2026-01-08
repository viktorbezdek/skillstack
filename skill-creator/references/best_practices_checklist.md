# Skill Best Practices Checklist

Comprehensive checklist of best practices extracted from Anthropic's official skill-authoring guidelines.

---

## Core Principles

### ✅ Conciseness is Key

- [ ] SKILL.md body is under 500 lines
- [ ] Uses progressive disclosure for larger skills
- [ ] Assumes Claude already knows common concepts
- [ ] Only includes information Claude doesn't already have
- [ ] Challenges each piece of information: "Does Claude really need this?"
- [ ] Total tokens < 5000 for SKILL.md
- [ ] Ran `python scripts/analyze_conciseness.py` and addressed feedback
- [ ] Removed common concept definitions (PDF, JSON, API, CSV, etc.)
- [ ] Cut hedge words (basically, essentially, typically, generally)
- [ ] Consolidated or removed excessive examples
- [ ] No long parenthetical definitions

**Example:**
````markdown
<!-- ✅ Good: Concise (50 tokens) -->
## Extract PDF text

Use pdfplumber for text extraction:
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

<!-- ❌ Bad: Too verbose (150 tokens) -->
## Extract PDF text

PDF (Portable Document Format) files are a common file format...
There are many libraries available... we recommend pdfplumber because...
````

**Tools**:
- `python scripts/analyze_conciseness.py <skill-dir>` - Token analysis by section
- `python scripts/validate_skill.py --full-check <skill-dir>` - Verbosity detection

---

## Evaluation-Driven Development

### ✅ EDD Cycle

- [ ] Created 3-5 test scenarios from concrete examples
- [ ] Ran baseline tests WITHOUT skill (documented gaps)
- [ ] Categorized gaps: information, efficiency, quality
- [ ] Added ONLY minimal documentation addressing identified gaps
- [ ] Re-tested after each addition
- [ ] Stopped adding content when scenarios pass consistently (>90% success)
- [ ] Documented test scenarios for regression testing
- [ ] Measured improvements: success rate, time, questions asked

### ✅ Gap Analysis

- [ ] **Information gaps**: Documented what Claude doesn't know (library/tool choice)
- [ ] **Efficiency gaps**: Identified repeated code (candidates for scripts)
- [ ] **Quality gaps**: Found missing validation or error handling
- [ ] Prioritized gaps by impact on success rate
- [ ] Addressed gaps systematically, one at a time

### ✅ Minimal Documentation

- [ ] One-line guidance for information gaps
- [ ] Bundled scripts for efficiency gaps
- [ ] Validation workflows for quality gaps
- [ ] No hypothetical features or "nice to have" content
- [ ] No documentation for edge cases not seen in testing

**Reference**: See `references/evaluation_driven_development.md` for complete methodology

---

## Naming Conventions

### ✅ Skill Naming

- [ ] Uses gerund form: "Processing PDFs" not "PDF Processor"
- [ ] Clear and descriptive
- [ ] Consistent with other skills in collection
- [ ] Avoids vague names like "Helper", "Utils", "Tools"

**Examples:**
- ✅ "Processing PDFs"
- ✅ "Analyzing spreadsheets"
- ✅ "Managing databases"
- ✅ "Testing code"
- ❌ "PDF Helper"
- ❌ "Utils"
- ❌ "Documents"

###✅ File Naming

- [ ] Lowercase with hyphens: `my-skill` not `My_Skill` or `MySkill`
- [ ] Max 64 characters for skill name
- [ ] Descriptive filenames: `form_validation_rules.md` not `doc2.md`

---

## Description Writing

### ✅ Description Quality

- [ ] Under 1024 characters
- [ ] Includes WHAT the skill does
- [ ] Includes WHEN to use it (trigger terms)
- [ ] Third-person voice ("This skill..." not "You can...")
- [ ] Specific, not vague
- [ ] Includes key terms for discoverability

**Template:**
```
[WHAT]: [Action] [Object] [specific features].
[WHEN]: Use when [trigger scenario] or when the user mentions [keywords].
```

**Examples:**
````markdown
<!-- ✅ Good: Specific with triggers -->
description: Extract text and tables from PDF files, fill forms, merge documents.
Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.

<!-- ✅ Good: Clear triggers -->
description: Analyze Excel spreadsheets, create pivot tables, generate charts.
Use when analyzing Excel files, spreadsheets, tabular data, or .xlsx files.

<!-- ❌ Bad: Vague -->
description: Helps with documents

<!-- ❌ Bad: Second person -->
description: You can use this to process Excel files
````

---

## Progressive Disclosure

### ✅ File Organization

- [ ] SKILL.md contains overview and main workflow
- [ ] Detailed documentation in REFERENCE.md or references/
- [ ] Scripts in scripts/ with clear usage
- [ ] Assets in assets/ (not loaded into context)
- [ ] File references are one level deep (not deeply nested)

**Pattern:**
```
skill-name/
├── SKILL.md              # Main instructions (< 500 lines)
├── REFERENCE.md          # API reference (loaded as needed)
├── EXAMPLES.md           # Usage examples
└── references/
    ├── domain_a.md       # Domain-specific details
    └── domain_b.md
```

### ✅ Reference Files

- [ ] Include table of contents for files > 100 lines
- [ ] Referenced directly from SKILL.md (one level deep)
- [ ] Organized by domain for multi-domain skills
- [ ] Include grep search patterns for large files

---

## Writing Style

### ✅ Voice and Tone

- [ ] Imperative/infinitive form: "To do X, do Y"
- [ ] NOT second person: "You should do X"
- [ ] Objective, instructional language
- [ ] Consistent terminology throughout

**Examples:**
````markdown
<!-- ✅ Good: Imperative -->
To extract text from PDFs, use pdfplumber.
Run the script with: `python process.py input.pdf`

<!-- ❌ Bad: Second person -->
You should use pdfplumber to extract text.
You can run the script like this...
````

### ✅ Consistency

- [ ] One term per concept (not "API endpoint", "URL", "route" interchangeably)
- [ ] Consistent formatting for code, commands, file paths
- [ ] Consistent section structure across similar skills

---

## Content Quality

### ✅ Examples and Code

- [ ] Provides concrete examples for complex operations
- [ ] Code examples are complete and runnable
- [ ] Examples show both input and expected output
- [ ] Includes error handling in code examples

**Example Pattern:**
````markdown
## Example 1: Basic Usage
Input: User data with name and email
Output:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "validated": true
}
```

Code:
```python
def validate_user(name, email):
    # Validate inputs
    if not name or not email:
        raise ValueError("Name and email required")
    return {"name": name, "email": email, "validated": True}
```
````

### ✅ Workflows

- [ ] Clear, numbered steps for multi-step processes
- [ ] Includes validation/verification steps
- [ ] Feedback loops where appropriate (check → fix → retry)
- [ ] Checklists for complex workflows

**Workflow Pattern:**
```markdown
## Workflow

Copy this checklist:
```
- [ ] Step 1: Analyze input
- [ ] Step 2: Validate
- [ ] Step 3: Process
- [ ] Step 4: Verify output
```

**Step 1: Analyze input**
Run: `python scripts/analyze.py input.json`

**Step 2: Validate**
Run: `python scripts/validate.py input.json`
⚠️ Only proceed if validation passes
...
```

---

## Degrees of Freedom

### ✅ Appropriate Specificity

Match the level of specificity to the task's fragility and variability.

- [ ] Assessed task fragility (low/medium/high risk)
- [ ] Matched instruction specificity to fragility level
- [ ] Used appropriate language markers (consider/use/MUST)
- [ ] Consistent freedom level within each workflow section
- [ ] Added ⚠️ warnings for low-freedom critical operations
- [ ] No mixed messages (MUST + feel free in same section)

**High Freedom** (text-based instructions):
- Use when multiple approaches are valid
- Decisions depend on context
- Language: "Consider", "typically", "common approaches"
- No warnings or MUST statements

**Medium Freedom** (scripts with parameters):
- Use when a preferred pattern exists
- Some variation is acceptable
- Language: "Use X with options", documented parameters
- Escape hatch provided for custom needs

**Low Freedom** (specific scripts, strict sequence):
- Use when operations are fragile and error-prone
- Consistency is critical
- Language: ⚠️ warnings, "MUST", "Do not modify", "In exact order"
- Numbered sequential steps with validation checkpoints

**Reference**: See `references/degrees_of_freedom.md` for detailed calibration guide

---

## Scripts and Code Execution

### ✅ Script Quality: "Solve, Don't Punt"

Scripts must handle errors explicitly with fallbacks rather than punting to Claude.

- [ ] All file operations wrapped in try/except
- [ ] Specific exceptions caught (not bare `except:`)
- [ ] Helpful error messages for each exception type
- [ ] Recovery guidance provided ("Check file path", "Verify permissions")
- [ ] Sensible fallback behavior (defaults, retries, alternatives)
- [ ] No silent failures
- [ ] Clear documentation and usage examples
- [ ] Single responsibility per script
- [ ] No "voodoo constants" (all values justified with comments)

**Error Handling Pattern:**
```python
# ✅ Good: Handle errors explicitly
def process_file(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {path}")
        print("💡 Check the file path is correct")
        return ''
    except PermissionError:
        print(f"❌ Cannot access: {path}")
        print("💡 Check file permissions")
        return ''

# ❌ Bad: Punt to Claude
def process_file(path):
    return open(path).read()  # Let Claude figure out errors
```

**Documented Constants:**
```python
# ✅ Good: Justified values
# HTTP requests typically complete within 30 seconds
# Longer timeout accounts for slow connections
REQUEST_TIMEOUT = 30

# Three retries balances reliability vs speed
# Most intermittent failures resolve by the second retry
MAX_RETRIES = 3

# ❌ Bad: Magic numbers
TIMEOUT = 47  # Why 47?
RETRIES = 5   # Why 5?
```

### ✅ Script Usage

- [ ] Clear whether to execute or read script
- [ ] Usage examples with expected output
- [ ] Documentation of script parameters
- [ ] Error messages guide toward correct usage

---

## File Paths and References

### ✅ Path Conventions

- [ ] Always use forward slashes: `scripts/helper.py`
- [ ] NEVER use backslashes: ~~`scripts\helper.py`~~
- [ ] All file references exist and are accessible
- [ ] Paths are relative to skill directory root

---

## Testing and Validation

### ✅ Testing Requirements

- [ ] At least 3 test scenarios created
- [ ] Tested with target model(s)
- [ ] Tested with real usage scenarios
- [ ] Team feedback incorporated (if applicable)

### ✅ Test Scenario Characteristics

- [ ] Independent (not dependent on other scenarios)
- [ ] Read-only operations preferred for testing
- [ ] Complex enough to stress the skill
- [ ] Realistic (based on actual use cases)
- [ ] Verifiable (clear success criteria)

---

## Security and Best Practices

### ✅ Security

- [ ] No hardcoded API keys or credentials
- [ ] No sensitive data in skill files
- [ ] Input validation in scripts
- [ ] Safe handling of user-provided paths/data

### ✅ Documentation

- [ ] README or usage guide included (if complex)
- [ ] Change log for iterations (recommended)
- [ ] Clear licensing information
- [ ] Examples of expected usage

---

## Anti-Patterns to Avoid

### ❌ Common Mistakes

- [ ] Avoid: Windows-style paths (`\`)
- [ ] Avoid: Offering too many options without guidance
- [ ] Avoid: Deeply nested file references (> 1 level)
- [ ] Avoid: Time-sensitive information
- [ ] Avoid: Assuming tools are installed
- [ ] Avoid: Vague descriptions
- [ ] Avoid: Second-person voice
- [ ] Avoid: Inconsistent terminology

### ❌ Bad Examples to Learn From

**Vague description:**
```yaml
# ❌ Bad
description: Helps with documents

# ✅ Good
description: Extract text and tables from PDF files.
Use when working with PDFs or document extraction.
```

**Too many options:**
````markdown
# ❌ Bad: Confusing
You can use pypdf, or pdfplumber, or PyMuPDF, or pdf2image...

# ✅ Good: Clear default with escape hatch
Use pdfplumber for text extraction.
For scanned PDFs requiring OCR, use pdf2image with pytesseract instead.
````

**Deeply nested references:**
```markdown
# ❌ Bad: Too deep
See advanced.md → See details.md → Here's the info

# ✅ Good: One level deep
See [advanced.md](advanced.md) or [details.md](details.md)
```

---

## Quick Reference Checklist

Before packaging, verify:

**Structure:**
- [ ] SKILL.md exists with proper frontmatter
- [ ] Name ≤ 64 chars, description ≤ 1024 chars
- [ ] SKILL.md body < 500 lines (use references/ if larger)
- [ ] All referenced files exist

**Quality:**
- [ ] Description is specific with trigger terms
- [ ] Third-person voice throughout
- [ ] Imperative/infinitive form (no "you should")
- [ ] Examples provided for complex operations
- [ ] Consistent terminology

**Organization:**
- [ ] Progressive disclosure implemented correctly
- [ ] Scripts have clear usage documentation
- [ ] Reference files organized logically
- [ ] Forward slashes in all paths

**Testing:**
- [ ] 3+ test scenarios created
- [ ] Tested with target model
- [ ] Real usage validated
- [ ] All validation checks pass

---

## Resources

- **Official Guide**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
- **Skills Overview**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- **Pattern Library**: See `patterns.md`
- **Examples**: `examples/` directory

---

## Validation Command

Run automated validation:
```bash
python scripts/validate_skill.py --full-check <skill-dir>
```

This checks many of these best practices automatically.
