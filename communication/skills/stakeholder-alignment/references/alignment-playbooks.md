# Alignment Playbooks

Templates fail without process. These playbooks cover the common alignment situations and the repeatable moves that produce a decision.

## Playbook 1 — Async cross-team alignment on a technical change

**Situation:** Three to ten teams will be affected by an architectural change. Full synchronous alignment meetings are expensive.

### Steps

1. **Identify the change scope in one sentence.** Write it down. If you cannot state it, you're not ready to start.

2. **Identify stakeholders.** List every team with a dependency, integration, or affected workflow. Named contacts per team.

3. **Draft the short-form RFC.** BLUF at top. Options section with at least 3 options including do-nothing. Trade-offs explicit. DACI roles assigned.

4. **Post with explicit comment deadline.** "Comments by [date]. Approval from [Approver] by [date]." Without dates, the RFC drifts.

5. **Prompt contributors individually.** A broadcast post is easy to ignore. Personal ping to named contributors explaining why their input matters.

6. **Address every comment.** Either incorporate the change, or reply in thread with "declined, because..." No comment gets silent treatment.

7. **At deadline, summarize.** "Here's what changed based on feedback. Here are the unresolved concerns. Approver decides by [date]." This snapshots the decision-readiness.

8. **Decider decides.** Not "the group consents." The Decider decides on the doc; Contributors' concerns are on record.

9. **Post the decision.** Short announcement linking the RFC, the decision, and the follow-up plan.

10. **Execute.** Plan milestones in the RFC become tickets; owners track.

### Common failures

- **Broadcast without personal pings.** Assumes people read Slack announcements in full. They don't.
- **Comments ignored.** The Approver makes the decision without responding to concerns, and contributors feel unheard. Even if you override a concern, acknowledge it.
- **Soft deadline.** "Comments soon" instead of "Comments by Friday EOD." Soft deadlines get ignored.
- **Deferring the decision.** Contributor A disagrees, so the decision waits for more input. Often the Approver should decide anyway; the job of Contributors is to raise concerns, not to block.

---

## Playbook 2 — Decision meeting with a pre-read

**Situation:** A 30-minute meeting is scheduled to decide a topic. Want it to be efficient.

### Steps

1. **Draft the pre-read 48 hours before the meeting.** 1-2 pages max. BLUF, options, recommendation, specific meeting ask.

2. **Confirm attendees have time to read.** Send with the calendar invite. Not in the chat day-of.

3. **Start the meeting with role confirmation.** "Decider is X. Contributors are A, B, C." Re-state so no ambiguity.

4. **Ask: does everyone agree the pre-read describes the decision accurately?** 30 seconds. Catches mis-framed problems before you waste the meeting.

5. **Walk through open questions only.** Do NOT re-explain the pre-read. If someone didn't read, that's their problem — walk the open questions as if they did.

6. **Decider decides.** Before the meeting ends. If the Decider cannot decide, name what's missing and set a follow-up with a date.

7. **Summarize decision in the meeting.** Before closing, say aloud: "We decided X. A and B will do Y and Z by W." Get nods.

8. **Post a written summary within 24 hours.** Includes: decision, roles, rationale (brief), follow-ups with owners and dates.

### Common failures

- **Pre-read not read.** Meeting becomes re-reading the pre-read. Either the pre-read was too long, sent too late, or attendees don't prioritize.
- **Decider hedges.** "Let's let it ferment." Fermenting is a real choice sometimes; usually it's avoidance.
- **No written summary.** Decision made, but nobody documents. Two weeks later nobody agrees on what was decided.

---

## Playbook 3 — Announcing an unpopular decision

**Situation:** A decision has been made that will be received poorly by some. Layoffs, pricing changes, deprecations, strategy pivots.

### Steps

1. **Accept the reaction is part of the plan.** Unpopular decisions don't have a communications path that eliminates pain. The goal is honest communication, not minimizing discomfort.

2. **Write the announcement with inverted pyramid.** Headline fact first. Details second. Context last.

3. **Do not apologize for the decision, but acknowledge impact.** "We know this affects X. Here's what we're doing about it." Different from "We're sorry we made this choice" — you decided, own it.

4. **Name what is and isn't negotiable.** Hedging about whether the decision is final produces worse follow-up conversations than directly stating it is final.

5. **State what comes next concretely.** Timelines. Contacts. Support processes. Financial implications. Decision-tree answers.

6. **Send at a time respectful of recipients.** Not 5pm Friday. Not mid-vacation. Monday morning gives a full week for follow-up.

7. **Be present for questions.** Whoever owns the decision is available for conversations for at least the next week.

8. **Track follow-up questions and answer them publicly.** FAQ document updated as questions come in.

### Common failures

- **Burying the decision.** Opening with two paragraphs of context, then the decision in paragraph 4. The reader's attention finds the decision anyway; the burial just reads as cowardice.
- **Fake options.** "We considered several options." If options were considered seriously, say what they were. If not, don't pretend.
- **Leader invisibility after announcement.** Send the message and disappear. Recipients interpret the silence as "management doesn't care."
- **Hedging on finality.** "We may revisit this." If the decision is final, say so. If it's not final, don't call it a decision.

---

## Playbook 4 — Escalating a stalled decision

**Situation:** A decision has been debated for weeks; no one is deciding.

### Steps

1. **Name the stall.** Write down: "We have been discussing X for N weeks. No decision has been made. The cost of delay is Y per week."

2. **Identify the Decider.** If there is none, the decision structure is broken; name a Decider and proceed. If there is a Decider who is not deciding, the issue is confidence or missing information.

3. **Surface the blocker.** What does the Decider need to decide? More data? More opinions? Written down explicitly.

4. **Escalate the question, not the debate.** Send the Decider a one-page summary: the decision, the options, the stall cause, the cost of continued delay. Ask: "What do you need to decide by [date]?"

5. **Set a hard deadline.** "We will decide by [date]. If no decision is made, we default to [do nothing / option A / escalate further]." Having a fallback disarms the cost of inaction.

6. **If the Decider still doesn't decide, escalate.** One level up. With the same one-pager. Escalation is not personal; it's a process step.

### Common failures

- **Re-running the debate in escalation.** The escalation meeting becomes another round of the same discussion. Re-assert: "The decision is between A and B. What information does the Decider need to decide?"
- **Decider absorbs escalation.** Takes the question, then stalls again. Pin with a dated deadline and a fallback.
- **Nobody wants to escalate.** Escalation feels like tattling. Reframe: escalation is calling on the process, not the person.

---

## Playbook 5 — Aligning after misalignment

**Situation:** The team acted on what they thought was the decision. Leadership thought a different thing was decided. Team has been executing a wrong plan for weeks.

### Steps

1. **Identify the gap without blame.** "Team thought X. Leadership thought Y. Reading the decision doc, it's actually ambiguous." Blame-free diagnosis first.

2. **Decide what the decision actually is.** The written artifact is the source of truth. If it's ambiguous, re-decide now.

3. **Decide what to do about the wrong direction.** Stop and pivot? Complete the current work and then pivot? The "blame-free" part of step 1 is critical so the team can make the right call, not the political call.

4. **Revise the decision doc.** Add clarifying language. Note the ambiguity and how it was resolved.

5. **Explicitly note the misalignment in a post-mortem.** Process improvement: why was the decision ambiguous? Was the doc short on detail? Were assumptions not named? Fix the process, not the people.

6. **Announce the revised decision.** Same channel as the original. Transparency about the correction.

### Common failures

- **Blame.** "Who misread the doc?" The doc was ambiguous; nobody misread. Fix the doc, not the person.
- **Sunk-cost anchoring.** "We've spent 3 weeks on X; let's finish anyway." Separate the question of what was decided from what should happen now.
- **No retrospective.** Same kind of misalignment recurs in 3 months. The playbook is only useful if you learn from it.

---

## Playbook 6 — Pre-mortem for a major decision

**Situation:** A major one-way-door decision is about to be made. Want to surface risks before committing.

### Steps

1. **Assemble 5-8 stakeholders with diverse views.** Not just yes-people.

2. **Prompt:** "Imagine it's six months from now and this decision was a disaster. Write what happened, in 10 minutes, silently."

3. **Read each story aloud.** Without judgment or defense.

4. **Cluster themes.** Which failure modes appeared multiple times?

5. **For each cluster, decide:**
   - Is this a risk we can mitigate? → Add mitigation to the plan.
   - Is this a risk we should accept? → Document the acceptance.
   - Is this a deal-breaker? → Stop, reconsider the decision.

6. **Update the decision doc with risks and mitigations.**

### Common failures

- **Pre-mortem as ceremony.** The ceremony is held but findings are ignored. The point is to let pre-mortem findings change the decision.
- **Shallow disaster stories.** Participants write vague failures ("it didn't work"). Push for specificity: "customer churn spiked 15% because X."
- **Defensive responses.** The Decider defends the decision during the pre-mortem. Rule: no defense during the pre-mortem — just listen and note.

---

## Cross-cutting principles

1. **Deadlines are dates, not adjectives.** "Soon", "quickly", "ASAP" are not deadlines.
2. **One Decider per decision.** Always. No exceptions.
3. **Contributors' concerns must be addressed — not necessarily accommodated.** The doc reflects that their concerns were heard.
4. **Escalation is a tool, not a failure.** Use it when needed without guilt.
5. **Write it down.** Decisions that live only in chat or memory disappear under the first disagreement.
6. **Name the cost of delay.** Stalled decisions usually have a cost nobody is counting. Count it.
