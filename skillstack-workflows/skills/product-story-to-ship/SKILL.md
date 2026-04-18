---
name: product-story-to-ship
description: PM funnel workflow for turning user research into prioritized engineering stories — product story, user research to backlog, user needs to stories, PM workflow. Chains elicitation (deep interviews that surface real needs), user-journey-design (touchpoints, pain points, emotions), persona-definition (who we're building for), outcome-orientation (measurable success criteria), and prioritization (RICE/MoSCoW/ICE scoring). Use when translating user research into engineering work, when the backlog is unranked feature requests, when launching a new product from interviews to sprint-ready stories, or when the team builds features nobody asked for. NOT for technical architecture — use strategic-decision. NOT for backlog grooming without new research — use prioritization directly.
---

# Product Story to Ship

> The gap between "we talked to users" and "engineering is building the right thing" is where most product work fails. This workflow closes that gap by forcing every story to trace back to an observed user need, a mapped journey, a named persona, and a measurable outcome — before it enters the backlog.

Most backlogs are graveyards of good intentions. Features added because someone in a meeting said "what if we also..." without tracing back to a user need. This workflow makes that impossible by requiring provenance: every story traces back through outcomes, personas, journeys, to the original user voice.

---

## When to use this workflow

- Translating user interviews or research into engineering stories
- Launching a new product and going from zero to a prioritized backlog
- The backlog is a pile of feature requests with no framework for saying no
- The team suspects they're building features nobody asked for
- A PM is joining a project and needs to establish a research-to-shipping pipeline
- Preparing for a planning cycle and needing evidence-based priorities

## When NOT to use this workflow

- **Technical architecture decisions** — use `strategic-decision`
- **Grooming an existing backlog without new research** — use `prioritization` directly
- **Writing marketing copy from personas** — use `ux-writing` or `persona-mapping`
- **The product is already built and you need to optimize it** — use `user-research-to-insight` for the research, then this workflow only if new stories are needed

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install elicitation@skillstack
/plugin install user-journey-design@skillstack
/plugin install persona-definition@skillstack
/plugin install outcome-orientation@skillstack
/plugin install prioritization@skillstack
```

---

## Core principle

**Every story must trace back to an observed user need.** Not a stakeholder's opinion, not a competitor's feature list, not a hypothesis that sounded good in a brainstorm. An actual user, describing an actual problem, in their actual words. Stories without provenance are how teams build things nobody wants.

Secondary principle: **prioritize outcomes, not features.** A feature is a bet that a particular implementation will produce a particular outcome. The outcome is what matters. Two different features might achieve the same outcome — the cheaper one wins. This workflow separates the outcome definition from the implementation so the team can make that comparison.

---

## The funnel

### Phase 1 — elicit real needs (elicitation)

Load the `elicitation` skill. This is the foundation — everything downstream depends on the quality of what you learn here.

The skill provides deep interview techniques from narrative identity (McAdams), self-defining memories (Singer), and Motivational Interviewing. The key insight: users don't know what they need. They know what they do, what frustrates them, and what they wish were different. Your job is to hear THOSE things, not the solutions they propose.

Design and run interviews that surface:

- **Current behavior** — what do users actually do today? Not what they say they do. Observe if possible; narrate if not.
- **Pain points** — where do they get stuck, frustrated, confused, or give up? These are the real opportunities.
- **Workarounds** — what hacks have they built to compensate? Workarounds are evidence that a need is real and urgent enough that people invest effort to address it.
- **Emotional stakes** — what does success feel like? What does failure feel like? Emotional intensity predicts willingness to pay and willingness to switch.
- **Context** — when, where, and under what pressure do they encounter these problems? Context shapes what kind of solution is appropriate.

Output: a set of interview transcripts or notes with highlighted verbatim quotes, observed behaviors, and identified pain points. Raw material, not yet interpreted.

The discipline: do not propose solutions during this phase. Solutions come later. This phase is for listening.

### Phase 2 — map the journey (user-journey-design)

Load the `user-journey-design` skill. Using the raw research from Phase 1, map the user's experience as a journey:

- **Stages** — what are the major phases the user goes through? (Awareness, consideration, onboarding, regular use, edge cases, churn risk)
- **Touchpoints** — at each stage, where does the user interact with your product (or your competitor, or a workaround)?
- **Actions** — what does the user do at each touchpoint?
- **Emotions** — what does the user feel at each touchpoint? (Confident, confused, frustrated, delighted, anxious)
- **Pain points** — where on the journey do things break down? Map these to the pain points from Phase 1.
- **Opportunities** — for each pain point, where could an intervention make the biggest difference?

The journey map is not a flowchart of your product. It's a flowchart of the user's EXPERIENCE, which may include time away from your product, use of competitors, manual workarounds, and emotional states that have nothing to do with features.

Output: a journey map document with stages, touchpoints, emotions, pain points, and opportunity areas.

### Phase 3 — define personas (persona-definition)

Load the `persona-definition` skill. From the research and journey maps, cluster users into distinct personas:

- **Demographics and context** — not for stereotyping, but for understanding constraints (technical skill level, time pressure, organizational role)
- **Goals** — what is each persona trying to accomplish? Not feature requests — goals.
- **Pain points** — which pain points from the journey map hit this persona hardest?
- **Behaviors** — how does this persona typically approach the problem? (Power user vs. casual, methodical vs. exploratory, cost-sensitive vs. time-sensitive)
- **Quotes** — verbatim quotes from the research that capture this persona's voice
- **Anti-personas** — who are you explicitly NOT building for? This is as important as defining who you are building for. Without anti-personas, scope expands to serve everyone and serves no one well.

Keep personas to 3-5. More than 5 means you haven't found the meaningful clusters. Fewer than 2 means you're treating all users as the same (they're not).

Output: a persona deck — 3-5 personas with goals, pain points, behaviors, and representative quotes.

### Phase 4 — define measurable outcomes (outcome-orientation)

Load the `outcome-orientation` skill. For each major opportunity from the journey map:

- **Outcome statement** — what changes for the user if this is solved? Written as a measurable change, not a feature. ("Users complete onboarding in under 3 minutes" not "Add a setup wizard.")
- **Success metric** — how will you know this outcome has been achieved? Must be observable and measurable. Completion rate, time-to-task, error rate, NPS delta, retention at day-7.
- **Baseline** — what's the current state of this metric? If you don't know, measuring it becomes the first task.
- **Target** — what's the goal? Be specific. "Improve retention" is not a target. "Day-7 retention from 40% to 55%" is a target.
- **Leading indicators** — what will you see BEFORE the outcome metric moves? These are your early signals that the bet is working or not.

The outcome-to-metric chain is what makes prioritization possible in Phase 5. Without measurable outcomes, prioritization degenerates into "what does the loudest stakeholder want?"

Output: an outcomes document — each opportunity mapped to a measurable outcome with baseline, target, and leading indicators.

### Phase 5 — prioritize and scope the backlog (prioritization)

Load the `prioritization` skill. Now that you have personas, journeys, and measurable outcomes, score and rank:

- **Scoring framework** — apply RICE (Reach, Impact, Confidence, Effort), MoSCoW (Must/Should/Could/Won't), or ICE (Impact, Confidence, Ease). The `prioritization` skill has guidance on which to use when. RICE is strongest when you have quantitative reach data; ICE is fastest for early-stage products.

For each candidate story:

- **Reach** — how many of your target personas does this affect?
- **Impact** — how much does it move the outcome metric?
- **Confidence** — how sure are you about reach and impact? (Low confidence = needs more research, not more building)
- **Effort** — engineering estimate, not PM estimate
- **Provenance** — which persona, which journey pain point, which outcome metric? If a story can't answer all three, it doesn't belong in this backlog.

Scope the first sprint/cycle:

- **Must-haves** — stories that address the top-scored outcomes for the primary persona
- **Should-haves** — stories that address secondary personas or secondary outcomes
- **Could-haves** — stories with high potential but low confidence (may need more research)
- **Won't-haves (this cycle)** — explicitly deprioritized. Saying no is the point of prioritization.

Output: a prioritized backlog with scores, provenance chains, and a clear scope boundary for the next cycle.

---

## Decision Tree

```
Where are you in the product cycle?
│
├─ Starting from zero with user interviews planned
│   └─ Run all 5 phases — this is the full funnel
│
├─ Interviews done, need to make sense of them
│   └─ Phase 2 (journey) → Phase 3 (personas) → Phase 4 (outcomes) → Phase 5 (prioritize)
│
├─ Personas exist, need to prioritize work
│   └─ Phase 4 (outcomes) → Phase 5 (prioritize)
│
├─ Backlog exists but no provenance to user needs
│   └─ Phase 1 (elicit) → Phase 4 (outcomes) → Phase 5 (re-prioritize)
│      audit existing stories against research
│
├─ "Features nobody asked for" problem
│   └─ Phase 1 (elicit real needs) → Phase 5 (re-score existing backlog)
│
└─ Grooming backlog without new research
    └─ Skip this workflow — use prioritization skill directly
```

## Anti-Patterns

| # | Anti-Pattern | Symptom | Fix |
|---|---|---|---|
| 1 | **Stakeholder injection** | Senior person says "we need feature X" and it enters the backlog without provenance | The provenance requirement: if it can't trace to research, it's flagged as a hypothesis needing validation — not a story ready for engineering. |
| 2 | **Persona sprawl** | Eight personas with overlapping needs; engineering can't tell who they're building for | Phase 3 limits to 3-5 personas and requires anti-personas. More than 5 means you haven't found meaningful clusters. |
| 3 | **Outcome-free stories** | "As a user, I want a dashboard" — no measurable outcome, no success metric | Phase 4's outcome chain: every story needs a metric. If you can't measure it, you can't prioritize it. |
| 4 | **Research theater** | Interviews conducted but findings cherry-picked to support pre-existing roadmap | Phase 1's discipline: record verbatim quotes and observed behaviors. Raw data should be available for anyone to review. |
| 5 | **The infinite funnel** | More research, more personas, more scoring — and nothing ships | Phase 5 forces a scope boundary. Output is a FINITE backlog for a SPECIFIC cycle, not an ever-growing list. |
| 6 | **Prioritizing features over outcomes** | Backlog is ranked by what sounds coolest, not by what moves the metric | Phase 4 separates outcome definition from implementation. Two features may achieve the same outcome — the cheaper one wins. |

## Gates and failure modes

**Gate 1: the research gate.** Phase 2 cannot start until Phase 1 has produced real user research. Journey maps built from assumptions are fiction — they look professional but mislead.

**Gate 2: the persona gate.** Phase 4 cannot start until Phase 3 has produced personas. Outcomes defined for "users in general" are too vague to measure.

**Gate 3: the provenance gate.** No story enters the backlog in Phase 5 without tracing back to a persona, a journey pain point, and a measurable outcome. Stories without provenance are the ones that waste engineering time.

**Failure mode: stakeholder injection.** A senior person says "we need feature X" and it enters the backlog without going through the funnel. Mitigation: the provenance requirement. If it can't trace to research, it gets flagged as a hypothesis that needs validation — not a story ready for engineering.

**Failure mode: persona sprawl.** Eight personas with overlapping needs. Engineering can't tell who they're building for. Mitigation: Phase 3's limit of 3-5 personas and the requirement for anti-personas.

**Failure mode: outcome-free stories.** "As a user, I want a dashboard" — no measurable outcome, no success metric, no way to know if it worked. Mitigation: Phase 4's outcome chain. Every story needs a metric.

**Failure mode: research theater.** Interviews were conducted but the findings were cherry-picked to support a pre-existing roadmap. Mitigation: Phase 1's discipline of recording verbatim quotes and observed behaviors. The raw data should be available for anyone to review.

**Failure mode: the infinite funnel.** More research, more personas, more journey maps, more scoring — and nothing ships. Mitigation: Phase 5 forces a scope boundary. The output is a FINITE backlog for a SPECIFIC cycle, not an ever-growing list.

---

## Output artifacts

A completed funnel produces:

1. **Research notes** — interview transcripts/notes with verbatim quotes and observed behaviors
2. **Journey maps** — user experience mapped with stages, touchpoints, emotions, and pain points
3. **Persona deck** — 3-5 personas with goals, pain points, behaviors, and anti-personas
4. **Outcomes document** — measurable outcomes with baselines, targets, and leading indicators
5. **Prioritized backlog** — scored stories with provenance chains, scoped for the next cycle
6. **Deprioritization log** — what was explicitly NOT included this cycle, and why

The provenance chain (research -> journey -> persona -> outcome -> story) is the real deliverable. The backlog is its expression.

---

## Related workflows and skills

- For deeper user research methodology before starting this workflow, use the `user-research-to-insight` workflow
- For presenting the prioritized backlog to stakeholders, use the `pitch-sprint` workflow
- For the technical architecture of what you'll build, use `strategic-decision`
- For mapping stakeholders who influence the backlog, use `persona-mapping` directly

---

> *SkillStack Workflows by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
