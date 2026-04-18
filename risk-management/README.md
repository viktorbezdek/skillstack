# Risk Management

> **v1.0.11** | Strategic Thinking | 11 iterations

> Systematic risk assessment, mitigation planning, and monitoring for projects, products, and organizations -- from identification through response planning to ongoing review.
> Single skill, self-contained methodology

## The Problem

Projects fail not because teams did not see the risks, but because they did not systematically assess and track them. A lead engineer mentions during standup that the new payment provider's API has been unreliable, but nobody writes it down, scores the likelihood and impact, or assigns an owner. Three weeks later the integration fails in production, and the team scrambles for a workaround that should have been planned as a contingency.

Risk management in most teams is either completely absent or reduced to a one-time brainstorm at project kickoff that produces a list nobody revisits. Without a structured assessment matrix, risks are evaluated by gut feeling -- the loudest voice in the room determines what gets attention. Without a risk register, mitigation actions have no owners and no review dates. Without monitoring cadences, trigger conditions go unchecked until the risk materializes and becomes a crisis.

Even teams that attempt risk management often confuse it with worry. They list everything that could go wrong without scoring likelihood and impact, so a catastrophic-but-unlikely risk gets the same attention as a near-certain-but-minor one. The result is either analysis paralysis (everything is "high risk") or false confidence (a long risk list makes people feel thorough while the actual mitigations are vague).

## Context to Provide

Risk identification is contextual -- generic project descriptions produce generic risks. The more specific you are about your situation, team, constraints, and what has already gone wrong, the more targeted and actionable the risk register becomes.

**What information to include in your prompt:**
- **Project description** -- what you are building, migrating, launching, or changing. Be specific about scope: "migrating 12 microservices to Aurora PostgreSQL" is actionable; "doing a database migration" is not.
- **Timeline and deadline type** -- is the deadline hard (contract expiration, regulatory) or soft (planning target)? Hard deadlines change the risk calculus significantly.
- **Team composition and expertise gaps** -- who will do the work, and what do they not know well? A team with no Aurora experience has different technical risks than one that has done similar migrations.
- **Known concerns** -- if you already suspect specific risks, name them. The skill builds on your knowledge rather than duplicating it.
- **Constraints and dependencies** -- what external systems, vendors, approvals, or teams does this project depend on? Dependencies are a primary source of schedule and external risks.
- **Previous incidents or near-misses** -- if similar projects have failed before, or if there was a recent incident that relates to this work, include it. History is the best predictor.

**What makes results better:**
- Describing what "failure" looks like for this specific project (data loss, downtime, missed deadline, stakeholder rejection)
- Mentioning contractual, regulatory, or SLA constraints that bound the acceptable risk level
- Indicating the audience for the risk register (engineering team vs. executive presentation requires different language and level of detail)

**What makes results worse:**
- Generic project names without scope ("help me with risk management for our project")
- Omitting team and expertise context -- the same migration is very different risk for an experienced team vs. a first-timer
- Asking for a risk assessment without indicating any timeline (risk urgency and monitoring cadence depend on it)

**Template prompt (for new project risk assessment):**
```
Build a risk register for this project.

Project: [description -- what we are doing, why, and the expected outcome]
Timeline: [start date, end date, any hard deadlines and why they're hard]
Team: [size, relevant expertise, known skill gaps]
Dependencies: [external APIs, vendors, teams, regulatory approvals, infrastructure]
Constraints: [uptime requirements, data integrity requirements, budget, compliance]

Known concerns we already have:
- [Concern 1]
- [Concern 2]

Previous incidents that are relevant: [any past failures or near-misses on similar work]

Please identify risks across all five categories (Technical, Schedule, Resource, External, Organizational), score each on likelihood and impact, and recommend mitigation strategies with specific actions and owners.
```

**Template prompt (for pre-mortem):**
```
Run a pre-mortem on this project.

Project: [description]
Timeline: [when it should be complete]

Assume it is [date -- the project end date] and the project has failed. Work backward from failure and identify the most likely reasons it went wrong. Convert each finding into a scored risk register entry with a preventive action.

Focus especially on risks that forward-looking analysis tends to miss because of optimism bias.
```

## The Solution

This plugin provides a complete risk management framework: a risk assessment matrix for consistent scoring, five risk categories (Technical, Schedule, Resource, External, Organizational) for comprehensive identification, a risk register template for structured tracking, four mitigation strategies (Avoid, Transfer, Mitigate, Accept) for deliberate response planning, monitoring cadences for ongoing review, and a pre-mortem technique for proactive risk discovery before projects begin.

The skill produces concrete artifacts -- risk registers with scored entries, response plans with trigger conditions and contingency actions, and monitoring schedules with assigned owners and review dates. When you describe a project, migration, product launch, or organizational change, the skill systematically walks through risk identification by category, scores each risk on the likelihood-impact matrix, recommends mitigation strategies, and produces a register you can share with stakeholders.

The pre-mortem technique inverts the usual approach: instead of asking "what could go wrong?", you imagine the project has already failed and work backward to understand why. This surfaces risks that forward-looking analysis misses because it bypasses optimism bias.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Risks discussed verbally but never documented -- forgotten within a week | Risk register with ID, category, score, mitigation action, owner, and status for every identified risk |
| Likelihood and impact assessed by gut feeling -- the loudest voice wins | 3x3 assessment matrix (Low/Med/High) produces consistent, comparable scores across all risks |
| No distinction between "we should worry about this" and "here is the contingency plan" | Four explicit strategies (Avoid, Transfer, Mitigate, Accept) with assigned actions for each risk |
| One-time risk brainstorm at project kickoff, never revisited | Monitoring cadence: daily trigger checks, weekly active reviews, monthly score reassessment, quarterly full review |
| Risk identification limited to what the team thinks of in the moment | Five categories (Technical, Schedule, Resource, External, Organizational) ensure systematic coverage |
| Optimism bias hides real risks -- team assumes things will work out | Pre-mortem technique assumes failure and works backward, surfacing risks that forward analysis misses |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install risk-management@skillstack
```

### Verify installation

After installing, test with:

```
We're migrating our monolith to microservices over the next 6 months. Team: 4 backend engineers, 1 DevOps engineer -- none have done a microservices migration before. Hard deadline: new architecture must be live before Q4 when we plan a 3x traffic event. We're dependent on a third-party message queue vendor we haven't integrated with before. Previous incident: our last infrastructure change caused 4 hours of downtime. Help me identify and assess the risks.
```

The skill should activate and produce a categorized risk register with scored entries and mitigation recommendations.

## Quick Start

1. **Install** the plugin using the commands above
2. **Describe your project or initiative**: `We're launching a new payment system that integrates with Stripe and replaces our legacy billing`
3. The skill **identifies risks** across five categories: Technical (integration complexity), Schedule (API certification delays), Resource (team lacks Stripe expertise), External (regulatory compliance), Organizational (stakeholder alignment)
4. Each risk is **scored** on the likelihood-impact matrix and assigned a mitigation strategy with specific actions
5. You receive a **complete risk register** you can share with your team, plus a monitoring schedule for ongoing review

---

## System Overview

```
User describes project / initiative / change
    │
    ▼
┌──────────────────────────────────────────────────────┐
│              risk-management (skill)                    │
│                                                        │
│  Step 1: IDENTIFY                                      │
│  ┌─────────────────────────────────────────────────┐   │
│  │  Five Risk Categories                            │   │
│  │  Technical | Schedule | Resource | External |    │   │
│  │  Organizational                                  │   │
│  └─────────────────────────────────────────────────┘   │
│          │                                             │
│  Step 2: ASSESS                                        │
│  ┌─────────────────────────────────────────────────┐   │
│  │  3x3 Assessment Matrix                           │   │
│  │  Likelihood (1-3) x Impact (1-3) = Score (1-9)  │   │
│  └─────────────────────────────────────────────────┘   │
│          │                                             │
│  Step 3: RESPOND                                       │
│  ┌─────────────────────────────────────────────────┐   │
│  │  Four Mitigation Strategies                      │   │
│  │  Avoid | Transfer | Mitigate | Accept            │   │
│  │  + trigger conditions + contingency actions      │   │
│  └─────────────────────────────────────────────────┘   │
│          │                                             │
│  Step 4: MONITOR                                       │
│  ┌─────────────────────────────────────────────────┐   │
│  │  Monitoring Cadences                             │   │
│  │  Daily: trigger checks                           │   │
│  │  Weekly: active risk review                      │   │
│  │  Monthly: score reassessment                     │   │
│  │  Quarterly: full register review                 │   │
│  └─────────────────────────────────────────────────┘   │
│                                                        │
│  Optional: PRE-MORTEM                                  │
│  Imagine failure → work backward → convert to risks    │
│                                                        │
│  Output: Risk Register + Response Plans + Schedule     │
└──────────────────────────────────────────────────────┘
```

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `risk-management` | skill | Complete methodology: assessment matrix, five risk categories, risk register template, four mitigation strategies, response template, monitoring cadences, pre-mortem technique |

This is a self-contained plugin -- the complete methodology lives in the SKILL.md body with no reference files needed. The risk register and response templates are embedded directly in the skill for immediate use.

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

### Component Spotlights

#### risk-management (skill)

**What it does:** Activates when you need to identify, assess, and plan responses for risks in projects, products, migrations, launches, or organizational changes. Walks through systematic risk identification by category, scores each risk on a likelihood-impact matrix, recommends mitigation strategies, and produces a structured risk register.

**Input -> Output:** A description of a project, initiative, or change -> A scored risk register with mitigation strategies, response plans with trigger conditions and contingency actions, and a monitoring schedule with owners and review dates.

**When to use:** Starting a new project or initiative. Planning a migration, launch, or infrastructure change. Running a pre-mortem before a critical project begins. Activating a contingency plan when a tracked risk materializes. Assessing organizational risks from team restructuring or strategic changes.

**When NOT to use:** Security vulnerability scanning of code (use dedicated security audit tools). Financial risk modeling requiring quantitative analysis (Monte Carlo, VaR). Real-time incident response during outages (use debugging for troubleshooting).

**Try these prompts:**

```
We're migrating from AWS to GCP over the next quarter -- what are the risks and how do we mitigate them?
```

```
Build a risk register for our upcoming product launch -- we're a 5-person startup shipping our first B2B SaaS product
```

```
Run a pre-mortem on this project: we're replacing our authentication system with Clerk across 3 applications
```

```
This risk register has 20 items but no scores or owners -- help me prioritize and assign mitigation actions
```

```
What are the organizational and resource risks of restructuring our engineering team from feature teams to platform teams?
```

```
We accepted a risk 3 months ago and the trigger conditions are now appearing -- help me activate the contingency plan
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, produces generic output) | Good (specific, produces actionable risk register) |
|---|---|
| "What are the risks of this project?" | "We're migrating 12 microservices to Aurora PostgreSQL with a 10-week deadline and near-zero downtime requirement -- build a risk register" |
| "Help me with risk management" | "Run a pre-mortem on our auth system replacement -- we're switching from custom JWT to Clerk across 3 apps with shared sessions" |
| "Is this risky?" | "Score the likelihood and impact of our vendor dependency on Twilio for SMS -- they had 3 outages last quarter and we have no fallback provider" |
| "What could go wrong?" | "Identify the technical, schedule, and resource risks of launching a new feature that depends on a third-party API we haven't integrated before" |
| "Make a risk plan" | "We have a risk register with 15 items but no monitoring schedule or owners -- add scores, assign mitigation strategies, and set review dates" |

### Structured Prompt Templates

**For new project risk assessment:**
```
We're [project description: migrating / launching / building / restructuring] [scope].
Timeline: [duration]. Team: [size and composition]. Key constraints: [hard deadlines,
compliance, dependencies]. Build a risk register covering all five categories.
```

**For pre-mortem:**
```
Run a pre-mortem on [project description]. Imagine it's [timeline] from now and the
project has failed. What went wrong? Convert the findings into scored risk register
entries with mitigation strategies.
```

**For contingency activation:**
```
We identified [risk description] [timeframe] ago and chose to Accept it with a
contingency plan. The trigger condition [describe what happened] has now occurred.
Help me activate the contingency plan and identify new risks from the response.
```

**For existing risk register improvement:**
```
Here's our current risk register: [paste]. It's missing [scores / owners / mitigation
strategies / monitoring schedule]. Help me complete it with proper scoring and
assigned actions.
```

### Prompt Anti-Patterns

- **Listing concerns without project context:** Saying "is microservices risky?" produces generic advice. Instead, describe your specific situation: team size, timeline, current architecture, constraints. The skill tailors risk identification to your actual circumstances.
- **Asking for risks without specifying the assessment scope:** "What are the risks?" could mean anything from a code change to a company reorganization. Specify what you are assessing -- a migration, a launch, a hiring decision, a vendor change -- so the skill applies the right risk categories.
- **Expecting the skill to replace domain expertise:** The skill provides the framework (categories, matrix, strategies, monitoring), but you provide the domain knowledge. "What are the risks of our Kubernetes migration?" works best when you describe your current infrastructure, team expertise, and constraints.

## Real-World Walkthrough

Your company is planning to migrate from a self-hosted PostgreSQL database to a managed Aurora PostgreSQL instance on AWS. The migration affects 12 microservices, needs to happen with near-zero downtime, and must be completed before the current hosting contract expires in 10 weeks. The engineering team has done database migrations before, but never at this scale and never with a hard deadline.

You open Claude Code and say:

```
We're migrating 12 microservices from self-hosted PostgreSQL to Aurora PostgreSQL. Near-zero downtime required, 10-week deadline. Help me build a risk register.
```

The skill begins with **systematic risk identification** across all five categories.

**Technical risks** come first. The skill identifies: (R1) schema incompatibility between PostgreSQL extensions and Aurora-supported extensions -- some extensions like `pg_cron` or custom C extensions may not be available on Aurora. (R2) Data migration integrity -- 12 services means 12 databases with cross-references, and a partial migration could leave services pointing at inconsistent data. (R3) Connection pooling differences -- Aurora's connection handling differs from self-hosted, and services configured for PgBouncer may need reconfiguration. (R4) Performance regression -- query plans may change under Aurora's optimizer, and the team will not know until production load hits.

**Schedule risks** follow. (R5) 10-week deadline with no buffer -- if any service migration takes longer than estimated, the entire timeline compresses. (R6) Dependency on AWS support for Aurora provisioning and configuration -- if account limits or approval processes delay provisioning, the team cannot start integration testing. (R7) Testing each service sequentially creates a bottleneck -- services 10, 11, and 12 may get rushed testing.

**Resource risks** emerge next. (R8) The team has self-hosted PostgreSQL expertise but limited Aurora-specific knowledge -- connection string patterns, IAM authentication, and failover behavior are different. (R9) The database migration will compete for engineering time with feature development already committed to the product roadmap.

**External risks** include (R10) the hosting contract expiration as a hard deadline with financial penalties for overrun, and (R11) Aurora pricing model uncertainty -- actual costs under production load may exceed estimates.

**Organizational risks** surface (R12) -- stakeholders may not understand the near-zero-downtime constraint and push for a "just do it over a weekend" approach that the technical team knows is too risky.

The skill **scores each risk** on the assessment matrix. R1 (schema incompatibility) gets Likelihood: Medium, Impact: High, Score: 6. R4 (performance regression) gets Likelihood: High, Impact: Medium, Score: 6. R5 (deadline with no buffer) gets Likelihood: High, Impact: High, Score: 9 -- the highest-scored risk in the register.

For each risk, the skill recommends a **mitigation strategy**. R1 gets "Mitigate": run Aurora extension compatibility audit in week 1, identify alternatives for unsupported extensions, and have a fallback plan (RDS PostgreSQL without Aurora features) if critical extensions cannot be replaced. R5 gets "Mitigate": build the migration schedule with two-week buffer by starting immediately, and "Accept" the residual risk with a contingency plan to negotiate a contract extension if needed.

The skill produces a **complete risk register** with all 12 risks scored, categorized, and assigned to owners. It adds a **monitoring schedule**: the database team checks extension compatibility daily during week 1, the project lead reviews migration progress weekly, scores are reassessed at weeks 4 and 8, and a full register review happens at the midpoint (week 5).

Finally, the skill runs a **pre-mortem**: "Imagine it is week 11. The migration failed. What happened?" This surfaces an additional risk: (R13) rollback complexity -- if a migrated service needs to roll back after other services have already written new data to Aurora, the rollback path may corrupt data. This gets scored Critical and assigned an "Avoid" strategy: maintain dual-write capability during the migration window so rollback is always clean.

You now have a 13-entry risk register, a monitoring schedule, and contingency plans for the three highest-scored risks.

## Usage Scenarios

### Scenario 1: Product launch risk assessment

**Context:** You are a product manager preparing to launch a new feature to 50,000 users. The feature involves a third-party API, new database tables, and a billing integration.

**You say:** `Help me build a risk register for our feature launch next month -- it uses a new API from a vendor we haven't worked with before`

**The skill provides:**
- Technical risks (API reliability, rate limits, error handling gaps)
- External risks (vendor SLA, API breaking changes, billing discrepancies)
- Schedule risks (API certification timeline, testing bottleneck)
- Scored risk register with mitigation actions and owners

**You end up with:** A risk register with 8-12 scored entries, mitigation assignments, and a monitoring schedule you can review weekly with the team.

### Scenario 2: Pre-mortem for a critical project

**Context:** Your team is about to start a 3-month project to rebuild the company's search infrastructure. Everyone is optimistic, but you have seen similar projects go sideways before.

**You say:** `Run a pre-mortem on our search infrastructure rebuild -- imagine it's 3 months from now and the project failed`

**The skill provides:**
- Backward analysis from assumed failure to root causes
- Risk identification that bypasses optimism bias
- Conversion of pre-mortem findings into scored risk register entries
- Preventive actions for each identified failure mode

**You end up with:** A set of risks the team would not have identified through forward-looking analysis, each with a concrete preventive action.

### Scenario 3: Organizational change risk assessment

**Context:** The VP of Engineering wants to reorganize from feature teams to platform teams. You need to present the risks to leadership before the reorg is approved.

**You say:** `What are the risks of moving from feature teams to platform teams? I need a risk assessment I can present to the leadership team`

**The skill provides:**
- Resource risks (knowledge silos, skill gaps, team morale)
- Schedule risks (productivity dip during transition, delayed roadmap delivery)
- Organizational risks (unclear ownership during transition, cross-team communication overhead)
- Presentation-ready risk register with executive-level mitigation descriptions

**You end up with:** A structured risk assessment that frames the reorg decision in terms of quantified trade-offs rather than abstract concerns.

### Scenario 4: Activating a contingency plan

**Context:** Three months ago, you identified "vendor API deprecation" as a risk and accepted it with a contingency plan. The vendor just announced the deprecation timeline.

**You say:** `We accepted a risk about our payment vendor deprecating their API and it's happening -- help me activate the contingency plan`

**The skill provides:**
- Transition from the risk register's "Accept" strategy to active response
- Contingency activation checklist (notify stakeholders, assess timeline, mobilize resources)
- Updated risk register reflecting the risk's new status (Triggered)
- New risks that emerge from the response itself (migration risks, testing gaps)

**You end up with:** An activated response plan with clear next steps, timeline, and owner assignments -- not a panic scramble.

---

## Decision Logic

**How does the skill choose which technique to use?**

The skill routes based on your request:
- Describing a project, initiative, or change -> **Full risk assessment** with five-category identification, scoring, mitigation strategies, and monitoring schedule
- Asking for a pre-mortem -> **Pre-mortem technique**: assume failure, work backward, convert findings to scored risk register entries
- Presenting an existing risk list without scores -> **Risk scoring and prioritization**: apply the 3x3 matrix, assign strategies, add owners and review dates
- Reporting that a tracked risk has materialized -> **Contingency activation**: transition from monitoring to active response, generate new risks from the response itself

**How does the scoring system work?**

Likelihood (1 = Low, 2 = Medium, 3 = High) multiplied by Impact (1 = Low, 2 = Medium, 3 = High) produces a Score from 1 to 9. Scores map to priority: 1-2 = Low priority (Accept or monitor), 3-4 = Medium (Mitigate with standard actions), 6-9 = High/Critical (Mitigate aggressively, Avoid, or Transfer). The 3x3 matrix is intentionally simple -- it forces decisive categorization instead of allowing teams to hide behind nuanced 5-point scales.

**When is Avoid vs Mitigate vs Transfer vs Accept the right strategy?**

- **Avoid**: The risk is Critical (score 6-9) and can be eliminated by changing the approach. Example: avoid vendor lock-in risk by using an open-source alternative.
- **Transfer**: The risk involves financial loss or liability that can be shifted. Example: transfer data breach risk through cyber insurance.
- **Mitigate**: The risk cannot be avoided but its likelihood or impact can be reduced. Example: mitigate performance regression risk by running load tests before migration.
- **Accept**: The risk is Low (score 1-2) or the cost of mitigation exceeds the expected impact. Example: accept the risk that a minor UI change confuses some users temporarily.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Risk register becomes a checkbox exercise | Team fills in the register mechanically without real analysis -- every risk gets "Medium/Medium" scores | Challenge the scores: for each "Medium," ask "what specific evidence supports this?" and "what would change this to High?" Use the pre-mortem technique to surface risks the team is unconsciously minimizing. |
| Monitoring schedule is not followed | Risks are identified and scored but nobody checks trigger conditions between reviews | Assign each risk a specific owner with a concrete check action ("run load test against staging Aurora instance every Monday"). Vague monitoring ("keep an eye on it") always fails. |
| Risk register grows indefinitely | Every concern gets added but nothing is ever closed or accepted, creating a 50-item list that nobody reads | At each quarterly review, close resolved risks, merge duplicates, and force an Accept decision on low-score items that have been open for 2+ review cycles. A register over 20 items loses its usefulness. |
| Pre-mortem produces only obvious risks | The team imagines failure but only surfaces risks they already knew about | Push deeper with "why did that happen?" for each failure mode. If "the API failed" is a risk, ask "why did it fail? Was it rate limits, authentication changes, or schema incompatibility?" The second-order causes are where the non-obvious risks hide. |
| Mitigation strategies are vague | Register says "Mitigate: reduce risk" without specific actions, triggers, or owners | Every mitigation must answer three questions: What specific action? Who owns it? By when? "Mitigate: reduce risk" is not a strategy. "Mitigate: run Aurora compatibility audit by end of week 1, owned by DB lead, trigger: any incompatible extension found" is a strategy. |

## Ideal For

- **Engineering leads planning complex migrations or infrastructure changes** -- systematic risk identification catches the risks that "we'll deal with it when it happens" thinking misses
- **Product managers preparing for launches** -- the risk register format produces artifacts that stakeholders understand and can act on
- **Project managers running multi-team initiatives** -- monitoring cadences and owner assignments ensure risks are reviewed, not just identified
- **Anyone running a pre-mortem** -- the backward-from-failure technique surfaces risks that forward-looking analysis misses due to optimism bias

## Not For

- **Security vulnerability scanning** -- use dedicated security audit tools for code-level security risks; this skill handles project and organizational risk
- **Financial risk modeling** -- use specialized financial tools for quantitative risk models (Monte Carlo, VaR); this skill covers qualitative risk assessment
- **Incident response during outages** -- use [debugging](../debugging/) for real-time troubleshooting; this skill is for proactive risk planning, not reactive crisis management

## Related Plugins

- **[Systems Thinking](../systems-thinking/)** -- Analyze problems through feedback loops and leverage points to identify systemic risks that traditional risk assessment misses
- **[Prioritization](../prioritization/)** -- Apply RICE, MoSCoW, and ICE frameworks to prioritize risk mitigation actions when resources are limited
- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate novel mitigation strategies when standard approaches (Avoid, Transfer, Mitigate, Accept) are insufficient
- **[CI/CD Pipelines](../cicd-pipelines/)** -- Implement technical mitigations for deployment risks through automated testing and staged rollouts

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
