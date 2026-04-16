# Systems Thinking

> **v1.0.10** | Strategic Thinking | 11 iterations

> Analyze complex problems through feedback loops, leverage points, system archetypes, and causal loop diagrams -- see the structure behind the symptoms.
> Single skill, self-contained methodology

## Context to Provide

Systems thinking is most valuable when applied to specific recurring problems with history -- not hypothetical situations. The richer your description of what has already been tried, the more precisely the skill can identify the feedback loops at work.

**What information to include in your prompt:**

- **The specific problem and how long it has been recurring** -- "we have had production outages 5 times in 3 months" is diagnosable; "we have outages sometimes" is not
- **What interventions have already been tried** -- listing failed fixes is essential because the pattern of failed fixes often reveals the archetype (Fixes that Fail, Shifting the Burden). Without knowing what did not work, the skill cannot identify why
- **What different stakeholders blame** -- when managers point to different causes, that is a signal of a multi-loop system. List the competing explanations
- **Quantitative changes over time** -- "deploy frequency dropped from 15/week to 4/week over one year despite adding 30 engineers" is far more useful than "deployments are slow"
- **The proposed interventions you are debating** -- if you want leverage point ranking, list the actual options under consideration

**What makes results better vs worse:**

- Better: describe what changed in the system over time (new people, new process, new tooling) alongside the outcome that got worse
- Better: name the competing explanations from different teams -- these become the variables in the causal loop
- Better: specify the boundary explicitly ("within the engineering org" not "the whole company")
- Worse: asking "why are we failing?" without providing the history of what was tried
- Worse: framing the request as a single-cause question ("what is the root cause of our outages?") -- this prevents systemic analysis
- Worse: including so many variables that no boundary is clear -- narrow scope produces actionable output

**Template prompt:**

```
[Problem] has been happening for [timeframe]. We have tried [list of interventions] but
[what happened each time -- did it help temporarily, make it worse, shift to a different area].

Different people on my team blame: [list competing explanations].

Key metrics that changed: [list what got better or worse and by how much].

I want to: [choose one: map the feedback loops / identify the system archetype / rank these interventions by leverage: list interventions].
```

## The Problem

Most problem-solving is linear: identify the symptom, trace it to a cause, apply a fix. This works for simple problems where A causes B. But most real-world problems are systemic -- A causes B, B causes C, and C loops back to amplify A. Teams fix the symptom and celebrate, only to find the problem returns six months later, often worse. They never see the feedback loop that regenerates the issue because they are focused on events, not structures.

Engineering teams experience this constantly. They add more developers to a late project, and the project gets later (Brook's Law is a balancing loop). They ship a quick fix for a production outage, and the fix creates a new failure mode that causes a bigger outage later (Fixes that Fail archetype). They optimize one microservice's performance, and the improved throughput overwhelms a downstream service they did not consider (boundary error). Without systems thinking, every intervention is a guess -- and many interventions make things worse.

The deeper problem is that people confuse correlation with causation and causation with feedback. When revenue drops, the instinct is to ask "what caused it?" -- singular cause, linear explanation. But revenue drops are usually the result of multiple interacting loops: customer acquisition slowing (reinforcing loop weakening), churn increasing (balancing loop dominating), and competitor improvement creating a new reinforcing loop in the other direction. Without the vocabulary to describe these dynamics, teams debate root causes endlessly while the system continues to degrade.

## The Solution

This plugin provides a structured systems thinking methodology: feedback loop identification (reinforcing and balancing), Meadows' 12 leverage points for ranking intervention effectiveness, four system archetypes that describe recurring structural patterns (Fixes that Fail, Shifting the Burden, Limits to Growth, Tragedy of the Commons), causal loop diagramming notation, and a five-step analysis workflow.

The skill produces concrete analytical artifacts: causal loop diagrams showing how variables interact, feedback loop identification with reinforcing/balancing classification, leverage point analysis ranking where interventions will have the most impact, and archetype matching that connects your specific situation to well-documented system patterns with known intervention strategies.

The methodology prevents four common pitfalls: linear thinking (ignoring B-to-A feedback), event focus (treating symptoms instead of structures), boundary errors (scoping the system too narrowly or too widely), and delay blindness (not accounting for time lags between cause and effect). Each pitfall has a diagnostic question that surfaces the blind spot before it leads to a failed intervention.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Fix the symptom, celebrate, then watch it return six months later worse than before | Identify the feedback loop that regenerates the problem and intervene at the structural level |
| Debate "the root cause" as if complex problems have a single linear cause | Map multiple interacting feedback loops and identify which loop is dominant in the current state |
| Add resources to fix a bottleneck without seeing that the bottleneck shifts downstream | Boundary definition and element mapping surface downstream effects before intervention |
| Optimize one part of the system and degrade the whole -- "we made search faster but the database crashed" | Causal loop diagrams make second-order effects visible before changes ship |
| Interventions ranked by urgency instead of effectiveness -- tweaking parameters instead of changing rules | Meadows' 12 leverage points rank interventions from most powerful (paradigm shifts) to least (parameter tweaks) |
| Same organizational patterns repeat across projects but nobody recognizes them | System archetypes (Fixes that Fail, Limits to Growth, etc.) name the patterns so teams can recognize and break them |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install systems-thinking@skillstack
```

### Verify installation

After installing, test with:

```
Our engineering team keeps adding people to projects that are behind schedule, but the projects keep slipping further. Help me understand why.
```

The skill should activate and identify the reinforcing loop (more people, more communication overhead, slower progress) and the balancing loop that makes this intervention counterproductive.

## Quick Start

1. **Install** the plugin using the commands above
2. **Describe a recurring problem**: `We keep having production outages. We fix them, but new ones keep appearing in different services.`
3. The skill **maps the system**: defines boundaries, identifies variables (deploy frequency, test coverage, incident response time, tech debt), traces causal connections
4. It **identifies feedback loops**: a reinforcing loop where quick fixes increase tech debt which increases outage probability, and a balancing loop where outages reduce deploy confidence which slows releases
5. It **recommends leverage points**: not more monitoring (parameter-level, low leverage) but changing the deployment rules to require test coverage thresholds (rule-level, high leverage)

---

## System Overview

```
User describes a recurring / complex / systemic problem
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│               systems-thinking (skill)                    │
│                                                           │
│  5-Step Analysis Workflow:                                 │
│                                                           │
│  1. BOUNDARY DEFINITION                                   │
│     Scope, internal vs external, timescale                │
│         │                                                 │
│  2. ELEMENT MAPPING                                       │
│     Variables, stocks, flows                              │
│         │                                                 │
│  3. RELATIONSHIP IDENTIFICATION                           │
│     Causal connections, +/- classification                │
│     A --[+]--> B (same direction)                         │
│     A --[-]--> B (opposite direction)                     │
│         │                                                 │
│  4. LOOP DETECTION                                        │
│     Reinforcing (R) and Balancing (B) loops               │
│     Dominant loop identification                          │
│         │                                                 │
│  5. LEVERAGE POINT ANALYSIS                               │
│     Meadows' 12 levels (paradigms → parameters)           │
│     Intervention ranking by systemic effectiveness        │
│                                                           │
│  System Archetypes (pattern matching):                    │
│  ├── Fixes that Fail                                      │
│  ├── Shifting the Burden                                  │
│  ├── Limits to Growth                                     │
│  └── Tragedy of the Commons                               │
│                                                           │
│  Output: Causal loop diagrams + loop classification +     │
│          archetype identification + leverage rankings      │
└─────────────────────────────────────────────────────────┘
```

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `systems-thinking` | skill | Feedback loops (reinforcing/balancing), Meadows' 12 leverage points, four system archetypes, causal loop notation, five-step analysis workflow, four common pitfalls |

This is a self-contained plugin -- the complete methodology lives in the SKILL.md body. Systems thinking is a lens, not a procedure, so the value comes from applying the concepts to your specific situation rather than from loading reference material.

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

### Component Spotlights

#### systems-thinking (skill)

**What it does:** Activates when you need to analyze complex problems through a systems lens -- mapping feedback loops, identifying leverage points, recognizing system archetypes, and designing interventions that address structure rather than symptoms. Applies a five-step workflow: boundary definition, element mapping, relationship identification, loop detection, and leverage point analysis.

**Input -> Output:** A description of a recurring, complex, or systemic problem -> Causal loop diagrams, feedback loop classification (reinforcing/balancing), archetype identification, leverage point rankings for proposed interventions, and structural intervention recommendations.

**When to use:** A problem keeps returning after being "fixed." Adding resources does not help. Multiple people blame different causes for the same problem. A growth initiative stalled. Organizational changes produce unexpected side effects. You need to rank competing interventions by systemic effectiveness.

**When NOT to use:** Simple linear problems where fixing A solves B permanently. Detailed project risk tracking (use risk-management for registers and monitoring). Data analysis and visualization (use domain-specific tools). Problems that need execution, not analysis.

**Try these prompts:**

```
We have shipped 6 emergency hotfixes in the last 2 months. Each hotfix is followed by a post-mortem and a
new process rule, but outages keep happening in different services. My VP says it's flaky tests; my lead
says it's tech debt; my PM says it's unclear requirements. Help me map the feedback loops these explanations
are all pointing at.
```

```
Our startup grew from 10 to 80 engineers in 18 months and deployment frequency dropped from 20 per week to
3 per week. We added more code reviewers, automated more tests, and bought better tooling -- none of it helped.
Map the system dynamics driving this and tell me where the leverage is.
```

```
We optimized our product search service -- latency dropped from 200ms to 40ms. Within two weeks, our
recommendation service started timing out because it was getting 5x more requests. I want to understand
why before we optimize anything else.
```

```
Our situation: we outsource feature development to go faster, the outsourcing creates more coordination
overhead so we hire more managers, more managers create more processes, features slow down again, so
we outsource more. Which system archetype is this and what breaks the cycle?
```

```
We are debating five interventions for our overwhelmed customer support team: hire 10 more agents,
build a better self-serve help center, improve onboarding so fewer users need support, add better
product error messages, create an AI triage bot. Rank them by Meadows leverage point level.
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (linear framing, gets linear answer) | Good (systemic framing, gets structural analysis) |
|---|---|
| "Why are we having outages?" | "We've had 5 outages in 3 months. Each gets a fix but new ones keep appearing in different services. Map the systemic pattern." |
| "How do we go faster?" | "Our deployment frequency dropped from 15/week to 4 despite adding 30 engineers. My managers each blame different things. Find the systemic cause." |
| "Should we hire more people?" | "Adding more engineers to our late project made it later. Help me map the feedback loops to understand why and find a higher-leverage intervention." |
| "What's the root cause?" | "Revenue growth stalled after 3 months of 40% MoM. We doubled the referral budget but it didn't help. What system dynamics are at play?" |
| "Fix our team morale" | "Team morale is declining and attrition is up, but exit interviews mention different reasons. Map the reinforcing loops driving the decline." |

### Structured Prompt Templates

**For recurring problems:**
```
[Problem] keeps happening. We've tried [interventions], but [what happens].
Map the feedback loops that regenerate this problem and identify which
leverage point would break the cycle.
```

**For ranking interventions:**
```
We're debating [N] proposals: [list interventions]. Rank them by their
Meadows leverage point level and explain which one addresses the most
structural cause in our system.
```

**For understanding unexpected side effects:**
```
We [changed something]. We expected [desired outcome]. Instead, [unexpected
outcome] happened. Map the causal connections to show why and identify the
feedback loop we missed.
```

**For archetype identification:**
```
We're experiencing [pattern: growth plateau / recurring failures / resource
depletion / burden shift]. Which system archetype describes this, and what
is the known intervention strategy?
```

### Prompt Anti-Patterns

- **Asking for "the root cause" of a systemic problem:** This frames a multi-loop problem as single-cause, which is exactly the linear thinking systems thinking exists to overcome. Instead, ask to "map the feedback loops" or "identify the interacting causes."
- **Describing a problem without specifying what has already been tried:** The most valuable insight from systems thinking is why interventions fail. If you describe only the problem but not the failed fixes, the skill misses the opportunity to identify Fixes that Fail or Shifting the Burden archetypes.
- **Asking to "analyze the system" without defining scope:** Every system exists within a larger system. Without boundaries (which variables, what timescale, which organizational scope), the analysis expands indefinitely. Specify the boundary: "within the engineering org," "over the last 6 months," "focusing on the deployment pipeline."

## Real-World Walkthrough

You are the VP of Engineering at a 200-person company. Over the last year, deployment frequency has dropped from 15 deploys per week to 4. The team is larger than it was a year ago, the tooling is better, and yet output has slowed. The CEO is asking why. Your engineering managers each point to different causes: flaky tests, code review bottleneck, unclear requirements, and growing tech debt. You suspect these are all symptoms of the same underlying structure.

You open Claude Code and say:

```
Our deployment frequency dropped from 15/week to 4/week over the past year despite adding 30 engineers. My managers each blame different things. Help me find the systemic cause.
```

The skill begins with **boundary definition**. It scopes the system to the software delivery lifecycle -- from requirement to production deployment -- and identifies the key variables: team size, deploy frequency, cycle time, defect rate, code review queue length, test suite reliability, tech debt volume, and engineer confidence.

Next, **element mapping** and **relationship identification** produce the causal connections:

```
Team Size --[+]--> Code Review Queue Length
Code Review Queue Length --[+]--> Cycle Time
Cycle Time --[+]--> Batch Size
Batch Size --[+]--> Defect Rate
Defect Rate --[+]--> Tech Debt
Tech Debt --[+]--> Defect Rate
Defect Rate --[-]--> Engineer Confidence
Engineer Confidence --[+]--> Deploy Frequency
```

**Loop detection** identifies two critical loops:

**Reinforcing Loop R1 (Vicious Cycle of Batch Size):** Longer cycle time causes larger batches, which cause more defects, which cause more tech debt, which causes more defects, which further reduces deploy frequency and extends cycle time. This is the dominant loop -- it is self-amplifying.

**Balancing Loop B1 (Code Review Bottleneck):** More engineers create more PRs, which increases the review queue, which increases cycle time. Adding reviewers helps temporarily but creates more code that needs reviewing.

The skill identifies the **system archetype**: **Limits to Growth**. The initial growth (more engineers) hit a constraint (review capacity and deployment confidence) that created a reinforcing loop in the opposite direction.

**Leverage point analysis** ranks the proposed interventions:

| Intervention | Leverage Level | Assessment |
|---|---|---|
| Add more reviewers | Level 1 (Parameters) | Low -- temporarily reduces queue but adds to the system that creates it |
| Fix flaky tests | Level 4 (Material stocks) | Medium -- reduces one defect input but does not address batch size |
| Reduce PR size limits | Level 9 (Rules) | High -- directly breaks the batch-size reinforcing loop |
| Create clear deploy criteria | Level 8 (Information flows) | High -- makes deployment confidence evidence-based |
| Change to trunk-based development | Level 10 (Self-organization) | Highest -- restructures the development model entirely |

The skill recommends starting with PR size limits and deploy criteria -- these two interventions break the reinforcing loop at its strongest point and restore the information engineers need to deploy confidently. You now have a causal loop diagram, the pattern name (Limits to Growth), and a ranked intervention list you can present to the CEO.

## Usage Scenarios

### Scenario 1: Understanding why a growth initiative stalled

**Context:** Your referral program grew 40% month-over-month for three months, then plateaued despite doubling the budget.

**You say:** `Our referral program grew 40% for 3 months then flatlined. We doubled the budget but it didn't help. What's happening systemically?`

**The skill provides:**
- Limits to Growth archetype: reinforcing loop (referrals generate users who generate referrals) hit a balancing loop (market saturation)
- Causal loop diagram showing the interacting loops
- Leverage point analysis: budget is Level 1 (parameter, low leverage); new user segment is Level 10 (self-organization, high leverage)

**You end up with:** A system map showing the constraint is market saturation, not budget.

### Scenario 2: Diagnosing recurring production outages

**Context:** Five outages in three months. Each gets a post-mortem and fix, but new ones keep appearing.

**You say:** `We keep having production outages. Each gets fixed but new ones appear. Help me map the systemic pattern.`

**The skill provides:**
- Fixes that Fail archetype: quick fixes increase system complexity, increasing fragility
- Shifting the Burden: symptomatic solution (patches) undermines fundamental solution (complexity reduction)
- Causal loop diagram with both symptomatic and fundamental loops

**You end up with:** A structural explanation for why fixing individual outages worsens the overall outage rate, plus a strategy targeting the fundamental loop.

### Scenario 3: Evaluating competing organizational changes

**Context:** Leadership debates three proposals for improving velocity: hire 20 engineers, adopt microservices, or implement trunk-based development.

**You say:** `Rank these three proposals by systemic leverage: hiring 20 engineers, adopting microservices, implementing trunk-based development`

**The skill provides:**
- Leverage point classification: hiring = Level 4, microservices = Level 2, trunk-based = Level 10
- Second-order effects for each proposal
- Recommendation based on which addresses the highest-leverage point

**You end up with:** An evidence-based ranking that prevents investing in low-leverage interventions while ignoring high-leverage ones.

---

## Decision Logic

**How does the skill choose which archetype applies?**

The skill matches your situation to archetype recognition patterns:
- **Fixes that Fail**: A fix is applied, the problem temporarily improves, then returns worse. The fix created a side effect.
- **Shifting the Burden**: A quick solution is available alongside a slower fundamental solution. The quick solution reduces pressure to implement the fundamental one, and over time the system becomes dependent on the quick solution.
- **Limits to Growth**: Rapid growth or improvement hits a plateau. Pushing harder on the growth engine does not help because a constraint has activated.
- **Tragedy of the Commons**: Multiple actors share a common resource. Each acts rationally in self-interest but the collective effect depletes the resource.

If the situation matches multiple archetypes, the skill presents both and explains which loop is currently dominant.

**How does leverage point ranking work?**

Meadows' 12 levels rank from most powerful (Level 12: changing the paradigm or mental model underlying the system) to least powerful (Level 1: adjusting parameters like budgets and headcounts). Most organizations default to Level 1-4 interventions because they are easiest to implement. The skill's value is surfacing Level 7-12 interventions that the team has not considered.

**When does the analysis stop?**

The five-step workflow has natural stopping points. Boundary definition prevents scope creep. Loop detection identifies the dominant loops (usually 2-3). Leverage point analysis ranks the top interventions. If the analysis keeps expanding, the boundary was set too wide -- the skill will suggest narrowing scope.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| System boundary is too wide | The analysis expands indefinitely with dozens of variables and loops, none clearly dominant | Narrow the boundary: focus on one subsystem (e.g., "the deployment pipeline" not "the engineering organization"). A good analysis has 6-10 variables and 2-3 dominant loops. |
| Problem is actually linear, not systemic | The causal chain does not loop back -- A causes B causes C, and fixing A permanently solves C | Systems thinking is not needed for linear problems. If the five-step workflow finds no feedback loops, the fix is straightforward: address the upstream cause. |
| Archetype matching forces a fit | The situation does not cleanly match any of the four archetypes, but the analysis tries to squeeze it in | Not every system matches a named archetype. The archetypes are recognition shortcuts, not exhaustive. The causal loop diagram is the primary output -- archetype matching is supplementary. |
| Leverage point recommendations are too abstract | "Change the paradigm" is Level 12 advice that nobody can act on Monday morning | The skill should ground high-leverage recommendations in concrete actions. Level 12 (paradigm) becomes "reframe from 'deploy less to reduce risk' to 'deploy more with smaller changes to reduce risk.'" Every level needs an actionable translation. |
| Analysis becomes academic instead of actionable | Beautiful causal loop diagram but no clear intervention recommendation | The analysis should always end with a ranked intervention list. If the diagram is done but no interventions are clear, the boundary is wrong or the variables are too abstract. Redefine variables as things that can be changed. |

## Ideal For

- **Engineering leaders diagnosing recurring organizational problems** -- systems thinking reveals the feedback loops that make problems return after being "fixed"
- **Product and business leaders evaluating strategic initiatives** -- leverage point analysis ranks proposed interventions by systemic effectiveness
- **Technical architects analyzing complex system behavior** -- causal loop diagrams surface second-order effects of architectural changes
- **Anyone stuck in a pattern that keeps repeating** -- system archetypes name the patterns so you can recognize and break them

## Not For

- **Detailed project risk tracking** -- use [risk-management](../risk-management/) for risk registers, scoring matrices, and monitoring cadences
- **Data analysis and metrics dashboards** -- use domain-specific analytics tools; systems thinking interprets data but does not produce visualizations
- **Simple linear problems** -- if A causes B and fixing A solves B permanently, systems thinking adds unnecessary complexity

## Related Plugins

- **[Risk Management](../risk-management/)** -- Track and mitigate the risks that systems thinking identifies; use together for systemic risk assessment
- **[Prioritization](../prioritization/)** -- Apply RICE, MoSCoW, or ICE to prioritize the interventions that leverage point analysis recommends
- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate novel interventions when standard leverage points are exhausted
- **[Debugging](../debugging/)** -- Apply systems thinking to technical debugging: trace feedback loops in code, not just stack traces

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
