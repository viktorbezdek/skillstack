# Documentation Decision Tree

What to write, when to write it, and which artifact type. This reference is the full decision tree from the SKILL with worked examples and the reasoning behind each branch.

## The master tree

```
Is the question likely to be asked again?
├── No → don't document (Slack thread, wiki FAQ, or nothing)
└── Yes → keep going ↓

Is the answer likely to change often?
├── Yes (weekly / monthly) → FAQ or living doc, owned + dated
├── Medium (quarterly) → runbook or reference doc
└── No (rarely) → keep going ↓

Is the answer a decision with long-term consequences?
├── Yes, architectural → ADR (numbered, immutable)
├── Yes, other → decision doc (from stakeholder-alignment)
└── No → keep going ↓

Is the answer operational (how to do X)?
├── Yes, repeatable procedure → runbook
└── No → keep going ↓

Is the answer reference information (constants, schemas, APIs)?
├── Yes → reference doc / README section
└── No → keep going ↓

Is the answer a rough idea for discussion?
├── Yes → one-pager
└── No → probably doesn't need a doc
```

## Branch explanations

### "Is the question likely to be asked again?"

**Yes if:**
- You have heard the same question 2+ times.
- New hires ask it.
- The answer is not obvious from the code or system.

**No if:**
- It's a one-off question answered in chat.
- The answer is trivially derivable from reading the code.
- The question is context-specific and won't recur.

**Edge case:** questions asked infrequently but with high stakes (how to handle X in an incident) should be documented as runbooks even if the frequency is low.

### "Is the answer likely to change often?"

**Often (weekly/monthly):**
- Team rotations
- Current on-call schedules
- Product roadmap
- Employee directory

**Rarely:**
- Architecture decisions
- Naming conventions
- Code organization

High-change-rate content should live in living docs (wiki pages, spreadsheets, FAQs) with clear ownership. ADRs and decision docs are for stable content.

### "Is the answer a decision with long-term consequences?"

**Architectural decisions (→ ADR):**
- Choice of language, framework, database
- Communication style (REST vs gRPC vs GraphQL)
- Deployment model (Kubernetes vs serverless)
- Storage approach (relational vs document)
- Auth model
- API versioning strategy

**Non-architectural decisions (→ decision doc):**
- Team structure changes
- Process adoptions (e.g., "we use Conventional Commits")
- Tool selections (e.g., "pnpm over npm")
- Business rules (e.g., pricing-model change)
- Hiring guidelines

The distinction: ADRs are for choices that shape the **running system**. Other decisions shape the team or process.

### "Is the answer operational?"

**Yes (→ runbook) if:**
- It's a procedure you follow.
- There are steps and expected results.
- Getting them wrong has consequences.

**Examples:**
- Deploy procedure
- Backup verification
- Incident response
- Release cut
- Customer escalation handling

### "Is the answer reference information?"

**Yes (→ reference doc) if:**
- It's a list of things (constants, codes, status values).
- It's a schema or API definition.
- It's a glossary of terms.
- It's a configuration matrix.

Reference docs don't teach; they look up. Best formats: tables, sorted lists, auto-generated from source.

### "Is the answer a rough idea for discussion?"

**Yes (→ one-pager) if:**
- You want feedback before investing more.
- The idea might change substantially based on input.
- You want to avoid writing a full RFC if the idea is not ready.

One-pagers are pre-RFC. Not binding. Designed to get a fast reaction.

## The write-it-down test

Before writing anything, answer all five:

1. **Will this be read more than once?** (If no, don't write.)
2. **Is there a specific reader in mind?** (If no, the doc has no audience.)
3. **Is the answer stable enough to justify writing?** (If no, write an FAQ or don't write.)
4. **Who owns it after you publish?** (If no one, don't publish yet.)
5. **When will it be reviewed next?** (Put a review date or don't publish.)

Five yes answers → write. Any no → revisit before writing.

## Worked examples

### Example 1 — A new eng joined and asked "how do we deploy?"

**Run the tree:**
- Asked again? Yes — every new hire asks.
- Changes often? No — deploy process is stable.
- Decision with long-term consequences? No — operational.
- Operational? Yes. **→ runbook**

**Action:** Write "Deploy runbook" with steps, expected results, rollback. Owner: platform eng.

### Example 2 — Team discussed moving from npm to pnpm

**Run the tree:**
- Asked again? Yes — future joiners will ask why pnpm.
- Changes often? No — package manager choice is stable.
- Decision with long-term consequences? Yes.
  - Architectural? No — it's a toolchain choice.
  - **→ decision doc** (not ADR)

**Action:** Write a decision doc. Alternative argument: if the org treats toolchain as architecturally relevant, write an ADR. Either is defensible; pick one convention and stick with it.

### Example 3 — Engineer wants feedback on caching approach

**Run the tree:**
- Not a question needing documentation; it's a proposal.
- Jump to proposal/RFC/one-pager branch.
- Rough idea, wants feedback → **one-pager** (NOT full RFC yet).
- If idea survives → **RFC** (from stakeholder-alignment).

**Action:** Write a one-pager. Post for quick reactions. If no strong objections, write the full RFC.

### Example 4 — A senior eng is leaving in 4 weeks

**Situation:** They built an internal tool three teams depend on.

**Multiple decisions:**

1. **Architectural decisions in the tool:**
   - ADRs for major design choices (language, framework, architecture pattern).
   - Three to five at most.

2. **Operational procedures:**
   - Runbooks for the three to five routine operations (deploy, backup verification, incident response, etc.).

3. **Reference info:**
   - API documentation, config reference, database schema (prefer auto-generated where possible).

4. **One-pager indexing the tool.**

**Action:** Before the engineer leaves, produce: 3-5 ADRs + 3-5 runbooks + reference docs (auto-generated if possible) + a top-level README. Assign owners for each. Schedule review dates.

**Gate:** name the owner before writing. Docs without owners decay within months.

### Example 5 — Customer asked a novel question via support

**Run the tree:**
- Asked again? Probably not — it's novel.
- Unless support thinks it will recur → then FAQ.

**Action:** Answer in support. If the same question appears twice more, elevate to FAQ.

### Example 6 — Quarterly all-hands

**Situation:** Want to announce and document the Q4 strategy.

**Run the tree:**
- Asked again? Yes — team will reference it all quarter.
- Changes often? Medium (updates through the quarter).
- Decision with long-term consequences? Partially.
  - → living doc (wiki page or Notion) with clear ownership and update cadence.

**Action:** Write the Q4 strategy as a living document, owned by CEO or head of product, reviewed monthly.

## Common mistakes by branch

### "Not asked again" → wrote it anyway

**Symptom:** docs with 3 lifetime views. Owner doesn't maintain them. They're wrong within a year.

**Fix:** if the question wasn't asked twice, don't document.

### "Changes often" → wrote an ADR

**Symptom:** ADR that says "we use npm; maybe pnpm later" and gets "updated" every few months.

**Fix:** ADRs are immutable. If the answer changes often, it's not an ADR. Use a living doc.

### "Decision with consequences" → wrote nothing

**Symptom:** three months later, team can't remember why they chose X. Debate restarts.

**Fix:** always document decisions with long-term consequences, even if it feels obvious at the time.

### "Operational" → wrote a prose doc without expected results

**Symptom:** "Follow these steps" with no validation per step. Runbook decays silently.

**Fix:** every step has an expected result. See `runbook-framework.md`.

### "Reference" → wrote a tutorial

**Symptom:** a lookup doc that reads as a narrative. Reader can't find what they need.

**Fix:** reference docs are tables, sorted lists, schemas. Not tutorials.

### "Rough idea" → wrote a full RFC

**Symptom:** 10-page RFC for an idea not yet baked. Rejection feels personal; author invested too much.

**Fix:** one-pager first. Full RFC only if the idea survives feedback.

## The review cadence table

| Doc type | Review cadence |
|---|---|
| FAQ / living doc | Monthly |
| Runbook (high volatility) | Every 3 months |
| Runbook (medium volatility) | Every 6 months |
| Runbook (low volatility) | Every 12 months |
| ADR | Never (immutable) — but index / supersede |
| Decision doc | Review if circumstances change |
| Reference doc | With every code change affecting it (ideally auto-generated) |
| One-pager | Every 3 months — is the idea still alive? |

Every doc should have a next-review date visible. Without one, rot is silent.
