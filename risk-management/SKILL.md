---
name: risk-management
description: Apply risk assessment frameworks, mitigation strategies, risk registers, and monitoring practices. Use when identifying project risks, planning contingencies, evaluating decisions, creating risk registers, or managing uncertainty. Triggers include risk assessment, mitigation, risk register, contingency planning, and uncertainty management.
---

# Risk Management

Identify, assess, and mitigate risks systematically.

## Risk Assessment Matrix

```
           IMPACT
           Low    Med    High
LIKELIHOOD
High       Med    High   Critical
Med        Low    Med    High
Low        Low    Low    Med
```

## Risk Categories

| Category | Examples |
|----------|----------|
| Technical | Architecture, integration, performance |
| Schedule | Dependencies, estimation, resources |
| Resource | Skills, availability, turnover |
| External | Vendors, regulations, market |
| Organizational | Priorities, funding, politics |

## Risk Register Template

```markdown
## Risk Register

| ID | Risk | Category | Likelihood | Impact | Score | Mitigation | Owner | Status |
|----|------|----------|------------|--------|-------|------------|-------|--------|
| R1 | [desc] | Technical | High | Med | 6 | [action] | [name] | Open |
| R2 | [desc] | Schedule | Med | High | 6 | [action] | [name] | Open |
```

### Scoring
- Likelihood: 1 (Low) - 3 (High)
- Impact: 1 (Low) - 3 (High)
- Score = Likelihood x Impact

## Mitigation Strategies

| Strategy | When to Use |
|----------|-------------|
| **Avoid** | Eliminate the risk entirely |
| **Transfer** | Shift to third party (insurance) |
| **Mitigate** | Reduce likelihood or impact |
| **Accept** | Acknowledge and monitor |

## Risk Response Template

```markdown
## Risk: [Name]

**Description**: [what could go wrong]
**Trigger**: [warning signs]
**Probability**: [%]
**Impact**: [consequence]

### Response Plan
- **Strategy**: [avoid/transfer/mitigate/accept]
- **Actions**:
  1. [preventive action]
  2. [contingency if occurs]
- **Owner**: [responsible person]
- **Review date**: [when to reassess]
```

## Monitoring Practices

| Frequency | Activity |
|-----------|----------|
| Daily | Check trigger conditions |
| Weekly | Review active risks |
| Monthly | Reassess scores |
| Quarterly | Full register review |

## Pre-Mortem Technique

Before project starts, imagine it failed.
1. What went wrong?
2. Why did it happen?
3. What could we have done?

Convert answers to risks and mitigations.

