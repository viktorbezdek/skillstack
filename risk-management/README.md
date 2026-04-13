# Risk Management

> **v1.0.10** | Strategic Thinking | 11 iterations

> Systematic risk assessment, mitigation planning, and monitoring for projects, products, and organizations -- from identification through response planning to ongoing review.

## The Problem

Projects fail not because teams did not see the risks, but because they did not systematically assess and track them. A lead engineer mentions during standup that the new payment provider's API has been unreliable, but nobody writes it down, scores the likelihood and impact, or assigns an owner. Three weeks later the integration fails in production, and the team scrambles for a workaround that should have been planned as a contingency.

Risk management in most teams is either completely absent or reduced to a one-time brainstorm at project kickoff that produces a list nobody revisits. Without a structured assessment matrix, risks are evaluated by gut feeling -- the loudest voice in the room determines what gets attention. Without a risk register, mitigation actions have no owners and no review dates. Without monitoring cadences, trigger conditions go unchecked until the risk materializes and becomes a crisis.

Even teams that attempt risk management often confuse it with worry. They list everything that could go wrong without scoring likelihood and impact, so a catastrophic-but-unlikely risk gets the same attention as a near-certain-but-minor one. The result is either analysis paralysis (everything is "high risk") or false confidence (a long risk list makes people feel thorough while the actual mitigations are vague).

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
We're migrating our monolith to microservices over the next 6 months -- help me identify and assess the risks
```

The skill should activate and produce a categorized risk register with scored entries and mitigation recommendations.

## Quick Start

1. **Install** the plugin using the commands above
2. **Describe your project or initiative**: `We're launching a new payment system that integrates with Stripe and replaces our legacy billing`
3. The skill **identifies risks** across five categories: Technical (integration complexity), Schedule (API certification delays), Resource (team lacks Stripe expertise), External (regulatory compliance), Organizational (stakeholder alignment)
4. Each risk is **scored** on the likelihood-impact matrix and assigned a mitigation strategy with specific actions
5. You receive a **complete risk register** you can share with your team, plus a monitoring schedule for ongoing review

## What's Inside

This is a single-skill plugin with no reference files -- the complete methodology is contained in the SKILL.md body.

| Component | Purpose |
|---|---|
| `SKILL.md` | Risk assessment matrix, five risk categories, risk register template, four mitigation strategies, risk response template, monitoring cadences, pre-mortem technique |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

### risk-management

**What it does:** Activates when you need to identify, assess, and plan responses for risks in projects, products, migrations, launches, or organizational changes. The skill walks through systematic risk identification by category, scores each risk on a likelihood-impact matrix, recommends mitigation strategies, and produces a structured risk register with owners and review dates.

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

The skill **scores each risk** on the assessment matrix. R1 (schema incompatibility) gets Likelihood: Medium, Impact: High, Score: 6 -- it is likely that at least one extension is incompatible, and the impact is a blocked migration path for that service. R4 (performance regression) gets Likelihood: High, Impact: Medium, Score: 6 -- query plan changes are almost certain, but the impact is degraded performance rather than outright failure.

For each risk, the skill recommends a **mitigation strategy**. R1 gets "Mitigate": run Aurora extension compatibility audit in week 1, identify alternatives for unsupported extensions, and have a fallback plan (RDS PostgreSQL without Aurora features) if critical extensions cannot be replaced. R5 (deadline with no buffer) gets "Mitigate": build the migration schedule with two-week buffer by starting immediately, and "Accept" the residual risk with a contingency plan to negotiate a contract extension if needed.

The skill produces a **complete risk register** with all 12 risks scored, categorized, and assigned to owners. It adds a **monitoring schedule**: the database team checks extension compatibility daily during week 1, the project lead reviews migration progress weekly, scores are reassessed monthly (weeks 4 and 8), and a full register review happens at the midpoint (week 5).

Finally, the skill runs a **pre-mortem**: "Imagine it is week 11. The migration failed. What happened?" This surfaces an additional risk the team had not considered: (R13) rollback complexity -- if a migrated service needs to roll back to the old database after other services have already migrated and written new data to Aurora, the rollback path may corrupt data. This gets scored Critical and assigned an "Avoid" strategy: maintain dual-write capability during the migration window so rollback is always clean.

You now have a 13-entry risk register, a monitoring schedule, and contingency plans for the three highest-scored risks, all in a format you can paste directly into a project plan.

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

## Ideal For

- **Engineering leads planning complex migrations or infrastructure changes** -- systematic risk identification catches the risks that "we'll deal with it when it happens" thinking misses
- **Product managers preparing for launches** -- the risk register format produces artifacts that stakeholders understand and can act on
- **Project managers running multi-team initiatives** -- monitoring cadences and owner assignments ensure risks are reviewed, not just identified
- **Anyone running a pre-mortem** -- the backward-from-failure technique surfaces risks that forward-looking analysis misses due to optimism bias

## Not For

- **Security vulnerability scanning** -- use dedicated security audit tools for code-level security risks; this skill handles project and organizational risk
- **Financial risk modeling** -- use specialized financial tools for quantitative risk models (Monte Carlo, VaR); this skill covers qualitative risk assessment
- **Incident response during outages** -- use [debugging](../debugging/) for real-time troubleshooting; this skill is for proactive risk planning, not reactive crisis management

## How It Works Under the Hood

The plugin is a compact single-skill plugin with no reference files. The SKILL.md body contains the complete risk management methodology: the 3x3 assessment matrix, five risk categories, risk register template with scoring, four mitigation strategies, risk response template with trigger conditions and contingency planning, monitoring frequency table, and the pre-mortem technique. This design means the full methodology is available in every interaction without needing progressive disclosure.

The risk register template uses a standardized format (ID, Risk, Category, Likelihood, Impact, Score, Mitigation, Owner, Status) that maps directly to project management tools and spreadsheets. The scoring system (Likelihood 1-3 x Impact 1-3 = Score 1-9) is simple enough for non-technical stakeholders to understand while providing sufficient granularity for prioritization.

## Related Plugins

- **[Systems Thinking](../systems-thinking/)** -- Analyze problems through feedback loops and leverage points to identify systemic risks that traditional risk assessment misses
- **[Prioritization](../prioritization/)** -- Apply RICE, MoSCoW, and ICE frameworks to prioritize risk mitigation actions when resources are limited
- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate novel mitigation strategies when standard approaches (Avoid, Transfer, Mitigate, Accept) are insufficient
- **[CI/CD Pipelines](../cicd-pipelines/)** -- Implement technical mitigations for deployment risks through automated testing and staged rollouts

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
