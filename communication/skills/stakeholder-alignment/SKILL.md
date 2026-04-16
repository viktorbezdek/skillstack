---
name: stakeholder-alignment
description: >-
  Align stakeholders in writing using RFCs, design docs, proposals, pre-reads,
  and decision docs with explicit role assignments (DACI, RAPID). Use when the
  user asks to write an RFC, design doc, proposal, pre-read, or decision doc,
  wants to align async stakeholders on a decision, needs to assign deciders
  vs consulted vs informed, wants to structure a cross-team proposal, or is
  preparing a pre-read for a decision meeting. NOT for structuring a generic
  memo (use structured-writing). NOT for stakeholder power maps (use
  persona-mapping). NOT for storytelling pitches or investor decks (use
  storytelling-for-stakeholders).
---

# Stakeholder Alignment

Decisions fail more often in the alignment than in the logic. A good RFC or decision doc does two things: makes the best argument for the chosen path, and makes the roles of everyone affected explicit so no one is surprised.

## Pick the right artifact

| Artifact | When to use | Length |
|---|---|---|
| **RFC** / design doc | Technical decision affecting multiple teams; invites comment | 3-10 pages |
| **Proposal** | Bet on a direction that requires budget/headcount/scope | 1-3 pages |
| **Pre-read** | Input for a scheduled decision meeting | 1-2 pages |
| **Decision doc** | Record a decision that has been made (or is being made now) | 1 page |
| **One-pager** | Early alignment on an idea before full RFC | 1 page |

Use the smallest artifact that produces alignment. A 10-page RFC for a two-team change is over-investment; a Slack thread for a 10-team change is under-investment.

## RFC / design doc structure

```markdown
# [Title] — [state: Draft / Reviewing / Accepted / Rejected / Superseded]

## BLUF
[One-paragraph summary: the problem, the proposed direction, the ask.]

## Roles (DACI)
- **Driver:** [who writes + shepherds]
- **Approver:** [who makes the final call — name, not group]
- **Contributors:** [who provides input]
- **Informed:** [who needs to know]

## Context
[Shared understanding. What led here. Keep controversial claims for later sections.]

## Problem
[What we are trying to solve. Why now.]

## Options considered
- Option A: [name] — [one paragraph] — pros / cons / rough cost
- Option B: [name] — [same]
- Option C: do nothing — [same]

## Recommendation
[Chosen option + why, in one paragraph.]

## Trade-offs
[What we are giving up. What we are not solving. Second-order effects.]

## Open questions
- [ ] [Question needing input] — @person
- [ ] [Assumption needing validation] — @person

## Plan
[Milestones with dates. Dependencies on other teams.]

## Appendix
[Supporting material, benchmarks, prior discussions.]
```

Variations: for short changes, collapse Options / Recommendation into one section. For contentious changes, expand Trade-offs with a pre-mortem.

Worked examples and short-form variants in `references/rfc-design-doc-templates.md`.

## Role assignment — DACI vs RAPID

Both frameworks make roles explicit. Pick one and use it consistently across the org.

### DACI

| Role | Meaning |
|---|---|
| **Driver** | Shepherds the decision. Writes the doc, runs the meeting. |
| **Approver** | Makes the final call. Usually one person. |
| **Contributors** | Provide input. Their concerns must be addressed; they do not have veto. |
| **Informed** | Need to know once the decision is made. |

### RAPID

| Role | Meaning |
|---|---|
| **Recommend** | Proposes the decision. |
| **Agree** | Formal sign-off required (legal, security, etc.). |
| **Perform** | Executes once decided. |
| **Input** | Consulted. Not a veto. |
| **Decide** | Makes the call. |

Rules:
- **One Approver / Decider.** If two people share the role, you do not yet have a decision process.
- **Name, not team.** "Platform Engineering" is not an approver. "Sarah Kim (Platform)" is.
- **Contributors ≠ vetoers.** Disagreement is logged, not blocking.
- **Publish roles before the debate, not after.** Otherwise roles migrate to favor the person who shouts loudest.

## Pre-reads

A pre-read makes a 30-minute decision meeting take 10 minutes.

Structure:

1. **The decision being made** — one sentence.
2. **Options with crisp summaries** — ≤2 paragraphs each.
3. **Recommendation** — with confidence.
4. **What we need from the meeting** — specific, actionable, under 3 items.

Sent 24-48 hours before the meeting. If the meeting still takes 30 minutes, either the pre-read was bad or the decision was not yet decision-ready.

## Decision docs

A decision doc captures a decision AFTER it has been made. Purpose: future reference, onboarding, accountability.

```markdown
# Decision: [title]

**Date:** [YYYY-MM-DD]
**Decider:** [name]
**Status:** Accepted / Superseded by [link] / Reversed

## Context
[Why a decision was needed.]

## Decision
[What was decided, in one paragraph.]

## Alternatives considered
[Brief: option → reason not chosen.]

## Consequences
[What this means going forward. What we are giving up.]

## Follow-ups
- [ ] [Action] — @owner — [date]
```

This is distinct from an ADR (Architecture Decision Record) which focuses on architecture specifically — see `documentation-discipline` for ADRs.

## Escalation patterns

When alignment fails:

1. **Restate the open question.** "The disagreement is whether X or Y. We need the approver to decide by [date]."
2. **Name the cost of delay.** "Every week without a decision costs [concrete cost]."
3. **Escalate the decision, not the debate.** The approver decides the question; they do not re-run the debate.

## Anti-patterns

- **RFC as rationalization** — the doc is written to justify a decision already made. Readers sense this and disengage.
- **Group approver** — "Engineering leadership" as the approver. No one decides.
- **Missing trade-offs section** — every doc lists only upsides. Readers suspect the downsides were not examined.
- **Options theater** — Option A is the real proposal; Options B and C are strawmen. Serious options or no options section at all.
- **Consensus-seeking** — trying to get everyone to agree on everything, instead of getting the decider to decide while contributors contribute.
- **Pre-reads read in the meeting** — meeting time wasted re-reading the doc. If the group didn't read, the doc wasn't sent early enough or wasn't short enough.
- **Missing kill condition** — the proposal has no clause for "what evidence would reverse this decision."

## Workflow

1. **Pick the artifact.** RFC, proposal, pre-read, decision doc, one-pager — by scope and audience.
2. **Assign roles before writing.** DACI/RAPID. Name, not team.
3. **Draft BLUF.** One paragraph. If you can't write it, you're not ready.
4. **Write the options section honestly.** Include "do nothing." Real trade-offs.
5. **Recommend with confidence + trade-offs.**
6. **Send for comment with an explicit deadline and the ask.** "Comments by Friday. I need approval from [Approver] by the 15th."
7. **Record the decision.** If not already the doc's purpose, create a decision doc.

## References

| File | Contents |
|---|---|
| `references/rfc-design-doc-templates.md` | RFC templates (short + long), variants per decision type, naming conventions |
| `references/daci-rapid-cheatsheet.md` | Full DACI and RAPID specs, role-assignment rules, common mistakes |
| `references/alignment-playbooks.md` | Pre-read checklist, escalation patterns, async alignment vs sync meeting trade-off |

## Related skills

- **structured-writing** — the BLUF at the top of the RFC.
- **clarity-editing** — make the RFC readable.
- **documentation-discipline** — decide whether this decision deserves an ADR.
- **visual-communication** — architecture diagrams inside the RFC.
- **trade-off-analysis** — the Options section is a trade-off matrix.
- **storytelling-for-stakeholders** — for investor decks and board materials (narrative-heavy).
