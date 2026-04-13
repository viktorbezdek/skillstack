# Prioritization

> **v1.0.10** | Strategic Thinking | 11 iterations

---

## The Problem

Every team has more ideas than capacity. The backlog grows faster than the team can ship, and without a principled way to decide what comes first, prioritization degrades into politics. The highest-paid person's opinion (HiPPO) wins. The loudest customer gets their feature next. The most recent request displaces work that has been planned for weeks. Last quarter's half-finished initiative gets continued because of sunk cost, not because it is still the best use of time.

The consequences are expensive. Teams work on medium-impact features while high-impact ones wait. Quick wins that could be shipped in a day sit in the backlog behind multi-month projects. Engineering capacity is consumed by features that reach few users while features that would affect thousands are deprioritized because nobody scored them. When stakeholders ask "why are we building this and not that?", the answer is narrative ("the customer asked for it") rather than analytical ("it scores 3x higher on reach, impact, and confidence").

Most teams know about RICE, MoSCoW, and ICE but do not apply them consistently. They run a scoring exercise once, then abandon it when the next urgent request arrives. The frameworks feel heavyweight because nobody standardized the scales, documented the rationale, or made scoring a repeatable process. Without embedded frameworks that integrate into decision-making cadence, prioritization remains an occasional ritual rather than a continuous discipline.

## The Solution

The Prioritization plugin gives Claude expertise in four prioritization frameworks -- RICE scoring, MoSCoW categorization, ICE scoring, and the Effort-Impact matrix -- with standardized scales, scoring templates, and decision logic. It transforms ad hoc prioritization into a repeatable, defensible process.

The plugin provides a single focused skill that activates when you need to rank features, score initiatives, categorize requirements, or create effort-impact matrices. It includes the RICE formula (Reach x Impact x Confidence / Effort) with calibrated scales, MoSCoW with the 60% effort rule for Must-haves, ICE with averaged scoring, the Effort-Impact quadrant matrix (Quick Wins -> Big Bets -> Fill Ins -> avoid Money Pits), a prioritization template with decision rationale, and anti-pattern detection for HiPPO, recency bias, squeaky wheel, and sunk cost fallacies.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| HiPPO decides: the VP's pet feature wins regardless of impact | RICE scoring with documented reach, impact, confidence, and effort -- decisions are analytical, not political |
| All requirements feel equally important -- no way to distinguish "must have" from "nice to have" | MoSCoW categorization with the 60% rule: Must-haves cannot exceed 60% of total effort |
| Quick wins languish in the backlog behind multi-month projects | Effort-Impact matrix surfaces Quick Wins (high impact, low effort) for immediate action |
| No standardized scoring -- every conversation reinvents the evaluation criteria | Calibrated scales: RICE impact 0.25-3, ICE 1-10, MoSCoW with explicit definitions |
| Sunk cost keeps zombie projects alive: "we already invested 3 months" | Anti-pattern detection flags sunk cost reasoning and redirects to forward-looking impact assessment |
| Stakeholders cannot explain why feature A was prioritized over feature B | Prioritization template with scored rationale: reach, impact, confidence, effort, and decision narrative |

## Installation

Add the marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install prioritization@skillstack
```

### Prerequisites

None. For defining the outcomes that prioritization serves, also install `outcome-orientation`. For defining the personas whose needs inform impact scoring, also install `persona-definition`.

### Verify installation

After installing, test with:

```
I have 8 feature requests and capacity for 3 this quarter. Help me score and prioritize them using RICE.
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `Prioritize our backlog: search improvements, onboarding redesign, API v2, mobile push notifications, SSO integration. We have 2 engineers for 3 months.`
3. The skill scores each item using RICE and places them on an effort-impact matrix
4. You receive a ranked list with scores, rationale, and a recommended order of execution
5. Next, try: `Our PM insists we build the CEO's pet feature next -- help me use data to push back constructively`

---

## System Overview

```
prioritization/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
└── skills/
    └── prioritization/
        ├── SKILL.md         # Core skill (RICE, MoSCoW, ICE, Effort-Impact, templates, anti-patterns)
        └── evals/
            ├── trigger-evals.json   # 13 trigger evaluation cases
            └── evals.json           # 3 output evaluation cases
```

A single skill with no additional references. The SKILL.md contains the complete prioritization framework: four frameworks (RICE, MoSCoW, ICE, Effort-Impact), calibrated scales, the prioritization template, and anti-pattern detection.

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `prioritization` | Skill | RICE scoring, MoSCoW categorization, ICE scoring, Effort-Impact matrix, prioritization template, anti-patterns |

### Component Spotlight

#### prioritization (skill)

**What it does:** Activates when you need to rank, score, or categorize work items for decision-making. Provides four frameworks with calibrated scales, a scoring template with decision rationale, and anti-pattern detection for common prioritization failures.

**Input -> Output:** A list of features, initiatives, or requirements with context -> Scored and ranked items with framework-appropriate analysis, effort-impact placement, and recommended execution order with rationale.

**When to use:**
- Scoring features or initiatives to decide quarterly priorities
- Categorizing requirements as Must/Should/Could/Won't for a release
- Creating effort-impact matrices for sprint planning
- Defending prioritization decisions to stakeholders with data
- Auditing existing prioritization for bias (HiPPO, recency, squeaky wheel)

**When NOT to use:**
- Defining OKRs or success metrics (use `outcome-orientation`)
- Assessing project risks (use `risk-management`)
- Detailed project estimation and task breakdown (use a project management tool)
- Stakeholder analysis for whose input to weight in scoring (use `persona-mapping`)

**Try these prompts:**

```
Score these 6 features using RICE: real-time notifications, bulk data export, SSO integration, advanced search, API rate limiting, onboarding wizard
```

```
Categorize our release requirements using MoSCoW -- we have 15 items and 60% of capacity is already committed to must-haves
```

```
Create an effort-impact matrix for our sprint backlog -- I need to identify the quick wins we should do first
```

```
Our backlog prioritization is driven by whoever complains loudest. Help me introduce a RICE scoring process the team will actually follow.
```

```
Is ICE or RICE better for a small startup with limited data on reach and confidence? We need something lightweight.
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Help me prioritize" | "Score these 5 features using RICE. Reach data: [estimates]. I need a ranked list with rationale for the top 3." |
| "What should we build?" | "We have capacity for 3 features this quarter. Here are 8 options with rough effort estimates. Help me pick using effort-impact analysis." |
| "Is this important?" | "Compare SSO integration (reaches 200 enterprise users, 2 months effort) vs search improvements (reaches 5000 users, 1 month effort) using RICE." |
| "Prioritize my backlog" | "Apply MoSCoW to these 12 requirements for our v2 release. Budget constraint: Must-haves cannot exceed 60% of the 4-month timeline." |

### Structured Prompt Templates

**For RICE scoring:**
```
Score these features using RICE: [list features]. For each, provide your best estimate of: Reach (users affected per quarter), Impact (0.25-3 scale), Confidence (50-100%). I'll provide effort estimates: [list efforts in person-months].
```

**For MoSCoW categorization:**
```
Categorize these requirements for [release/project]: [list requirements]. Total capacity: [person-months]. Constraint: Must-haves <= 60% of capacity. Context: [business priorities, user feedback, competitive pressure].
```

**For effort-impact matrix:**
```
Place these items on an effort-impact matrix: [list items with rough effort and impact descriptions]. Identify: quick wins (do first), big bets (plan carefully), fill-ins (if time permits), money pits (avoid).
```

### Prompt Anti-Patterns

- **Providing features without context** -- "prioritize A, B, C" without reach, impact, or effort data forces the skill to guess; provide whatever data you have, even rough estimates
- **Asking the skill to decide without scoring** -- "should we build search or SSO?" is a decision question; provide the data and let the framework score them, then you decide
- **Using RICE when you have no reach data** -- if you cannot estimate reach, use ICE (which averages three subjective scores) instead of RICE
- **Ignoring the 60% rule for MoSCoW** -- marking everything as "Must" defeats the purpose; the skill enforces the constraint that Must-haves cannot exceed 60% of capacity

## Real-World Walkthrough

**Starting situation:** You are a product manager at a B2B SaaS company. The Q3 planning session is next week. You have 12 feature requests from customers, sales, engineering, and executive leadership. The engineering team has 3 engineers for 3 months (9 person-months of capacity). Everyone thinks their feature should be next, and the previous quarter's priorities were set by the CEO's intuition. You need a defensible, data-driven ranking.

**Step 1: Gathering scoring data.** You ask: "I need to prioritize 12 features for Q3 using RICE. Here they are with my best effort estimates. Help me score them."

You provide the list:
1. Advanced search (2 PM), 2. Onboarding redesign (3 PM), 3. API v2 (4 PM), 4. SSO integration (2 PM), 5. Mobile push notifications (1.5 PM), 6. Bulk data export (1 PM), 7. Custom dashboards (3 PM), 8. Audit logging (1.5 PM), 9. Slack integration (1 PM), 10. PDF reports (0.5 PM), 11. Dark mode (0.5 PM), 12. AI-powered insights (5 PM)

The skill prompts you for reach and impact estimates per feature. You provide rough numbers based on customer requests, usage data, and sales feedback.

**Step 2: RICE scoring.** The skill calculates RICE for each feature. Results (simplified):

| Feature | Reach | Impact | Confidence | Effort | RICE Score |
|---|---|---|---|---|---|
| Bulk data export | 3000 | 2 | 90% | 1 | 5400 |
| Advanced search | 5000 | 2 | 80% | 2 | 4000 |
| PDF reports | 2000 | 1 | 90% | 0.5 | 3600 |
| Onboarding redesign | 1000 | 3 | 70% | 3 | 700 |
| SSO integration | 200 | 3 | 90% | 2 | 270 |
| ... | ... | ... | ... | ... | ... |

Bulk data export scores highest -- high reach (most users need it), straightforward (high confidence), low effort. Advanced search is second. PDF reports is a quick win. AI-powered insights scores low despite excitement because confidence is 50% and effort is 5 PM.

**Step 3: Effort-Impact matrix.** The skill plots the 12 features on the quadrant matrix:
- **Quick Wins (high impact, low effort):** Bulk data export, PDF reports, Slack integration
- **Big Bets (high impact, high effort):** Advanced search, Onboarding redesign, API v2
- **Fill-Ins (low impact, low effort):** Dark mode, Mobile push notifications
- **Money Pits (low impact, high effort):** AI-powered insights, Custom dashboards

The skill recommends: execute Quick Wins first (they fit in ~2.5 PM and deliver immediate value), then invest remaining capacity in the top Big Bet (Advanced search at 2 PM). Total: 4.5 PM of the 9 PM capacity used on the highest-impact items.

**Step 4: MoSCoW for the quarter.** The skill categorizes using the 60% rule (5.4 PM for Must-haves):
- **Must:** Bulk data export (1 PM), Advanced search (2 PM), PDF reports (0.5 PM) = 3.5 PM (39% of capacity)
- **Should:** Onboarding redesign (3 PM), SSO integration (2 PM)
- **Could:** Slack integration (1 PM), Audit logging (1.5 PM)
- **Won't (this quarter):** AI insights, Custom dashboards, Dark mode, Mobile push

Remaining capacity (5.5 PM) goes to Should items, fitting the onboarding redesign (3 PM) and SSO integration (2 PM) for a total of 8.5 PM committed.

**Step 5: Anti-pattern audit.** The skill checks for bias:
- HiPPO: AI-powered insights was the CEO's pet project but scores lowest on RICE. The data provides a constructive way to defer it: "High potential but low confidence -- let's run a prototype next quarter to increase confidence before committing 5 PM."
- Recency bias: Slack integration was requested last week and nearly displaced the long-planned search improvement. RICE scoring shows search scores 4x higher.
- Sunk cost: Custom dashboards had 1 PM invested in Q2 prototyping. The skill flags that prior investment does not change the forward-looking RICE score -- it is still a Money Pit.

**Step 6: Stakeholder communication.** The skill generates a prioritization template for each feature showing the RICE score, quadrant placement, and decision rationale. This document replaces "the PM decided" with "here's the scoring and data."

**Final outcome:** A Q3 roadmap with 5 features prioritized by RICE scoring and effort-impact analysis, anti-pattern audit removing three bias-driven items, and a stakeholder-ready document with scored rationale for every decision. Planning session goes from 3 hours of debate to 45 minutes of review.

**Gotchas discovered:** The skill flagged that SSO integration has low RICE reach (200 enterprise users) but might be a strategic requirement (enterprise sales depends on it). RICE alone does not capture strategic value -- the skill suggested using MoSCoW to override the RICE ranking for strategic items, with explicit documentation of the override reason.

## Usage Scenarios

### Scenario 1: Sprint planning with quick wins

**Context:** Your sprint has 10 candidate items and capacity for 5. You need to identify the quick wins that deliver the most value with the least effort.

**You say:** "Place these 10 items on an effort-impact matrix for our 2-week sprint. I want to start with quick wins."

**The skill provides:**
- Effort-Impact quadrant placement for all 10 items
- Quick Wins highlighted for immediate execution
- Big Bets flagged for future sprint planning (not this sprint)
- Money Pits flagged to remove from the backlog entirely
- Recommended sprint composition: 3 Quick Wins + 1 Big Bet (if capacity permits)

**You end up with:** A sprint loaded with high-impact, low-effort items instead of the default "continue whatever was started last sprint."

### Scenario 2: Choosing between RICE and ICE

**Context:** You are at an early-stage startup with 50 users. You have no reliable reach data and only rough intuition about impact. RICE feels too data-heavy.

**You say:** "We're a 50-user startup with limited data. Is RICE or ICE better for us? We need something we'll actually use weekly."

**The skill provides:**
- Recommendation: ICE for now. It uses three subjective 1-10 scores (Impact, Confidence, Ease) averaged together -- no reach data needed.
- Transition plan: switch to RICE when you have 500+ users and usage analytics that can estimate reach per feature
- ICE scoring template for the 8 features in your backlog
- Warning: ICE is more susceptible to bias (all scores are subjective); mitigate by having 3 team members score independently and average

**You end up with:** A lightweight prioritization framework you can run in 15 minutes at the start of each week, with a clear upgrade path to RICE as data matures.

### Scenario 3: Defending against HiPPO

**Context:** The VP of Sales wants to build a custom reporting feature for one large prospect. Your RICE analysis shows it scores low (reach: 1 customer, effort: 3 months). You need a constructive way to push back.

**You say:** "The VP wants us to build custom reporting for one prospect. RICE score is low but they're pushing hard. How do I constructively push back?"

**The skill provides:**
- RICE comparison: custom reporting (score: 45) vs the top-scored alternative (score: 5400) -- 120x difference
- Reframe: "Is this a product feature or a sales concession? If it's a sales concession, fund it from the sales budget, not engineering capacity."
- Compromise option: build a lightweight export feature (1 week) that addresses 80% of the prospect's need at 10% of the custom reporting cost
- Anti-pattern label: this is HiPPO + squeaky wheel combined; provide the data and let the framework make the case

**You end up with:** A data-backed pushback with a compromise option, so the conversation shifts from "my opinion vs your opinion" to "here are the scores and tradeoffs."

---

## Decision Logic

**When to use which framework?**

- **RICE** -- when you have data on reach (users affected) and need quantitative rigor. Best for quarterly planning at scale (100+ users). Most defensible with stakeholders because it separates reach from impact from confidence.
- **ICE** -- when you lack reach data or need a lightweight framework for weekly decisions. Best for early-stage startups or small teams. More subjective but faster.
- **MoSCoW** -- when you need to categorize requirements for a specific release with a capacity constraint. Best for release planning and scope management. The 60% rule prevents scope creep.
- **Effort-Impact matrix** -- when you need a quick visual sort for sprint-level decisions. Best for sprint planning and identifying quick wins vs money pits.

Use RICE or ICE for quarterly prioritization, MoSCoW for release scoping, and Effort-Impact for sprint-level decisions. They complement, not replace, each other.

**When this skill vs outcome-orientation?**

Use `outcome-orientation` to define WHAT outcomes to measure. Use `prioritization` to decide WHICH features or initiatives to pursue to achieve those outcomes. Outcomes first, then prioritization.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| HiPPO override | Executive insists on a feature despite low scores; team builds it, displacing higher-impact work | Present RICE comparison data; offer compromise options; if overridden, document the override reason explicitly |
| Recency bias | Most recent customer request jumps to top of backlog; long-planned high-impact work keeps getting displaced | Score every request before adding to backlog; compare new request RICE score against current top items |
| All Must-haves | MoSCoW has 15 "Must" items exceeding capacity | Enforce the 60% rule; force-rank within Must and demote the lowest to Should |
| Confidence inflation | Team scores 90% confidence on everything, eliminating confidence as a differentiator | Calibrate: 90% = strong evidence (customer data, A/B test), 70% = reasonable belief, 50% = intuition only |
| Sunk cost continuation | Ongoing project continues because "we already invested 3 months" | Re-score with RICE looking only at remaining effort and remaining impact; past investment is irrelevant |
| RICE without data | Team guesses all RICE values, producing meaningless scores | Switch to ICE (designed for subjective scoring) or invest in usage analytics before RICE |

## Ideal For

- **Product managers** making quarterly roadmap decisions who need defensible, data-driven prioritization instead of opinion-driven debates
- **Engineering leads** managing sprint backlogs who want to identify quick wins and avoid money pits
- **Founders** at early-stage startups who need a lightweight framework (ICE) for weekly prioritization decisions
- **Program managers** scoping releases using MoSCoW with the 60% capacity rule to prevent scope creep
- **Anyone** who needs to push back constructively against HiPPO, recency bias, or squeaky wheel prioritization

## Not For

- **Defining success metrics** -- what outcomes to measure uses `outcome-orientation`, not prioritization
- **Risk assessment** -- evaluating what could go wrong with prioritized work uses `risk-management`
- **Stakeholder analysis** -- determining whose input to weight in scoring uses `persona-mapping`

## Related Plugins

- **outcome-orientation** -- defining the outcomes that prioritization serves (outcomes first, then prioritize)
- **persona-definition** -- understanding whose needs inform impact scoring
- **persona-mapping** -- stakeholder dynamics that influence which priorities get executive support
- **risk-management** -- assessing risks to prioritized initiatives
- **systems-thinking** -- understanding second-order effects of prioritization decisions

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
