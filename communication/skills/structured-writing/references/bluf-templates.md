# BLUF Templates

BLUF (Bottom Line Up Front) is a structure, not a slogan. It opens with the ask, answer, or conclusion in 30 words, then supports it with detail the reader can skip. The discipline is that the first 30 words must be self-contained — someone who stops reading at that point must still understand the message.

## The core template

```
BLUF: [ask / decision / answer — one sentence, under 30 words]

Why it matters:
- [reason 1 in ≤12 words]
- [reason 2]
- [reason 3, if needed]

Details (only if the BLUF doesn't answer the reader's next question):
- [supporting fact with number or reference]
- [supporting fact]

What I need from you:
- [specific ask with deadline] — OR — "FYI, no action needed"
```

## By medium

### Email

Subject = BLUF compressed.

```
Subject: Rollback proposed onboarding changes Monday — need approval

BLUF: I'm proposing we roll back last month's onboarding changes on Monday and
re-test them one at a time. Need approval from @Alex by Friday.

Why:
- July activation rate dropped 12% vs June (first decline in 6 quarters)
- Analytics attributes 8 of 12 points to onboarding friction
- Rolling back before Q3 planning lets us rebuild from baseline

Details:
- Attribution analysis: [link]
- Rollback takes ~2 hours; re-test plan is 3 sprints

What I need:
- @Alex: approve by Friday (async OK)
- @Jess: confirm mobile team can absorb the re-test
```

### Slack

One message. No second paragraph unless truly needed.

```
⚠️ Deploy at 4pm — need +1 from @channel

BLUF: Deploying the auth fix at 4pm PT today; covers CVE-2026-0042.
Low-risk change, rollback tested. Need a +1 to proceed.

Details: [PR link] | [rollback plan]
```

### Standup update

```
Yesterday: [shipped / blocked on]
Today: [shipping / investigating]
Blockers: [named or "none"]
Decision needed from team: [yes/no — if yes, one line]
```

Keeps the structure even shorter — standups are skimmed, not read.

### PR description

```
## BLUF
[One sentence: what this PR does + why + risk level.]

## Changes
- [Change 1 in 5-10 words]
- [Change 2]

## Testing
- [How you tested, not that you tested]

## Rollback
- [One-line rollback plan, or 'straightforward revert']

## Related
- [Ticket / issue / discussion link]
```

### Status report (weekly/monthly)

```
BLUF: [One-sentence summary of the period — green/yellow/red + reason.]

Highlights:
- [Concrete win with metric]
- [Concrete win with metric]

Concerns:
- [Concrete concern with what's being done]

Asks:
- [Specific ask from leadership, or "none"]

Details (optional): [link to full doc]
```

## BLUF rules

1. **The BLUF sentence is the message.** Everything else is optional.
2. **Under 30 words.** If you can't fit it, the scope is too wide; send two messages.
3. **Ask or answer, not both.** An email that ends with "thoughts?" is not a BLUF — it's a discussion opener.
4. **No preamble.** Nobody needs "I hope you're doing well. I wanted to reach out because…" in a BLUF.
5. **Deadlines explicit.** "ASAP" is not a deadline. "By Thursday EOD PT" is.

## Common mistakes

- **BLUF as ceremony** — writing "BLUF:" at the top but then burying the actual point in paragraph 3. The label is not the structure.
- **Multiple BLUFs** — two or three asks in one message. Each ask deserves its own message.
- **BLUF-then-wall** — the BLUF is tight, then followed by 800 words of context. If the BLUF worked, cut the context by 70%.
- **BLUF without ask** — every BLUF implies an ask (action, decision, acknowledgment). Name it, or say "FYI, no action needed."
- **Structural BLUF but passive voice** — the structure helps but the sentence is still mushy. BLUF compresses; clarity-editing polishes.

## When BLUF is wrong

- **Sensitive topics requiring context before the ask** — layoffs, restructures, personal feedback. Use SPQR or a more narrative structure.
- **Narrative pieces** — a blog post or essay is not a BLUF.
- **Very short messages** — "LGTM, shipping" does not need BLUF scaffolding.

## Worked transformation

### Before (buried lede)

> "Hi team, hope you all had a good week. I wanted to share some thoughts on our recent Q3 performance. We had a solid start to the quarter in July and saw some encouraging trends in early August. However, upon closer inspection of the data and in conversations with various team members, I've come to believe that we may want to consider the possibility of rolling back some of the onboarding changes we made at the end of June. I'd love to hear your thoughts on this and perhaps we can discuss at our next staff meeting. Let me know what you think."

Problems: opens with pleasantry (waste), narrative chronology, hedges ("may want to consider the possibility"), no clear ask, no deadline.

### After (BLUF)

> **Subject: Roll back onboarding changes Monday — need approval by Friday**
>
> **BLUF:** Rolling back the late-June onboarding changes Monday to rebuild Q3 from baseline. Need approval from @Alex by Friday EOD.
>
> Why:
> - July activation rate down 12%; analytics attributes 8 pts to onboarding friction.
> - Re-test plan isolates each change over 3 sprints.
>
> What I need: @Alex approval (async OK).
> Full attribution analysis: [link]

Word count: 55 vs 135. Clear ask. Clear deadline. Readers who stop after the subject line still know the ask.
