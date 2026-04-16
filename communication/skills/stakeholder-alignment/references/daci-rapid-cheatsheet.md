# DACI and RAPID — Role Assignment Cheatsheet

DACI and RAPID are the two most common frameworks for assigning roles in decisions. Both make roles explicit so disagreement doesn't stall progress and contributors know whether they are shaping or rubber-stamping.

Pick ONE framework and use it consistently across the org. Mixing is confusing.

## DACI

Simpler. Four roles.

| Role | Definition |
|---|---|
| **Driver** | Shepherds the decision. Writes the doc. Runs the meeting. Ensures the decision gets made. |
| **Approver** | Makes the final call. Usually one person. Accountable for the outcome. |
| **Contributors** | Provide input. Their concerns must be addressed; they do NOT have veto. |
| **Informed** | Need to know once the decision is made. Read-only role. |

### When to use DACI

- Teams 10-200 people
- Decisions where accountability matters more than distributed expertise
- When you want simple role assignments without disagreement about who plays what

### DACI worked example

**Decision:** Move from REST to gRPC for internal service APIs.

| Role | Assignee | Why |
|---|---|---|
| **Driver** | @sarah-kim (API platform lead) | Writes the RFC, runs the decision meeting |
| **Approver** | @eng-dir | Ultimate call; accountable for the outcome |
| **Contributors** | @mobile-lead, @web-lead, @sre-lead | Have constraints or concerns that must be addressed |
| **Informed** | @eng-org | Notified when decision is made |

**Rules applied:**
- One Approver (not "eng leadership")
- Named individuals, not teams
- Contributors represent specific constraints (mobile has build-size limits, web has browser-compat, SRE has ops concerns)
- Informed is broader than Contributors

## RAPID

More granular. Five roles. Developed by Bain. Rearranged order is intentional — the letters don't map to a decision sequence.

| Role | Definition |
|---|---|
| **Recommend** | Proposes the decision. Does the analysis. Presents options. |
| **Agree** | Formal sign-off required (legal, security, compliance). Real veto power within scope. |
| **Perform** | Executes once decided. Their operational reality shapes what's realistic. |
| **Input** | Consulted for expertise or data. Not a veto. Concerns must be heard. |
| **Decide** | Makes the call. One person. Accountable. |

### When to use RAPID

- Larger organizations where formal sign-offs exist (legal, security, compliance)
- Decisions crossing many functions with distinct expertise
- When Perform vs Input vs Decide need to be distinct roles

### RAPID worked example

**Decision:** Launch a regulated financial product in a new country.

| Role | Assignee |
|---|---|
| **Recommend** | @product-manager (makes the recommendation) |
| **Agree** | @legal-counsel (regulatory sign-off required), @security-lead (data residency sign-off) |
| **Perform** | @engineering-team + @ops-team (build + run it) |
| **Input** | @finance-lead (pricing impact), @cs-lead (support load) |
| **Decide** | @ceo (accountable for go/no-go) |

**Rules applied:**
- One Decider
- Two "Agree" roles — each has veto within their specific scope (legal veto on regulatory; security veto on data residency)
- Perform is operational — the team that builds and runs it
- Input is consultative only

## DACI vs RAPID — picking one

| Dimension | DACI | RAPID |
|---|---|---|
| Roles | 4 | 5 |
| Veto power | Only Approver | Agree (within scope) + Decide |
| Granularity | Lower | Higher |
| Common in | Tech companies, startups | Large enterprises, Bain-influenced orgs |
| Sign-off gates | Implicit | Explicit ("Agree") |
| Learning curve | Lower | Higher |

**Rule of thumb:**
- ≤200 people, no formal sign-off gates → DACI
- Cross-functional decisions with compliance / legal / security gates → RAPID
- Pick one org-wide and stick with it

## Rules that apply to both

### 1. One Approver / Decider

If two people share the role, you don't yet have a decision process. "Joint approval" is a request for permanent argument. Name one accountable person.

### 2. Name individuals, not teams

| Wrong | Right |
|---|---|
| "Platform Engineering" | "@sarah-kim (Platform Engineering)" |
| "Engineering Leadership" | "@eng-dir" |
| "The Security Team" | "@security-lead" |
| "Stakeholders" | Individual names |

A team is not a decider. A person is.

### 3. Contributors / Input are NOT vetoes

Their concerns MUST be addressed in the doc — but they do not block the decision. If a Contributor disagrees with the Decider, the disagreement is logged; the Decider decides anyway.

Exception in RAPID: "Agree" roles do have veto, but ONLY within their scope (legal can veto on legal grounds, not on preference).

### 4. Assign roles BEFORE debate starts

If roles are assigned after positions are taken, roles migrate to favor whoever shouts loudest. Publish roles in the doc's first draft.

### 5. Ambiguous situations need explicit tie-breaking

If no single Decider is obvious, escalate one level up. "We can't decide who decides" is itself a decision-escalation question.

## Common mistakes

### Mistake 1 — Group Approver / Decider

**Symptom:** "Approver: Engineering Leadership Team"
**Fix:** Name one individual. If that person wants to delegate downward or escalate upward, they can — but the buck stops with them.

### Mistake 2 — Everyone is a Contributor

**Symptom:** 15 Contributors listed. Every engineering opinion is a Contributor.
**Fix:** Contributors have distinct constraints or expertise. Broad interest ≠ Contributor; that's Informed.

### Mistake 3 — Missing Informed

**Symptom:** Decision is made, relevant people only learn in the Slack announcement.
**Fix:** Informed role exists specifically to catch people who need to know but don't shape the decision.

### Mistake 4 — Roles assigned post-hoc

**Symptom:** Debate happens, then roles are labeled after.
**Fix:** Draft the DACI / RAPID in the first version of the doc, before comment.

### Mistake 5 — RAPID "Agree" overreach

**Symptom:** Legal vetoes on commercial grounds; security vetoes on UX grounds.
**Fix:** "Agree" has veto only within scope. If legal has a commercial opinion, it's Input, not Agree.

### Mistake 6 — Treating Contributor disagreement as blocking

**Symptom:** Decision stalls because one Contributor objects; Decider defers.
**Fix:** Log the objection in the doc, the Decider decides anyway. Contributor's job was to raise the concern; Decider's job is to decide.

### Mistake 7 — Driver/Recommend = Decider

**Symptom:** Same person proposes and decides. Looks like rubber-stamping.
**Fix:** The Driver writes and shepherds; the Decider decides. Same person is possible but should be called out (e.g., "as the service owner, I'm both Driver and Decider — input from Contributors flagged below").

## Applying to common scenarios

### Scenario: Small technical choice (which library to use)

| Role | Typical assignee |
|---|---|
| Driver | Senior eng on the owning team |
| Approver | Tech lead of owning team |
| Contributors | Peer eng from related teams |
| Informed | Broader eng |

Often done in a PR description or short RFC.

### Scenario: Pricing model change

| Role | Typical assignee |
|---|---|
| Recommend | Head of Product |
| Agree | Legal (contracts), Finance (forecasting) |
| Perform | Product + Billing Engineering |
| Input | Sales (deal impact), CS (retention risk) |
| Decide | CEO or CFO |

RAPID fits better because of formal sign-off gates.

### Scenario: Architectural deprecation

| Role | Typical assignee |
|---|---|
| Driver | Architect or platform lead |
| Approver | VP Engineering |
| Contributors | Owning team leads of dependent services |
| Informed | All of engineering |

DACI usually sufficient unless legal/compliance is involved.

## Integration with the RFC template

The RFC template uses DACI by default but can be swapped for RAPID. The Roles section goes immediately below BLUF so the reader knows who plays what before reading any content.
