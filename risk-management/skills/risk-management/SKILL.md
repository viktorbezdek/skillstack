---
name: risk-management
description: >-
  Systematically assess and mitigate risks using risk registers, probability-impact
  matrices, mitigation strategies, and contingency plans. Use when the user asks to
  assess risks, build a risk register, plan for failure modes, evaluate downside
  scenarios, prepare contingency plans, or quantify uncertainty before a decision
  or launch. NOT for finding conceptual flaws or blind spots in ideas (use critical-intuition).
  NOT for security vulnerability auditing in code (use code-review). NOT for identifying
  boundary conditions in code (use edge-case-coverage).
---

# Risk Management

Identify, assess, and mitigate risks systematically.

## When to use this skill

- Starting a new project or initiative — before committing resources
- Planning a migration, launch, or infrastructure change
- Running a pre-mortem before a critical project begins
- Assessing organizational risks from restructuring or strategic changes
- Activating a contingency plan when a tracked risk materializes
- Building a risk register from an existing list of concerns

## When NOT to use this skill

- **Security vulnerability scanning** → use dedicated security audit tools
- **Financial risk modeling (Monte Carlo, VaR)** → use specialized quantitative tools
- **Real-time incident response** → use debugging/troubleshooting workflows
- **Finding conceptual flaws in ideas** → use `critical-intuition`
- **Edge-case coverage in code** → use `edge-case-coverage`

---

## Decision tree

```
What are you trying to do?
  │
  ├─ Assess risks for a NEW project/initiative
  │   └─ Full risk assessment: identify by category → score → mitigate → monitor
  │
  ├─ Imagine the project already FAILED and find out why
  │   └─ Pre-mortem technique (see below)
  │
  ├─ Score and prioritize an EXISTING list of concerns
  │   └─ Apply 3x3 matrix → assign strategies → add owners and review dates
  │
  └─ A tracked risk has MATERIALIZED
      └─ Contingency activation: execute response → update register → surface new risks
```

---

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
- 1-2: Low priority (Accept/monitor), 3-4: Medium (Mitigate), 6-9: High/Critical (Avoid/Mitigate/Transfer)

## Mitigation Strategies

| Strategy | When to Use | Example |
|----------|-------------|---------|
| **Avoid** | Risk is Critical (6-9) and can be eliminated by changing approach | Use open-source alternative to avoid vendor lock-in |
| **Transfer** | Risk involves financial loss or liability that can be shifted | Cyber insurance for data breach risk |
| **Mitigate** | Risk cannot be avoided but likelihood/impact can be reduced | Run load tests before migration to reduce performance regression risk |
| **Accept** | Risk is Low (1-2) or mitigation cost exceeds expected impact | Minor UI change may confuse some users temporarily |

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
1. What went wrong? — list specific failure modes (not "it failed" but "the database migration corrupted production data")
2. Why did it happen? — trace each failure to a root cause; ask "why?" three times
3. What could we have done? — convert each finding into a preventive action with an owner

Convert answers to risks and mitigations. The pre-mortem bypasses optimism bias because starting from assumed failure removes the temptation to say "that probably won't happen."

**When to run a pre-mortem**: before any project with a hard deadline, irreversible commitment, or budget > 2 team-months.

## Anti-Patterns with Solutions

1. **Medium-Medium everything** — every risk gets scored "Medium/Medium" without analysis, making the register useless for prioritization.
   - **Solution**: for each "Medium," demand evidence: "what specific fact supports this score? What would change it to High?" If no evidence exists, the score is a guess — gather data before scoring.

2. **Vague mitigations** — "Mitigate: reduce risk" without specific actions, triggers, or owners.
   - **Solution**: every mitigation must answer four questions: What specific action? Who owns it? By when? What trigger activates it? Example: "Mitigate: run Aurora compatibility audit by end of week 1 (owned by DB lead), trigger: any incompatible extension found."

3. **Register as checkbox exercise** — team fills it mechanically and never revisits.
   - **Solution**: assign each risk a specific owner with a concrete check action (not "keep an eye on it" but "run load test against staging every Monday"); schedule quarterly reviews that close resolved risks and force Accept decisions on stale items.

4. **Optimism bias** — forward-looking analysis misses risks because "things usually work out."
   - **Solution**: use the pre-mortem technique; it bypasses optimism bias by starting from assumed failure.

5. **Infinite register growth** — every concern gets added, nothing is ever closed.
   - **Solution**: cap at 20 items; at each review, close resolved risks, merge duplicates, and force decisions on items open for 2+ cycles. A register over 20 items loses its usefulness.

6. **Single-category tunnel vision** — only technical risks get identified, ignoring schedule, resource, external, and organizational risks.
   - **Solution**: systematically walk all five categories during identification; use the category table as a checklist, not a suggestion.
