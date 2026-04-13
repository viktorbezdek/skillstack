# Outcome Orientation

> **v1.0.10** | Strategic Thinking | 11 iterations

---

## The Problem

Teams confuse activity with progress. They ship features, write documentation, hold meetings, and deploy code -- measuring outputs instead of outcomes. A team that "shipped 12 features this quarter" has no idea whether those features moved any business metric. The sprint velocity dashboard shows high throughput, but customer churn is unchanged, activation rates are flat, and revenue growth has stalled.

OKRs are the standard tool for fixing this, but most OKR implementations fail. Teams write objectives that are really tasks ("Launch feature X") and key results that are really activities ("Write 10 docs," "Conduct 5 interviews"). These output-disguised-as-outcome OKRs provide a false sense of direction. The team completes every key result and still moves no business needle because the key results measured effort, not impact.

The gap between outputs and outcomes is invisible without deliberate practice. A product manager reports "we completed our quarterly roadmap 100%" while the CEO asks "why isn't growth moving?" Both are right within their frame -- the PM tracked outputs, the CEO expects outcomes. This misalignment persists across engineering, product, design, and operations because nobody applies the "so what?" test: following each output up the value chain until it reaches a measurable change in the world.

Without a systematic framework for outcome thinking -- the output-to-outcome distinction, proper OKR construction, leading vs lagging metrics, and the results chain from activities to impact -- teams remain stuck in the activity trap: busy, shipping, and going nowhere.

## The Solution

The Outcome Orientation plugin gives Claude expertise in results-driven thinking. It provides the outputs-vs-outcomes distinction with concrete examples, the OKR framework with proper structure (qualitative objectives, quantitative key results), good-vs-bad OKR comparison, outcome metrics categorized as leading vs lagging indicators, the results chain (activities -> outputs -> outcomes -> impact), and an outcome definition checklist.

The plugin is a single focused skill that activates when you need to define OKRs, set success metrics, distinguish outputs from outcomes, or ensure that planned work connects to measurable business impact. It applies the "so what?" test systematically, forcing every output to trace to a real outcome.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| OKRs are disguised task lists: "Launch feature X" as an objective | Objectives are inspiring and qualitative; key results are quantitative measures of impact |
| "Ship 12 features" is the quarterly success metric | "Reduce time-to-value by 30%" connects work to measurable user impact |
| No distinction between leading and lagging indicators | Metrics categorized as lagging (result: monthly revenue) and leading (predictor: pipeline created) |
| Activity completion reported as progress -- 100% of roadmap done, no business impact | Results chain traced: Activities -> Outputs -> Outcomes -> Impact, with "so what?" applied at each step |
| Key results measure effort: "Write 10 docs" | Key results measure change: "90% of users complete onboarding" |
| Success defined as what was delivered, not what changed | Outcome definition checklist: end state, measurable, time-bound, valuable, stretching |

## Installation

Add the marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install outcome-orientation@skillstack
```

### Prerequisites

None. For prioritizing which outcomes to pursue, also install `prioritization`. For defining who the outcomes serve, also install `persona-definition`.

### Verify installation

After installing, test with:

```
Help me write OKRs for our engineering team this quarter -- we need to improve developer experience and reduce deployment failures
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `I need to define success metrics for our new onboarding flow -- right now we just count feature completion`
3. The skill transforms your output metrics into outcome metrics with leading and lagging indicators
4. You receive an OKR with a qualitative objective and 3 quantitative key results measuring actual user impact
5. Next, try: `Our team shipped everything on the roadmap but NPS hasn't moved -- what's wrong with our goal-setting?`

---

## System Overview

```
outcome-orientation/
├── .claude-plugin/
│   └── plugin.json            # Plugin manifest
└── skills/
    └── outcome-orientation/
        ├── SKILL.md           # Core skill (OKR framework, metrics, results chain, checklists)
        └── evals/
            ├── trigger-evals.json   # 13 trigger evaluation cases
            └── evals.json           # 3 output evaluation cases
```

A single skill with no additional references. The SKILL.md contains the complete outcome orientation framework: outputs vs outcomes distinction, OKR structure, good vs bad OKR examples, metrics taxonomy, results chain, and outcome definition checklist.

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `outcome-orientation` | Skill | OKR framework, outcome vs output distinction, metrics taxonomy, results chain, definition checklist |

### Component Spotlight

#### outcome-orientation (skill)

**What it does:** Activates when you need to define OKRs, set success metrics, or connect planned work to measurable outcomes. Applies the "so what?" test to transform output-focused goals into outcome-focused ones, structures OKRs with qualitative objectives and quantitative key results, and categorizes metrics as leading vs lagging indicators.

**Input -> Output:** A goal, initiative, or set of planned activities -> Properly structured OKRs with outcome-focused key results, leading/lagging indicator identification, and a results chain connecting work to impact.

**When to use:**
- Defining quarterly or annual OKRs for teams
- Setting success metrics for features, projects, or initiatives
- Reviewing existing goals that feel output-focused
- Connecting engineering work to business impact
- Distinguishing between leading indicators (predictors) and lagging indicators (results)

**When NOT to use:**
- Prioritizing which features or initiatives to pursue (use `prioritization`)
- Risk assessment for planned work (use `risk-management`)
- Detailed project planning and task decomposition (use a project management tool)
- Defining user personas that outcomes serve (use `persona-definition`)

**Try these prompts:**

```
Write OKRs for a platform engineering team focused on improving developer productivity and reducing incident response time
```

```
Our product team's OKRs are all outputs: ship feature A, launch campaign B, hire 3 engineers. Help me rewrite them as outcomes.
```

```
What leading indicators should I track to predict whether our new pricing page will improve conversion?
```

```
Trace the results chain for "we built a notification system" -- what output, outcome, and impact does this connect to?
```

```
Our team hit 100% of our key results but the business metric didn't move. Diagnose what went wrong with our OKR structure.
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Help me with goals" | "Write OKRs for our Q3 engineering team -- we need to reduce deployment failures and improve mean time to recovery" |
| "What should we measure?" | "What leading and lagging indicators should I track for a feature that aims to reduce customer support ticket volume?" |
| "We need OKRs" | "Convert these output goals into outcome OKRs: ship search feature, redesign onboarding, migrate to microservices" |
| "Are my goals good?" | "Review this OKR: Objective: Improve user experience. KR1: Redesign 5 pages. KR2: Fix 20 bugs. KR3: Launch mobile app." |

### Structured Prompt Templates

**For writing new OKRs:**
```
Write OKRs for [team/individual] this [quarter/half/year]. Our focus areas are [area 1] and [area 2]. Current baseline metrics: [what you measure today and their values]. Business context: [what the company needs].
```

**For converting outputs to outcomes:**
```
Our team planned these deliverables: [list of features/projects/tasks]. Help me find the outcomes behind each one and write proper OKRs that measure impact, not completion.
```

**For metrics design:**
```
I need success metrics for [feature/initiative]. The goal is to [desired change]. Who is affected: [user type]. What does success look like in [timeframe]?
```

### Prompt Anti-Patterns

- **Listing features and asking for OKRs** -- features are outputs; tell the skill what problem the features solve and it will define the outcomes those features should produce
- **Setting key results with no baseline** -- "increase activation by 30%" is meaningless without knowing the starting point; provide current metric values
- **Confusing objectives with key results** -- objectives are qualitative and inspiring ("Make onboarding effortless"); key results are quantitative and measurable ("90% completion rate within 5 minutes")
- **Asking for too many OKRs** -- 3 objectives with 3 key results each is the practical maximum; more dilutes focus

## Real-World Walkthrough

**Starting situation:** You lead an engineering team at a B2B SaaS company. The team has been asked to "improve the product" this quarter. Last quarter, the team shipped 14 features and closed 87 tickets, but customer churn increased 5% and the CEO is asking what engineering is doing about it. The team feels productive -- they completed their roadmap -- but the business sees no impact.

**Step 1: Diagnosing the output trap.** You ask: "Our team shipped 14 features last quarter but churn increased 5%. We're told to 'improve the product' this quarter. Help me set goals that actually connect to business impact."

The skill applies the "so what?" test to last quarter's outputs. 14 features shipped -- so what? Users gained new capabilities -- so what? Were the capabilities things churning customers needed? The skill identifies the disconnect: the roadmap was feature-driven (outputs) not problem-driven (outcomes). Features were built based on internal intuition rather than churn analysis.

**Step 2: Defining the objective.** The skill structures the objective: "Retain at-risk enterprise customers by solving their top 3 unmet needs." This is qualitative, inspiring, and directly connected to the churn problem. It is NOT "ship 10 features" or "reduce churn by 5%" (that's a key result, not an objective).

**Step 3: Setting outcome key results.** The skill constructs 3 key results:
- KR1: Reduce monthly enterprise churn from 5% to 2.5% (lagging indicator -- the ultimate outcome)
- KR2: Increase product usage frequency among at-risk accounts from 2x/week to 5x/week (leading indicator -- usage predicts retention)
- KR3: Achieve NPS >= 40 among enterprise accounts, up from current 28 (leading indicator -- satisfaction predicts retention)

Each key result has a baseline, a target, and is measurable. None is a feature or an activity.

**Step 4: Tracing the results chain.** The skill maps the chain:
- Activities: interview 20 churning customers, analyze usage data, build targeted fixes
- Outputs: 5 targeted improvements addressing top churn reasons (not 14 random features)
- Outcomes: at-risk accounts use the product more, report higher satisfaction
- Impact: churn drops, revenue retention improves, CEO sees the connection

The skill notes that "initiatives" (the how) are separate from OKRs (the what). The team decides how to achieve the key results; the OKRs measure whether they succeeded.

**Step 5: Leading vs lagging metrics.** The skill structures the metrics dashboard:
- Lagging (result): monthly churn rate (updates monthly, slow feedback)
- Leading (predictor): weekly active usage among at-risk accounts (updates weekly, fast feedback), NPS survey responses (updates bi-weekly), support ticket resolution time for enterprise (updates daily)

The team can track leading indicators weekly to see if their work is trending toward the lagging outcome, instead of waiting until end-of-quarter to discover their efforts failed.

**Step 6: Outcome definition checklist.** The skill validates each key result:
- Describes an end state, not an activity? Yes -- churn rate, usage frequency, NPS score
- Measurable and time-bound? Yes -- quarterly targets with baselines
- Within the team's influence? Yes -- they can build features that affect usage and satisfaction
- Valuable to user/business? Yes -- directly tied to revenue retention
- Achievable but stretching? Yes -- 50% churn reduction is ambitious but not impossible

**Final outcome:** A properly structured OKR with one qualitative objective, 3 quantitative key results (1 lagging + 2 leading), a results chain connecting activities to impact, and a metrics dashboard the team can track weekly. Total time: one session instead of a week of debates about what "improve the product" means.

**Gotchas discovered:** The skill flagged that the team's instinct to set "ship 5 improvements" as a key result is the same output trap that caused last quarter's failure. Features shipped is an output; user behavior change is the outcome.

## Usage Scenarios

### Scenario 1: Converting a roadmap to outcome-focused OKRs

**Context:** Product management hands engineering a roadmap with 8 features for the quarter. Engineering needs to convert this into OKRs that measure impact, not just completion.

**You say:** "Our quarterly roadmap has: new search, onboarding redesign, API v2, mobile push notifications, SSO integration, dashboard redesign, export to PDF, bulk import. Help me find the outcomes behind these features."

**The skill provides:**
- Grouping by outcome: search + dashboard redesign -> "users find what they need faster" (reduce time-to-task), onboarding + mobile -> "new users reach value faster" (activation rate), API v2 + SSO + export + bulk -> "enterprise customers can integrate and scale" (enterprise adoption)
- 3 OKRs with qualitative objectives and quantitative key results for each outcome group
- Warning: 8 features may be too many to move any single outcome; recommend focusing on 2 outcome groups

**You end up with:** 3 outcome-focused OKRs derived from the 8-feature roadmap, with clear metrics that measure user impact rather than feature completion.

### Scenario 2: Designing metrics for a new feature

**Context:** You are launching a new collaboration feature and need to define what success looks like beyond "we shipped it."

**You say:** "We're launching real-time collaboration in our document editor. How do I define success metrics that go beyond 'feature launched'?"

**The skill provides:**
- Results chain: Activity (build collab feature) -> Output (feature live in production) -> Outcome (users collaborate more, reduce email/Slack for document feedback) -> Impact (faster project completion, reduced tool-switching)
- Lagging metrics: percentage of documents with 2+ collaborators, average time from document creation to final version
- Leading metrics: collaboration session frequency, feature adoption rate in first 30 days, return usage after first session

**You end up with:** A metrics framework that measures collaboration behavior change, not just feature availability.

### Scenario 3: Diagnosing OKRs that don't work

**Context:** Your team achieved 100% of their key results but the executive team says the business metrics they care about did not improve.

**You say:** "We hit 100% on all three KRs -- redesigned 5 pages, fixed 20 bugs, reduced page load by 40%. But customer satisfaction didn't improve. What went wrong?"

**The skill provides:**
- Diagnosis: all 3 KRs are outputs (pages redesigned, bugs fixed) or technical metrics (page load), not user behavior outcomes
- The missing link: faster pages and fewer bugs are necessary conditions, not sufficient ones; the question is whether users noticed and changed behavior
- Rewritten KRs: KR1: "User task completion rate increases from 65% to 85%", KR2: "Support tickets about page errors decrease from 50/week to 15/week", KR3: "User-reported satisfaction with page experience increases from 3.2 to 4.0"
- Note: technical improvements (page load, bug count) become tracked inputs, not key results

**You end up with:** Diagnosis of the output-as-outcome trap and rewritten KRs that measure user behavior change, with technical metrics repositioned as tracked inputs.

---

## Decision Logic

**When to track leading vs lagging indicators?**

- **Lagging indicators** (monthly revenue, churn rate, NPS) -- track for quarterly OKR evaluation. These are the ultimate proof that outcomes were achieved. Downside: slow feedback, no course correction during the quarter.
- **Leading indicators** (activation rate, weekly usage, support ticket volume) -- track weekly for early signal. These predict whether lagging indicators will move. Upside: fast feedback, enables mid-quarter course correction.

Always pair at least one lagging indicator (the outcome you want) with at least one leading indicator (the predictor you can track weekly).

**When is this skill vs prioritization?**

Use `outcome-orientation` to define WHAT outcomes to measure. Use `prioritization` to decide WHICH outcomes to pursue when you cannot pursue all of them. The two skills are sequential: define possible outcomes first, then prioritize which ones to focus on.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Output-disguised-as-outcome OKRs | Key results measure completion (shipped, launched, wrote) not change (increased, reduced, improved) | Apply "so what?" test: follow each output until you reach a measurable behavior or business change |
| No baseline for key results | "Increase activation by 30%" with no starting number | Establish baselines before setting targets; if no baseline exists, make "measure current state" the first activity |
| Too many OKRs | 7 objectives with 5 key results each | Maximum 3 objectives with 3 KRs each; more dilutes focus and makes tracking impossible |
| Lagging-only metrics | Track monthly churn but have no weekly leading indicators | Add at least one leading indicator per OKR that provides weekly feedback |
| Key results outside team's influence | "Increase company revenue by 20%" set for a platform engineering team | Key results should be within the team's influence (they can affect it) even if not full control |

## Ideal For

- **Product managers** setting quarterly OKRs who want to ensure goals measure impact, not just feature delivery
- **Engineering leads** translating business strategy into measurable team goals connected to user outcomes
- **Founders and executives** diagnosing why teams ship features but business metrics don't move
- **Teams transitioning** from output-based roadmaps to outcome-based goal setting and needing the foundational framework
- **Anyone writing OKRs** who wants to avoid the most common mistakes (task-as-objective, output-as-key-result)

## Not For

- **Prioritizing between outcomes** -- use `prioritization` for RICE, MoSCoW, ICE scoring to rank which outcomes to pursue
- **Risk assessment** -- use `risk-management` for evaluating what could go wrong with planned initiatives
- **Detailed project planning** -- outcomes define what to achieve, not how to break work into tasks

## Related Plugins

- **prioritization** -- ranking which outcomes to pursue using RICE, MoSCoW, or effort-impact analysis
- **persona-definition** -- defining the users whose outcomes matter most
- **risk-management** -- assessing risks to outcome achievement
- **systems-thinking** -- understanding the system dynamics that connect outputs to outcomes

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
