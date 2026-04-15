# Value Proposition Canvas — Walkthrough

The Value Proposition Canvas (VPC) forces explicit alignment between what a customer needs and what a product offers. Each element on the value map must trace to an element on the customer profile. Orphans on either side are the primary diagnostic signal.

## Canvas structure

```
                CUSTOMER PROFILE (right)              VALUE MAP (left)
        ┌───────────────────────────────┐     ┌─────────────────────────────┐
        │                               │     │                             │
        │       JOBS (what they         │     │  PRODUCTS & SERVICES        │
        │       try to get done)        │◄────┤  (what you offer)           │
        │                               │     │                             │
        │       PAINS (what gets        │     │  PAIN RELIEVERS             │
        │       in the way)             │◄────┤  (how you reduce pains)     │
        │                               │     │                             │
        │       GAINS (wanted           │     │  GAIN CREATORS              │
        │       outcomes)               │◄────┤  (how you produce gains)    │
        │                               │     │                             │
        └───────────────────────────────┘     └─────────────────────────────┘
```

Arrows are mandatory. Every item on the left must point to an item on the right.

## Step-by-step

### Step 1 — Segment first

Do not build a canvas for "users." Build one per segment. Typical segmentation axes:

- Role (end user, buyer, admin).
- Company size or maturity (startup, mid-market, enterprise).
- Use case (daily driver, occasional task).
- Stage of adoption (prospect, new user, power user).

If two segments have different pains or jobs, they need different canvases. If they share 80% of jobs and pains, a single canvas is fine.

### Step 2 — Fill the customer profile from evidence

Jobs, pains, gains come from interviews, observation, and support data — not team speculation.

**Jobs**: use JTBD framing. Write 5-10 jobs, ordered by importance (see `user-needs-identification` deep-dive on scoring).

**Pains**:
- What is too time-consuming, costly, or effortful?
- What makes users feel bad (emotional friction)?
- What makes the job risky (financial, social, functional)?
- What currently does not work well in their workaround?

**Gains**:
- Required (the job cannot be called done without this).
- Expected (table stakes — the user assumes it).
- Desired (nice to have — the user would mention it if asked).
- Unexpected (would delight — the user would not imagine it).

Mark each pain and gain by importance: high / medium / low.

### Step 3 — Fill the value map as hypotheses

The left side is your bet. Every item is a hypothesis, not a fact, until validated.

**Products & services**: what you provide (features, tangible outputs).
**Pain relievers**: how the offering reduces or removes specific customer pains.
**Gain creators**: how the offering produces specific customer gains.

### Step 4 — Trace every left item to a right item

This is the most-skipped step and the most diagnostic.

For each pain reliever and gain creator, draw an arrow to the specific pain or gain it addresses. Three possible outcomes:

1. **Clean trace** — each left item maps to one or more specific right items. Keep.
2. **Orphan** — a pain reliever that addresses no stated pain. Either cut the feature, or update the customer profile (you missed a real pain).
3. **Unmet need** — a pain or gain with no matching pain reliever or gain creator. Either add to the roadmap, or explicitly decide this segment's pain is not served.

### Step 5 — Rank coverage

For each pain and gain, how much is covered?

- 0 (not addressed)
- 1 (partially addressed)
- 2 (fully addressed)

Sum across all pains → pain coverage score. Sum across all gains → gain coverage score. A segment with low coverage on high-importance pains is under-served; a segment with full coverage but low importance pains is over-built.

## Example (remote-team-lead segment)

### Customer profile

**Jobs**:
1. Run a productive weekly standup across three time zones (high importance)
2. Spot when a team member is blocked without calling it out publicly (medium)
3. Keep async context for team members who were offline (high)

**Pains**:
- Someone is always attending at an uncivilized hour (high)
- Spoken updates get lost; no searchable record (high)
- Long meetings dilute the signal (medium)

**Gains**:
- Decisions reached in ≤20 minutes (required)
- Everyone feels heard regardless of timezone (desired)
- A searchable log that new team members can catch up with (expected)

### Value map

**Products & services**: async standup tool with threaded updates, digest emails, time-zone-aware scheduling.

**Pain relievers**:
- No live call required → removes "someone always attends at odd hours" pain.
- Everything is written and searchable → removes "spoken updates lost" pain.
- Skim-readable format → removes "long meetings dilute signal" pain.

**Gain creators**:
- Decision digest surfaced in daily email → produces "decisions reached ≤20 min" gain.
- Threaded updates let every voice land → produces "everyone heard" gain.
- Auto-archived log → produces "searchable record" gain.

### Traceability check

Every pain and gain has a matching reliever / creator. No orphans. Problem-solution fit on paper; PMF still requires customer validation.

## When the canvas fails

- **Team-written jobs** — nobody interviewed the segment; jobs are speculation.
- **No importance ranking** — all pains treated as equal, so the product over-serves low-importance pains and under-serves high-importance ones.
- **Features on the left, not relievers** — "real-time collaboration" is a feature; it becomes a reliever only when tied to a specific pain.
- **Single canvas for multiple segments** — the canvas is vague because it averages across segments.
- **No iteration** — the canvas is built once and never updated as evidence arrives.

The canvas is a living document, not a deliverable. Revisit quarterly and after any meaningful customer research.
