# Risk Management

> **v1.0.10** | Strategic Thinking | 11 iterations

Apply risk assessment frameworks, mitigation strategies, risk registers, and monitoring practices.

## What Problem Does This Solve

Projects fail predictably -- third-party dependencies slip, key people leave, integrations break at the worst moment -- yet most teams only react after the damage is done. Ad-hoc risk discussions produce vague worries ("the vendor might be late") without scores, owners, or response plans, and those worries never get tracked. When a risk materializes, the team scrambles because nobody assigned a contingency owner or defined trigger conditions. This skill provides a structured register-based approach that turns gut-level concerns into tracked, scored risks with assigned owners, concrete mitigation strategies, and a monitoring cadence that keeps the register alive.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "What could go wrong with this project?" | Pre-mortem technique: imagine the project already failed, reverse-engineer what went wrong, convert answers to tracked risks with scores and owners |
| "Help me build a risk register for this initiative" | Risk register template with ID, category, likelihood/impact scoring (1-3 scale), mitigation actions, owner, and status columns |
| "How serious is this risk -- should we worry about it?" | 3x3 risk assessment matrix mapping Likelihood x Impact to Low, Medium, High, or Critical severity |
| "What type of risk is this and how should we handle it?" | Five categories (Technical, Schedule, Resource, External, Organizational) and four response strategies (Avoid, Transfer, Mitigate, Accept) with selection guidance |
| "Write a response plan for this specific risk" | Risk response template: description, trigger warning signs, probability, impact, actions, owner, and review date |

## When NOT to Use This Skill

- Structured decision-making with RICE/MoSCoW scoring -- use [prioritization](../prioritization/) instead
- Identifying feedback loops and systemic causes -- use [systems-thinking](../systems-thinking/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install risk-management@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the risk-management skill to build a risk register for our API migration
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `risk`
- `risk assessment`
- `mitigation`
- `contingency planning`
- `uncertainty management`

## What's Inside

This is a focused single-skill plugin with no external references or scripts -- all guidance is in the SKILL.md.

| Component | Purpose |
|---|---|
| **Risk Assessment Matrix** | 3x3 Likelihood x Impact grid classifying combinations as Low, Medium, High, or Critical |
| **Risk Categories** | Five types with examples: Technical (architecture, integration, performance), Schedule (dependencies, estimation), Resource (skills, turnover), External (vendors, regulations), Organizational (priorities, funding) |
| **Risk Register Template** | Markdown table with columns for ID, description, category, likelihood, impact, calculated score, mitigation action, owner, and status |
| **Mitigation Strategies** | Four response strategies (Avoid, Transfer, Mitigate, Accept) with guidance on when to apply each |
| **Risk Response Template** | Structured plan for a single risk: description, trigger signs, probability, impact, response actions, owner, and review date |
| **Monitoring Practices** | Recommended cadence from daily trigger checks through weekly active review, monthly score reassessment, and quarterly full-register reviews |
| **Pre-Mortem Technique** | Three-question future-failure exercise that surfaces risks before a project starts |

## Usage Scenarios

**Scenario 1 -- Kickoff risk register.** A new initiative is starting and the team has no documented risks. The skill runs a pre-mortem exercise ("imagine this project failed -- what went wrong?"), classifies each answer into the five risk categories, scores them on the 3x3 matrix, assigns owners, and produces a risk register the team can track weekly.

**Scenario 2 -- Evaluating a vendor dependency.** You depend on a third-party API that has had two outages this quarter. The skill creates a risk entry (External, High likelihood, High impact = Critical), selects the Mitigate strategy, defines trigger conditions (API response time > 2s for 5 minutes), and documents the contingency (failover to cached data, notify users).

**Scenario 3 -- Architecture migration risk.** You are migrating from a monolith to microservices. The skill identifies Technical risks (integration failures, data consistency), Schedule risks (underestimated decomposition time), and Resource risks (team lacks distributed systems experience), scoring each and recommending whether to Avoid (defer risky splits), Mitigate (add integration tests), or Accept (tolerate temporary performance dip).

**Scenario 4 -- Quarterly register review.** The existing risk register has grown stale with risks still marked "Open" from three months ago. The skill walks through the monitoring cadence: reassess scores (has likelihood changed?), close materialized or resolved risks, surface new risks from recent incidents, and update owners for any personnel changes.

## Related Skills

- **[Systems Thinking](../systems-thinking/)** -- Analyze the feedback loops and systemic structures that generate risks in the first place.
- **[Prioritization](../prioritization/)** -- RICE, MoSCoW, and ICE scoring to decide which risks get mitigation resources first.
- **[Outcome Orientation](../outcome-orientation/)** -- Define measurable outcomes so risk impact can be quantified against actual goals.
- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate unconventional mitigation strategies when standard approaches are insufficient.
- **[Critical Intuition](../critical-intuition/)** -- Detect hidden risks through pattern recognition and bias analysis.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 52 production-grade plugins for Claude Code.
