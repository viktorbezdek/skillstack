# RFC / Design Doc — Templates

Templates for the three common alignment artifacts: standard RFC, short-form RFC, and decision doc. Use the smallest template that produces alignment.

## Standard RFC (3-10 pages)

Use for cross-team technical decisions that invite comment.

```markdown
# RFC-NNN: [Title — verb phrase stating the proposed change]

**State:** Draft / Reviewing / Accepted / Rejected / Superseded
**Comment deadline:** YYYY-MM-DD
**Last updated:** YYYY-MM-DD

## BLUF

[One paragraph (3-5 sentences). The problem, the proposal, and the ask. A reader who stops here knows what you want.]

## Roles

**Driver:** [Name] — writes, shepherds, owns the doc until accepted.
**Approver:** [Name] — makes the final call. One person.
**Contributors:** [Names] — provide input. Concerns must be addressed; no veto.
**Informed:** [Names / groups] — notified once accepted.

## Context

[Shared understanding. What led here. Uncontroversial claims.
Keep short — 2-4 paragraphs. Do not re-litigate decisions already made.]

## Problem

[What are we trying to solve. Why does it matter now.
Name the cost of the status quo in concrete terms — time, money, user impact.]

## Options considered

### Option A: [Name]

[One paragraph description.]

- **Pros:** [2-4 points]
- **Cons:** [2-4 points]
- **Rough cost:** [engineering weeks, infrastructure cost, coordination overhead]

### Option B: [Name]

[Same structure.]

### Option C: Do nothing

[Include this always. Never a strawman.]

## Recommendation

[Option chosen + one paragraph of reasoning.
State your confidence: "high", "medium with low-confidence on X", etc.]

## Trade-offs

[What we give up. What we explicitly do NOT solve.
Second-order effects. Named concessions.]

## Plan

| Milestone | Owner | Target date | Dependencies |
|---|---|---|---|
| [Phase 1] | @name | YYYY-MM-DD | [team/blocker] |
| [Phase 2] | @name | YYYY-MM-DD | [team/blocker] |

## Open questions

- [ ] [Question or assumption to validate] — @owner
- [ ] [Question or assumption to validate] — @owner

## Appendix

[Benchmarks, prior discussions, supporting analyses.
Not required reading — reference material.]
```

## Short-form RFC (1-2 pages)

Use for smaller cross-team decisions where a 5-page RFC is over-investment.

```markdown
# RFC-NNN: [Title]

**State:** Draft | **Comment deadline:** YYYY-MM-DD

## BLUF
[3 sentences: problem, proposal, ask.]

## Roles
- **Driver:** @name
- **Approver:** @name
- **Contributors:** @names
- **Informed:** [group]

## What we'll do and why
[2-3 paragraphs. Problem + proposed solution + why this one.]

## Options we rejected
- **[Option X]** — [one-line rejection reason]
- **Do nothing** — [one-line reason]

## Trade-offs
- [What we give up]
- [What we're not solving]

## Plan
- [Phase 1 with date + owner]
- [Phase 2 with date + owner]

## Open questions
- [ ] @owner — [question]
```

## Decision doc template

Captures a decision AFTER it has been made. Purpose: future reference + accountability.

```markdown
# Decision: [Title]

**Date:** YYYY-MM-DD
**Decider:** [Name — not group]
**Status:** Accepted / Superseded by [link] / Reversed

## Context
[Why a decision was needed. 1-2 paragraphs.]

## Decision
[What was decided. One paragraph, present tense.]

## Alternatives considered
- **[Option]** — [why not chosen, one sentence]
- **[Option]** — [why not chosen, one sentence]

## Consequences
- **Positive:** [what we gain]
- **Negative:** [what we give up]
- **Neutral:** [trade-offs not clearly good or bad]

## Follow-ups
- [ ] [Action] — @owner — [date]
- [ ] [Action] — @owner — [date]
```

Decision docs are for non-architectural decisions. For architecture, use an ADR (see `documentation-discipline`).

## One-pager template

Early-stage idea, not yet an RFC. Used to get reactions before full investment.

```markdown
# [Idea] — one-pager

**Owner:** @name
**Status:** Idea / Exploring / Active / Paused

## What
[One sentence.]

## Why
[Problem + evidence it's real — numbers, quotes, incidents.]

## How (sketch)
[Two paragraphs. Not a plan.]

## Open questions
- [ ] [Question]
- [ ] [Question]

## What I want from you
[React / poke holes / push forward / kill.]
```

One page. If it is two, it is a proposal.

## Variant: Bugfix / incident response RFC

For significant bugs or incident-driven changes.

```markdown
# RFC-NNN: Fix [incident summary]

**State:** Accepted (incident-driven) | **Date:** YYYY-MM-DD

## Incident summary
[What happened. Links to incident doc.]

## Root cause
[One paragraph.]

## Fix
[What we did. Short-term mitigation + long-term fix.]

## Follow-ups
- [ ] [Preventive change] — @owner
- [ ] [Monitoring addition] — @owner
- [ ] [Runbook update] — @owner

## Approvals
- [x] @sre-lead
- [x] @eng-lead
```

Incident RFCs often skip the Options section — the situation dictated the response.

## Naming conventions

| Artifact | File pattern |
|---|---|
| Standard RFC | `docs/rfcs/YYYY-MM-DD-short-title.md` or `NNN-short-title.md` |
| ADR | `docs/adr/NNNN-short-title.md` (sequential number) |
| Decision doc | `docs/decisions/YYYY-MM-DD-short-title.md` |
| One-pager | `docs/ideas/short-title.md` |

Numbering rules:
- **ADRs: sequential, never renumbered**, even when superseded.
- **RFCs: date-based or sequential**, team preference.
- **Decision docs: date-based**, no sequence required.

## When to use which

| Situation | Artifact |
|---|---|
| Multi-team technical decision, high impact | Standard RFC |
| Small cross-team change | Short-form RFC |
| Single-team decision to record | Decision doc |
| Architecture-specific, immutable | ADR (see `documentation-discipline`) |
| Need input on an idea before committing | One-pager |
| Incident-driven change | Bugfix RFC variant |

## Common mistakes

- **Wrong template for scope** — 10-page RFC for a 2-team change; 1-paragraph message for a 10-team change.
- **Missing approver** — "engineering leadership" as the approver. Someone must be named.
- **Rejected options omitted** — only one option considered. Readers assume the analysis was lazy.
- **Deadlines vague** — "soon", "next month-ish". Specific date, or no real deadline.
- **BLUF after context** — the one-paragraph summary comes after 3 pages of preamble. Move BLUF to the top.
- **Appendix as body** — main content hidden in appendix while summary-level material dominates the body. Invert.
