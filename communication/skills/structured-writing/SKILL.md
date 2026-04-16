---
name: structured-writing
description: >-
  Structure a written piece using BLUF (Bottom Line Up Front), the Minto
  Pyramid Principle, inverted pyramid, or SPQR (Situation-Problem-Question-
  Resolution). Use when the user asks to write BLUF-style, apply the Pyramid
  Principle, structure a memo/email/doc, lead with the conclusion, outline a
  long message so it is skim-readable, or reorganize buried-lede writing. NOT
  for line-level clarity and concision editing (use clarity-editing). NOT for
  UI microcopy (use ux-writing). NOT for narrative or story arcs (use
  storytelling). NOT for slide decks (use frontend-slides).
---

# Structured Writing

Most writing fails by burying the point. A structured document leads with the conclusion, supports it with grouped evidence, and lets the reader stop reading the moment they have what they need.

## Pick a structure

| Structure | Best for | Lead |
|---|---|---|
| **BLUF** (Bottom Line Up Front) | Emails, status updates, requests | The ask or the answer |
| **Minto Pyramid** | Reports, strategy memos, analyses | The single governing thought |
| **Inverted pyramid** | News-style updates, announcements | The headline fact |
| **SPQR** (Situation-Problem-Question-Resolution) | Briefs, consulting narratives | The situation, built to the ask |

Pick by reader, not by habit. A busy executive needs BLUF; a peer reviewing analysis needs a pyramid; a team reading an announcement needs inverted pyramid.

## BLUF — the default for async work

A BLUF message opens with: **the ask, the answer, or the conclusion** — in under 30 words — followed by supporting detail the reader can skip.

```
BLUF: [ask / decision / answer in one sentence]

Why it matters:
- [reason 1 in ≤12 words]
- [reason 2]

Details (only if the BLUF doesn't answer their question):
- [supporting fact with number]
- [supporting fact with reference]

What I need from you:
- [explicit ask with deadline] or "FYI — no action needed."
```

Rules:
- The subject line is the BLUF, compressed.
- The BLUF sentence is self-contained — it must make sense without the rest.
- If someone replies from the first 30 words, the message worked.

Full worked examples and email/Slack/standup templates in `references/bluf-templates.md`.

## The Minto Pyramid

Barbara Minto's pyramid: every document has one governing thought, supported by 3-5 grouped arguments, each supported by evidence.

```
                  Governing thought
                 (what + why + so-what)
                          |
          ┌───────────────┼───────────────┐
      Argument 1      Argument 2      Argument 3
          |               |               |
       Evidence       Evidence       Evidence
```

Rules:
- Arguments at the same level share a logical relationship (MECE — mutually exclusive, collectively exhaustive).
- Each argument answers a "why" or a "how" that the governing thought raises.
- If an argument doesn't raise a predictable question, it doesn't belong at that level.

See `references/minto-pyramid-method.md` for the question-answer logic, MECE groupings, and the SCQ (Situation-Complication-Question) introduction.

## SPQR for briefs

When the reader needs context before the ask:

- **Situation** — one paragraph of shared, uncontroversial context.
- **Problem** — the change or complication that makes a decision necessary.
- **Question** — the specific question you need answered.
- **Resolution** — your recommendation + what you need from the reader.

Useful for consulting-style briefs, board materials, vendor proposals. Less useful for async team updates (use BLUF instead).

## Skim-readability checklist

Structured writing is skim-tested, not read-tested. Before sending, ask:

- [ ] Can the reader get the main point in the first 30 words?
- [ ] Does every paragraph have a clear topic sentence?
- [ ] Are supporting lists parallel in structure?
- [ ] Can the reader stop reading at any paragraph and still have the main point?
- [ ] Does the ask (if any) appear in the first sentence AND the last sentence?
- [ ] Is the longest paragraph under 100 words?

If any answer is no, restructure before polishing words.

## Anti-patterns

- **Buried lede** — the conclusion is in paragraph 4. Move it to paragraph 1.
- **Chronological narrative** — "here's what we did, then what we discovered, then what we decided." Invert: lead with the decision.
- **Argument without governing thought** — three arguments pointing in different directions with no synthesizing claim.
- **Evidence dumping** — numbers and screenshots with no argument they support.
- **Parallel violations** — some list items are nouns, others are verbs, others are sentences. Make them parallel.
- **Structure for its own sake** — applying BLUF to a 200-word email nobody would read twice anyway. Structure serves speed, not ceremony.

## Workflow

1. **Identify the reader.** Who reads this, how fast, with what in their head?
2. **Pick the structure.** BLUF for action, pyramid for analysis, inverted for announcement, SPQR for briefs.
3. **Write the single governing thought.** If you can't state it in one sentence, you're not ready to write.
4. **List supporting points.** 3-5, parallel, MECE.
5. **Fill in evidence.** Numbers, references, quotes.
6. **Polish after structure is right.** Clarity editing comes last — see `clarity-editing`.

## References

| File | Contents |
|---|---|
| `references/bluf-templates.md` | BLUF templates for email, Slack, standup updates, PR descriptions with worked examples |
| `references/minto-pyramid-method.md` | Full Minto method — governing thought, MECE arguments, SCQ intros, question-answer logic |
| `references/structure-selection-matrix.md` | Reader × purpose × medium matrix for picking the right structure |

## Related skills

- **clarity-editing** — line-level editing once the structure is right.
- **stakeholder-alignment** — when the piece is an RFC/proposal, structure plus roles.
- **documentation-discipline** — when to write at all, and which artifact type to use.
- **visual-communication** — when a diagram replaces paragraphs.
- **storytelling-for-stakeholders** — narrative-heavy pitches and board materials.
