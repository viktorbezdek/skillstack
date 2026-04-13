# Outcome Orientation

> **v1.0.10** | Strategic Thinking | 11 iterations

> Focus on measurable outcomes using OKRs, results-driven thinking, and the outcome vs output distinction -- stop measuring what you ship and start measuring what changes.

## The Problem

Teams measure what is easy to count instead of what matters. They celebrate shipping 12 features this quarter without asking whether any of them moved a business metric. They write OKRs that are actually task lists in disguise -- "Launch feature X" is an output, not an outcome, and hitting it tells you nothing about whether users are better off.

This confusion between outputs and outcomes is everywhere. A documentation team measures "docs written" instead of "users who successfully complete onboarding." An engineering team tracks "PRs merged" instead of "defect rate reduced." A sales team counts "demos conducted" instead of "pipeline created." Every team is busy, every team can show activity, but nobody can connect their work to the results the business actually needs.

The OKR framework is supposed to fix this, but most teams implement it badly. Their objectives are task descriptions, not inspiring goals. Their key results are binary (launch/don't launch) instead of measurable on a spectrum. They confuse leading indicators (things they can influence now) with lagging indicators (things they measure later), and end up tracking metrics they cannot affect within the quarter. By the time the OKR review happens, the numbers are whatever they are, and the team cannot explain why.

## The Solution

This plugin provides a clear framework for thinking in outcomes instead of outputs. It starts with the fundamental distinction -- outputs are what you produce, outcomes are what changes as a result -- and gives you the "so what?" test to trace any activity back to real value. Ship a feature? So what? Users complete onboarding faster. So what? Time-to-value drops. So what? Retention increases. That last one is the outcome.

You get a structured OKR template with the objective-key-results-initiatives hierarchy, concrete examples of good vs bad OKRs, a results chain model (Activities > Outputs > Outcomes > Impact), and a metric categorization framework that separates lagging indicators (what you measure) from leading indicators (what you can influence). The outcome definition checklist ensures every outcome you write describes an end state, is measurable, is within your influence, and is valuable to users or the business.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| OKRs are task lists in disguise ("Launch feature X") | Outcome-focused OKRs ("Reduce time-to-value by 30%") |
| Track activity metrics (features shipped, docs written) | Track result metrics (problems solved, users successful) |
| Cannot connect team work to business results | Results chain traces activities through outputs to outcomes to impact |
| Confuse leading and lagging indicators, track metrics you cannot influence | Metric categorization separates predictors (pipeline) from results (revenue) |
| "We shipped everything we planned" but no improvement in user metrics | "So what?" test applied until reaching real value |
| OKR reviews are status reports, not learning conversations | Key results on a measurable spectrum with baseline, target, and current |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install outcome-orientation@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention relevant topics.

## Quick Start

1. Install the plugin using the commands above.
2. Bring a goal you are working toward:
   ```
   Help me write OKRs for our product team this quarter -- we want to improve user onboarding
   ```
3. The skill transforms your goal into an outcome-focused objective with measurable key results and a baseline/target framework.
4. Test your existing metrics:
   ```
   We track features shipped, PRs merged, and sprint velocity. Are these the right metrics?
   ```
5. Get an outcome-focused alternative for each metric, with the "so what?" chain showing why activity metrics miss the point.

## What's Inside

Compact single-skill plugin focused on outcome-driven thinking and OKR design.

| Component | Description |
|---|---|
| **SKILL.md** | Core skill covering the outcomes vs outputs distinction, OKR framework with templates, good vs bad OKR examples, outcome metrics (leading vs lagging), results chain model, and outcome definition checklist |
| **evals/** | 13 trigger evaluation cases + 3 output quality evaluation cases |

### outcome-orientation

**What it does:** Activates when you need to define OKRs, set success metrics, distinguish outcomes from outputs, design KPIs, or align team goals with business results. It provides the frameworks and templates to shift from activity-based thinking to results-based thinking.

**Try these prompts:**

```
Write OKRs for our engineering team focused on improving platform reliability
```

```
I defined "launch the mobile app" as my objective -- is this a good OKR?
```

```
What's the difference between a leading and lagging indicator? Help me pick the right metrics for our growth team.
```

```
My team shipped everything we planned but our user metrics didn't improve. Help me figure out what went wrong with our goal-setting.
```

```
Convert these output metrics into outcome metrics: docs written, features shipped, bugs fixed, meetings held
```

```
Build a results chain from our planned activities to the business impact we actually care about
```

## Real-World Walkthrough

You lead a platform engineering team at a mid-stage SaaS company. The CEO wants better platform reliability after a quarter with three major outages that caused customer churn. Your first instinct is to write OKRs like "Implement automated failover" and "Set up better monitoring." You bring these to the skill for a reality check.

**Step 1: Test your initial OKRs.**

You present your draft:

```
Review my OKRs: Objective: Improve platform reliability. KR1: Implement automated failover for all critical services. KR2: Set up PagerDuty alerting with <5min response time. KR3: Achieve 99.95% uptime.
```

The skill immediately flags KR1 and KR2 as outputs, not outcomes. "Implement automated failover" is an activity -- you could implement it poorly and still check the box. "Set up PagerDuty" is a task. Only KR3 (99.95% uptime) is actually an outcome. But even that needs a baseline: what is uptime today? If it is already 99.9%, then 99.95% is an incremental improvement. If it is 98%, then 99.95% is ambitious.

**Step 2: Rewrite with outcomes.**

The skill helps you apply the "so what?" test. Automated failover -- so what? Fewer minutes of downtime during incidents. Better alerting -- so what? Faster incident response. Faster response -- so what? Lower mean time to recovery. Lower MTTR -- so what? Less customer impact per incident.

The rewritten OKR:

```
Objective: Make outages a non-event for customers

KR1: Reduce mean time to recovery (MTTR) from 47 minutes to under 10 minutes
KR2: Achieve 99.95% uptime (up from 99.82% last quarter)
KR3: Zero customer-impacting incidents lasting more than 5 minutes
```

Each key result describes an end state, has a baseline and target, and is measurable. The initiatives (automated failover, PagerDuty, chaos engineering) are listed separately as the "how" -- they drive the key results but are not the key results themselves.

**Step 3: Identify leading indicators.**

The key results above are lagging indicators -- you will not know if you hit them until the quarter ends. You ask:

```
What leading indicators should I track weekly to know if we're on track for these reliability OKRs?
```

The skill maps out the leading/lagging relationship:

| Lagging (Quarter-end Result) | Leading (Weekly Predictor) |
|---|---|
| MTTR under 10 minutes | Runbook coverage for critical paths |
| 99.95% uptime | Chaos engineering tests passing |
| Zero 5-min+ incidents | Automated failover test success rate |

Now the team has weekly signals. If runbook coverage is not increasing, MTTR will not improve. If chaos tests are failing, you will not hit uptime targets. The leading indicators give you time to course-correct before the quarter ends.

**Step 4: Connect to business impact.**

The CEO cares about churn, not MTTR. You build the full results chain:

```
Activities (implement failover, write runbooks, set up alerting)
  → Outputs (failover configured, 12 runbooks written, alerting live)
    → Outcomes (MTTR < 10min, 99.95% uptime, zero long incidents)
      → Impact (customer churn from outages drops from 2.1% to <0.5%)
```

The impact line is what the CEO reports to the board. The outcomes are what your team owns. The outputs are what your team does. The activities are the tasks in Jira. Each layer answers "so what?" for the layer below it.

**Step 5: Apply the outcome definition checklist.**

Before finalizing, you run each key result through the checklist:
- Describes end state, not activity? MTTR under 10 minutes -- yes, it is a state, not a task.
- Measurable and time-bound? Yes, numeric target within the quarter.
- Within influence (not full control)? Yes -- the team can improve reliability but cannot prevent all external failures.
- Valuable to user/business? Yes, directly tied to customer experience and retention.
- Achievable but stretching? MTTR from 47 to 10 minutes is aggressive but achievable with the planned initiatives.

The result: the team goes from task-oriented OKRs ("implement failover") to outcome-oriented OKRs ("MTTR under 10 minutes") with a clear results chain connecting daily activities to quarterly outcomes to annual business impact. Weekly leading indicators give early warning when the team is off track. The CEO can see exactly how platform engineering work maps to the churn reduction the board cares about.

## Usage Scenarios

### Scenario 1: Writing quarterly OKRs

**Context:** You are a product manager preparing quarterly OKRs for your team. Leadership wants to see how your team's work connects to company goals.

**You say:** "Help me write OKRs for the product team. Our company objective is to increase net revenue retention to 120%. My team owns the user engagement part of that."

**The skill provides:**
- Outcome-focused objective connected to the company goal
- 3 key results with baseline, target, and measurement method
- Leading indicators for weekly tracking
- Results chain from team activities to company-level impact

**You end up with:** A set of OKRs that clearly connect your team's outcomes to the company's revenue retention goal, with weekly leading indicators for course correction.

### Scenario 2: Converting outputs to outcomes

**Context:** Your team tracks features shipped, PRs merged, and story points completed. The VP of Engineering wants outcome metrics instead.

**You say:** "Convert these metrics to outcomes: features shipped per sprint, PR cycle time, sprint velocity, test coverage percentage."

**The skill provides:**
- The "so what?" chain for each metric
- Outcome-oriented alternatives: user task completion rate, deployment frequency to production, time from idea to user value, defect escape rate
- Leading vs lagging classification for each new metric
- A dashboard structure that shows both activity (leading) and results (lagging)

**You end up with:** A metrics framework that shows what your team produces AND what changes as a result, satisfying both the VP and the team.

### Scenario 3: Diagnosing why OKRs are not working

**Context:** Your team hit 100% of their OKRs last quarter but the product metrics did not improve. Something is wrong with how the OKRs are structured.

**You say:** "We hit all our OKRs but nothing got better. Here are our OKRs from last quarter -- what's wrong?"

**The skill provides:**
- Analysis of each OKR against the outcome definition checklist
- Identification of OKRs that are actually outputs or tasks masquerading as outcomes
- Rewritten versions that would have caught the disconnect
- Advice on setting the right ambition level (70% achievement target for stretch OKRs)

**You end up with:** A diagnosis of why hitting OKRs did not drive results, plus rewritten OKRs for next quarter that actually measure what matters.

## Ideal For

- **Product managers writing quarterly OKRs** -- the template and good/bad examples prevent the most common OKR mistakes
- **Engineering leads connecting technical work to business results** -- the results chain traces activities to outputs to outcomes to impact
- **Teams whose metrics measure activity instead of results** -- the output vs outcome distinction with the "so what?" test reveals the gap
- **Leaders who need to report upward on team impact** -- the framework produces outcomes that connect to company-level goals
- **Anyone whose OKRs feel like task lists with percentages** -- the outcome definition checklist catches fake outcomes before the quarter starts

## Not For

- **Prioritizing which features to build** -- use [prioritization](../prioritization/) for RICE, MoSCoW, ICE scoring, and effort-impact matrices
- **Defining user personas and pain points** -- use [persona-definition](../persona-definition/) for user research that informs what outcomes to target
- **Risk assessment and mitigation planning** -- use [risk-management](../risk-management/) for identifying risks to achieving your outcomes

## How It Works Under the Hood

The skill is a compact, focused knowledge base built around the outcomes vs outputs distinction. The SKILL.md provides the complete framework: the output/outcome comparison table, the OKR structure with templates, good vs bad OKR examples, outcome metrics categorized by leading (predictors) and lagging (results), the results chain model (Activities > Outputs > Outcomes > Impact), and the outcome definition checklist.

There are no additional reference files -- the skill is deliberately compact so it loads fully into context and delivers immediate, actionable guidance for goal-setting and metric design.

The evaluation suite (13 trigger cases, 3 output quality cases) ensures the skill activates reliably on OKR and outcome-related queries.

## Related Plugins

- **[Prioritization](../prioritization/)** -- RICE, MoSCoW, and ICE scoring for deciding which work to pursue toward your outcomes
- **[Systems Thinking](../systems-thinking/)** -- Understanding the feedback loops and leverage points that connect activities to outcomes
- **[Risk Management](../risk-management/)** -- Identifying risks to achieving the outcomes you defined
- **[Persona Definition](../persona-definition/)** -- Understanding the users whose lives your outcomes should improve

## Version History

- `1.0.10` fix(design+docs): regenerate READMEs for design and documentation plugins
- `1.0.9` fix: add standard keywords and expand READMEs to full format
- `1.0.8` fix: change author field from string to object in all plugin.json files
- `1.0.7` fix: rename all claude-skills references to skillstack
- `1.0.0` Initial release

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
