# Cookbook Patterns for Skill Development

This document captures practical patterns and lessons learned from the Claude Code Skills Cookbook and example implementations.

---

## Pattern 1: Evaluation-Driven Development

**Concept:** Build evaluations BEFORE writing extensive documentation.

### Why This Matters

Creating evaluations first ensures your skill solves real problems rather than documenting imagined ones.

### The Process

**1. Identify Gaps**
Run Claude on representative tasks WITHOUT a skill. Document specific failures or missing context.

**2. Create Evaluations**
Build 3-5 scenarios that test these gaps.

**3. Establish Baseline**
Measure Claude's performance without the skill.

**4. Write Minimal Instructions**
Create just enough content to address the gaps and pass evaluations.

**5. Iterate**
Execute evaluations, compare against baseline, and refine.

### Evaluation Structure Example

```json
{
  "skills": ["pdf-processing"],
  "query": "Extract all text from this PDF file and save it to output.txt",
  "files": ["test-files/document.pdf"],
  "expected_behavior": [
    "Successfully reads the PDF using an appropriate library",
    "Extracts text content from all pages",
    "Saves extracted text to output.txt in clear format"
  ]
}
```

### Benefits

- Ensures you're solving actual problems
- Provides clear success criteria
- Prevents over-engineering
- Creates automatic testing

---

## Pattern 2: Iterative Development with Claude

**Concept:** Work with one Claude instance ("Claude A") to create skills that other instances ("Claude B") will use.

### The Workflow

**Creating a New Skill:**

1. **Complete task without skill**: Work through a problem with Claude A using normal prompting
2. **Identify pattern**: After completing, identify what context you repeatedly provided
3. **Ask Claude A to create skill**: "Create a skill that captures this pattern we just used"
4. **Review for conciseness**: Ask Claude A to remove unnecessary explanations
5. **Improve organization**: Ask Claude A to organize content effectively
6. **Test with Claude B**: Use the skill with a fresh instance on related use cases
7. **Iterate based on observation**: Return to Claude A with specifics from Claude B's performance

**Example Dialogue:**

```
User to Claude A: "Create a skill that captures this BigQuery analysis pattern.
Include the table schemas, naming conventions, and the rule about filtering test accounts."

Claude A: [Creates SKILL.md]

User: "Remove the explanation about what win rate means - Claude already knows that."

Claude A: [Refines SKILL.md]

User: "Organize this so the table schema is in a separate reference file."

Claude A: [Creates references/schema.md and updates SKILL.md]

[User tests with Claude B]

User to Claude A: "When Claude used this skill, it forgot to filter by date for Q4.
Should we add a section about date filtering patterns?"

Claude A: [Updates skill with date filtering guidance]
```

### Benefits

- Claude understands skill format natively
- Rapid iteration based on real usage
- Natural conversation drives improvements
- Learns from actual agent behavior

### Key Insight

Claude models understand both how to write effective agent instructions and what information agents need. Leverage this!

---

## Pattern 3: Workflow Checklists

**Concept:** Provide copy-paste checklists for complex multi-step workflows.

### Why Checklists Work

- Claude can track progress visibly
- Users see what's done and what's next
- Steps are less likely to be skipped
- Clear communication of status

### Checklist Pattern

````markdown
## Research synthesis workflow

Copy this checklist and track your progress:

```
Research Progress:
- [ ] Step 1: Read all source documents
- [ ] Step 2: Identify key themes
- [ ] Step 3: Cross-reference claims
- [ ] Step 4: Create structured summary
- [ ] Step 5: Verify citations
```

**Step 1: Read all source documents**
Review each document in the `sources/` directory.
Note the main arguments and supporting evidence.

**Step 2: Identify key themes**
Look for patterns across sources.
What themes appear repeatedly?

**Step 3: Cross-reference claims**
For each major claim, verify it appears in the source material.

**Step 4: Create structured summary**
Organize findings by theme with supporting evidence.

**Step 5: Verify citations**
Check that every claim references the correct source.
If citations are incomplete, return to Step 3.
````

### When to Use

- Multi-step workflows (3+ steps)
- Steps that must be done in order
- Workflows where steps might be forgotten
- Complex analysis tasks
- Document generation workflows

---

## Pattern 4: Feedback Loops

**Concept:** Run validator → fix errors → repeat until clean.

### Common Pattern

**Validate → Fix → Repeat**

This pattern greatly improves output quality by catching errors early.

### Example: Document Editing

```markdown
## Document editing process

1. Make your edits to `word/document.xml`
2. **Validate immediately**: `python ooxml/scripts/validate.py unpacked_dir/`
3. If validation fails:
   - Review the error message carefully
   - Fix the issues in the XML
   - Run validation again
4. **Only proceed when validation passes**
5. Rebuild: `python ooxml/scripts/pack.py unpacked_dir/ output.docx`
6. Test the output document
```

### Example: Style Guide Compliance

```markdown
## Content review process

1. Draft your content following guidelines in STYLE_GUIDE.md
2. Review against checklist:
   - Check terminology consistency
   - Verify examples follow standard format
   - Confirm all required sections present
3. If issues found:
   - Note each issue with specific section reference
   - Revise the content
   - Review checklist again
4. Only proceed when all requirements met
5. Finalize and save
```

### Benefits

- Catches errors early before they propagate
- Clear, actionable error messages
- Safer workflows with validation gates
- Better debugging (isolate which step failed)

---

## Pattern 5: Template Pattern

**Concept:** Provide templates for consistent output format.

### Two Approaches

**Strict Requirements (for API responses, data formats):**

````markdown
## Report structure

ALWAYS use this exact template structure:

```markdown
# [Analysis Title]

## Executive summary
[One-paragraph overview of key findings]

## Key findings
- Finding 1 with supporting data
- Finding 2 with supporting data
- Finding 3 with supporting data

## Recommendations
1. Specific actionable recommendation
2. Specific actionable recommendation
```
````

**Flexible Guidance (when adaptation is useful):**

````markdown
## Report structure

Here is a sensible default format, but use your best judgment:

```markdown
# [Analysis Title]

## Executive summary
[Overview]

## Key findings
[Adapt sections based on what you discover]

## Recommendations
[Tailor to the specific context]
```

Adjust sections as needed for the specific analysis type.
````

### Benefits

- Consistency across outputs
- Clear expectations
- Faster generation
- Professional results

---

## Pattern 6: Conditional Workflows

**Concept:** Guide Claude through decision points in workflows.

### Pattern

```markdown
## Document modification workflow

1. Determine the modification type:

   **Creating new content?** → Follow "Creation workflow" below
   **Editing existing content?** → Follow "Editing workflow" below

2. Creation workflow:
   - Use docx-js library
   - Build document from scratch
   - Export to .docx format

3. Editing workflow:
   - Unpack existing document
   - Modify XML directly
   - Validate after each change
   - Repack when complete
```

### When Workflows Get Complex

If workflows become large with many steps, push them into separate files:

```markdown
## Workflow Selection

**Document Type:**
- Creating Excel workbook → See [workflows/excel_creation.md](workflows/excel_creation.md)
- Creating PowerPoint → See [workflows/ppt_creation.md](workflows/ppt_creation.md)
- Editing existing document → See [workflows/document_editing.md](workflows/document_editing.md)
```

---

## Pattern 7: Examples Pattern

**Concept:** Provide input/output pairs just like in regular prompting.

### Example: Commit Messages

````markdown
## Commit message format

Generate commit messages following these examples:

**Example 1:**
Input: Added user authentication with JWT tokens
Output:
```
feat(auth): implement JWT-based authentication

Add login endpoint and token validation middleware
```

**Example 2:**
Input: Fixed bug where dates displayed incorrectly in reports
Output:
```
fix(reports): correct date formatting in timezone conversion

Use UTC timestamps consistently across report generation
```

**Example 3:**
Input: Updated dependencies and refactored error handling
Output:
```
chore: update dependencies and refactor error handling

- Upgrade lodash to 4.17.21
- Standardize error response format across endpoints
```

Follow this style: type(scope): brief description, then detailed explanation.
````

### Why Examples Work

- Show desired style and level of detail
- More effective than descriptions alone
- Claude learns the pattern quickly
- Consistent output format

---

## Pattern 8: Old Patterns Section

**Concept:** Preserve historical context without cluttering main content.

### Why Not Time-Sensitive Information

Don't include information that will become outdated:

````markdown
<!-- ❌ Bad: Will become wrong -->
If you're doing this before August 2025, use the old API.
After August 2025, use the new API.

<!-- ✅ Good: Use "old patterns" section -->
## Current method

Use the v2 API endpoint: `api.example.com/v2/messages`

## Old patterns

<details>
<summary>Legacy v1 API (deprecated 2025-08)</summary>

The v1 API used: `api.example.com/v1/messages`

This endpoint is no longer supported.
</details>
````

### Benefits

- No time-sensitive content to maintain
- Historical context preserved
- Main content stays clean
- Clear what's current vs legacy

---

## Pattern 9: Progressive File Organization

**Concept:** Start simple, add structure as needed.

### Evolution Path

**Simple skill (< 500 lines):**
```
skill/
└── SKILL.md
```

**Growing skill (500-2000 lines):**
```
skill/
├── SKILL.md           # Overview and workflow
└── REFERENCE.md       # Detailed documentation
```

**Complex skill (> 2000 lines):**
```
skill/
├── SKILL.md           # Overview and navigation
├── references/
│   ├── api.md
│   ├── examples.md
│   └── troubleshooting.md
└── scripts/
    └── helpers.py
```

### When to Add Structure

- **Add REFERENCE.md**: When SKILL.md approaches 500 lines
- **Add references/**: When you have 3+ distinct topic areas
- **Add scripts/**: When you're repeatedly writing the same code
- **Add assets/**: When you need templates or output files

---

## Pattern 10: Domain-Specific Search Patterns

**Concept:** Include grep search patterns for large reference files.

### Pattern

````markdown
## BigQuery Data Analysis

## Available datasets

**Finance**: Revenue, ARR, billing → See [reference/finance.md](reference/finance.md)
**Sales**: Opportunities, pipeline → See [reference/sales.md](reference/sales.md)
**Product**: API usage, features → See [reference/product.md](reference/product.md)

## Quick search

Find specific metrics using grep:

```bash
grep -i "revenue" reference/finance.md
grep -i "pipeline" reference/sales.md
grep -i "api usage" reference/product.md
```
````

### Benefits

- Claude can find information quickly
- Works even with large reference files
- No need to load entire file
- Explicit search guidance

---

## Skill Development Anti-Patterns

### ❌ Skipping Evaluation Step

**Problem:** Building extensive documentation without testing

**Solution:** Create evaluations first (Evaluation-Driven Development)

### ❌ Over-Explaining Common Concepts

**Problem:** Wasting tokens on things Claude already knows

**Solution:** Trust Claude's knowledge, only add domain-specific details

### ❌ No Iteration Strategy

**Problem:** Creating skill once and never improving

**Solution:** Use Iterative Development pattern with regular testing

### ❌ Missing Checklists for Complex Workflows

**Problem:** Steps get skipped in multi-step processes

**Solution:** Add copy-paste checklists

### ❌ No Validation in Workflows

**Problem:** Errors cascade through steps

**Solution:** Add Feedback Loop pattern

---

## Combining Patterns for Maximum Effect

Successful skills often combine multiple patterns:

**Example: Financial Analysis Skill**

1. **Evaluation-Driven**: Created test scenarios first
2. **Iterative Development**: Refined with Claude's help
3. **Workflow Checklist**: Multi-step calculation process
4. **Feedback Loops**: Validate calculations before reporting
5. **Templates**: Consistent report format
6. **Examples**: Show expected analysis outputs

**Result**: High-quality skill that reliably produces accurate analysis.

---

## Quick Pattern Selection Guide

| Your Need | Use This Pattern |
|-----------|------------------|
| Starting new skill | Evaluation-Driven Development |
| Refining existing skill | Iterative Development with Claude |
| Complex workflow | Workflow Checklist |
| Quality assurance | Feedback Loops |
| Consistent output | Template Pattern |
| Multiple paths | Conditional Workflows |
| Show expected style | Examples Pattern |
| Large reference files | Domain-Specific Search |

---

## Resources

- **Skills Cookbook**: See `reference_docs/claude_code_skills/cookbook/`
- **Pattern Library**: See `references/patterns.md`
- **Best Practices**: See `references/best_practices_checklist.md`
- **Examples**: `examples/` directory

---

## Next Steps

1. **Review patterns**: Which patterns fit your skill?
2. **Start with evaluation**: Create test scenarios first
3. **Iterate with Claude**: Use Claude A to refine your skill
4. **Test with fresh instance**: Validate with Claude B
5. **Combine patterns**: Use multiple patterns together
6. **Validate**: Run `validate_skill.py --full-check`
