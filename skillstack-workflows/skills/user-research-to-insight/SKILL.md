---
name: user-research-to-insight
description: Funnel workflow for turning user interviews into actionable product direction that the team actually acts on. Designs the research conversations using elicitation frameworks (OARS, narrative identity, values elicitation, schema detection), synthesizes findings into grounded personas (persona-definition), places them in the organizational landscape (persona-mapping), maps their journeys with touchpoints and friction (user-journey-design), audits for what the research missed (critical-intuition), and presents insights as narrative rather than report (storytelling). Use when you're running a research project and want the outputs to change product direction, not just sit in a Notion page. NOT for quantitative research — different methodology.
---

# User Research to Product Insight

> User research fails at two endpoints. At the top: interviewers ask surface questions and get stated preferences, not real motivations. At the bottom: findings become a report nobody reads instead of a narrative that moves the team. This workflow stops both.

The middle of user research (analyzing what you heard) is not usually where research fails. It's the first hour (how you asked) and the last hour (how you presented) that decide whether the research matters.

---

## When to use this workflow

- Starting a user research project for a product decision
- Pre-launch research for a new feature or product
- Understanding why an existing product isn't gaining traction
- Building empathy across a team that's lost touch with users
- Updating stale personas that no longer match who's actually using the product

## When NOT to use this workflow

- **Quantitative research** — surveys, analytics analysis, A/B tests use different methodology
- **Usability testing** — you already have a prototype; use moderated testing protocols
- **Market sizing** — use market research tools, not interview synthesis
- **One-off validation** — if you just need to check a specific hypothesis, design a targeted experiment

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install elicitation@skillstack
/plugin install persona-definition@skillstack
/plugin install persona-mapping@skillstack
/plugin install user-journey-design@skillstack
/plugin install critical-intuition@skillstack
/plugin install storytelling@skillstack
```

---

## Core principle

**Depth comes from patience, not probing.** This is the `elicitation` skill's first principle and it applies to every research interview. Users tell you what they think you want to hear when you ask directly. They tell you what they actually think when you create the conditions for disclosure. The whole workflow downstream depends on getting this first phase right.

Secondary principle: **insights don't travel well as reports.** A research report with 40 findings will change nothing. A single narrative that makes the team feel what users feel will change everything. Phase 6 is not decoration — it's the part that converts research into action.

---

## The funnel

### Phase 1 — design the research conversations (elicitation)

Load the `elicitation` skill. Before recruiting, decide what depth of disclosure you need.

**Depth tiers:**

- **Shallow** — stated preferences, recent behavior, context. Any conversation can surface this. 20-minute interviews are fine.
- **Medium** — motivations, tradeoffs, decision processes. Requires trust and specific technique. 45-60 minute interviews.
- **Deep** — values, schemas, formative experiences, identity concerns. Requires extensive rapport-building and specific frames. 60-90 minute interviews minimum.

Most product research needs medium depth. Teams over-aim for shallow (quick surveys, fast interviews) OR reach too deep (life-story interviews for feature decisions). Match the depth to the decision the research will inform.

**Techniques to apply from `elicitation`:**

- **OARS framework** — 2:1 reflection-to-question ratio. Most research interviews are 100% questions. Reflect more, ask less.
- **Self-defining memory frames** (if formative experiences matter) — "Is there a moment that comes to mind when you think about [problem area]?"
- **Values elicitation** (if motivations are the research target) — role model technique, decision archaeology, anger-as-signal
- **Schema detection via downward arrow** (if stable belief patterns matter) — gently probe from surface concerns to underlying beliefs

**Recruiting:**

- Aim for 6-12 interviews for saturation on any single question. Beyond 12, you hit diminishing returns.
- Recruit for variation, not similarity. The participant who looks like every other participant is less valuable than one who's noticeably different.
- Real users, not proxies. Colleagues pretending to be users produce colleague insights.

**What you need by end of Phase 1:** an interview guide that uses reflection more than questioning, specific frames for the depth you need, and a recruiting plan targeting variation.

### Phase 2 — run the interviews

Run them. Take notes in the participant's actual words — verbatim quotes, not paraphrases. Paraphrasing at note-taking time destroys the specificity that downstream synthesis depends on.

After each interview, write a one-paragraph impression while the interview is fresh: what surprised you, what felt evasive, what felt deeply true. These impressions are data even when they don't make it into formal analysis.

Time-box each interview tightly. A good 60-minute interview produces more than a rambling 90-minute one.

### Phase 3 — synthesize into personas (persona-definition)

Load the `persona-definition` skill.

After the interviews, group the participants by *pattern*, not by demographics. Demographics are easy to cluster and almost always meaningless. The patterns that matter:

- **What they're trying to accomplish** — the job-to-be-done framing
- **What frustrates them** — specific moments of friction, not general complaints
- **How they make decisions** — what criteria they actually use vs. what they say they use
- **What they value** — from the values elicitation techniques in Phase 1
- **Their relationship to the problem domain** — expert, novice, reluctant user, enthusiast

Each persona should:

- **Carry real quotes** from the interviews. A persona without quotes is fiction. A persona with quotes is grounded.
- **Name specific goals and pain points** — not "wants to save time" but "spends 45 minutes every Monday morning pulling the weekly report together and resents the repetition"
- **Include an empathy map** — what they say, think, do, feel
- **Have decision criteria** — how they'd choose between options

Aim for 3-5 personas, not 12. Too many personas means you haven't actually patterned; you're just listing participants.

### Phase 4 — map personas onto the org (persona-mapping)

Load the `persona-mapping` skill.

If the research is for a B2B product, individual personas aren't enough. The decision to adopt, expand, or churn is usually a multi-stakeholder process. Map:

- **Power-Interest matrix** — which personas have influence over the decision? which are actively involved? which are affected but not deciding?
- **RACI** — responsible, accountable, consulted, informed
- **Influence network** — who convinces whom?
- **Blockers and champions** — who moves this forward, who can kill it?

For B2C products, this phase is lighter — usually just "who else is in the user's environment" (family members, coworkers, managers) and how they affect decisions.

Output: a stakeholder map or an influence diagram, plus short notes on what each stakeholder type needs from the product.

### Phase 5 — map the journeys (user-journey-design)

Load the `user-journey-design` skill.

For each primary persona, map the journey:

- **Phases** — awareness, consideration, first use, regular use, expansion, attrition
- **Touchpoints** — each interaction with the product, the team, the docs, the support system
- **Emotional state** at each touchpoint — confident, confused, delighted, frustrated, abandoned
- **Pain points** — specific, grounded in interview quotes
- **Opportunities** — where a small intervention would have outsized impact (crosses over with `systems-thinking`'s leverage points)

The journey map is the thing that reveals what the product actually needs. Features emerge from journey gaps, not from wish lists.

### Phase 6 — audit (critical-intuition)

Load the `critical-intuition` skill before presenting findings. Ask:

- **What did we miss?** Which questions didn't get asked? Which participant types didn't get recruited? Every research project has blind spots; naming yours is a sign of quality, not weakness.
- **What's ambiguous?** Findings that seem clear often aren't on second look. Re-read the evidence for every major conclusion and ask: "could a reasonable person read this differently?"
- **What are we protecting?** What did we not want to find that we're downplaying? Research team bias is real. The findings you resisted are often the most important.
- **What would a skeptic say?** Construct the strongest case against each major finding. If the case is strong, re-examine the finding.
- **What's the evidence for each claim?** For each finding in the synthesis, trace it back to specific interview quotes. If you can't, the finding is speculation.

The audit's output isn't a rewrite; it's a revised findings document with caveats in the right places and overclaims removed.

### Phase 7 — present as narrative (storytelling)

Load the `storytelling` skill, especially the `business-storytelling` and `speech-and-presentation` references.

A research report of 40 findings will be skimmed and forgotten. A narrative that makes the team feel what users feel will be remembered and acted on.

Structure the presentation as:

- **The user as protagonist** (not the product, not the company, not the research team)
- **A specific, named persona** (even if fictional — specificity is memorability)
- **A concrete scene** — not "users want X" but "here's what Monday morning looks like for Aisha, a nurse manager in Cleveland..."
- **The friction** — the moment in Aisha's day where she gets stuck
- **The stakes** — what happens to her, the patients, the hospital
- **The opportunity** — what a better version would look like
- **The ask** — what the team should do with this

Use real quotes. Use real artifacts (screenshots, screencasts, actual notebooks users showed you). Specificity is what makes research feel real and change product direction.

Duration target: 20-30 minutes for a team presentation. Any longer and you lose the emotional arc to exhaustion.

---

## Gates and failure modes

**Gate 1: the depth gate.** Phase 2 cannot start until Phase 1 has defined the depth tier. Interviewers reaching for deep disclosure with a shallow-tier guide produce surface answers.

**Gate 2: the quote gate.** Phase 3 cannot start until Phase 2 has produced a notebook of verbatim quotes. Paraphrased notes hide the specificity that makes personas real.

**Gate 3: the audit gate.** Phase 7 cannot start until Phase 6's audit has been done. Presenting uncritical findings is how research teams lose credibility.

**Failure mode: interrogation mode.** Interviews become interviews. Participants answer briefly and wait for the next question. Nothing deepens. Mitigation: Phase 1's OARS discipline. If your interview is 80% questions, it's wrong.

**Failure mode: premature patterning.** After 3 interviews, the team "sees the pattern" and stops really listening to interviews 4-12. Confirmation bias. Mitigation: note-take before synthesis. Don't start patterning until all interviews are complete.

**Failure mode: demographic personas.** The personas are age / gender / company size. These are segments, not personas. Actual personas capture what someone wants, fears, and believes. Mitigation: Phase 3's pattern-by-motivation rule.

**Failure mode: the report as artifact.** The team produces a 40-page Notion doc and pats itself on the back. Nobody reads it. Nothing changes. Mitigation: Phase 7. The report is not the deliverable; the narrative presentation is.

**Failure mode: too many personas.** More than 5 and you haven't patterned. You have a list. Mitigation: cluster ruthlessly in Phase 3. Better to merge two tentative personas than to ship with 8.

---

## Output artifacts

A completed research project produces:

1. **An interview notebook** — verbatim quotes, participant metadata, impressions (reusable across projects)
2. **3-5 personas** — grounded in quotes, with specific goals, pain points, decision criteria, and empathy maps
3. **A stakeholder map** — for B2B, showing influence and decision flow
4. **Journey maps** — one per primary persona, with emotional states and friction points
5. **An audited findings document** — with caveats, unknowns, and conservative claims
6. **A narrative presentation** — 20-30 minutes, protagonist-driven, with real quotes and artifacts
7. **An action list** — what the team should do with this, with owners

The narrative presentation is the deliverable. Everything else is supporting material.

---

## Related workflows and skills

- For designing a specific user interview (not a full project), use `elicitation` directly
- For the pitch to change product strategy based on research, use the `pitch-sprint` workflow with this research as input
- For the decision that follows ("should we build X"), use the `strategic-decision` workflow
- For presenting to a non-team audience (investors, board), use `speech-and-presentation` from the `storytelling` skill

---

> *Workflow part of [skillstack-workflows](../../../README.md) by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
