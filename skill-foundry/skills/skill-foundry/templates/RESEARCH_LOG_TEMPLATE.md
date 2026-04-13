# Research Log: [TOOL-NAME]

**Created:** [DATE]
**Documentation Source:** [URL or Path]
**Tool Type:** [CLI/API/Library/Framework]
**Version:** [Extracted or Unknown]

---

## Phase 1: Documentation Acquisition

### Source Information
- **Primary docs:** [URL or path]
- **Crawled pages:** [count]
- **Key pages identified:**
  - [Page 1 URL or path] - [Description]
  - [Page 2 URL or path] - [Description]
  - ...

### Crawl Metadata
- **Date:** [timestamp]
- **Tool used:** crawl4ai-cli / manual markdown
- **Success rate:** [X/Y pages successful]
- **Failed pages:** [List any failed URLs with reasons]

### Raw Documentation Storage
- **Location:** `planning/research-logs/[tool-name]/raw/`
- **Format:** [Markdown / HTML / JSON]
- **Total size:** [KB/MB]

---

## Phase 2: Documentation Analysis

### Tool Type Classification
**Classification:** [CLI/API/Library/Framework]

**Reasoning:**
- [Indicator 1 - e.g., "Contains command-line flags and usage examples"]
- [Indicator 2 - e.g., "Shows REST endpoints with HTTP methods"]
- ...

### Workflow Patterns Identified

#### Pattern 1: [Pattern Name]
- **Description:** [What this workflow does]
- **Frequency:** [Common / Occasional / Advanced]
- **Example Source:** [URL#section or file:line]
- **Steps:**
  1. [Step 1]
  2. [Step 2]
  ...

#### Pattern 2: [Pattern Name]
[Repeat structure]

### Example Code Catalog

#### Example 1: [Title/Description]
- **Source:** [URL#section or file:line]
- **Type:** [Basic usage / Advanced / Edge case]
- **Language:** [bash/python/javascript/etc]
- **Extracted Code:**
  ```[language]
  [verbatim code from documentation]
  ```
- **Notes:** [Any important context about this example]

#### Example 2: [Title/Description]
[Repeat structure for each example]

### Gap Analysis

**Gaps Identified:**
- [ ] **Gap 1:** [Description of what's missing or unclear]
  - **Impact:** [Low / Medium / High]
  - **Status:** [To research / Documented / Resolved / Accepted]
  - **Notes:** [Additional context]

- [ ] **Gap 2:** [Description]
  [Repeat structure]

### Pitfall Warnings

**Warnings Extracted from Documentation:**
1. **Pitfall:** [Description from docs]
   - **Source:** [URL#section]
   - **Severity:** [Low / Medium / High]
   - **Guardrail Strategy:** [How we'll prevent this - inline warning / script check / checklist item / automated handling]

2. **Pitfall:** [Description]
   [Repeat structure]

---

## Phase 3: Research & Clarification

### Research Queries (Perplexity MCP)

#### Query 1: [Search query text]
- **Rationale:** [Why this research was needed - e.g., "Documentation mentions 'rate limiting' but doesn't specify limits"]
- **Findings:**
  - [Key finding 1]
  - [Key finding 2]
- **Sources:**
  - [URL 1]
  - [URL 2]
- **Incorporation Decision:** [Generally useful / Task-specific / Not used]
- **Reasoning:** [Why incorporated or not]

#### Query 2: [Search query text]
[Repeat structure]

### Unresolved Gaps

**Items Requiring Human Review:**
- [ ] **Unresolved 1:** [Description]
  - **Why unresolved:** [Research failed / Contradictory info / Proprietary]
  - **Recommendation:** [Suggested approach]

---

## Phase 4: Template Synthesis

### Templates Created

#### Template 1: [filename.ext]
- **Purpose:** [What this template is for]
- **Synthesized from:** [Example IDs: e.g., "Example 1, Example 3, Example 7"]
- **Pattern used:** [Pattern name from Phase 2]
- **Abstraction level:** [Minimal / Moderate / High]
- **Variables:** [List of ${PLACEHOLDER} variables]
- **Defaults provided:** [Yes/No - if yes, what defaults]

#### Template 2: [filename.ext]
[Repeat structure]

### Pattern Generalizations

**Generalization 1:** [Pattern name]
- **Original examples:** [Count] examples
- **Common structure identified:** [Description]
- **Variable parts:** [What changes between examples]
- **How generalized:** [Abstraction approach]

---

## Phase 5: Guardrails Creation

### Layer 1: Inline Warnings
- **Templates with warnings:** [Count]
- **Total warnings added:** [Count]
- **Pitfalls covered:** [List of pitfall IDs from Phase 2]

### Layer 2: Pre-flight Validation Scripts
- **Scripts created:**
  - `validate_prereqs.sh/py` - [Checks X, Y, Z]
  - [Other scripts]

### Layer 3: Checklists
- **Checklists created:**
  - `checklists/pre-flight.md` - [X items]
  - `checklists/validation.md` - [X items]
  - `checklists/troubleshooting.md` - [X items]

### Layer 4: Automated Boilerplates
- **Setup automation:** [scripts/setup.sh - handles X, Y, Z]
- **Error handling:** [Built into templates: Yes/No]
- **"Solve once" implementations:** [List features]

---

## Phase 6: Support Assets Creation

### Setup/Installation Scripts
- `scripts/setup.sh` - [Description]
- [Other scripts]

### Configuration Templates
- `.toolnamerc` - [Description]
- `config/template.yaml` - [Description]

### Troubleshooting Decision Trees
- `docs/troubleshooting-tree.md` - [Covers X errors/scenarios]

### Quick Reference Cards
- `docs/quick-reference.md` - [Contains X commands/patterns]

---

## Phase 7: Test & Validation Creation

### Automated Test Scripts
- `tests/test_templates.sh` - [Tests X templates]
- `tests/validate_config.py` - [Validates Y configurations]

### Validation Checklists
- `checklists/validation.md` - [X manual verification steps]

### Example Usage Scenarios
- **Scenario 1:** [Description]
- **Scenario 2:** [Description]

---

## Summary

### Metrics
- **Total examples extracted:** [count]
- **Templates created:** [count]
- **Guardrails generated:** [count] (across [count] layers)
- **Research queries:** [count]
- **Unresolved items:** [count]

### Coverage
- **Workflows documented:** [count] patterns
- **Pitfalls addressed:** [count]/[total identified]
- **Documentation pages analyzed:** [count]

### Quality Indicators
- **Template synthesis accuracy:** [Estimated %]
- **Guardrail coverage:** [% of pitfalls covered]
- **Research depth:** [Shallow / Moderate / Deep]

### Next Steps
1. [Step 1 - e.g., "Resolve unresolved gaps with human review"]
2. [Step 2 - e.g., "Test templates with real use cases"]
3. [Step 3 - e.g., "Validate SKILL.md against standards"]

---

## Appendices

### A. Documentation Structure Map
[Visual or text representation of doc organization]

### B. Pattern Matrix
[Table showing which patterns appear in which examples]

### C. Research Query Log
[Complete list of all Perplexity queries with timestamps]
