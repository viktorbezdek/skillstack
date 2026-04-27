---
name: design-review-sprint
description: Sequential-audit workflow for running a full UX review pass across an application or product. Walks through five phases — visual audit of design system adherence (frontend-design), navigation and information architecture review (navigation-design), microcopy and error-message audit (ux-writing), end-to-end journey validation (user-journey-design), and cross-product consistency check (consistency-standards). Use when launching a new product version, onboarding a design system, preparing for an accessibility audit, or when user feedback signals "something feels off" but nobody can pinpoint what. NOT for single-component fixes — use frontend-design directly. NOT for greenfield design — design the system first, then audit it.
---

# Design Review Sprint

> Most design quality problems are invisible in isolation. A button looks fine until you see it next to the other button that uses different casing, different padding, and a different error pattern. This workflow forces you to look at the product as a whole, not one screen at a time.

Design review is not design. It's quality assurance applied to the experience layer. You're not creating — you're measuring what exists against what was promised (the design system, the content guidelines, the journey maps). If what was promised doesn't exist yet, stop — build those artifacts first, then come back.

---

## When to use this workflow

- Pre-launch quality gate before a major release
- Design system adoption audit — did the team actually use the tokens, components, and patterns?
- Post-redesign sanity check — does the new design hold together across all screens?
- User feedback triage — complaints about "confusing" or "inconsistent" UX with no single root cause
- Onboarding a new design team member who needs to understand the current state
- Accessibility or compliance prep — a systematic pass catches things spot checks miss

## When NOT to use this workflow

- **Single-component fixes** — use `frontend-design` directly
- **Greenfield design** — you need to build the system before you can audit it
- **Visual redesign** — this workflow finds problems, it doesn't redesign
- **Performance audits** — this is UX quality, not page speed
- **Content strategy** — use `content-modelling` for information architecture at the content level

---

## Prerequisites

Install these SkillStack plugins first — each phase loads one explicitly:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install frontend-design@skillstack
/plugin install navigation-design@skillstack
/plugin install ux-writing@skillstack
/plugin install user-journey-design@skillstack
/plugin install consistency-standards@skillstack
```

The workflow still gives structure without these installed, but each phase loses the depth that makes the audit actionable.

---

## Core principle

**Audit top-down, fix bottom-up.** Run all five phases before fixing anything. If you fix during the audit, you'll optimize locally and miss systemic patterns. The audit produces a ranked list of findings; fixing starts from the highest-impact items after the full picture is clear.

Secondary principle: **every finding needs a reference.** "This doesn't look right" is an opinion. "This violates the 8px spacing grid defined in the design system" is an actionable finding. If there's no reference to cite, the finding is either wrong or the reference is missing — and the missing reference is the real finding.

---

## The phases

### Phase 1 — Visual audit (frontend-design)

Load the `frontend-design` skill. Walk every screen (or a representative sample for large apps) and check:

- **Design token adherence** — are the actual colors, spacing, typography, and border-radius values from the design system, or are there hardcoded overrides? Every override is a finding.
- **Component usage** — are standard components used where they should be, or are there custom implementations that duplicate existing components?
- **Visual hierarchy** — does each screen have a clear primary action, secondary actions, and a readable scan path? Screens where everything has equal weight fail this check.
- **Responsive behavior** — check at least three breakpoints (mobile, tablet, desktop). Components that break, overlap, or lose hierarchy at different sizes are findings.
- **Accessibility basics** — contrast ratios, focus states, touch target sizes. Not a full WCAG audit, but the mechanical checks that catch the majority of violations.

Output: a list of visual findings, each with a screenshot or reference, the violated standard, and severity (broken / inconsistent / minor).

### Phase 2 — Navigation review (navigation-design)

Load the `navigation-design` skill. Evaluate information architecture and wayfinding:

- **Navigation structure** — is the hierarchy flat enough to reach key content in 3 clicks or fewer? Are there orphan pages with no clear path back?
- **Labeling** — do navigation labels match what the user expects to find behind them? Ambiguous labels ("Resources", "More", "Solutions") are findings.
- **Wayfinding cues** — does the user always know where they are, where they can go, and how to get back? Check breadcrumbs, active states, back affordances.
- **Search** — if the product has search, does it return useful results for the top 10 queries users would try? Broken or unhelpful search is a critical finding.
- **Deep linking** — can a user land on any page from an external link and orient themselves? Pages that only make sense when navigated to in sequence are findings.

Output: a navigation findings list with the same structure as Phase 1.

### Phase 3 — Copy audit (ux-writing)

Load the `ux-writing` skill. Audit every piece of interface text:

- **Error messages** — are they specific, actionable, and blame-free? "Something went wrong" is a finding. "Your file is too large — the maximum is 25 MB" is correct.
- **Button labels** — do they describe the action, not the object? "Submit" is almost always worse than a specific verb ("Save changes", "Send invitation").
- **Empty states** — does every empty state explain what will appear here and how to get started? Blank screens are findings.
- **Confirmation dialogs** — do destructive actions have confirmation with clear consequences? "Are you sure?" without saying what happens is a finding.
- **Tone consistency** — does the voice stay consistent across the product? Formal in one section and casual in another without reason is a finding.
- **Jargon and assumptions** — does the copy assume knowledge the target user might not have?

Output: a copy findings list, each with the current text, the problem, and a suggested rewrite.

### Phase 4 — Journey validation (user-journey-design)

Load the `user-journey-design` skill. Test the top 3-5 user journeys end to end:

- **Identify the critical journeys** — onboarding, the core task the product exists for, error recovery, account management. Not every flow — the ones that matter most.
- **Walk each journey step by step** — note every moment of friction, confusion, unnecessary steps, or dead ends.
- **Emotional arc** — map the user's likely emotional state at each step. Are there anxiety peaks with no reassurance? Are there delight opportunities being missed?
- **Edge cases in the journey** — what happens when the user goes back, refreshes, loses connection, enters unexpected data? Test the unhappy paths, not just the golden path.
- **Cross-device continuity** — if the journey spans devices (start on mobile, finish on desktop), does state persist?

Output: annotated journey maps with friction points, severity, and the phase (1-3) findings that contribute to each friction point.

### Phase 5 — Consistency check (consistency-standards)

Load the `consistency-standards` skill. This phase is the cross-cutting audit that ties the previous four together:

- **Naming consistency** — are the same concepts called the same thing everywhere? "Project" in one place and "Workspace" in another for the same entity is a critical finding.
- **Pattern consistency** — are similar interactions handled the same way? If deletion is a modal in one place and inline in another, that's a finding.
- **Taxonomy alignment** — do categories, tags, and groupings follow a single organizing principle?
- **Style guide adherence** — check against the documented content style guide (if one exists). If none exists, that's the finding.
- **Cross-phase pattern detection** — look for systemic patterns across Phase 1-4 findings. Ten individual spacing violations might be one root cause: the team isn't using the spacing scale.

Output: a consistency report that identifies systemic patterns, not just individual violations. Group related findings from all phases into themes.

---

## Assembling the final report

After all five phases, combine findings into a single prioritized report:

1. **Critical** — broken functionality, accessibility blockers, journey dead ends
2. **High** — systemic inconsistencies, confusing navigation, misleading copy
3. **Medium** — individual component violations, minor copy issues, spacing drift
4. **Low** — polish items, nice-to-have improvements

For each finding: what it is, where it is, what standard it violates, suggested fix, and which phase found it.

---

## Decision Tree

```
What triggered the design review?
│
├─ Pre-launch quality gate
│   └─ Run all 5 phases — this is the full audit use case
│
├─ User feedback says "something feels off"
│   └─ Phase 3 (copy audit) → Phase 4 (journey validation) first
│      these surface the friction; then Phase 5 (consistency) for root causes
│
├─ Design system adoption check
│   └─ Phase 1 (visual audit) → Phase 5 (consistency) — skip journey validation
│
├─ Post-redesign sanity check
│   └─ Phase 1 (visual) → Phase 2 (navigation) → Phase 5 (consistency)
│
├─ Accessibility / compliance prep
│   └─ Phase 1 (visual, with accessibility checks) → Phase 3 (copy) → Phase 4 (journey)
│
└─ No design system or guidelines exist yet
    └─ Stop. Build the standards first, then audit against them.
```

## Anti-Patterns

| # | Anti-Pattern | Symptom | Fix |
|---|---|---|---|
| 1 | **Auditing without standards** | Findings are opinions ("it feels wrong") not actionable violations | If no design system or content guidelines exist, stop the audit. Build the standards first. The missing standard IS the finding. |
| 2 | **Fixing during the audit** | You optimize locally and miss systemic patterns | Gate 2: complete all 5 phases before fixing anything. The audit produces a ranked list; fixing starts after the full picture is clear. |
| 3 | **Audit fatigue** | Hundreds of findings, team overwhelmed, nothing gets fixed | Use priority tiers. Fix only Critical and High in the first sprint. Medium and Low go to the backlog. |
| 4 | **Findings without references** | "This doesn't look right" with no cited standard | Gate 1: every finding must cite a specific standard. If no standard exists, the missing standard is the finding. |
| 5 | **Design-by-committee from findings** | Group reviews of individual fixes slow everything down | One person or small team owns each fix. The audit produces findings, not design decisions. |
| 6 | **Skipping the consistency phase** | Phase 5 seems redundant after Phases 1-4 | Phase 5 finds systemic root causes. Ten spacing violations may be one root cause: the team isn't using the spacing scale. |

## Gates and failure modes

**Gate 1: the reference gate.** Every finding must cite a specific standard (design token, content guideline, journey map, pattern library). "It feels wrong" is not a finding. If the standard doesn't exist, document the missing standard as a finding — that's often more valuable than any single violation.

**Gate 2: the full-pass gate.** Do not start fixing until all five phases are complete. Premature fixing biases the remaining audit.

**Failure mode: audit fatigue.** Large products generate hundreds of findings. The team gets overwhelmed and fixes nothing. Mitigation: the priority tiers. Fix only Critical and High in the first sprint. Medium and Low go into the backlog.

**Failure mode: auditing without standards.** If there's no design system, no content guidelines, and no journey maps, the audit has nothing to measure against. Stop the audit. Build the standards first. Come back.

**Failure mode: design-by-committee from audit findings.** The audit produces findings, not design decisions. One person or a small team should own the fix for each finding. Group reviews of individual fixes slow everything down.

---

## Output artifacts

A completed design review sprint produces:

1. **A prioritized findings report** — every finding with location, violated standard, severity, and suggested fix
2. **A systemic patterns summary** — the 3-5 root causes behind the majority of individual findings
3. **A standards gap list** — missing design tokens, undocumented patterns, absent content guidelines
4. **Journey friction maps** — annotated journey maps with pain points linked to specific findings
5. **A fix backlog** — findings converted to actionable tickets, prioritized by severity

---

## Related workflows and skills

- For building the design system before auditing, use `frontend-design` directly
- For content architecture beyond copy, use `content-modelling`
- For user research to understand which journeys matter most, use the `user-research-to-insight` workflow
- For building the product from scratch with these standards, use the `content-platform-build` workflow

---

> *SkillStack Workflows by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
