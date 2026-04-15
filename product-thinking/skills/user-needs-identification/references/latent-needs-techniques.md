# Latent Needs — Surfacing Techniques

Latent needs are real needs that users cannot articulate — usually because they have habituated to the workaround. They are the highest-value needs to find because nobody else has spotted them yet, and they point to differentiators rather than parity features.

## Why latent needs are hard

Users describe what they want, not what they need. Stated wants are an imperfect proxy for real needs. Latent needs are the subset of real needs that are not even articulated as wants — they are invisible because the user has adapted.

Four signals that a latent need is present:

1. Workaround
2. Apology
3. Shadow tool
4. Repeated question

Each signal corresponds to a specific elicitation technique.

## 1. Workarounds — watch what they do

A workaround is a behavior the user performs that the product did not intend. When a user pastes data into Excel, maintains a separate doc, or has two browser tabs open to compare — that is a workaround, and it points to an unmet job.

### Technique: workaround audit

1. Shadow users for 30-60 minutes doing a typical task.
2. Note each behavior that leaves your product (paste, switch app, manual transform).
3. For each exit, ask: "what were you trying to do there?"
4. Cluster exits by job. A job that has three different workarounds is a high-priority latent need.

### What good looks like

- The audit reveals workarounds the team did not know existed.
- At least one workaround produces a concrete feature idea.
- The audit produces new questions for the next research cycle.

## 2. Apologies — listen for "sorry, I still …"

An apology flags a job the main product is not doing. "Sorry, I still keep a spreadsheet for this" / "Sorry, I still export to PDF for review."

### Technique: apology mining

1. Review customer support transcripts, sales call notes, onboarding Q&A for phrases like "I still", "still have to", "I just use", "on the side."
2. For each, identify the job the user is doing outside the product.
3. Ask: is this a known gap (on the roadmap), a rejected use case (explicit non-goal), or a latent need (not on anyone's radar)?
4. Latent needs are the category worth investigating.

### What good looks like

- You find apologies that nobody inside the team had noted.
- Multiple users apologize for the same external tool / workflow.
- The apologies point to a shared need, not a personal preference.

## 3. Shadow tools — who pays out of pocket

When users pay out-of-pocket for tools that duplicate official tooling, the shadow purchase signals misalignment. A developer who pays for their own GitHub Copilot when the company provides a different AI tool is telling you something.

### Technique: shadow tool audit

1. Survey users about tools they pay for personally that relate to their work.
2. For each tool, identify the job it does.
3. Compare to what the company / official product covers.
4. Gaps are latent needs (or known gaps the team has ignored).

### What good looks like

- You discover consistent shadow tools across a segment.
- At least one shadow tool points to a capability gap in your product.
- The shadow tool's pricing model gives you willingness-to-pay data.

## 4. Repeated questions — the support / forum signal

When the same question appears over and over in support, forums, or Slack, the product is leaving a need unaddressed at the moment of need. The question is a symptom; the need is the information / capability that should have been obvious.

### Technique: repeated-question analysis

1. Pull the most-frequent questions from the last 90 days (support tags, forum topics, help-center searches).
2. Cluster by job.
3. For the top cluster, ask: why does the user reach the question? What did the UI / documentation fail to communicate?
4. The answer points to a need for in-context information, better default behavior, or new capability.

### What good looks like

- The top three questions represent 30-50% of volume. Fixing the underlying cause moves a measurable slice of support load.
- At least one cluster reveals a need the team assumed was obvious but is not.
- Some clusters are signs of onboarding gaps (fixable with education); others are genuine capability gaps (fixable with product).

## Combining signals

A high-confidence latent need shows at least two of these signals together. For example, a workaround the user apologizes for — "sorry, I still paste this into Excel to get a per-user count" — is double-witnessed, and the job (per-user count) can be promoted to roadmap candidate with confidence.

## Common mistakes

- **Trusting surveys for latent needs**: users cannot self-report needs they haven't articulated. Use behavioral / textual evidence.
- **Over-indexing on one user**: a workaround for one user is a quirk; a workaround across a segment is a need.
- **Conflating latent needs with feature requests**: feature requests are articulated wants. Latent needs are unarticulated jobs.
- **Ignoring the emotional layer of apologies**: users apologize because they feel the workaround is shameful. The shame is data — the job matters enough to compromise on.
- **Counting unmet needs, not scoring them**: a latent need that affects 2% of users once a quarter is not a priority. Score by frequency × pain × breadth before acting.

## Output: the latent-needs log

Maintain a log over time:

```
LATENT NEED                  | SIGNALS            | SEGMENT  | CANDIDATE
-----------------------------+--------------------+----------+----------
Per-user usage breakdown in  | Workaround (Excel) | Admins   | Dashboard
  a single view              | Apology ("still")  |          |  widget
Audit trail for team actions | Repeated question  | Leads    | Activity
                             | Shadow tool (3rd-  |          |  feed
                             | party audit tool)  |          |
```

The log is durable — revisit quarterly. Needs that stay unaddressed accumulate pressure until a competitor solves them.
