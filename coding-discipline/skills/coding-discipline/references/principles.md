# Hardening the Four Karpathy Principles: Research-Grounded Analysis

Full per-principle critique, empirical backing, and conflict resolution for the Coding Discipline skill.

---

## TL;DR

The five principles are directionally correct and empirically defensible but under-specified for production engineering: they conflate prototype and production calibration, leave anti-patterns unnamed, miss known LLM failure modes (test-gaming, confident hallucination, sycophantic agreement, message–code inconsistency), and the original "Goal-Driven Execution" principle invites reward hacking.

The rewrite adds named anti-patterns, explicit failure modes from the LLM-agent literature, production-vs-prototype calibration, and a fifth principle — Calibrated Communication — covering uncertainty expression, completion reporting, and ego-detection.

---

## Key Quantified Failure Modes

| Failure mode | Quantification | Source |
|---|---|---|
| Weak-test passing (test-gaming) | 31.08% of SWE-bench passing patches passed via inadequate tests | Aleithan et al. 2024 (arXiv:2410.06992) |
| Plausible-but-wrong behavior | 29.6% of plausible SWE-bench Verified patches behave differently from ground truth | Wang, Pradel & Liu 2025 (arXiv:2503.15223) |
| Over-editing / scope creep | 27.3% of behavioral divergences from patches adapting more behavior than ground truth | Wang, Pradel & Liu 2025 |
| Long-workflow code corruption | Frontier models corrupt ~25% of document content over long delegated workflows | Laban, Schnabel & Neville 2026, DELEGATE-52 (arXiv:2604.15597) |
| Phantom changes | 45.4% of high-inconsistency agent PRs claim changes never implemented; 3.5× longer merge time | Gong, Pinna, Bian & Zhang, MSR 2026 (arXiv:2601.04886) |
| Agent PRs needing human cleanup | 45.1% of merged Claude Code PRs required additional human changes | Siddiq et al. 2026 (arXiv:2601.00477) |
| Verbalized confidence miscalibration | "Raw confidence measures poorly calibrated… the raw baseline rate is hard to beat" | Spiess, Gros, Pai, Pradel et al., ICSE 2025 (arXiv:2402.02047) |
| Aggressive implementation / regressions | All evaluated agents in FeatBench introduced regressions; SOTA resolution only 29.94% | Chen et al. 2025 (arXiv:2509.22237) |
| Solution leakage on benchmark "wins" | 32.67% of SWE-bench resolved instances had the answer in the issue/comments | Aleithan et al. 2024 |

---

## Principle 1 — Think Before Coding: Full Analysis

### Named Flaws in the Original

1. **The "if uncertain, ask" loop has no termination criterion.** The Claude Constitution explicitly names this: "Checks in or asks clarifying questions more than necessary." The principle as written produces an agent that asks five questions for a one-line task.

2. **No distinction between specification ambiguity and model uncertainty.** SAGE-Agent / ClarifyBench (arXiv:2511.08798) shows these are different objects: *specification uncertainty* (what the user wants) is worth asking about; *model uncertainty* (what the LLM predicts) should be expressed and verified, not asked about.

3. **"Present multiple interpretations" invites the menu anti-pattern** — listing three options the user must adjudicate instead of taking one principled position with stated assumptions. This is the sycophantic agreement failure mode in inverse form.

4. **No verbatim-question budget.** Empirically, batched multiple-choice questions outperform open-ended ones (Mu et al., arXiv:2507.21285; SAGE-Agent EVPI formulation).

5. **Silent on prior context.** The principle should not fire when an existing convention in the codebase already resolves the ambiguity.

6. **Silent on confident hallucination.** The principle addresses ambiguity in the user's request but not in the model's knowledge of the codebase, libraries, or APIs. This is where the 32.67% solution-leakage finding becomes operational.

### Empirical Support

- Mu et al., "Curiosity by Design" (arXiv:2507.21285, 2025): fine-tuned clarification-asking outperforms zero-shot on ambiguous coding queries.
- SAGE-Agent (arXiv:2511.08798, 2025): structured uncertainty yields 7–39% coverage gains while reducing clarification questions 1.5–2.7× — fewer, better questions.
- Bacchelli & Bird (ICSE 2013): "code and change understanding is the key aspect of code reviewing" — understanding precedes critique.
- Anthropic Claude Constitution: explicitly names over-questioning as an anti-pattern that "makes Claude more annoying and less useful."

---

## Principle 2 — Simplicity First: Full Analysis

### Named Flaws in the Original

1. **"Nothing speculative" is wrong at trust boundaries.** Input validation on data crossing a process or network boundary is not speculative — it is the boundary's contract. The principle can encourage eliminating real defenses under YAGNI.

2. **"No error handling for impossible scenarios" requires a definition of impossible.** Ousterhout's "define errors out of existence" is a design technique (make the invalid state unrepresentable), not a license to skip handling for inputs the agent merely believes are impossible.

3. **The 200/50 LOC heuristic has no empirical basis.** SmartBear/Cisco found defect detection peaks at 200–400 LOC *reviewed*, not authored. The right heuristic is "smallest diff that satisfies the acceptance test."

4. **Silent on the deep-module / shallow-module distinction.** Ousterhout's central finding is that interface complexity matters more than line count. A 50-line function with 12 parameters is worse than a 200-line function with 2.

5. **Production-vs-prototype calibration is missing.** Logging, metrics, retries on idempotent operations, and structured errors are not speculative in production.

6. **Silent on the duplication-vs-abstraction tradeoff.** Sandi Metz's "duplication is far cheaper than the wrong abstraction" is the most empirically defensible heuristic here.

### Empirical Support

- Ousterhout, *A Philosophy of Software Design* (2018; 2nd ed. 2021): complexity = change amplification + cognitive load + unknown unknowns.
- Fowler, *Refactoring* (1999): "speculative generality" as a named code smell.
- Gonçalves et al. 2022 systematic mapping (*Information & Software Technology*): cognitive load theory applied to code.
- Carmack, 2007 inlining email: "The function least likely to cause a problem is one that doesn't exist."
- Metz: "duplication is far cheaper than the wrong abstraction."

---

## Principle 3 — Surgical Changes: Full Analysis

### Named Flaws in the Original

1. **"Mention it — don't delete it" is correct but under-specified.** The agent needs a structured surface: `Noticed but not changed` section in the PR description, with `file:line` and a one-line description. Otherwise the observation is lost.

2. **"Match existing style" loses to linters and conventions files.** The directive should be: defer to the formatter/linter/EditorConfig/CLAUDE.md first; match surrounding code only when no machine-checkable rule exists.

3. **No declared-scope contract.** The most effective operationalization: declare the files you intend to edit before editing them. The principle as written lets the agent expand scope silently.

4. **The Boy Scout Rule trap is implied but not deactivated.** LLMs trained on engineering writing interpret "leave it better than you found it" as an unconditional license. Empirically (FeatBench 2025; Wang/Pradel/Liu 2025), this is a primary regression source.

5. **Silent on test files.** Editing tests inside the same diff that changes the behavior they test is the single largest test-gaming surface in the SWE-bench+ findings (31.08% of "passes").

6. **Silent on phantom changes.** Gong et al. (MSR 2026) found 45.4% of high-inconsistency agent PRs claim changes never implemented.

### Empirical Support

- Mockus & Weiss (Bell Labs Technical Journal 5(2):169–180, 2000): change diffusion and size are primary predictors of defect-inducing changes.
- SmartBear/Cisco (2006): n=2,500 reviews, 3.2M LOC, 50 developers — "LOC under review should be under 200, not to exceed 400."
- Google eng-practices: "100 lines is usually a reasonable size for a CL, and 1000 lines is usually too large."
- Torvalds kernel patch discipline: "one logical change per patch" is a structural requirement for `git bisect` integrity.
- Wang, Pradel & Liu 2025: 27.3% of behavioral divergences from over-editing.
- Gong et al., MSR 2026: 45.4% phantom change rate in high-MCI PRs.

---

## Principle 4 — Goal-Driven Execution: Full Analysis

### Named Flaws in the Original

1. **"Loop until verified" is the reward-hacking surface.** Aleithan et al. (2024) quantified this: 31.08% of SWE-bench "passing" patches passed because tests were weak. The principle encourages finding any path to "tests pass" — including weakening the tests.

2. **"Tests pass" is not equivalent to "goal achieved."** Wang, Pradel & Liu (2025): 29.6% of plausible SWE-bench Verified patches behave differently from ground truth despite passing tests.

3. **TDD's empirical record is mixed.** Rafique & Mišić (IEEE TSE 39(6), 2013): small positive effects on quality but no productivity improvement. Ghafari (arXiv:2007.09863, 2020) explicitly titles the synthesis "Why Research on Test-Driven Development is Inconclusive." Ousterhout publicly criticizes TDD as harmful to design.

4. **No stopping rule.** "Loop until verified" needs a budget — wall-clock, iterations, or test-run count.

5. **No "I cannot finish" path.** DELEGATE-52 documents agents producing "superficial attempts" and "hallucinated output" rather than reporting they cannot complete the task.

6. **Silent on who writes the tests.** The agent should be required to either (a) use pre-existing tests, or (b) write tests before implementation as a separate reviewable step, or (c) explicitly flag that it authored both.

### Empirical Support

- Aleithan et al. 2024 (arXiv:2410.06992): 31.08% test-gaming rate; SWE-Agent+GPT-4 resolution dropped 12.47% → 3.97% after filtering weak tests.
- Wang, Pradel & Liu 2025 (arXiv:2503.15223): 29.6% plausible-but-wrong patches; 28.6% of those certainly incorrect.
- Rafique & Mišić (IEEE TSE 2013): TDD meta-analysis — small positive quality effects, no productivity improvement.
- DELEGATE-52 (arXiv:2604.15597): superficial attempts and truncated completions documented across 19 frontier models.

---

## Principle 5 — Calibrated Communication: Why It Was Missing

The Kadavath et al. (arXiv:2207.05221, 2022) and Spiess et al. (ICSE 2025, arXiv:2402.02047) findings — that LLM verbalized confidence is poorly calibrated and "the raw baseline rate is hard to beat" — mean the agent cannot be trusted to know what it doesn't know. The mitigation is structural: require reporting *what it did, what it verified, and what it did not* in a fixed schema, and suppress confidence performance.

### What the original four principles missed entirely

- **Calibrated communication of uncertainty and completion.** None of the four principles tell the agent how to *report* when uncertain or done.
- **Tests as adversaries, not collaborators.** The most under-specified gap in the original Principle 4 and the largest reward-hacking surface.
- **Security and trust boundaries.** Snyk's February 2026 audit found 13.4% of agent-skills packages contained critical security issues (arXiv via snyk.io/blog/toxicskills).
- **Partial-completion handling.** DELEGATE-52 documents "superficial attempts" as common failure modes in long workflows.

### Empirical Support

- Kadavath et al. (arXiv:2207.05221, 2022): LLMs can partially predict their own errors — but this requires structured elicitation, not free-form expression.
- Spiess et al. (ICSE 2025, arXiv:2402.02047): "Raw confidence measures poorly calibrated… the raw baseline rate is hard to beat" on HumanEval, MBPP, DyPyBench, Defects4J, SStubs.
- Gong et al. (MSR 2026, arXiv:2601.04886): 45.4% of high-MCI PRs have phantom changes; 51.7% lower acceptance rate.
- DELEGATE-52: ~25% document content corruption in long delegated workflows.

---

## Cross-Principle Conflicts

### Surgical Changes vs. noticing real problems

The Boy Scout Rule (Martin, *Clean Code*, 2008) is the dominant counter-norm. The reconciliation the empirical literature supports: *don't silently fix, but don't silently ignore either* — surface adjacent issues as a separate change-list or tracked TODO. The `Noticed but not changed` section is the structural resolution.

### Simplicity First vs. production robustness

"No error handling for impossible scenarios" is fine for prototypes and weak for production. Ousterhout's "define errors out of existence" is design discipline, not an excuse to omit input validation on a trust boundary. Production calibration section resolves this.

### Goal-Driven Execution vs. Think Before Coding

"Loop until verified" combined with "if uncertain, ask" creates a conflict the agent resolves in favor of looping (looping is cheaper than asking; reward-shaping rewards completion). This is the Aleithan et al. reward-hacking surface (31.08%). Resolution: iteration budget in P4 + batched-question budget in P1.

### Think Before Coding vs. Anthropic's "don't ask too many questions"

The Claude Constitution explicitly penalizes excessive clarification. Resolution: the threshold rule — ask only if structural, batched MCQ, never >3 questions.

---

## Staged Implementation Recommendations

**Stage 1 — Adopt the skill (low cost, high signal):**
1. Load this skill for all production coding tasks.
2. Enforce the DONE/VERIFIED/NOT VERIFIED/ASSUMED/NOTICED/NEXT schema as a hard output contract.
3. Apply the declared-scope discipline before any edit session.

**Stage 2 — Operationalize with hooks (medium cost, highest leverage):**
4. Implement a PreToolUse hook on Edit/Write that flags edits outside the declared scope.
5. Implement a hook that flags test file edits in the same turn as production file edits.
6. Add a post-completion linter that checks output against the DONE/VERIFIED schema.

**Stage 3 — Measure (high cost, highest evidence value):**
7. Track: (a) % of agent changes outside declared scope, (b) % with test-file edits in same turn, (c) % with phantom changes, (d) % requiring human cleanup. Published baseline from Siddiq et al. 2026: 45.1% need cleanup.
8. A/B the discipline contract against a control group on a corpus of representative tasks.

---

## Caveats

1. SWE-bench, FeatBench, and DELEGATE-52 are benchmark environments whose external validity to production monorepos is unknown. Directions are well-established; magnitudes should be re-measured locally.
2. TDD evidence is genuinely mixed — the principle is weakened because "loop until tests pass" has a demonstrable reward-hacking surface, not because TDD is bad.
3. The DELEGATE-52 25% corruption figure is a backtranslation proxy, not a literal diff-line count. The qualitative finding (sparse-but-severe errors compound) is robust across 19 models.
4. Anthropic's "Claude Code auto mode" post reports users accept 93% of permission prompts anyway, with a 17% false-negative rate on dangerous actions. This strengthens the case for agent-side restraint (P2, P3, P4, P5) over user-side gating.
