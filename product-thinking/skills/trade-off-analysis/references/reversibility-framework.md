# Reversibility — One-Way and Two-Way Doors

Bezos's framing: decisions split into two categories based on reversibility. Matching decision speed to reversibility is the most common discipline gap in product organizations.

## The two categories

### Two-way door

A decision you can walk back. The cost of wrongness is small — you reverse, you learn, you move on.

Characteristics:
- Low switching cost to reverse.
- Few dependencies outside the team.
- Failure is observable within days or weeks.
- No customer trust damage from reversal.

Examples:
- Feature-flagged experiment on 5% of users.
- UI copy change.
- A new onboarding email in the sequence.
- An internal tooling tweak.
- A pricing experiment gated to one segment.

**How to decide**: fast. Test, learn, iterate. Debate should be short because the cost of the wrong decision is small and the cost of debating is larger.

### One-way door

A decision that is hard or impossible to reverse. The cost of wrongness is large — months of work, customer trust damage, legal or financial consequences.

Characteristics:
- High switching cost to reverse.
- External dependencies (customers, regulators, contracts).
- Failure only visible months or quarters later.
- Reversal causes visible harm (broken trust, legal exposure, team morale collapse).

Examples:
- Changing the pricing model globally.
- Renaming the product.
- Deprecating an API with external consumers.
- Choosing a foundation database or cloud.
- Public commitments (roadmap pledges, SLA promises).
- Major architectural decisions with cross-team rippling.

**How to decide**: slow. Gather evidence. Lower confidence intervals. Build consensus. The cost of the decision is so large that the cost of extra debate is small by comparison.

## The common mismatch

Teams invert the pairing:

- **Too slow on two-way doors.** Weeks of debate over a UI copy change that could have been A/B tested in a day. The cost is time and momentum.
- **Too fast on one-way doors.** A pricing model change decided in a single meeting. The cost is a quarter of damage-control when it turns out wrong.

The fix is to classify first, then match decision speed to class.

## Borderline cases

Some decisions look one-way but are two-way (or vice versa). Diagnostic questions:

**Could be two-way disguised as one-way**:
- Can the change be gated by a feature flag?
- Can we roll out to a subset first?
- Can we keep the old path alive alongside the new one?

If yes to any, you may have a two-way door. Test for confirmation.

**Could be one-way disguised as two-way**:
- Does the change affect customers who will form habits or expectations?
- Does it trigger external dependencies (integrations, SEO, contracts)?
- Does reversal require asking for forgiveness publicly?

If yes to any, you may have a one-way door. Treat it carefully.

## Worked examples

### Rename the product (one-way door)

Surface: "It's just a rename — update the logo and the docs."
Reality: customers have muscle memory, integrations reference the name, SEO is anchored to it, docs and tutorials on the open web reference it, partners have negotiated terms using the old name.
Reversal cost: months of confusion and re-education.
Decision speed: slow. Pilot with a specific segment, measure recognition, validate before global rollout.

### Change pricing model from per-seat to usage-based (one-way door)

Surface: "We just update the billing engine."
Reality: existing customers have contracts, procurement negotiated terms that assumed the old model, forecasts and commissions are built against the old model, finance teams plan around it.
Reversal cost: breaking active contracts, renegotiating, re-building trust.
Decision speed: slow. Gather extensive evidence. Run pilots. Grandfather existing customers.

### Experiment on 10% of users with a feature flag (two-way door)

Surface: "We're running an A/B test."
Reality: the flag isolates the change; if results are bad, you disable the flag; customers not in the cohort never saw the change.
Reversal cost: minutes.
Decision speed: fast. Ship the experiment, read the results, decide.

### Deprecate a public API (one-way door)

Surface: "We'll announce 6 months of deprecation and move on."
Reality: integrators have production systems built on it, some cannot migrate in the timeline, deprecating too quickly damages trust.
Reversal cost: high — reversing requires public apology and re-commitment.
Decision speed: slow. Over-communicate. Consider whether "deprecate" can instead be "support in read-only mode indefinitely."

## Decision-speed heuristics

- **Two-way door**: when debate time exceeds decision value, ship it. If reversal is a day of work, 3 days of meetings to avoid a bad decision is worse economics than 1 day to reverse.
- **One-way door**: when the cost of wrongness exceeds a quarter of work, invest in evidence before deciding. Consensus is not the goal; shared evidence base is.
- **When in doubt**: treat as one-way and look for ways to convert it into two-way (flags, pilots, phased rollout). Converting a one-way door into a two-way door is often the most valuable move available.

## Meta-rule

Every important decision should have an explicit answer to the question: **if this turns out wrong, what does reversal cost?** Teams that can't answer are deciding blind on reversibility and will eventually eat the cost.
