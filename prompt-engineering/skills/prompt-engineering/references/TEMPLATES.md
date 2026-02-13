# Reusable Prompt Templates

Library of battle-tested prompt patterns for common use cases.

## Table of Contents
1. Analysis & Research
2. Creative Content
3. Technical Tasks
4. Business & Strategy
5. Education & Training
6. Data Processing
7. Decision Support

---

## 1. Analysis & Research Templates

### Comprehensive Research Template
```
You are a [DOMAIN] research analyst with expertise in [SPECIALIZATION].

**Research Objective:**
[SPECIFIC RESEARCH QUESTION]

**Scope:**
- Time period: [DATE RANGE]
- Geographic focus: [REGIONS]
- Key areas: [LIST AREAS]

**Research Framework:**
1. Background Analysis
   - Current state assessment
   - Historical context
   - Key stakeholders

2. Data Collection
   - Primary sources: [SPECIFY]
   - Secondary sources: [SPECIFY]
   - Validation criteria

3. Analysis Methodology
   - [ANALYTICAL FRAMEWORK]
   - Key metrics
   - Comparison benchmarks

4. Synthesis
   - Pattern identification
   - Trend analysis
   - Implications

**Output Format:**
# [RESEARCH TITLE]

## Executive Summary
[2-3 paragraphs]

## Methodology
[Approach description]

## Findings
### [Category 1]
- Finding with evidence
- Finding with evidence

### [Category 2]
- Finding with evidence

## Analysis
[Detailed interpretation]

## Recommendations
1. [Actionable recommendation]
2. [Actionable recommendation]

## Appendix
- Data sources
- Additional details

**Requirements:**
- Cite all sources
- Use data from [TIME PERIOD]
- Length: [WORD COUNT]
- Evidence-based conclusions only
```

### Competitive Analysis Template
```
Analyze [COMPANY/PRODUCT] competitive landscape.

**Competitors to analyze:**
1. [COMPETITOR 1]
2. [COMPETITOR 2]
3. [COMPETITOR 3]

**Analysis Dimensions:**
- Product features
- Pricing strategy
- Market positioning
- Strengths/weaknesses
- Unique selling propositions

**Deliverable:**
Create comparison table:

| Dimension | Us | Competitor 1 | Competitor 2 | Competitor 3 |
|-----------|----|--------------| -------------|--------------|
| Key Features | | | | |
| Pricing | | | | |
| Target Market | | | | |
| Differentiators | | | | |
| Strengths | | | | |
| Weaknesses | | | | |

**Below table, provide:**
- Strategic insights (3-5 bullets)
- Market gaps/opportunities
- Positioning recommendations

**Sources:** Use current data, cite sources
```

---

## 2. Creative Content Templates

### Blog Post Template
```
Write a [WORD_COUNT]-word blog post about [TOPIC] for [TARGET_AUDIENCE].

**Audience Profile:**
- Role: [JOB TITLE/ROLE]
- Knowledge level: [BEGINNER/INTERMEDIATE/EXPERT]
- Pain points: [LIST]
- Goals: [LIST]

**Post Structure:**

**Title:** [ATTENTION-GRABBING TITLE]

**Hook (100 words):**
- Start with relatable scenario or surprising stat
- State the problem clearly
- Preview the solution

**Body (800 words):**

### Section 1: [SUBTOPIC]
[Educational content with examples]

### Section 2: [SUBTOPIC]
[Practical tips with actionable advice]

### Section 3: [SUBTOPIC]
[Case study or real-world application]

**Conclusion (100 words):**
- Recap key takeaways (3 bullets)
- Clear call-to-action
- Next steps for reader

**Requirements:**
- Conversational tone
- Include 2-3 specific examples
- One actionable tip per section
- SEO: Include keyword [KEYWORD] naturally 3-5 times
- Add 1-2 relevant statistics with sources
```

### Product Description Template
```
Create compelling product description for [PRODUCT_NAME].

**Product Details:**
- Category: [CATEGORY]
- Target customer: [CUSTOMER_PROFILE]
- Key features: [LIST]
- Price point: [PRICE_RANGE]
- Main competitors: [LIST]

**Description Structure:**

**Headline (10-15 words):**
[Benefit-focused hook that grabs attention]

**Opening (50 words):**
- Address customer pain point
- Position product as solution

**Features & Benefits (150 words):**
[For each key feature:]
- **[FEATURE]:** [Benefit in customer language]
  Example: How it helps in real use

**Why Choose Us (75 words):**
- Differentiator 1
- Differentiator 2
- Social proof/trust element

**Call-to-Action:**
[Clear next step]

**Style Guidelines:**
- Tone: [PROFESSIONAL/CASUAL/LUXURY/FUN]
- Voice: Active, benefit-focused
- Language: Simple, jargon-free
- Length: ~300 words total
```

---

## 3. Technical Tasks Templates

### Code Generation Template
```
Generate [LANGUAGE] code for [FUNCTIONALITY].

**Requirements:**
- Language/Framework: [SPECIFY]
- Version: [VERSION]
- Purpose: [DETAILED DESCRIPTION]

**Specifications:**

**Input:**
- Type: [DATA_TYPE]
- Format: [FORMAT]
- Validation: [CONSTRAINTS]

**Output:**
- Type: [DATA_TYPE]
- Format: [FORMAT]
- Success criteria: [CRITERIA]

**Constraints:**
- Performance: [TIME/SPACE COMPLEXITY]
- Dependencies: [ALLOWED_LIBRARIES]
- Compatibility: [PLATFORM/VERSION]

**Code Requirements:**
1. Follow [STYLE_GUIDE] conventions
2. Include comprehensive docstrings
3. Add type hints (if applicable)
4. Handle errors gracefully
5. Write defensive code

**Deliverable:**
```[LANGUAGE]
# [FILE_NAME]

"""
[MODULE DOCSTRING]
"""

# Implementation with inline comments
# explaining non-obvious logic

# Include usage example
if __name__ == "__main__":
    # Example usage
    pass
```

**Testing:**
Include:
- Unit test examples
- Edge case handling
- Performance considerations
```

### Code Review Template
```
Review this [LANGUAGE] code for [PURPOSE].

**Review Criteria:**

1. **Correctness**
   - Logic errors?
   - Edge cases handled?
   - Expected behavior matches actual?

2. **Code Quality**
   - Readability: Clear variable names, comments
   - Maintainability: DRY principle, modularity
   - Style: Follows [STYLE_GUIDE]

3. **Performance**
   - Time complexity: [EXPECTED]
   - Space complexity: [EXPECTED]
   - Optimization opportunities?

4. **Security**
   - Input validation
   - SQL injection risks
   - XSS vulnerabilities
   - Sensitive data handling

5. **Best Practices**
   - Error handling
   - Logging
   - Documentation
   - Testing coverage

**Output Format:**

## Summary
- Overall assessment: [APPROVE/APPROVE_WITH_CHANGES/REJECT]
- Critical issues: [NUMBER]
- Suggestions: [NUMBER]

## Critical Issues (Must Fix)
1. [ISSUE]: [DESCRIPTION]
   - Location: Line X
   - Impact: [SEVERITY]
   - Fix: [SPECIFIC RECOMMENDATION]

## Suggestions (Should Consider)
1. [SUGGESTION]: [REASONING]

## Positive Highlights
- [What was done well]

## Code:
```[LANGUAGE]
[CODE_TO_REVIEW]
```
```

---

## 4. Business & Strategy Templates

### Strategic Plan Template
```
Develop strategic plan for [OBJECTIVE] at [COMPANY].

**Context:**
- Company: [DESCRIPTION]
- Market: [MARKET_DETAILS]
- Current state: [ASSESSMENT]
- Challenge: [SPECIFIC_PROBLEM]

**Strategic Framework:**

## 1. Situation Analysis

### Current State
- Market position
- Key capabilities
- Resource assessment

### SWOT Analysis
**Strengths:**
- [INTERNAL_POSITIVE]

**Weaknesses:**
- [INTERNAL_NEGATIVE]

**Opportunities:**
- [EXTERNAL_POSITIVE]

**Threats:**
- [EXTERNAL_NEGATIVE]

## 2. Strategic Objectives
1. [OBJECTIVE]: [MEASURABLE_OUTCOME]
2. [OBJECTIVE]: [MEASURABLE_OUTCOME]
3. [OBJECTIVE]: [MEASURABLE_OUTCOME]

## 3. Strategic Initiatives

### Initiative 1: [NAME]
- **Goal:** [SPECIFIC_GOAL]
- **Timeline:** [TIMEFRAME]
- **Resources:** [REQUIRED_RESOURCES]
- **KPIs:** [METRICS]
- **Dependencies:** [LIST]

[Repeat for each initiative]

## 4. Implementation Roadmap

**Phase 1 (Months 1-3):**
- [MILESTONE]
- [MILESTONE]

**Phase 2 (Months 4-6):**
- [MILESTONE]
- [MILESTONE]

**Phase 3 (Months 7-12):**
- [MILESTONE]
- [MILESTONE]

## 5. Risk Mitigation
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [RISK] | [H/M/L] | [H/M/L] | [STRATEGY] |

## 6. Success Metrics
- Metric 1: [TARGET]
- Metric 2: [TARGET]
- Metric 3: [TARGET]

**Output:** Professional strategic document (2000-2500 words)
```

### Business Case Template
```
Create business case for [INITIATIVE/INVESTMENT].

**Proposal:**
- Initiative: [NAME]
- Sponsor: [STAKEHOLDER]
- Requested investment: [AMOUNT]
- Timeline: [DURATION]

**Executive Summary** (1 paragraph)
[Problem, solution, expected impact]

**Problem Statement**
- Current situation
- Business impact
- Cost of inaction

**Proposed Solution**
- Description
- Key components
- How it addresses problem

**Benefits Analysis**

**Quantitative Benefits:**
| Benefit | Year 1 | Year 2 | Year 3 | Total |
|---------|--------|--------|--------|-------|
| Revenue increase | $X | $Y | $Z | $TOTAL |
| Cost savings | $X | $Y | $Z | $TOTAL |
| **Net benefit** | **$X** | **$Y** | **$Z** | **$TOTAL** |

**Qualitative Benefits:**
- [STRATEGIC_BENEFIT]
- [OPERATIONAL_BENEFIT]
- [COMPETITIVE_BENEFIT]

**Cost Analysis**
- Initial investment: $[AMOUNT]
- Ongoing costs: $[AMOUNT]/year
- Resource requirements: [HEADCOUNT/INFRASTRUCTURE]

**ROI Calculation**
- Payback period: [MONTHS]
- NPV: $[AMOUNT]
- IRR: [PERCENTAGE]

**Risk Assessment**
| Risk | Mitigation |
|------|------------|
| [RISK] | [STRATEGY] |

**Recommendation**
[APPROVE/DEFER/REJECT] with reasoning
```

---

## 5. Education & Training Templates

### Tutorial/Guide Template
```
Create [BEGINNER/INTERMEDIATE/ADVANCED] tutorial on [TOPIC].

**Learning Objectives:**
By the end, learners will be able to:
1. [SPECIFIC_SKILL]
2. [SPECIFIC_SKILL]
3. [SPECIFIC_SKILL]

**Prerequisites:**
- Knowledge: [REQUIRED_KNOWLEDGE]
- Tools: [REQUIRED_TOOLS]
- Time: [ESTIMATED_TIME]

**Tutorial Structure:**

## Introduction (5%)
- What you'll learn
- Why it matters
- What you'll build/create

## Section 1: [CONCEPT] (20%)

### Explanation
[Clear explanation with analogies]

### Example
[Simple, concrete example]

### Practice
[Guided exercise]

## Section 2: [CONCEPT] (25%)
[Same structure]

## Section 3: [APPLICATION] (30%)

### Bringing It Together
[How concepts connect]

### Hands-On Project
[Step-by-step guided project]

## Section 4: [ADVANCED] (15%)

### Beyond Basics
[Advanced techniques]

### Common Pitfalls
[What to avoid]

## Conclusion (5%)

### Review
[Key takeaways - 3-5 bullets]

### Next Steps
[How to continue learning]

### Resources
[Links to further learning]

**Style Requirements:**
- Use second person ("you will...")
- Include code examples
- Add screenshots/diagrams (describe what they should show)
- Conversational but precise
```

---

## 6. Data Processing Templates

### Data Analysis Template
```
Analyze [DATASET_DESCRIPTION] to [OBJECTIVE].

**Dataset Information:**
- Source: [SOURCE]
- Size: [ROWS × COLUMNS]
- Time period: [RANGE]
- Key variables: [LIST]

**Analysis Framework:**

## 1. Data Exploration

### Descriptive Statistics
For each key variable:
- Distribution
- Central tendency
- Variability
- Outliers

### Data Quality Check
- Missing values: [PERCENTAGE]
- Duplicates: [COUNT]
- Inconsistencies: [ISSUES]

## 2. Analysis Methodology

**Primary Analysis:**
- Method: [STATISTICAL_METHOD]
- Hypothesis: [H0 and H1]
- Significance level: α = 0.05

**Supporting Analyses:**
- [METHOD]: [PURPOSE]
- [METHOD]: [PURPOSE]

## 3. Results

### Key Findings
1. [FINDING with statistical evidence]
   - Test statistic: [VALUE]
   - p-value: [VALUE]
   - Interpretation: [MEANING]

2. [FINDING with statistical evidence]
   [Same structure]

### Visualizations
[Describe recommended charts/graphs]
- Chart 1: [TYPE] showing [INSIGHT]
- Chart 2: [TYPE] showing [INSIGHT]

## 4. Insights

### Patterns Identified
- Pattern 1: [DESCRIPTION with implications]
- Pattern 2: [DESCRIPTION with implications]

### Correlations
- [VARIABLE_A] and [VARIABLE_B]: r = [VALUE], p = [VALUE]
  Interpretation: [STRENGTH and DIRECTION]

### Anomalies
- [UNEXPECTED_FINDING]: [POSSIBLE_EXPLANATION]

## 5. Recommendations

Based on analysis:
1. [ACTIONABLE_RECOMMENDATION]: [EXPECTED_IMPACT]
2. [ACTIONABLE_RECOMMENDATION]: [EXPECTED_IMPACT]

**Caveats:**
- Limitation 1: [DESCRIPTION]
- Limitation 2: [DESCRIPTION]

**Output:** Comprehensive analysis report (1500-2000 words)
```

---

## 7. Decision Support Templates

### Decision Framework Template
```
Evaluate [DECISION] using structured decision framework.

**Decision Context:**
- Decision: [WHAT_NEEDS_TO_BE_DECIDED]
- Stakes: [HIGH/MEDIUM/LOW]
- Timeline: [WHEN_DECISION_NEEDED]
- Stakeholders: [WHO_IS_AFFECTED]

**Options Being Considered:**
1. [OPTION_A]
2. [OPTION_B]
3. [OPTION_C]
4. Status quo (do nothing)

**Evaluation Criteria:**

| Criterion | Weight | Importance |
|-----------|--------|------------|
| [CRITERION_1] | X% | Why it matters |
| [CRITERION_2] | Y% | Why it matters |
| [CRITERION_3] | Z% | Why it matters |

**Scoring:** 1-10 scale for each criterion

## Option Evaluation

### Option 1: [NAME]

**Description:** [DETAILS]

**Scoring:**
| Criterion | Score | Reasoning |
|-----------|-------|-----------|
| [CRITERION] | X/10 | [WHY] |
| Total Weighted | XX/100 | |

**Pros:**
- [ADVANTAGE]: [IMPACT]
- [ADVANTAGE]: [IMPACT]

**Cons:**
- [DISADVANTAGE]: [IMPACT]
- [DISADVANTAGE]: [IMPACT]

**Risk Assessment:**
- Primary risk: [RISK]: Probability [H/M/L], Impact [H/M/L]
- Mitigation: [STRATEGY]

[Repeat for each option]

## Comparison Matrix

| Option | Total Score | Key Strength | Key Weakness | Risk Level |
|--------|-------------|--------------|--------------|------------|
| Option 1 | XX/100 | [STRENGTH] | [WEAKNESS] | [H/M/L] |
| Option 2 | YY/100 | [STRENGTH] | [WEAKNESS] | [H/M/L] |
| Option 3 | ZZ/100 | [STRENGTH] | [WEAKNESS] | [H/M/L] |
| Status Quo | ZZ/100 | [STRENGTH] | [WEAKNESS] | [H/M/L] |

## Recommendation

**Recommended Option:** [OPTION]

**Reasoning:**
1. [PRIMARY_REASON]
2. [SUPPORTING_REASON]
3. [RISK_CONSIDERATION]

**Implementation Considerations:**
- Timeline: [PHASING]
- Quick wins: [IMMEDIATE_ACTIONS]
- Success metrics: [HOW_TO_MEASURE]

**Alternative If Primary Fails:**
[BACKUP_OPTION]: [WHY]
```

---

## Template Customization Guide

### How to Adapt Templates

1. **Replace Placeholders:**
   - [BRACKETS] = Fill with specific details
   - Adjust structure as needed
   - Keep sections relevant to your use case

2. **Scale Complexity:**
   - **Simple task:** Use fewer sections
   - **Complex task:** Add more detail/structure
   - **Professional:** Include all sections

3. **Adjust Tone:**
   - **Formal:** Professional language, structured
   - **Casual:** Conversational, flexible
   - **Technical:** Precise, detailed
   - **Creative:** Expressive, engaging

4. **Modify Length:**
   - Add word count constraints
   - Specify detail level per section
   - Balance depth vs. conciseness

5. **Platform Optimization:**
   - **ChatGPT:** Add conversation starters
   - **Claude:** Use XML tags for structure
   - **Gemini:** Leverage multimodal prompts

### Template Selection Matrix

| Use Case | Best Template | Priority Elements |
|----------|--------------|-------------------|
| Market research | Research Template | Methodology, Sources |
| Content marketing | Blog/Product Template | Audience, SEO |
| Software development | Code Template | Requirements, Tests |
| Business planning | Strategic Plan | Metrics, Timeline |
| Learning content | Tutorial Template | Objectives, Practice |
| Data insights | Analysis Template | Statistical rigor |
| Important choices | Decision Framework | Criteria, Comparison |

### Testing Your Template

1. **Run with test input**
2. **Evaluate output quality**
3. **Identify missing elements**
4. **Refine and iterate**
5. **Document successful patterns**
