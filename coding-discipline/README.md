# Coding Discipline

> **v1.0.0** | Engineering | Research-grounded behavioral contract for production LLM coding agents

Five empirically-grounded principles that give LLM coding agents named constraints, named anti-patterns, and a structured completion schema. Addresses the failure modes that benchmark studies have quantified: test-gaming, scope creep, phantom changes, confident hallucination, and overconfident completion claims.

## What Problem Does This Solve

LLM coding agents fail in predictable, named ways. Aleithan et al. (2024) found 31.08% of SWE-bench "passing" patches passed only because tests were weak. Wang, Pradel & Liu (2025) found 27.3% of behavioral divergences came from agents editing more than the ground truth required. Gong et al. (MSR 2026) found 45.4% of high-inconsistency agent PRs claimed changes that were never implemented.

This plugin encodes the structural mitigations: declare scope before editing, treat tests as adversaries not collaborators, define success before coding, report state not competence, and earn every abstraction.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "apply coding discipline to this implementation" | Full 5-principle behavioral contract for the task |
| "use surgical changes for this bug fix" | Scope declaration, trace test, test-gaming firewall |
| "the agent is doing Boy Scout trap edits" | P3 diagnosis and the declared-scope enforcement mechanism |
| "apply goal-driven execution" | Success criterion → verification stack → iteration budget → stop-and-report |
| "use the DONE/VERIFIED schema" | Principle 5 completion reporting with all six fields |
| "prevent ego-signaling in completions" | Ego-detection suppression list and calibrated confidence rules |
| "help prevent test-gaming" | Test-gaming firewall: adversarial test discipline and authorship disclosure |
| "apply production engineering principles" | Production calibration for trust-boundary code |

## When NOT to Use This Skill

- **For code review of human-written code** — use `code-review`
- **For CI/CD pipeline setup** — use `cicd-pipelines`
- **For API design** — use `api-design`
- **For test framework setup without discipline framing** — use `testing-framework`
- **For debugging without discipline framing** — use `debugging`

## Installation

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install coding-discipline@skillstack
```

## How to Use

**Direct invocation:**

```
Apply coding discipline to [task description]
```

**Principle-specific invocation:**

```
Use surgical changes to fix [bug]
Use goal-driven execution to implement [feature]
Apply production engineering discipline to [task]
```

**Anti-pattern prevention:**

```
Make sure there is no Boy Scout trap in this refactor
Prevent test-gaming — use the existing test suite as the adversarial check
Use the DONE/VERIFIED schema when reporting completion
```

## The Five Principles

| # | Principle | Core constraint | Key anti-patterns |
|---|---|---|---|
| 1 | Think Before Coding | Read before inferring; state uncertainty type; ask once, batched | Menu anti-pattern, confident hallucination, question-spam |
| 2 | Simplicity First | Earn every abstraction; calibrate to production vs. prototype | Premature abstraction, gold-plating, configuration cancer |
| 3 | Surgical Changes | Declare scope; treat tests as adversaries; surface don't sweep | Boy Scout trap, yak shaving, test-gaming, phantom change |
| 4 | Goal-Driven Execution | Define success first; iteration budget; stop and report | Green-diff fraud, goal drift, infinite loop |
| 5 | Calibrated Communication | DONE/VERIFIED schema; report state not competence | Ego-signaling, confidence inflation, phantom completion |

## Completion Schema

Every non-trivial task ends with:

```
DONE:         <imperative one-line — what was changed>
VERIFIED:     <which checks passed>
NOT VERIFIED: <what you did not check and why>
ASSUMED:      <assumptions whose violation would change the result>
NOTICED:      <unrelated issues, file:line, one line each>
NEXT:         <what a human reviewer should look at first>
```

## Running Evals

Offline structural validation (no API key needed):

```bash
uv run --with anthropic python plugin-dev/scripts/run_eval.py \
    --plugin-dir ./coding-discipline --skill coding-discipline --offline
```

Online activation and output evals:

```bash
uv run --with anthropic python plugin-dev/scripts/run_eval.py \
    --plugin-dir ./coding-discipline --skill coding-discipline --mode both
```

## What's Inside

- `skills/coding-discipline/SKILL.md` — operational 5-principle guide with anti-pattern table and completion schema
- `skills/coding-discipline/references/principles.md` — full per-principle analysis, empirical backing, cross-principle conflicts, and staged implementation recommendations
- `skills/coding-discipline/evals/trigger-evals.json` — 12 positive + 5 near-miss negative activation tests
- `skills/coding-discipline/evals/evals.json` — 4 output quality evals covering Boy Scout trap diagnosis, goal-driven execution, test-gaming firewall, and TDD interaction

## Empirical Backing

Key sources informing this plugin:

- Aleithan et al. 2024 (arXiv:2410.06992) — test-gaming quantification on SWE-bench
- Wang, Pradel & Liu 2025 (arXiv:2503.15223) — plausible-but-wrong patches and over-editing
- Gong, Pinna, Bian & Zhang, MSR 2026 (arXiv:2601.04886) — phantom changes in agent PRs
- Laban, Schnabel & Neville 2026, DELEGATE-52 (arXiv:2604.15597) — long-workflow corruption
- Spiess, Gros, Pai, Pradel et al., ICSE 2025 (arXiv:2402.02047) — confidence miscalibration
- Mockus & Weiss 2000; SmartBear/Cisco 2006; Google eng-practices — change size and diffusion
- Ousterhout, *A Philosophy of Software Design* (2018/2021); Metz on duplication vs abstraction

## Version History

- `1.0.0` Initial release

---

Part of the [SkillStack](https://github.com/viktorbezdek/skillstack) plugin collection.
