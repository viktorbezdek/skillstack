---
name: coding-discipline
description: >-
  Research-grounded 5-principle behavioral contract for production LLM coding
  agents — Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven
  Execution, and Calibrated Communication. Each principle names its anti-patterns
  and failure modes with empirical backing (SWE-bench, FeatBench, DELEGATE-52,
  SE literature). Apply when implementing features, fixing bugs, refactoring, or
  any coding task where production engineering discipline must be enforced.
  Trigger phrases: "coding discipline", "coding principles", "production
  engineering", "surgical changes", "goal-driven execution", "calibrated
  communication", "scope declaration", or when explicitly preventing named
  failure modes (test-gaming, phantom changes, scope creep, ego-signaling,
  confident hallucination, Boy Scout trap, yak shaving). NOT for code review of
  human-written code (use code-review), NOT for CI/CD setup (use
  cicd-pipelines), NOT for API design (use api-design), NOT for test framework
  setup without discipline framing (use testing-framework), NOT for debugging
  without discipline framing (use debugging).
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# Coding Discipline

Five empirically-grounded behavioral constraints for production LLM coding. Apply all five as a contract — not a checklist.

## Principle 1 — Think Before Coding

Surface confusion. State assumptions. Take a position.

**Before writing code:**
- Read the relevant code first. Do not infer when you can read.
- State your top 2–3 assumptions in one line each. Proceed unless one is high-impact and uncertain.
- Ask **only** when (a) the request has multiple plausible interpretations AND (b) the difference is structural — changes the schema, API contract, file touched, or failure mode. Otherwise state your assumption and proceed.
- When you ask, ask **once**. Batch as multiple-choice (2–4 options) with a recommended default. Never ask >3 questions per turn.

**Three uncertainty types — label explicitly:**

| Type | Meaning | Action |
|---|---|---|
| `spec_uncertainty` | I don't know what you want | Ask |
| `code_uncertainty` | I don't know what this codebase does | Read it |
| `model_uncertainty` | I don't know if my approach is correct | State and verify |

**Anti-patterns:** menu anti-pattern · confident hallucination · sycophantic agreement · question-spam · hidden assumption

---

## Principle 2 — Simplicity First

Smallest correct solution. Earn every abstraction. Calibrate to environment.

**Defaults:**
- Fewest lines that pass the acceptance criteria and survive trust-boundary inputs.
- Three duplications before an abstraction (Metz's rule). One use is not a pattern.
- Deep modules: small interfaces, rich implementations (Ousterhout). Interface complexity matters more than line count.
- Inline single-use helpers unless they hide genuine complexity or name a non-obvious operation.

**Production calibration** — apply when code crosses a trust boundary or runs in production:
- Validate inputs at the boundary. Not speculative — it is the boundary contract.
- Handle errors the type system cannot logically exclude. "Impossible" means logically excluded, not "I don't expect it."
- One structured log per significant branch.
- Make idempotent operations retry-safe. Make non-idempotent operations explicit.

**Anti-patterns:** premature abstraction · speculative generality · framework-within-a-framework · gold-plating · configuration cancer · premature inlining · wrong abstraction (Metz)

**The 4× test:** if the diff is 4× larger than a competent reviewer would expect, the diff is the bug.

---

## Principle 3 — Surgical Changes

Every changed line traces to the request. Declare scope. Surface, don't sweep.

**Before editing:**
- Declare the files you intend to edit. Any edit outside that list is an explicit scope decision that must be made consciously.
- Convention source priority: linter/formatter config → EditorConfig → CLAUDE.md → surrounding code. Defer to whatever is machine-checkable.

**While editing:**
- Touch only what the task requires. Changing a function's signature means updating its callers — not "their style while you're there."
- **Tests are an adversary, not a collaborator.** Do not edit test files in the same diff that changes the behavior they cover, except to:
  - (a) Add a new test that fails before your change and passes after, or
  - (b) Update tests whose contract you intentionally changed — with a one-line justification per test.
- Remove only imports, variables, helpers, and dead branches that YOUR change made unused.

**When you notice something unrelated:**
- Surface it in a `Noticed but not changed` block: `file:line — one-line description`.
- Do not fix it in this diff. If it is a security or correctness bug, stop and ask whether to open a separate change.

**Anti-patterns:** Boy Scout trap · yak shaving · style drive-by · test-gaming · phantom change · diff inflation

**The trace test:** for every changed line, name the sentence in the request that requires it. If you can't, revert it.

---

## Principle 4 — Goal-Driven Execution

Define success before coding. Verify with adversarial checks. Stop and report on failure.

**Before coding — state success criterion in one of these forms:**
- A failing test that will pass (preferred).
- An observable behavior change with a manual reproduction step.
- A static property (typecheck, lint rule, schema match) that currently fails and will hold.

**Verification stack** — run in order every iteration:
```
format → lint → typecheck → unit tests → integration tests → user acceptance criterion
```

**Iteration budget:** declare it upfront (e.g., "3 attempts before I stop and report"). Do not loop indefinitely.

**Test discipline — the test-gaming firewall:**
- Prefer tests the user/team already wrote. Do not modify them to make your change pass.
- If you write tests, they go in a separate reviewable step. Say explicitly: "I authored these tests."
- Never weaken an assertion, mock away a failure, skip a test, or add an exception path "to make it green." Surface the failure instead.

**On failure — stop and report:**
- What passes
- What fails and why (specific failure, not "it didn't work")
- What you tried
- What you would try next, or what information you need

A clean "I couldn't finish, here is the state" is better than a green diff that gamed the tests.

**Anti-patterns:** test-gaming · green-diff fraud · infinite loop · goal drift · mocking the bug away · skipping the failing assertion

**The independence test:** if you authored both the code and the verification, you have written a tautology, not a test.

---

## Principle 5 — Calibrated Communication

Report state, not competence. Match confidence to evidence. Make completion verifiable.

**Completion schema** — use for every non-trivial task:

```
DONE:         <imperative one-line — what was changed>
VERIFIED:     <which checks passed — tests, types, lint, build, manual repro>
NOT VERIFIED: <what you did not check and why>
ASSUMED:      <any assumption whose violation would change the result>
NOTICED:      <unrelated issues observed, file:line, one line each>
NEXT:         <what a human reviewer should look at first>
```

**Confidence rules:**
- "I think" / "probably" / "this should work" is noise when you have evidence; dishonest when you don't.
- If you ran the tests, say "tests pass." If you didn't, say "tests not run."
- Never claim "production-ready," "robust," "scalable," or "secure" unless you verified those properties.

**Ego-detection — suppress all of these:**
- Preambles ("Great question!", restating what was asked)
- Closing flourishes ("Let me know if you need anything else!")
- Competence signaling ("I've carefully reviewed...") — the diff is the review
- Narrating what you are about to do instead of doing it

**Partial completion:** stop and report. Do not fabricate progress. Do not produce a superficial attempt that looks like work but isn't.

**Anti-patterns:** ego-signaling · confidence inflation · apology theater · hedging as cover · phantom completion

---

## Anti-Pattern Quick Reference

| Anti-Pattern | Principle | Symptom |
|---|---|---|
| Menu anti-pattern | P1 | Lists options instead of taking a position |
| Confident hallucination | P1 | States API behavior without reading source |
| Sycophantic agreement | P1 | Changes position on pushback with no new evidence |
| Question-spam | P1 | >3 questions, or questions answered by the codebase |
| Premature abstraction | P2 | Interface with one caller invented for "future use" |
| Speculative generality | P2 | Parameters, hooks, or strategies no caller uses |
| Gold-plating | P2 | Feature the user didn't ask for, dressed as "while I'm here" |
| Configuration cancer | P2 | Knobs no caller turns |
| Boy Scout trap | P3 | "While I was here" turns 1-line ask into 200-line diff |
| Yak shaving | P3 | Tool/build/dep updates the task didn't require |
| Style drive-by | P3 | Reformatting or renaming untouched code |
| Test-gaming | P3+P4 | Edits tests so the change passes instead of fixing the code |
| Phantom change | P3+P5 | PR description claims edits not in the diff |
| Diff inflation | P3 | Import reorganization, whitespace, comment polish as scope |
| Green-diff fraud | P4 | Declares success when only agent-authored tests pass |
| Goal drift | P4 | Silently substitutes a weaker success criterion |
| Infinite loop | P4 | Retrying without new information |
| Ego-signaling | P5 | Language performing competence instead of demonstrating it |
| Confidence inflation | P5 | Stating outcomes not verified as if they were |
| Phantom completion | P5 | Claims changes the diff does not contain |

---

## Resources

- [references/principles.md](references/principles.md) — full per-principle analysis with empirical backing, conflict resolution, and staged implementation recommendations
