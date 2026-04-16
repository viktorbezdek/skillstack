---
name: documentation-discipline
description: >-
  Decide what and when to write down, and produce Architecture Decision Records
  (ADRs), one-pagers, runbooks, and decision logs. Use when the user asks
  whether something should be documented, wants to write an ADR, needs a
  runbook or operational playbook, wants to keep a decision log, or is trying
  to decide between a one-pager and an RFC. NOT for auto-generating docs from
  code (use documentation-generator). NOT for end-user tutorials or how-tos
  (use example-design). NOT for docs-site information architecture (use
  navigation-design). NOT for cross-team alignment via RFCs (use
  stakeholder-alignment).
---

# Documentation Discipline

Under-documentation forces re-discovery. Over-documentation forces maintenance. The discipline is to write what will be re-used, at the altitude it will be re-used, and to let the rest stay in chat.

## What to write down (the decision tree)

```
Is the question likely to be asked again?
├── No  → don't document (Slack thread is fine)
└── Yes → keep going ↓

Is the answer likely to change often?
├── Yes → runbook or FAQ (owned + dated)
└── No  → keep going ↓

Is the answer a decision with long-term consequences?
├── Yes → ADR (immutable, numbered, dated)
└── No  → keep going ↓

Is the answer operational (how to do X)?
├── Yes → runbook
└── No  → one-pager or reference doc
```

Red flags that you are under-documenting:

- The same question comes up every quarter.
- New hires ask the same question every cohort.
- "Tribal knowledge" is a phrase anyone uses non-ironically.
- A critical operation has to be learned by watching someone else do it.

Red flags that you are over-documenting:

- Docs are out of date within a month of writing.
- More than 20% of docs have no owner.
- Searches return 5 contradictory answers.
- Writing the doc took longer than doing the thing.

## Architecture Decision Records (ADRs)

An ADR captures an architecture decision and the reasoning behind it. Once published, an ADR is **immutable** — if the decision changes, you write a new ADR that supersedes the old one.

### ADR template

```markdown
# ADR-NNNN: [Title — a noun phrase]

**Date:** YYYY-MM-DD
**Status:** Proposed / Accepted / Superseded by ADR-MMMM / Deprecated
**Deciders:** [names]

## Context
What forced the decision? What constraints exist? What was true when this was decided?
(Keep short — 1-3 paragraphs. Do not re-litigate history.)

## Decision
What did we decide, stated as a present-tense claim. One paragraph.

## Consequences
- **Positive:** what we gain
- **Negative:** what we give up
- **Neutral:** what we accept (trade-offs not clearly positive or negative)

## Alternatives considered
- [Option] — why not chosen (one sentence each)
```

Rules:

- **Numbered sequentially**, never renumbered, even when superseded.
- **Stored in the repo** at a known path (`docs/adr/NNNN-title.md` or `architecture/decisions/`).
- **Immutable after Accepted.** Corrections are new ADRs, not edits.
- **Small.** An ADR is 1-3 pages, not a design doc.
- **Short titles.** "Use PostgreSQL for primary storage" — not "Database Selection Framework v2".

Full ADR templates and examples in `references/adr-template-examples.md`.

### ADR vs decision doc (in stakeholder-alignment)

| | ADR | Decision doc |
|---|---|---|
| Scope | Architecture only | Any decision |
| Storage | In repo, numbered | Anywhere (docs, wiki) |
| Mutability | Immutable once accepted | Can be updated |
| Purpose | Long-term architectural record | Accountability + reference |

Use ADRs for choices that shape the system (language, framework, primary storage, auth model). Use decision docs from `stakeholder-alignment` for everything else.

## Runbooks

A runbook is a steps-to-follow document for an operational task. It assumes the reader is competent but has never done this specific thing.

### Runbook structure

```markdown
# Runbook: [operation name]

**Owner:** [name / team]
**Last reviewed:** YYYY-MM-DD
**Related:** [links to other runbooks/ADRs]

## When to run this
[Trigger conditions.]

## Prerequisites
- [ ] [access / tool / context]

## Steps
1. [Action] — expected result: [what you should see]
2. [Action] — expected result: [...]
3. [Action — if step 2 failed, go to rollback]

## Verification
- [ ] [Check]
- [ ] [Check]

## Rollback
[How to undo, step by step.]

## Troubleshooting
- If you see [symptom], do [thing].
- If you see [symptom], escalate to [person/channel].
```

Rules:

- **Expected result per step.** A runbook without expected results is a wish list.
- **Rollback is non-negotiable.** If there's no rollback, say "irreversible" and explain what validates before proceeding.
- **Last-reviewed date.** Older than 6 months → revalidate before relying on it.
- **Owner, not orphan.** Every runbook has a named owner who owns its accuracy.

See `references/runbook-framework.md` for patterns including game-day exercises, dry-run verification, and runbook rot detection.

## Decision logs

A decision log is a chronological list of decisions at team or org level. Not the same as ADRs (architecture) or decision docs (individual decisions). A decision log is an index.

Format: one row per decision, with date, title, decider, link. Purpose: "what have we decided recently?" answered in 30 seconds.

```markdown
# Team decision log

| Date | Decision | Decider | Link |
|---|---|---|---|
| 2026-03-15 | Adopt pnpm over npm | @lead | [doc](link) |
| 2026-03-28 | Ship feature flags via GrowthBook | @platform | [ADR-0012](link) |
```

Used by: new joiners catching up; post-mortems tracing decision chains; retrospectives asking "did we decide this right?"

## One-pagers

A one-pager states an idea in one page so people can react without a meeting. Different from a proposal (which asks for approval) or a pre-read (which supports a meeting).

Structure:

```markdown
# [Idea] — one-pager

**Owner:** [name]
**Status:** idea / exploring / paused

## What
[One sentence. What is this idea?]

## Why
[Problem it solves. Evidence it's real.]

## How (sketch)
[Two-paragraph outline. Not a plan.]

## Open questions
- [ ] [question]

## What I want from you
[React? Poke holes? Push forward? Kill?]
```

Rules:
- Actually one page. If it's two, it's a proposal.
- "What I want from you" is mandatory. Without it, readers don't know if they should respond.

## Anti-patterns

- **Write-once docs** — written to prove the work happened, never read. Symptom: no ownership, no updates.
- **Docs as performance** — long, well-formatted docs that repeat what's obvious. Signals effort, carries no new information.
- **ADR mutation** — editing an accepted ADR instead of writing a new one that supersedes.
- **Runbooks without verification** — steps without expected results. Untestable, so they decay silently.
- **Decision theater** — recording decisions that were never in doubt. Log the contested ones, not the obvious ones.
- **Doc-firsting** — requiring a doc before any action. Appropriate for architecture; paralyzing for bug fixes.
- **Over-indexed on ADRs** — ADRs for non-architectural decisions (tooling preferences, UX copy). Use the right artifact.

## The write-it-down test

Before writing, ask:

1. **Will this be read more than once?** If no → don't write it.
2. **Is there a specific reader in mind?** If no → the doc has no audience, don't write it.
3. **Is the answer stable enough to justify writing?** If no → write a FAQ or don't write.
4. **Who owns it after you publish?** If no one → don't publish; assign an owner first.
5. **When will it be reviewed next?** Put it in the calendar.

If you cannot answer all five, you are not ready to write. The alternative is a message in chat — often the right choice.

## Workflow

1. **Decide whether to write at all.** The five-question test.
2. **Pick the artifact.** ADR, runbook, decision doc, one-pager. Smallest viable.
3. **Name the owner.** Before publication, not after.
4. **Draft using the appropriate template.**
5. **Peer review before publish.** Someone who was not in the decision reads for context gaps.
6. **Publish with a review date.** 3 / 6 / 12 months depending on volatility.

## References

| File | Contents |
|---|---|
| `references/adr-template-examples.md` | ADR template, worked examples across domains, supersession chains |
| `references/runbook-framework.md` | Runbook template with verification, game-day exercises, rot detection |
| `references/documentation-decision-tree.md` | Full decision tree (what to write, when, which artifact) with examples |

## Related skills

- **stakeholder-alignment** — RFCs and decision docs for cross-team decisions.
- **structured-writing** — structure each document well.
- **clarity-editing** — make each document readable.
- **documentation-generator** — for auto-generated code docs (README, API docs).
- **navigation-design** — docs-site information architecture.
- **example-design** — end-user tutorials and runnable samples.
