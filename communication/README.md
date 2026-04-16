# Communication

> **v1.0.0** | Professional Communication | 5 skills

---

## The Problem

Most knowledge work is delivered in writing — RFCs, proposals, ADRs, status updates, architecture notes, async alignment. The quality of that writing determines whether decisions land, teams align, and context survives. Yet most teams treat communication as a side skill instead of a discipline. The result is consistent: buried ledes that bury decisions, hedged prose nobody trusts, RFCs that never produce alignment because roles were never assigned, docs that bloat because nobody asked whether they should exist, and paragraphs that describe what a diagram would have shown in seconds.

These failures do not fix themselves. They compound — every unaligned decision creates the next misalignment, every unclear doc creates the next round of re-asking the same question. The discipline is a set of named techniques — BLUF, Minto Pyramid, active voice, DACI, ADRs, C4, Mermaid — applied consistently. Most teams know some of these; few apply all of them in sequence.

## The Solution

The Communication plugin gives Claude five composable communication skills, each scoped to one discipline:

1. **structured-writing** — Structure a written piece so it leads with the point (BLUF, Minto Pyramid, SPQR, inverted pyramid).
2. **clarity-editing** — Line-level editing for clarity and conciseness (active voice, hedge removal, jargon strip, nominalization fixes).
3. **stakeholder-alignment** — Write RFCs, proposals, pre-reads, and decision docs with explicit roles (DACI, RAPID).
4. **documentation-discipline** — Decide what/when to write down; write ADRs, runbooks, decision logs, one-pagers.
5. **visual-communication** — Diagram systems and flows (Mermaid flowchart, sequence, state, ER, C4 model).

Each skill activates on its own and composes in sequence: decide to write (documentation-discipline) → pick structure (structured-writing) → write it (stakeholder-alignment if cross-team) → diagram what paragraphs can't say (visual-communication) → edit for clarity (clarity-editing) → ship.

## Context to Provide

Each skill in this plugin activates on different signals. Providing the right context for each skill produces a usable artifact immediately rather than generic advice.

**What information to include in your prompt:**

- **The existing text**: For editing, structuring, or diagramming existing content, paste the text. The skill cannot improve what it cannot see.
- **Target audience**: Who reads this? (engineering team, non-technical executives, external customers, open-source contributors) -- drives vocabulary, tone, and assumed context
- **Document type**: RFC, ADR, status update, runbook, proposal, email, decision doc, or one-pager -- each has a different structure
- **Decision or ask**: For structured-writing and stakeholder-alignment, what is the single most important thing the reader must take away?
- **Roles**: For RFCs and proposals that need DACI or RAPID -- who is the decision-maker, who are the contributors, who is just informed?
- **Diagram type**: For visual-communication, what type of thing are you diagramming? (flow of a request, state machine, system architecture, data schema, sequence of API calls)
- **Constraints**: Length limit, formal vs. informal register, whether a diagram renderer is available (Mermaid in GitHub, Confluence, etc.)

**What makes results better:**
- Pasting the actual draft for clarity-editing -- the skill edits real text, not imaginary text
- Specifying the named decision-maker for stakeholder-alignment ("our CTO Ali owns the approval") enables DACI with real names
- Describing the flow in words before asking for a diagram ("the request hits the load balancer, then the API server checks the cache, then fetches from DB if miss") produces a diagram that matches your actual architecture
- Specifying whether a doc should exist first (documentation-discipline) saves time -- if the answer is "don't write it," no further work is needed

**What makes results worse:**
- "Write an RFC" with no topic -- the skill needs a subject and the key decision being made
- "Make this better" on a wall of text without specifying what dimension to improve (structure, clarity, or alignment)
- Requesting a Mermaid diagram without describing the system being diagrammed -- the skill invents a generic diagram instead of modeling your system

**Template prompts by skill:**

**structured-writing:**
```
Apply BLUF / Minto Pyramid to this [email / status update / proposal]. The key point is [one sentence]. Audience: [who reads this]. Target length: [approximate]. [Paste text.]
```

**clarity-editing:**
```
Edit this for clarity and conciseness. Remove hedges, passive voice, and jargon. Audience: [technical / non-technical]. Keep all technical facts; only compress the prose. [Paste text.]
```

**stakeholder-alignment:**
```
Write an RFC for [topic]. The decision being made: [what]. Decision-maker (Approver): [name/role]. Contributors: [names/roles]. Informed parties: [names/roles]. Open questions: [list]. Trade-offs already considered: [list].
```

**documentation-discipline:**
```
Should we document [topic]? Context: [who needs this information, how often, what happens without it]. If yes, write the [ADR / runbook / decision log / one-pager].
```

**visual-communication:**
```
Draw a Mermaid [flowchart / sequence / state / ER] diagram for [what you are modeling]. [Describe the flow or relationships in plain language.] Render in [GitHub / Confluence / other].
```

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Emails bury the ask in paragraph four. | BLUF in the first 30 words; reader stops reading the moment they have the answer. |
| Docs hedge with "it might be worth considering possibly" everywhere. | Authority, or explicit uncertainty with a number. No weasel words. |
| RFCs have "Engineering Leadership" as the approver — nobody decides. | Named approver, DACI/RAPID roles, explicit contributors and informed. |
| Teams write long docs for decisions nobody will revisit, and nothing for decisions that matter. | Documentation decision tree: ADR, runbook, one-pager, or "don't write it." |
| Architecture explained in four paragraphs when a Mermaid sequence diagram would have taken 20 seconds. | Mermaid-by-default for flows, sequences, states; C4 for big picture. |
| Prose-heavy RFCs that mix structure, clarity, and missing trade-offs. | Structured layout, edited for clarity, with explicit trade-offs and open questions. |

## Evaluation Results

Evaluated by running the live trigger harness at plugin-publish time. Metrics and per-skill deltas will be added here after live evals run.

## Installation

Add the marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install communication@skillstack
```

### Prerequisites

None. For adjacent disciplines:

- **`ux-writing`** — UI microcopy, error messages, button labels (this plugin covers long-form; ux-writing covers interface text).
- **`documentation-generator`** — auto-generates docs from a codebase (this plugin's `documentation-discipline` decides what to write and how; documentation-generator writes the repo-level stuff).
- **`storytelling`** / **`storytelling-for-stakeholders`** — narrative-driven pitches, investor decks (this plugin is for structured async work).
- **`example-design`** — runnable tutorials and samples (a different kind of doc).
- **`navigation-design`** — docs-site IA (when you have enough docs to need navigation).
- **`consistency-standards`** — enforce naming/style standards across a corpus.

### Verify installation

After installing, test with:

```
Rewrite this email as BLUF: [paste long email]
```

The `structured-writing` skill should activate and lead with the ask/answer in 30 words.

## Quick Start

1. Install the plugin using the commands above.
2. Try: `Tighten this doc — too many hedges and passive voice. [paste your text]` — activates `clarity-editing`.
3. Try: `Write an RFC for moving from REST to gRPC. Decision-maker: CTO. Contributors: backend leads. The key trade-off is latency vs. schema coupling. Include DACI roles.` — activates `stakeholder-alignment`.
4. Try: `Should we write an ADR for adopting pnpm? Context: we have 6 engineers, 3 repos, npm today. Write it if yes.` — activates `documentation-discipline`.
5. Try: `Draw a Mermaid sequence diagram for our login flow. The user submits credentials, we check the cache for a session token, on miss we validate against the DB, then issue a JWT. Show cache hit and miss branches.` — activates `visual-communication`.
6. Try: `Restructure this 800-word status update using the Pyramid Principle. The key message is that the launch is delayed by 2 weeks due to a third-party API dependency. [paste text]` — activates `structured-writing`.

## System Overview

```
communication/
├── .claude-plugin/
│   └── plugin.json
├── README.md
└── skills/
    ├── structured-writing/
    │   ├── SKILL.md
    │   ├── evals/{trigger-evals.json, evals.json}
    │   └── references/{bluf-templates.md, minto-pyramid-method.md, structure-selection-matrix.md}
    ├── clarity-editing/
    │   ├── SKILL.md
    │   ├── evals/{trigger-evals.json, evals.json}
    │   └── references/{compression-patterns.md, hedge-and-jargon-removal.md, editing-examples.md}
    ├── stakeholder-alignment/
    │   ├── SKILL.md
    │   ├── evals/{trigger-evals.json, evals.json}
    │   └── references/{rfc-design-doc-templates.md, daci-rapid-cheatsheet.md, alignment-playbooks.md}
    ├── documentation-discipline/
    │   ├── SKILL.md
    │   ├── evals/{trigger-evals.json, evals.json}
    │   └── references/{adr-template-examples.md, runbook-framework.md, documentation-decision-tree.md}
    └── visual-communication/
        ├── SKILL.md
        ├── evals/{trigger-evals.json, evals.json}
        └── references/{mermaid-cheatsheet.md, diagram-selection-matrix.md, c4-model-guide.md}
```

Five skills, 15 reference documents. Each skill has trigger-evals (13 cases: 8 positive + 5 negative) and output evals (3 scenarios).

## What's Inside

| Skill | Activates on | Primary artifacts |
|---|---|---|
| **structured-writing** | "Write this BLUF" / "apply Pyramid Principle" / "lead with the point" / "make this skim-readable" | BLUF template, Minto pyramid, SPQR, inverted pyramid |
| **clarity-editing** | "Tighten this" / "remove hedges" / "active voice" / "strip jargon" / "improve readability" | 4-pass editing (compress / active / hedges / nominalizations) |
| **stakeholder-alignment** | "Write an RFC" / "design doc" / "proposal" / "pre-read" / "DACI" / "RAPID" | RFC template, decision doc template, role-assignment frameworks |
| **documentation-discipline** | "Should this be documented?" / "write an ADR" / "need a runbook" / "decision log" | ADR, runbook, decision log, one-pager, the write-it-down decision tree |
| **visual-communication** | "Draw a flow" / "sequence diagram" / "state machine" / "ER diagram" / "C4 model" / "Mermaid" | Mermaid templates for flowchart/sequence/state/ER/class; C4 levels |

## Decision Logic

**When to use which skill:**

- **Starting a doc?** Use `documentation-discipline` first — should you write at all? If yes, which artifact type?
- **Doc is cross-team / needs alignment?** Use `stakeholder-alignment` for RFCs/proposals/decision docs.
- **Doc just needs to make the point?** Use `structured-writing` for BLUF or Pyramid.
- **Doc is drafted but wordy?** Use `clarity-editing` for the polish pass.
- **Explaining a system, flow, or state machine?** Use `visual-communication` — a diagram beats paragraphs.

**When is this plugin vs. adjacent plugins?**

- **UI copy?** — use `ux-writing` (microcopy only).
- **Repo docs auto-generated?** — use `documentation-generator` (this plugin's `documentation-discipline` decides strategy; documentation-generator writes code-derived docs).
- **Investor pitch or board narrative?** — use `storytelling-for-stakeholders` (narrative-heavy).
- **Docs-site IA?** — use `navigation-design`.
- **Tutorials / runnable samples?** — use `example-design`.

## Ideal For

- **Engineering leads** writing RFCs, proposals, decision docs for multi-team changes.
- **PMs** producing pre-reads, briefs, and announcement writing.
- **Staff+ engineers** writing ADRs, design docs, runbooks.
- **Founders** writing stakeholder updates, investor memos, team announcements.
- **Anyone whose work includes writing** for async audiences — the plugin is language-agnostic and role-agnostic.

## Not For

- **UI / microcopy** — use `ux-writing`.
- **Code generation or dev work** — this is a writing-tools plugin.
- **Marketing content / campaigns** — outside scope.
- **Creative writing / fiction** — use `storytelling`.
- **Auto-generated API docs** — use `documentation-generator`.

## Related Plugins

- **ux-writing** — interface text and microcopy.
- **documentation-generator** — auto-generate docs from code.
- **storytelling** — narrative structures and fiction/business stories.
- **storytelling-for-stakeholders** (via `skillstack-workflows`) — narrative-heavy pitches.
- **navigation-design** — docs-site information architecture.
- **example-design** — tutorials and runnable samples.
- **consistency-standards** — naming, taxonomy, and style standards.
- **frontend-slides** — presentations and decks.

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
