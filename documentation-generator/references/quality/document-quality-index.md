# Document Quality Index (DQI)

## Overview

The Document Quality Index (DQI) is a standardized scoring system for measuring documentation quality. It provides an objective, reproducible way to assess and improve documentation.

## Scoring System

**Total Score: 100 points**

| Category | Weight | Description |
|----------|--------|-------------|
| Structure | 40% | Organization, hierarchy, navigation |
| Content | 30% | Completeness, accuracy, examples |
| Style | 30% | Consistency, readability, formatting |

## Quality Thresholds

| Score | Rating | Action |
|-------|--------|--------|
| 90-100 | Excellent | Production ready |
| 70-89 | Good | Minor improvements needed |
| 50-69 | Acceptable | Significant improvements needed |
| Below 50 | Poor | Major revision required |

## Structure Scoring (40 points)

### Title and Headings (15 points)

| Criterion | Points | Check |
|-----------|--------|-------|
| Has H1 title | 5 | Document starts with a main title |
| Proper hierarchy | 5 | No skipped heading levels |
| Descriptive headings | 5 | Headings describe content |

**Good Example:**
```markdown
# User Authentication Guide

## Overview

## Prerequisites

## Step-by-Step Setup

### Configure Provider

### Set Up Callbacks
```

**Bad Example:**
```markdown
# Auth

### Setup
(Skipped H2)

#### Step 1
```

### Document Organization (15 points)

| Criterion | Points | Check |
|-----------|--------|-------|
| Logical section order | 5 | Information flows naturally |
| Related content grouped | 5 | Similar topics together |
| Progressive disclosure | 5 | Simple before complex |

**Recommended Section Order:**

1. Title
2. Overview/Introduction
3. Prerequisites (if any)
4. Quick Start
5. Main Content
6. Advanced Topics
7. Troubleshooting
8. Reference/Appendix

### Navigation (10 points)

| Criterion | Points | Check |
|-----------|--------|-------|
| Table of contents (long docs) | 5 | TOC for docs > 1000 words |
| Internal links | 3 | Cross-references to related sections |
| External links | 2 | Links to resources, references |

## Content Scoring (30 points)

### Completeness (10 points)

| Criterion | Points | Check |
|-----------|--------|-------|
| All features documented | 4 | No undocumented functionality |
| Edge cases covered | 3 | Handles special scenarios |
| Prerequisites listed | 3 | Dependencies clearly stated |

### Accuracy (10 points)

| Criterion | Points | Check |
|-----------|--------|-------|
| Code examples work | 4 | All code tested and functional |
| Up-to-date content | 3 | Matches current version |
| Correct terminology | 3 | Proper technical terms |

**Red Flags:**
- TODO markers: -2 points each (max -10)
- Placeholder text: -3 points each (max -15)
- Outdated references: -2 points each

### Examples (10 points)

| Criterion | Points | Check |
|-----------|--------|-------|
| Code examples present | 4 | At least one per major concept |
| Examples are practical | 3 | Real-world use cases |
| Examples are complete | 3 | Can be copied and run |

**Good Example:**
```python
# Complete, working example
from mylib import Client

client = Client(api_key="your-key")
result = client.fetch_data(query="example")
print(result.items)  # Output: ['item1', 'item2']
```

**Bad Example:**
```python
# Incomplete
client.fetch(...)  # What is client? What are the params?
```

## Style Scoring (30 points)

### Consistency (10 points)

| Criterion | Points | Check |
|-----------|--------|-------|
| Consistent formatting | 4 | Same style throughout |
| Consistent terminology | 3 | Same terms for same concepts |
| Consistent structure | 3 | Similar sections follow pattern |

**Formatting Consistency Checks:**
- Heading style (ATX vs Setext)
- List markers (-, *, +)
- Code fence style (``` vs ~~~)
- Emphasis style (* vs _)

### Readability (10 points)

| Criterion | Points | Check |
|-----------|--------|-------|
| Appropriate length | 4 | Not too long or too short |
| Clear language | 3 | Avoids jargon, defines terms |
| Good paragraph structure | 3 | Logical paragraph breaks |

**Readability Guidelines:**
- Sentences: 15-25 words average
- Paragraphs: 3-5 sentences
- Lists: 3-7 items
- Code blocks: With language hints

### Formatting (10 points)

| Criterion | Points | Check |
|-----------|--------|-------|
| Proper markdown syntax | 4 | Valid, renders correctly |
| No trailing whitespace | 2 | Clean line endings |
| Ends with newline | 2 | POSIX compliance |
| No multiple blank lines | 2 | Single blank line separators |

## Automated Validation

### Required Checks

```python
def validate_structure(doc):
    score = 0

    # Has H1 title
    if re.search(r'^# .+', doc, re.MULTILINE):
        score += 5

    # Proper heading hierarchy
    if not has_skipped_headings(doc):
        score += 5

    # Has multiple sections
    h2_count = len(re.findall(r'^## .+', doc, re.MULTILINE))
    if h2_count >= 3:
        score += 5
    elif h2_count >= 1:
        score += 2

    return score  # Max 15

def validate_content(doc):
    score = 0

    # Word count
    words = len(doc.split())
    if words >= 500:
        score += 4
    elif words >= 200:
        score += 2

    # Code examples
    code_blocks = len(re.findall(r'```[\s\S]*?```', doc))
    if code_blocks >= 3:
        score += 4
    elif code_blocks >= 1:
        score += 2

    # Deductions
    todos = len(re.findall(r'TODO', doc, re.IGNORECASE))
    score -= min(todos * 2, 10)

    return max(0, score)

def validate_style(doc):
    score = 0

    # Consistent heading style
    atx = len(re.findall(r'^#+\s+', doc, re.MULTILINE))
    setext = len(re.findall(r'^[=-]+$', doc, re.MULTILINE))
    if (atx > 0 and setext == 0) or (setext > 0 and atx == 0):
        score += 4

    # Code blocks have language hints
    with_lang = len(re.findall(r'```\w+', doc))
    without_lang = len(re.findall(r'```\s*\n', doc))
    if without_lang == 0 or with_lang >= without_lang:
        score += 4

    # Ends with newline
    if doc.endswith('\n'):
        score += 2

    return score
```

## Document Type Requirements

### README.md

| Requirement | Points |
|-------------|--------|
| Project title + description | 10 |
| Quick start instructions | 10 |
| Installation steps | 10 |
| Basic usage examples | 10 |
| Link to detailed docs | 5 |

**Minimum passing score: 35/45**

### API Reference

| Requirement | Points |
|-------------|--------|
| All endpoints documented | 15 |
| Request/response examples | 15 |
| Error codes documented | 10 |
| Authentication explained | 10 |

**Minimum passing score: 40/50**

### Tutorial

| Requirement | Points |
|-------------|--------|
| Clear learning objective | 10 |
| Step-by-step format | 15 |
| Working code examples | 15 |
| Verifiable outcome | 10 |

**Minimum passing score: 40/50**

## Improvement Priorities

When a document scores low, prioritize fixes in this order:

1. **Critical (Blocks usage)**
   - Missing installation steps
   - Broken code examples
   - Missing prerequisites

2. **High (Significantly impacts usability)**
   - Missing TODOs/placeholders
   - Outdated content
   - Missing error handling

3. **Medium (Reduces quality)**
   - Poor organization
   - Inconsistent formatting
   - Missing examples

4. **Low (Polish)**
   - Trailing whitespace
   - Line length
   - Minor style issues

## Continuous Improvement

### Weekly Review
- Run automated validation
- Address critical issues
- Track score trends

### Monthly Review
- Deep review of low-scoring docs
- User feedback integration
- Update scoring criteria if needed

### Quarterly Review
- Audit all documentation
- Identify systemic issues
- Plan major improvements

## Integration with CI/CD

```yaml
# Example GitHub Action
name: Documentation Quality

on: [push, pull_request]

jobs:
  validate-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Validate Documentation
        run: python scripts/validate_docs.py ./docs --min-score 70

      - name: Check for Drift
        run: python scripts/detect_drift.py . ./docs
```

## Further Reading

- [Write the Docs Style Guide](https://www.writethedocs.org/guide/)
- [Google Developer Documentation Style Guide](https://developers.google.com/style)
- [Microsoft Writing Style Guide](https://docs.microsoft.com/style-guide/)
