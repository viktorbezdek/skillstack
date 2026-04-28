# Output Formats

The brainstorm-swarm produces a synthesis. The synthesis can be rendered in different formats depending on what the user will do with it.

## Format selection guide

| User's intent | Format |
|---|---|
| Decide for themselves now | Standard Artifact (in-chat markdown) |
| Share with stakeholders for input | Decision One-Pager (markdown doc) |
| File as part of a PRD process | PRD section (hand off to `prd` skill) |
| Reference later for decision rationale | Standard Artifact + Per-Persona collapsed |
| Build a slide for a meeting | Decision Matrix (renders well to slides) |
| Track open questions | Dissent Log (becomes a tracking doc) |
| Validate next-step planning | Recommended-Next-Move section as standalone |

## Format 1: in-chat markdown (default)

For most brainstorms, the synthesis is rendered inline in the chat as markdown. The user reads it, reacts, decides whether to deepen, ask follow-ups, or commit.

Length: 600-1200 words excluding collapsed per-persona sections.

Renders well in the chat UI. Markdown headings make it scannable. Collapsed details preserve persona texture without clutter.

## Format 2: file-saved doc

When the synthesis is part of a longer process (PRD, decision log, RFC), save to a file. The user then continues with that file.

Default path: `/tmp/brainstorm-<slug>-<timestamp>.md` or wherever the user designates.

Include all sections of the standard artifact. Make the file self-contained — someone reading it later (without the brainstorm context) should understand it.

## Format 3: PRD section

The synthesis becomes a section in a Product Requirements Document. Hand off to the `prd` skill (skillstack):

- The synthesis's recommended-next-move becomes the PRD's "Decision" section
- The dissent log becomes the "Considered alternatives" section
- The open questions become the "Open questions / risks" section
- The personas-in-the-swarm becomes the "Stakeholder perspectives" section

This pattern is powerful: the brainstorm produces the substance; the PRD skill produces the structured artifact.

## Format 4: decision matrix slide

For meetings where the synthesis is presented to stakeholders, render the Decision Matrix format (see synthesis-frameworks.md).

The matrix renders well to:
- Google Slides / PowerPoint
- Notion databases
- Linear/Jira ticket descriptions
- Email decision-asks

Keep it under 8 rows × 5 columns. More than that loses the at-a-glance value.

## Format 5: tracking doc

When the brainstorm produced multiple open questions, a tracking doc helps the user follow up on each:

```markdown
## Open Questions Tracker — Brainstorm: [topic]

| # | Question | Source persona | Status | Owner | ETA |
|---|---|---|---|---|---|
| 1 | [Q] | [persona] | open | — | — |
| 2 | [Q] | [persona] | researching | [name] | [date] |
| 3 | [Q] | [persona] | resolved | [name] | [date] |

### Resolution notes
- Q3 resolved [date]: [outcome]
```

Becomes a living document the user updates as questions get answered.

## Format 6: standalone recommendation

For when the user just wants the action, no full synthesis:

```markdown
## Brainstorm conclusion: [topic]

**Recommended action**: [specific next move with reasoning]

Confidence: [low / medium / high] based on swarm consensus
Alternative: [the runner-up]
This recommendation changes if: [falsifying condition]

(Full synthesis available; reply if you want to see it.)
```

Useful when the user has already heard about the brainstorm and just needs the bottom line.

## Embedding into larger workflows

The synthesis is often an input to another process:

| Downstream process | What to extract |
|---|---|
| Writing a PRD | recommended-next-move, dissent (for "alternatives considered"), open-questions (for "risks") |
| Filing a Linear/Jira ticket | recommended-next-move + a 1-line summary of WHY |
| Drafting an RFC | full synthesis as the "Discussion" section |
| Sending a Slack/email update | one-line summary + the recommended next move |
| Planning a sprint | recommended-next-move + scope cuts from constraint-setter |

When the brainstorm is upstream of one of these, format the synthesis to feed it.

## Section-by-section length guidance

| Section | Target |
|---|---|
| Topic + framing | 1-2 sentences |
| Personas in swarm | 4-8 lines |
| Consensus | 3-5 bullets, ~60 words total |
| Dissent | 2-4 items, ~150 words total |
| Open questions | 1-3 items, ~100 words total |
| Recommended next move | 100-300 words |
| Per-persona contributions | full original content, collapsed |

## Voice across formats

All formats share the synthesizer's voice: **neutral integrator**.

- Don't editorialize on personas ("Skeptic was, as usual, contrarian")
- Don't reveal preferences ("I think X is the right answer")
- Use third-person crisply ("The swarm converged on..." not "We see that...")
- Reserve the recommendation as the only place to take a position

## Title conventions

For file-saved or external formats, the title should be:

```
Brainstorm: [topic phrased as the question being decided] (YYYY-MM-DD)
```

Examples:
- `Brainstorm: Should we add offline mode to the mobile app? (2026-04-28)`
- `Brainstorm: Postgres vs MySQL for the analytics workload (2026-04-28)`
- `Brainstorm: Kill or migrate the legacy notifications service? (2026-04-28)`

The question form helps later when the doc is one of many — the user remembers what was being decided.
