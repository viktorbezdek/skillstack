---
name: storytelling-for-stakeholders
description: Narrative-build workflow for turning data, technical results, or project outcomes into a compelling story for leadership, investors, or customers. Structures the narrative using proven story frameworks — 3-act, SparkLines, situation-complication-resolution (storytelling), finds the surprising angle through lateral thinking and reframing (creative-problem-solving), anchors every claim to measurable business impact using OKRs and outcome vs output framing (outcome-orientation), then iterates through craft and polish. Use when presenting quarterly results to leadership, pitching a technical initiative to non-technical stakeholders, writing a case study, summarizing a project for board review, or defending a budget request with narrative. Not for fiction writing — use storytelling directly. Not for investor pitches with full research — use the pitch-sprint workflow instead.
---

# Storytelling for Stakeholders

> The difference between a report and a story is causation. A report says "we did X and Y happened." A story says "we did X BECAUSE of Z, and Y happened WHICH MEANS W for the business." Stakeholders remember stories. They file reports.

Technical teams produce extraordinary work and then bury it in bullet points. The work deserves better. This workflow takes real results — data, shipped features, resolved incidents, cost savings — and builds a narrative that stakeholders actually remember, act on, and repeat to their own stakeholders.

---

## When to use this workflow

- Quarterly business review or all-hands presentation
- Pitching a technical initiative to non-technical leadership
- Writing a customer case study or success story
- Summarizing a completed project for board review
- Defending a budget request or headcount ask
- Post-incident review that needs to land as "we learned and improved", not "things broke"
- Internal newsletter or team update that should actually get read

## When NOT to use this workflow

- **Fiction or creative writing** — use the `storytelling` skill directly
- **Full investor pitch with research streams** — use the `pitch-sprint` workflow, which includes interviews and market analysis
- **Technical documentation** — use `documentation-generator`; narrative distorts reference material
- **Data analysis** — analyze first with the right tools, then come here to present the findings
- **The audience is already bought in** — a quick email or Slack message is enough; don't narrativize routine updates

---

## Prerequisites

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install storytelling@skillstack
/plugin install creative-problem-solving@skillstack
/plugin install outcome-orientation@skillstack
```

Three plugins, tightly composed. Each phase draws heavily on one.

---

## Core principle

**Every stakeholder story must pass the "so what?" test at every beat.** For each point in the narrative, the audience should never have to ask "so what?" — the narrative itself should answer it before they can. "We reduced latency by 40%" invites "so what?" — "We reduced latency by 40%, which means checkout completes before users lose patience, which is why abandoned carts dropped 12%" answers it. Chain every fact to a consequence the audience cares about.

Secondary principle: **the interesting part is rarely where you think it is.** Teams naturally lead with what was hardest to build. Stakeholders care about what changed for the business. Phase 2 exists to find the angle that matters to them, not to you.

---

## The phases

### Phase 1 — Structure the narrative (storytelling)

Load the `storytelling` skill. Before writing a single word, choose the right structure for this audience and context.

**Pick a framework:**

- **Situation-Complication-Resolution (SCR)** — the default for business storytelling. "Here's where we were (situation), here's what threatened that (complication), here's what we did and what happened (resolution)." Works for quarterly reviews, project summaries, and case studies.
- **SparkLines (Duarte)** — alternates between "what is" and "what could be", building tension until the audience wants the resolution. Best for pitches where you need the audience to feel the gap before you offer the solution. Use for budget requests, initiative proposals, and vision presentations.
- **3-act structure** — setup (context + stakes), confrontation (the challenge and failed approaches), resolution (what worked and the outcome). Best for longer narratives: keynotes, case studies, post-mortems turned into learning stories.
- **Before-After-Bridge** — "Here's where we were. Here's where we are now. Here's how we got there." The simplest structure. Use for short updates, newsletter items, and quick wins that need minimal setup.

**Map the beats:**
- Identify 3-5 beats (key moments) in the story. Not every data point — the moments where something changed.
- For each beat: what happened, why it matters, and what it caused next.
- Check causation: does each beat cause the next? If beats are just sequential ("and then... and then..."), the story has no engine. Reorder or reframe until each beat drives the next.

Output: a beat sheet — 3-5 beats in the chosen framework, each with the fact, the consequence, and the transition to the next beat.

### Phase 2 — Find the angle (creative-problem-solving)

Load the `creative-problem-solving` skill. The raw material is in the beat sheet. Now find what makes it interesting to THIS audience.

**Reframing techniques:**
- **Inversion** — instead of "we built X", try "without X, Y would have happened." Loss framing is more powerful than gain framing for most stakeholders.
- **Analogy** — connect the technical work to something the audience already understands. "Our caching layer works like inventory management — you pre-stock what sells fast so customers never wait." Analogies are bridges for non-technical audiences.
- **Surprise** — what's the least expected fact in the story? Lead with it or place it at the turn. "We expected the bottleneck to be the database. It was the PDF renderer." Surprise creates attention.
- **Contrast** — before vs. after with specific numbers. "Last quarter: 3 incidents per week, 45-minute mean resolution. This quarter: 1 incident per week, 8-minute resolution." Contrast makes magnitude tangible.

**The "so what?" chain:**
- Take each beat from Phase 1 and chain "so what?" three times:
  - Fact: "We reduced API response time from 800ms to 200ms"
  - So what? "Pages load in under a second"
  - So what? "Users complete the flow instead of bouncing"
  - So what? "Conversion is up 8%, which is $X per quarter"
- The third "so what?" is usually the one the stakeholder cares about. That's your real headline.

**Kill the obvious angle:**
- Whatever the first angle that comes to mind is, set it aside. It's usually "what we did" framed from the team's perspective. The audience doesn't care about what you did — they care about what changed for them. Find the angle that starts with the audience's world.

Output: the revised beat sheet with the chosen angle, the headline (the third-level "so what?"), and the specific reframing technique being used.

### Phase 3 — Anchor to outcomes (outcome-orientation)

Load the `outcome-orientation` skill. Every claim in the story must be tied to a measurable business outcome.

**Outcome vs. output:**
- **Output:** "We shipped 14 features this quarter." (Nobody cares.)
- **Outcome:** "Customer onboarding time dropped from 3 days to 4 hours." (Everyone cares.)
- Audit every beat in the story. Replace outputs with outcomes wherever possible. If a beat can only be described as an output, it might not belong in the story.

**Connect to existing OKRs or goals:**
- If the organization has OKRs, tie the story to them explicitly. "This work moved KR-3 from 60% to 85%."
- If there are no OKRs, frame the outcome in terms the audience already tracks: revenue, cost, time-to-market, customer satisfaction, retention, risk reduction.

**Quantify honestly:**
- Use real numbers, not inflated ones. Stakeholders detect exaggeration and discount everything after they catch it.
- If you can't quantify, qualify precisely: "We don't have the exact revenue impact yet, but the leading indicator (checkout completion rate) moved from 72% to 84%, and historically each point is worth approximately $X."
- Acknowledge what you don't know. Credibility compounds.

**The impact statement:**
- Write one sentence that captures the entire story's impact. This is the sentence the stakeholder will repeat to their stakeholder. If you can't write it, the story isn't focused enough.
- Test: would this sentence make sense to someone who hasn't heard the rest of the story? If yes, it's a good headline. If no, it depends on too much context.

Output: the final beat sheet with every beat anchored to a measurable outcome, plus the one-sentence impact statement.

### Phase 4 — Craft and polish

No new skill to load — this phase uses the combined output of Phases 1-3.

**Write the first draft:**
- Follow the beat sheet. One section per beat. The framework from Phase 1 provides the structure; the angle from Phase 2 provides the energy; the outcomes from Phase 3 provide the evidence.
- Open with the headline (the impact statement). Stakeholders are busy — lead with the conclusion, then tell the story of how you got there. This is not fiction; don't save the reveal for the end.

**Edit pass 1 — cut ruthlessly:**
- Every sentence must advance the story or provide evidence. If it does neither, cut it.
- Technical details that don't serve the narrative go into an appendix, not the body.
- Target length: 1 page for a written memo, 8-12 slides for a deck, 5 minutes for a spoken presentation. Shorter is almost always better.

**Edit pass 2 — concretize:**
- Replace every abstract word with a specific one. "Significant improvement" becomes "40% reduction." "Several customers" becomes "Acme Corp, Bravo Inc, and three others."
- Replace every passive sentence with an active one. "Latency was reduced" becomes "The team reduced latency."

**Edit pass 3 — read aloud:**
- If presenting, read the whole thing aloud. Every sentence you stumble on gets rewritten.
- If written, read aloud anyway. Awkward writing is awkward reading.

**Final check:**
- Does every beat pass the "so what?" test?
- Is the one-sentence impact statement still accurate after edits?
- Could a stakeholder retell this story in 30 seconds? If not, it's too complex.

Output: the final narrative — memo, deck, or script — ready for delivery.

---

## Gates and failure modes

**Gate 1: the structure gate.** No writing until the beat sheet exists. Writing without structure produces rambling, and rambling loses stakeholders in the first paragraph.

**Gate 2: the outcome gate.** Every beat must be anchored to a measurable outcome before the draft is written. If a beat can only be described as an output ("we shipped X"), either reframe it as an outcome or cut it.

**Failure mode: the team-hero trap.** The story is about how hard the team worked and how clever the solution was. The audience doesn't care — they care about what changed. Mitigation: Phase 2's "kill the obvious angle" step. If the angle is "look what we built", it's the wrong angle.

**Failure mode: data without narrative.** The presentation is a spreadsheet with a title slide. Numbers without causation don't stick. Mitigation: Phase 1's framework selection forces a narrative arc. Every number must live inside a beat.

**Failure mode: narrative without data.** The story is compelling but has no evidence. The first skeptical question collapses it. Mitigation: Phase 3's outcome anchoring. Every claim has a number or an honest qualifier.

**Failure mode: wrong audience.** The story is perfect for the CTO but you're presenting to the CFO. Mitigation: the "so what?" chain in Phase 2 must be run from the perspective of the actual audience, not the team.

---

## Output artifacts

A completed storytelling workflow produces:

1. **The narrative** — memo, deck, or script, ready for delivery
2. **A beat sheet** — the story's skeleton, reusable for future updates
3. **The impact statement** — one sentence, quotable, repeatable
4. **An evidence appendix** — supporting data, methodology, and caveats that didn't fit in the narrative but are ready for Q&A

---

## Related workflows and skills

- For a full pitch with primary research (interviews, market analysis), use the `pitch-sprint` workflow
- For data-specific presentations, use the `data-storytelling` reference within the `storytelling` skill
- For speeches and keynotes specifically, use the `speech-and-presentation` reference within the `storytelling` skill
- For defining the outcomes to build toward (not just present), use `outcome-orientation` directly

---

> *SkillStack Workflows by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
