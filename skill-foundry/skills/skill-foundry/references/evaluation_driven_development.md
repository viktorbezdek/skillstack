# Evaluation-Driven Development (EDD)

**This step is CRITICAL - create evaluations BEFORE extensive documentation.**

## Why Evaluations First?

Traditional approach: Write comprehensive docs → Test → Fix issues
**EDD approach**: Test → Identify gaps → Write minimal docs → Re-test

Building documentation without testing leads to:
- Solving non-existent problems
- Missing actual user needs
- Over-engineering simple cases
- Under-engineering complex cases

## Evaluation-Driven Development Process

Follow this sequence:

### 1. Baseline Testing (No Skill)

Run Claude on your test scenarios WITHOUT any skill.

Document:
- Where Claude hesitates or asks questions
- What Claude gets wrong
- What Claude does inefficiently
- What information Claude has to discover repeatedly

**Example baseline**:
```
Scenario: "Rotate pages 2-5 of document.pdf by 90 degrees"

Without skill:
- ❌ Claude asks which library to use
- ❌ Claude writes pypdf code from scratch each time
- ❌ Claude doesn't validate page numbers exist
- ⏱️  Takes 3-4 minutes to complete
```

### 2. Create 3-5 Test Scenarios

Convert concrete examples from Step 1 into specific test scenarios:

**PDF Editor Skill Examples**:
1. "Rotate pages 2-5 of document.pdf by 90 degrees"
2. "Merge invoices/invoice-*.pdf into combined-invoices.pdf"
3. "Extract all form fields from tax-form.pdf and save to fields.json"

**Database Query Skill Examples**:
1. "How many active users logged in during October 2024?"
2. "What's the average transaction value by customer segment?"
3. "Show me the top 10 products by revenue this quarter"

### 3. Document Identified Gaps

From baseline results, categorize specific gaps:

**Information Gaps**: Claude doesn't know what tool/approach to use
- Example: "Doesn't know pdfplumber is best for PDF manipulation"

**Efficiency Gaps**: Claude rewrites same code repeatedly
- Example: "Rewrites rotation code every time instead of using a script"

**Quality Gaps**: Claude skips validation or error handling
- Example: "Doesn't validate page numbers exist before rotating"

### 4. Define Success Criteria

For each scenario, define what "good" looks like:
- Success rate (e.g., "100% of scenarios complete successfully")
- Time improvement (e.g., "Complete in < 1 minute vs. 3-4 minutes")
- Quality metrics (e.g., "No repeated questions", "Validates inputs")

## Test Scenario Characteristics

Each test scenario should be:
- [ ] **Independent**: Not dependent on other scenarios
- [ ] **Realistic**: Based on actual use cases from Step 1
- [ ] **Verifiable**: Clear success criteria
- [ ] **Read-only preferred**: Avoid destructive operations when possible
- [ ] **Complex enough**: Should stress the skill appropriately

## Quality Checkpoint ✓

Before proceeding to Step 2, validate:

- [ ] Created 3-5 test scenarios from Step 1 examples
- [ ] Tested each scenario WITHOUT the skill (baseline)
- [ ] Documented what Claude struggled with or got wrong
- [ ] Categorized gaps (information, efficiency, quality)
- [ ] Defined clear success criteria for each scenario
- [ ] Confirmed scenarios are realistic and representative

## Navigation

- [Back to main SKILL.md](../SKILL.md)
- [Core Principles](core_principles.md)
- [Multi-Model Testing](multi_model_testing.md)