# Structure Selection Matrix

Pick the structure from reader × purpose × medium, not from habit. This matrix covers the major structures and when each lands.

## The selection table

| Reader | Purpose | Medium | Structure |
|---|---|---|---|
| Executive / busy | Decision / approval | Email | BLUF |
| Executive / busy | Status update | Email | BLUF |
| Peer / colleague | Decision request | Slack / email | BLUF |
| Peer / colleague | Analysis for review | Doc | Minto Pyramid |
| Broad audience (all-hands) | Announcement | Email / post | Inverted pyramid |
| External stakeholder | Briefing | Doc | SPQR |
| External stakeholder | Proposal | Doc | SPQR or Minto |
| Technical peer | Deep analysis | Doc | Minto Pyramid |
| Customer | Support answer | Email | Inverted pyramid or BLUF |
| Team | Weekly update | Email / post | BLUF |
| Oncall / SRE | Incident summary | Post / doc | Inverted pyramid |
| Leadership | Strategy argument | Doc | Minto Pyramid |
| Leadership | Board update | Doc | SPQR or Minto |
| Developer | Design doc | Doc | RFC format (see stakeholder-alignment) |

## By audience time-pressure

| Time the reader has | Structure |
|---|---|
| 30 seconds (subject line + one line) | BLUF (extreme compression) |
| 2 minutes | BLUF + bullets |
| 5 minutes | Inverted pyramid |
| 10 minutes | Minto Pyramid (short-form) |
| 30 minutes | Minto Pyramid (full) or SPQR |
| 1 hour+ | Narrative (but consider: is the length necessary?) |

A structure that requires more time than the reader has is wrong regardless of content quality.

## By purpose

### Purpose: Decision

Reader needs to approve / reject / escalate. Put the ask first.

- Short: BLUF
- Long: Minto Pyramid with BLUF at top

### Purpose: Alignment

Reader needs to understand so they can execute consistently.

- Short: Inverted pyramid (headline fact + supporting)
- Long: Minto Pyramid or RFC format

### Purpose: Announcement

Reader needs to know a thing happened or will happen.

- Short or long: Inverted pyramid (headline, then detail, then narrative context if appropriate)

### Purpose: Explanation / education

Reader needs to understand a complex idea.

- Short: Start with the takeaway (BLUF-style)
- Long: Narrative with clear structure (intro → parts → conclusion)

### Purpose: Argument / persuasion

Reader needs to be convinced of a position.

- Minto Pyramid with strong governing thought and MECE arguments
- SPQR if the complication is non-obvious

### Purpose: Briefing

Reader needs shared context before a decision.

- SPQR — Situation, Problem, Question, Resolution
- Works well for consulting, board materials, vendor briefs

## By medium

### Email

Default: BLUF. Subject line carries the message. Body fills in.

Exceptions:
- Long analyses going via email → Minto in the body with BLUF in first paragraph.
- Announcements → inverted pyramid.

### Slack / chat

BLUF, compressed further. Usually one message, one idea. Threads for follow-up.

Avoid:
- Dumping long prose into chat. Link to a doc instead.
- Multi-paragraph Slack messages with no structure. Even more confusing than unstructured email.

### Document (Google Docs, Notion, Confluence, Markdown)

Match structure to length:
- <1 page: BLUF or inverted pyramid.
- 1-3 pages: Inverted pyramid or short-form Minto.
- 3+ pages: Full Minto or RFC format.

Always include TOC or linked headings once the doc is over ~2 pages.

### Presentation / slides

Each slide is its own BLUF. The deck overall is a Minto pyramid (or sometimes SPQR for story-heavy decks).

### PR description

BLUF (one paragraph, under 30 words) + structured body. See the BLUF template for PR-specific structure.

### Incident summary / postmortem

Inverted pyramid in the TL;DR section. Narrative for the timeline. Minto-style pyramid for the "what we're changing" section.

## Structural fluency by seniority

Different roles benefit from different default structures:

| Role | Default | Why |
|---|---|---|
| IC engineer | BLUF for team, Minto for RFCs | Most work is async action + design docs |
| Engineering manager | BLUF for status, Minto for proposals, inverted pyramid for announcements | Most writing is upward (status) or outward (proposals) |
| Product manager | Minto Pyramid for decisions, SPQR for briefings | PMs build cases; pyramid is their home |
| Executive | BLUF for everything outgoing | Time-pressure on reading, so respect it for writing |
| Founder / CEO | Inverted pyramid for announcements, SPQR for investor briefs | Public-facing + external stakeholders |
| Designer | Narrative + BLUF for rationale | Design needs story + takeaway |

These are starting points, not rules. The right structure is whatever serves the specific reader-purpose-medium combination.

## When to change structure mid-doc

Some long documents change structure between sections:

- **RFC:** BLUF at top → SPQR or narrative for context → Minto for options → bulleted / tabular for roles and plans.
- **Strategy doc:** SPQR intro → Minto for the strategic claim → bulleted for execution.
- **Postmortem:** Inverted pyramid for TL;DR → narrative for timeline → Minto for recommendations.

Mixing is fine IF each section is internally consistent. A section that is half pyramid and half chronological is worse than either alone.

## Red flags — wrong structure for the job

- **BLUF for narrative content.** BLUF a story and you lose the story.
- **Narrative for decisions.** The reader has to wait for the ask. Decisions wait don't get made.
- **Minto for announcements.** A pyramid when everyone just needed a headline.
- **Inverted pyramid for arguments.** A fact in the headline does not substitute for a claim.
- **SPQR for status updates.** Way too much ceremony for "this sprint's work."

## The retrofit test

If you already have a draft and it feels wrong:

1. What's the governing thought / main ask? Write it in one sentence.
2. Where does that sentence appear in the draft? (Should be at the top.)
3. Can a reader stop at any paragraph and still get the main point? (Skim test.)
4. How long does the draft take to read? How long do they have?

If the draft's structure doesn't pass all four, move the thesis to the top and cut until the time budget matches the reader's.
