# ADR-{{ADR_NUMBER}}: {{DECISION_TITLE}}

## Status

{{STATUS}}

| Attribute | Value |
|-----------|-------|
| **Date** | {{DATE}} |
| **Decision Makers** | {{DECISION_MAKERS}} |
| **Consulted** | {{CONSULTED}} |
| **Informed** | {{INFORMED}} |

---

## Context

### Background

{{BACKGROUND}}

### Problem Statement

{{PROBLEM_STATEMENT}}

### Constraints

{{#CONSTRAINTS}}
- {{CONSTRAINT}}
{{/CONSTRAINTS}}

### Assumptions

{{#ASSUMPTIONS}}
- {{ASSUMPTION}}
{{/ASSUMPTIONS}}

---

## Decision Drivers

{{#DECISION_DRIVERS}}
- **{{DRIVER}}** - {{IMPORTANCE}}
{{/DECISION_DRIVERS}}

---

## Considered Options

{{#OPTIONS}}
### Option {{OPTION_NUM}}: {{OPTION_NAME}}

{{OPTION_DESCRIPTION}}

**Pros:**
{{#PROS}}
- {{PRO}}
{{/PROS}}

**Cons:**
{{#CONS}}
- {{CON}}
{{/CONS}}

**Estimated Effort:** {{EFFORT}}

**Risk Level:** {{RISK}}

{{/OPTIONS}}

---

## Decision

**Chosen Option:** {{CHOSEN_OPTION}}

### Rationale

{{RATIONALE}}

### Trade-offs Accepted

{{#TRADEOFFS}}
- {{TRADEOFF}}
{{/TRADEOFFS}}

---

## Consequences

### Positive

{{#POSITIVE_CONSEQUENCES}}
- {{CONSEQUENCE}}
{{/POSITIVE_CONSEQUENCES}}

### Negative

{{#NEGATIVE_CONSEQUENCES}}
- {{CONSEQUENCE}}
{{/NEGATIVE_CONSEQUENCES}}

### Neutral

{{#NEUTRAL_CONSEQUENCES}}
- {{CONSEQUENCE}}
{{/NEUTRAL_CONSEQUENCES}}

---

## Implementation

### Action Items

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
{{#ACTION_ITEMS}}
| {{ACTION}} | @{{OWNER}} | {{DUE}} | {{STATUS}} |
{{/ACTION_ITEMS}}

### Migration Plan

{{MIGRATION_PLAN}}

### Rollback Plan

{{ROLLBACK_PLAN}}

---

## Validation

### Success Criteria

{{#SUCCESS_CRITERIA}}
- [ ] {{CRITERION}}
{{/SUCCESS_CRITERIA}}

### Metrics to Track

| Metric | Baseline | Target | Measurement |
|--------|----------|--------|-------------|
{{#METRICS}}
| {{METRIC}} | {{BASELINE}} | {{TARGET}} | {{MEASUREMENT}} |
{{/METRICS}}

### Review Date

{{REVIEW_DATE}}

---

## Related Decisions

{{#RELATED_ADRS}}
- [ADR-{{NUMBER}}]({{URL}}): {{TITLE}} - {{RELATIONSHIP}}
{{/RELATED_ADRS}}

---

## Notes

{{NOTES}}

---

## Revision History

| Date | Author | Change |
|------|--------|--------|
{{#REVISIONS}}
| {{DATE}} | @{{AUTHOR}} | {{CHANGE}} |
{{/REVISIONS}}
