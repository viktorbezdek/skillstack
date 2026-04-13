# Troubleshooting Guide

Common issues encountered during skill creation and their solutions.

---

## Skill Discovery Issues

### Skill Not Being Discovered

**Symptoms:**
- Claude doesn't recognize when to use the skill
- Skill not triggered even with relevant queries

**Causes & Solutions:**

| Cause | Check | Solution |
|-------|-------|----------|
| Missing trigger terms | Review description | Add domain-specific keywords users would say |
| Description too generic | Compare to similar skills | Make description specific with concrete use cases |
| Name doesn't match domain | Check name field | Use gerund form related to actual functionality |

**Example Fix:**
```yaml
# ❌ Bad - Too generic
description: Helps with documents

# ✅ Good - Specific with triggers
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

---

### Claude Ignores Skill When Loaded

**Symptoms:**
- Skill triggers but Claude doesn't follow guidance
- Claude uses own approach instead of skill instructions

**Causes & Solutions:**

| Cause | Check | Solution |
|-------|-------|----------|
| "When to use" unclear | Description clarity | Add specific scenarios in description |
| Instructions too vague | SKILL.md content | Use imperative form with concrete examples |
| Conflicts with other skills | Skill overlap | Make trigger terms more specific |
| Too verbose | Token count | Condense to < 5000 tokens |

**Example Fix:**
```markdown
# ❌ Bad - Vague guidance
## Overview
This skill helps with databases.

# ✅ Good - Clear triggers and instructions
## When to Use
Use this skill when querying the company BigQuery database.
Trigger phrases: "query the database", "check user metrics", "BigQuery"

## How to Query
1. Check `references/schema.md` for table structures
2. Use the BigQuery:query_database tool
3. Reference column names exactly as documented
```

---

## Content Quality Issues

### Skill Too Verbose

**Symptoms:**
- Token count > 5000
- SKILL.md > 500 lines
- Takes long time to load

**Solution:**

1. **Move details to references/**
   ```markdown
   # In SKILL.md - Keep concise
   ## API Reference
   See [references/api-reference.md](references/api-reference.md) for complete API documentation.

   # Move detailed content to references/api-reference.md
   ```

2. **Remove basic explanations**
   ```markdown
   # ❌ Remove - Claude knows this
   PDF files are documents that can contain text and images.

   # ✅ Keep - Specific to your domain
   Use pdfplumber for text extraction:
   ```python
   import pdfplumber
   with pdfplumber.open("file.pdf") as pdf:
       text = pdf.pages[0].extract_text()
   ```
   ```

3. **Consolidate examples**
   - Keep 2-3 representative examples in SKILL.md
   - Move extensive examples to `references/examples.md`

---

### Missing Progressive Disclosure

**Symptoms:**
- All content in SKILL.md
- No reference files
- Exceeds 500 line recommendation

**Solution:**

Apply three-tier loading:
```
Tier 1 (Metadata):
- name + description only
- Always loaded

Tier 2 (SKILL.md):
- Overview and quick start
- Main workflow
- < 500 lines

Tier 3 (references/):
- Detailed documentation
- Extended examples
- Advanced topics
- Loaded as needed by Claude
```

**Example Structure:**
```
skill-name/
├── SKILL.md                  # < 500 lines
│   ├── Quick start
│   ├── Main workflow
│   └── Links to references/
└── references/
    ├── api-reference.md      # Detailed API docs
    ├── examples.md           # Extended examples
    └── troubleshooting.md    # Common issues
```

---

## Script Issues

### Scripts Fail with Unclear Errors

**Symptoms:**
- Scripts exit with generic error messages
- No guidance on what went wrong
- Claude unsure how to proceed

**Cause:** "Punt don't solve" anti-pattern

**Solution:** Implement explicit error handling

```python
# ❌ Bad - Punts to Claude
def process_file(path):
    with open(path) as f:
        return f.read()

# ✅ Good - Solves with fallbacks
def process_file(path):
    """Process a file, creating it if it doesn't exist."""
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {path} not found, creating default")
        with open(path, 'w') as f:
            f.write('')
        return ''
    except PermissionError:
        print(f"Cannot access {path}, using default")
        return ''
    except Exception as e:
        print(f"Error processing {path}: {str(e)}")
        return ''
```

---

### Scripts Not Executable

**Symptoms:**
- Permission denied errors
- Scripts won't run

**Solution:**
```bash
# Make scripts executable
chmod +x scripts/*.py

# Or run with interpreter
python scripts/script_name.py
```

---

## Validation Issues

### Validation Fails with Unclear Messages

**Common Validation Errors:**

| Error | Meaning | Fix |
|-------|---------|-----|
| "Description too long" | > 1024 chars | Condense description, move details to SKILL.md |
| "Missing frontmatter" | No YAML block | Add `---` delimited YAML at top of SKILL.md |
| "Invalid name format" | Wrong characters | Use lowercase, hyphens only, no spaces |
| "SKILL.md not found" | Missing file | Ensure SKILL.md exists in skill directory |

**Validation Command Reference:**

| Command | When to Use | What It Checks |
|---------|-------------|----------------|
| `--check-structure` | After initialization | Directory layout, required files, frontmatter format |
| `--check-content` | During editing | Writing style, progressive disclosure, resource references |
| `--full-check` | Before packaging | All quality checks combined |
| `--check-init` | After template copy | Template properly initialized, placeholders present |

**Running Validation:**
```bash
# Check structure
python scripts/validate_skill.py --check-structure <skill-dir>

# Check content quality
python scripts/validate_skill.py --check-content <skill-dir>

# Full pre-package validation
python scripts/validate_skill.py --full-check <skill-dir>
```

---

## Testing Issues

### Skill Works with Sonnet but Not Haiku

**Cause:** Insufficient guidance for smaller model

**Solution:**
- Add more explicit step-by-step instructions
- Include more examples
- Reduce ambiguity in descriptions
- Test iteratively with Haiku

**Example:**
```markdown
# ❌ Too terse for Haiku
## Workflow
1. Extract data
2. Process
3. Output results

# ✅ Explicit for Haiku
## Workflow
1. Extract data using `scripts/extract.py input.pdf`
2. Process extracted data:
   - Validate with `scripts/validate.py data.json`
   - Transform with `scripts/process.py data.json output.json`
3. Output results with `scripts/format.py output.json`
```

---

### Skill Too Detailed for Opus

**Cause:** Over-explaining concepts Opus can infer

**Solution:**
- Remove basic explanations
- Trust Opus to understand context
- Keep instructions concise
- Focus on domain-specific knowledge

---

## Packaging Issues

### Package Creation Fails

**Common Causes:**

1. **Validation errors** - Fix errors shown in validation output
2. **Missing files** - Ensure all referenced files exist
3. **Incorrect paths** - Use forward slashes, not backslashes
4. **Special characters** - Remove non-ASCII characters from filenames

**Solution:**
```bash
# Run full validation first
python scripts/validate_skill.py --full-check skill-dir

# Fix all errors before packaging
# Then package
python scripts/package_skill.py skill-dir output-dir
```

---

### Referenced Files Not Included in Package

**Cause:** Files not in standard directories

**Solution:**
Ensure files are in recognized locations:
```
skill-name/
├── SKILL.md           ✓ Included
├── scripts/           ✓ Included
├── references/        ✓ Included
├── assets/            ✓ Included
└── other-dir/         ✗ May not be included
```

---

## Performance Issues

### Skill Load Time Too Slow

**Symptoms:**
- Noticeable delay when skill triggers
- Context window fills up quickly

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| SKILL.md too large | Apply progressive disclosure, move content to references/ |
| Too many scripts loaded | Scripts aren't loaded unless read, but reduce if excessive |
| Large binary assets | Ensure assets/ are not being read into context |

---

## Resource Organization Issues

### Can't Decide: Script vs. Reference vs. Asset?

**Decision Tree:**

```
Is it code that executes?
├─ Yes → scripts/
│
└─ No → Will Claude read it while working?
    ├─ Yes → references/
    │
    └─ No → Is it used in output Claude creates?
        ├─ Yes → assets/
        └─ No → Probably doesn't belong in skill
```

**Examples:**
- `rotate_pdf.py` → scripts/ (executes)
- `api_docs.md` → references/ (Claude references)
- `template.xlsx` → assets/ (used in output)
- Company logo → assets/static/images/

---

## Auto-Activation System Troubleshooting

This section covers troubleshooting for skills with auto-activation systems using hooks (UserPromptSubmit, PreToolUse) and skill-rules.json configuration.

### Skill Not Triggering (UserPromptSubmit)

**Symptoms:** User asks relevant question, but no skill suggestion appears in output.

**Common Causes:**

#### 1. Keywords Don't Match Prompt

**Check:**
- Review `promptTriggers.keywords` in skill-rules.json
- Are keywords actually present in the user's prompt?
- Remember: case-insensitive substring matching

**Example:**
```json
"keywords": ["layout", "grid"]
```
- "how does the layout work?" → ✅ Matches "layout"
- "how does the grid system work?" → ✅ Matches "grid"
- "how does it work?" → ❌ No match

**Fix:** Add more keyword variations to skill-rules.json

#### 2. Intent Patterns Too Specific

**Check:**
- Review `promptTriggers.intentPatterns`
- Test regex patterns at https://regex101.com/
- Patterns may need to be broader

**Example:**
```json
"intentPatterns": [
  "(create|add).*?(database.*?table)"  // Too specific
]
```
- "create a database table" → ✅ Matches
- "add new table" → ❌ Doesn't match (missing "database")

**Fix:** Broaden the pattern:
```json
"intentPatterns": [
  "(create|add).*?(table|database)"  // Better
]
```

#### 3. Skill Name Mismatch

**Check:**
- Skill name in SKILL.md frontmatter
- Skill name in skill-rules.json
- Must match exactly (case-sensitive)

**Example:**
```yaml
# SKILL.md
name: project-catalog-developer
```
```json
// skill-rules.json
"project-catalogue-developer": {  // ❌ Typo: catalogue vs catalog
  ...
}
```

**Fix:** Make names match exactly

#### 4. JSON Syntax Error

**Check:**
```bash
cat .claude/skills/skill-rules.json | jq .
```

If invalid JSON, jq will show the error.

**Common JSON errors:**
- Trailing commas: `{"keywords": ["one", "two",]}`
- Missing quotes: `{type: "guardrail"}`
- Single quotes: `{'type': 'guardrail'}` (must use double quotes)
- Unescaped characters in strings

**Fix:** Correct JSON syntax, validate with jq

#### Debug Command

Test the hook manually:
```bash
echo '{"session_id":"debug","prompt":"your test prompt here"}' | \
  npx tsx .claude/hooks/skill-activation-prompt.ts
```

Expected: Your skill should appear in the output.

---

### Skill Not Blocking (PreToolUse)

**Symptoms:** Edit a file that should trigger a guardrail, but no block occurs.

**Common Causes:**

#### 1. File Path Doesn't Match Patterns

**Check:**
- File path being edited
- `fileTriggers.pathPatterns` in skill-rules.json
- Glob pattern syntax

**Example:**
```json
"pathPatterns": [
  "frontend/src/**/*.tsx"
]
```
- Editing: `frontend/src/components/Dashboard.tsx` → ✅ Matches
- Editing: `backend/src/app.ts` → ❌ Doesn't match

**Fix:** Adjust glob patterns or add missing path

#### 2. Excluded by pathExclusions

**Check:**
- Are you editing a test file?
- Review `fileTriggers.pathExclusions`

**Example:**
```json
"pathExclusions": [
  "**/*.test.ts",
  "**/*.spec.ts"
]
```
- Editing: `services/user.test.ts` → ❌ Excluded
- Editing: `services/user.ts` → ✅ Not excluded

**Fix:** If test exclusion too broad, narrow it or remove

#### 3. Content Pattern Not Found

**Check:**
- Does file actually contain the pattern?
- Review `fileTriggers.contentPatterns`
- Is regex correct?

**Example:**
```json
"contentPatterns": [
  "import.*[Pp]risma"
]
```
- File has: `import { PrismaService } from './prisma'` → ✅ Matches
- File has: `import { Database } from './db'` → ❌ Doesn't match

**Debug:**
```bash
# Check if pattern exists in file
grep -i "prisma" path/to/file.ts
```

**Fix:** Adjust content patterns or verify file content

#### 4. Session Already Used Skill

**Check session state:**
```bash
ls .claude/hooks/state/
cat .claude/hooks/state/skills-used-{session-id}.json
```

**Example:**
```json
{
  "skills_used": ["database-verification"],
  "files_verified": []
}
```

If skill is in `skills_used`, it won't block again in this session.

**Fix:** Delete state file to reset:
```bash
rm .claude/hooks/state/skills-used-{session-id}.json
```

#### 5. File Marker Present

**Check for skip marker:**
```bash
grep "@skip-validation" path/to/file.ts
```

If found, file is permanently skipped.

**Fix:** Remove marker if verification needed again

#### 6. Environment Variable Override

**Check:**
```bash
echo $SKIP_DB_VERIFICATION
echo $SKIP_SKILL_GUARDRAILS
```

If set, skill is disabled.

**Fix:** Unset environment variable:
```bash
unset SKIP_DB_VERIFICATION
```

#### Debug Command

Test the hook manually:
```bash
cat <<'EOF' | npx tsx .claude/hooks/skill-verification-guard.ts 2>&1
{
  "session_id": "debug",
  "tool_name": "Edit",
  "tool_input": {"file_path": "/path/to/test/file.ts"}
}
EOF
echo "Exit code: $?"
```

Expected:
- Exit code 2 + stderr message if should block
- Exit code 0 + no output if should allow

---

### Hook Not Executing At All

**Symptoms:** Hook doesn't run - no suggestion, no block, nothing.

**Common Causes:**

#### 1. Hook Not Registered

**Check `.claude/settings.json`:**
```bash
cat .claude/settings.json | jq '.hooks.UserPromptSubmit'
cat .claude/settings.json | jq '.hooks.PreToolUse'
```

Expected: Hook entries present

**Fix:** Add missing hook registration:
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/skill-activation-prompt.sh"
          }
        ]
      }
    ]
  }
}
```

#### 2. Bash Wrapper Not Executable

**Check:**
```bash
ls -l .claude/hooks/*.sh
```

Expected: `-rwxr-xr-x` (executable)

**Fix:**
```bash
chmod +x .claude/hooks/*.sh
```

#### 3. Incorrect Shebang

**Check:**
```bash
head -1 .claude/hooks/skill-activation-prompt.sh
```

Expected: `#!/bin/bash`

**Fix:** Add correct shebang to first line

#### 4. npx/tsx Not Available

**Check:**
```bash
npx tsx --version
```

Expected: Version number

**Fix:** Install dependencies:
```bash
cd .claude/hooks
npm install
```

#### 5. TypeScript Compilation Error

**Check:**
```bash
cd .claude/hooks
npx tsc --noEmit skill-activation-prompt.ts
```

Expected: No output (no errors)

**Fix:** Correct TypeScript syntax errors

---

### Performance Issues with Hooks

**Symptoms:** Noticeable delay before prompt/edit execution.

**Common Causes:**

#### 1. Too Many Patterns

**Check:**
- Count patterns in skill-rules.json
- Each pattern = regex compilation + matching

**Solution:**
- Reduce pattern count
- Combine similar patterns
- Remove redundant patterns

#### 2. Complex Regex

**Problem:**
```regex
(create|add|modify|update|implement|build).*?(feature|endpoint|route|service|controller|component)
```
- Long alternations = slow

**Solution:** Simplify
```regex
(create|add).*?(feature|endpoint)  // Fewer alternatives
```

#### 3. Too Many Files Checked

**Problem:**
```json
"pathPatterns": [
  "**/*.ts"  // Checks ALL TypeScript files
]
```

**Solution:** Be more specific
```json
"pathPatterns": [
  "form/src/services/**/*.ts",
  "form/src/controllers/**/*.ts"
]
```

#### 4. Large Files

Content pattern matching reads entire file - slow for large files.

**Solution:**
- Only use content patterns when necessary
- Keep files modular

#### Measure Performance

```bash
# UserPromptSubmit (target: < 100ms)
time echo '{"prompt":"test"}' | npx tsx .claude/hooks/skill-activation-prompt.ts

# PreToolUse (target: < 200ms)
time cat <<'EOF' | npx tsx .claude/hooks/skill-verification-guard.ts
{"tool_name":"Edit","tool_input":{"file_path":"test.ts"}}
EOF
```

**Target metrics:**
- UserPromptSubmit: < 100ms
- PreToolUse: < 200ms

---

### False Positives

**Symptoms:** Skill triggers when it shouldn't.

**Common Causes & Solutions:**

#### 1. Keywords Too Generic

**Problem:**
```json
"keywords": ["user", "system", "create"]  // Too broad
```
- Triggers on: "user manual", "file system", "create directory"

**Solution:** Make keywords more specific
```json
"keywords": [
  "user authentication",
  "user tracking",
  "create feature"
]
```

#### 2. Intent Patterns Too Broad

**Problem:**
```json
"intentPatterns": [
  "(create)"  // Matches everything with "create"
]
```

**Solution:** Add context
```json
"intentPatterns": [
  "(create|add).*?(database|table|feature)"
]
```

#### 3. File Paths Too Generic

**Problem:**
```json
"pathPatterns": [
  "form/**"  // Matches everything in form/
]
```

**Solution:** Use narrower patterns
```json
"pathPatterns": [
  "form/src/services/**/*.ts",
  "form/src/controllers/**/*.ts"
]
```

---

## Getting Help

### Where to Find More Information

**Documentation:**
- Core principles: `references/core_principles.md`
- Pattern library: `references/patterns.md`
- Detailed steps: `references/detailed_process_steps.md`
- Best practices: `references/best_practices_checklist.md`

**Examples:**
- Document processing: `examples/document-skills/pdf/`
- API integration: `examples/mcp-builder/`
- Analysis workflows: `examples/document-skills/analyzing-financial-statements/`

**Validation:**
- Run with `--help` flag: `python scripts/validate_skill.py --help`
- Check specific aspects: `--check-structure`, `--check-content`
- Full validation: `--full-check`

---

## Common Workflow Problems

### Step Numbering Confusion

**Issue:** Not sure what order to do steps

**Solution:** Follow this sequence:
1. Step 0: Initialize and create TodoWrite checklist
2. Step 1: Gather concrete examples
3. Step 1.1: Create test evaluations (EDD)
4. Step 1.2: Plan structure (scripts/references/assets)
5. Step 1.3: Extract patterns from examples/
6. Step 2: Plan resource contents
7. Step 3: Initialize from template
8. Step 4: Edit skill
9. Step 5: Package
10. Step 6: Iterate and test

---

### Unsure When Skill is "Done"

**Checklist for Completion:**
- [ ] All test scenarios pass
- [ ] Tested with Haiku, Sonnet, and Opus
- [ ] Full validation passes (`--full-check`)
- [ ] Token count < 5000
- [ ] Line count < 500
- [ ] Progressive disclosure applied
- [ ] All scripts have error handling
- [ ] Documentation complete
- [ ] Examples provided

---

This troubleshooting guide should help resolve most common issues encountered during skill creation. For issues not covered here, review the validation error messages carefully—they often indicate exactly what needs to be fixed.
