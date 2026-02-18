# Risk Management

> Apply risk assessment frameworks, mitigation strategies, risk registers, and monitoring practices to identify, assess, and mitigate risks systematically.

## Overview

Every project, product, and business decision carries risk. The difference between teams that succeed and those that get blindsided is not luck -- it is systematic risk identification and mitigation. This skill provides structured frameworks for assessing risks before they become problems, creating actionable mitigation plans, and maintaining ongoing visibility through risk registers and monitoring practices.

This skill is designed for project managers, engineering leads, product owners, and anyone responsible for delivering outcomes under uncertainty. Whether you are kicking off a new initiative, evaluating a technical architecture decision, or preparing for a launch, this skill gives you the tools to think rigorously about what could go wrong and what to do about it.

As part of the SkillStack collection, Risk Management is a core strategic skill that enhances decision-making across domains. It pairs naturally with Prioritization (for risk-weighted priority ranking), Systems Thinking (for understanding cascading risks in complex systems), and any development skill where deployment risk needs assessment.

## What's Included

This skill is self-contained in a single file:

### Core
- **SKILL.md** -- Complete skill definition covering the risk assessment matrix, risk categories, risk register templates, scoring methodology, mitigation strategies, response templates, monitoring cadences, and the pre-mortem technique.

## Key Features

- **Risk Assessment Matrix**: 3x3 likelihood-impact matrix for quick classification into Low, Medium, High, and Critical risk levels
- **Five risk categories**: Technical, Schedule, Resource, External, and Organizational -- ensuring comprehensive coverage
- **Risk Register template**: Ready-to-use markdown table with ID, description, category, likelihood, impact, score, mitigation, owner, and status columns
- **Quantitative scoring**: Likelihood (1-3) x Impact (1-3) scoring system for objective risk ranking
- **Four mitigation strategies**: Avoid, Transfer, Mitigate, and Accept -- with clear guidance on when to use each
- **Risk Response template**: Structured format for documenting triggers, probability, impact, response plans, owners, and review dates
- **Monitoring cadence**: Daily, weekly, monthly, and quarterly review schedule for ongoing risk management
- **Pre-mortem technique**: Prospective hindsight method for proactive risk identification before a project begins

## Usage Examples

Create a risk register for a new project:
```
We're starting a 6-month platform migration from monolith to microservices with a team of 8 engineers. Create a comprehensive risk register covering all five risk categories.
```

Assess risk for a technical decision:
```
We're deciding between building a custom auth system vs. using Auth0. Help me do a risk assessment for both options covering technical, schedule, and resource risks.
```

Run a pre-mortem on a launch:
```
We're launching our new product to 50,000 users next month. Run a pre-mortem exercise: imagine the launch failed badly. What went wrong? Create mitigation plans for each identified risk.
```

Evaluate and update existing risks:
```
Here's our current risk register [paste]. Reassess the scores based on these developments: we lost a senior engineer, the API vendor announced deprecation, and our beta testing showed 3x expected error rates.
```

Design a monitoring plan:
```
We have 12 active risks in our register. Design a monitoring plan with appropriate cadence, trigger conditions, and escalation criteria for each risk level.
```

## Quick Start

1. Describe the project, decision, or initiative you want to assess for risk.
2. The skill will identify risks across all five categories (Technical, Schedule, Resource, External, Organizational).
3. Each risk gets scored on the likelihood-impact matrix with clear rationale.
4. Mitigation strategies are assigned (Avoid, Transfer, Mitigate, Accept) with specific action plans.
5. The output is a structured risk register you can maintain and review on a regular cadence.

## Related Skills

- **Prioritization** -- Use risk scores to inform priority decisions (risk-adjusted RICE scoring)
- **Systems Thinking** -- Understand how risks cascade through interconnected systems
- **Creative Problem-Solving** -- Generate innovative mitigation strategies for novel risks

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install risk-management@skillstack` -- 34 production-grade skills for Claude Code.
