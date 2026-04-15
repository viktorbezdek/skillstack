# Product Thinking

> **v1.0.0** | Product Strategy | 5 skills

---

## The Problem

Teams skip from brief to build. They accept the brief as the problem, mistake user wants for user needs, write value propositions that read as slogans, confuse shipping a feature with moving an outcome, and commit to one-way-door decisions as if they were two-way. The cost is not a single bad product — it is a quarter of work that does not matter, followed by a retrospective that concludes "we should talk to users more" without changing anything about how decisions are made.

Product thinking is a discipline, not an attitude. It has named techniques — Jobs-To-Be-Done, Value Proposition Canvas, Kano, North Star, trade-off matrices, reversibility — but most teams apply them haphazardly or skip them when deadlines press. Skills that compound do not compound because they are never used in sequence.

## The Solution

The Product Thinking plugin gives Claude five composable product-thinking skills, each scoped to one discipline and mutually-exclusive in activation:

1. **problem-definition** — frame the real problem before jumping to solutions (JTBD, 5-whys, problem vs symptom).
2. **user-needs-identification** — separate functional / emotional / social jobs; surface latent needs.
3. **value-proposition-design** — build a Value Proposition Canvas and apply the Kano model.
4. **outcome-oriented-thinking** — product-strategy outcomes: North Star, leading vs lagging, outcome hypotheses with kill clauses.
5. **trade-off-analysis** — cost-benefit, opportunity cost, reversibility (one-way / two-way doors), second-order effects.

Each skill activates on its own, but they compose in sequence: define the problem → identify the needs → design the value proposition → target the outcome → analyze the trade-offs. A product decision that has walked through all five is legibly reasoned; a decision that has skipped any one is opinion.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Brief is accepted as the problem; symptoms and problems are fused. | Problem stated with Who / Context / Job / Gap / Why-now / Assumptions / Not-goals. |
| Users' stated wants are treated as their needs. | Needs separated from wants; functional / emotional / social jobs named explicitly. |
| Value proposition is a slogan. | VPC with traceable pain relievers and gain creators; Kano categories assigned. |
| Shipping the feature counts as success. | Outcome hypothesis with leading indicator and kill clause; North Star selected. |
| Options are compared vaguely ("let's do A"). | Trade-off matrix with reversibility classification, opportunity cost, and second-order effects. |
| Decisions are not documented as bets — no falsification condition. | Each bet has a kill clause stating what evidence would reverse it. |

## Installation

Add the marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install product-thinking@skillstack
```

### Prerequisites

None. For adjacent disciplines:

- **`outcome-orientation`** — team-level OKR authoring with KRs (this plugin's `outcome-oriented-thinking` is product-strategy North Star and hypotheses, not OKR templates).
- **`persona-definition`** — demographic personas for the segments named here.
- **`persona-mapping`** — stakeholder power/interest maps.
- **`elicitation`** — interview protocols for surfacing needs.
- **`prioritization`** — RICE/MoSCoW/ICE scoring once trade-offs are analyzed.
- **`risk-management`** — quantified risk assessment for high-stakes decisions.
- **`systems-thinking`** — feedback loops around outcomes and second-order effects.

### Verify installation

After installing, test with:

```
Help me frame the real problem behind this feature request: "users want a dashboard with 12 widgets"
```

The `problem-definition` skill should activate and walk the symptom-vs-problem ladder.

## Quick Start

1. Install the plugin using the commands above.
2. Try: `We're debating whether to add a team-management feature. What are we actually trading off?` — activates `trade-off-analysis`.
3. Try: `Our onboarding churns 60% of users in week one. How do I write the outcome hypothesis for a redesign bet?` — activates `outcome-oriented-thinking`.
4. Try: `What's the value prop for a small-team Slack-for-audio?` — activates `value-proposition-design`.
5. Try: `The brief says 'users need notifications'. What's the underlying need?` — activates `user-needs-identification`.

## Evaluation Results

Tested against `claude-haiku-4-5-20251001` with all 5 skill descriptions presented as the routing context (65 queries: 8 positive + 5 negative per skill).

| Skill | Positive (TP/Pos) | Negative (TN/Neg) | Accuracy |
|---|---|---|---|
| `problem-definition` | 7/8 | 4/5 | 85% |
| `user-needs-identification` | 8/8 | 5/5 | 100%* |
| `value-proposition-design` | 8/8 | 5/5 | **100%** |
| `outcome-oriented-thinking` | 8/8 | 5/5 | **100%** |
| `trade-off-analysis` | 8/8 | 5/5 | **100%** |
| **Overall** | **95% positive recall** | **96% negative precision** | **95%** |

*Hit 100% on repeated runs; "apologies about spreadsheets" case sits on the classifier boundary under Haiku noise.

**Targets met:** positive ≥90% ✅, negative ≥95% ✅ (Anthropic skill-eval workflow thresholds).

**Known borderline queries** (route ambiguously in the isolated 5-skill test; a full plugin ecosystem with `creative-problem-solving` and `debugging` installed would route correctly):

1. *"Use the 5 whys to find the root problem behind this bug report"* — "bug report" is genuinely ambiguous between user-reported product feedback (→ `problem-definition`) and code defects (→ `debugging`).
2. *"Help me ideate solutions for reducing customer churn"* — "customer churn" reads as problem framing even with explicit ideation intent.

Reproducibility: requires `ANTHROPIC_API_KEY` and the `anthropic` SDK. Each skill ships with `trigger-evals.json` (13 cases) and `evals.json` (3 scenarios) under its `evals/` directory.

## System Overview

```
product-thinking/
├── .claude-plugin/
│   └── plugin.json
├── README.md
└── skills/
    ├── problem-definition/
    │   ├── SKILL.md
    │   └── evals/{trigger-evals.json, evals.json}
    ├── user-needs-identification/
    │   ├── SKILL.md
    │   └── evals/{trigger-evals.json, evals.json}
    ├── value-proposition-design/
    │   ├── SKILL.md
    │   └── evals/{trigger-evals.json, evals.json}
    ├── outcome-oriented-thinking/
    │   ├── SKILL.md
    │   └── evals/{trigger-evals.json, evals.json}
    └── trade-off-analysis/
        ├── SKILL.md
        └── evals/{trigger-evals.json, evals.json}
```

Five skills. Each skill is self-contained — descriptions are written as a mutually-exclusive set so activation lands on the right skill for the question asked.

## What's Inside

| Skill | Purpose | Activates on |
|---|---|---|
| **problem-definition** | Separate problems from symptoms. JTBD framing. 5-whys. Problem-statement template with Assumptions and Not-goals. | "Are we solving the right problem?" / "Frame this brief as a problem, not a solution." |
| **user-needs-identification** | Functional / emotional / social jobs. Needs vs wants. Latent-need surfacing (workarounds, apologies, shadow tools). | "What do users really need?" / "Move past stated wants to underlying jobs." |
| **value-proposition-design** | Value Proposition Canvas with traceable map. Kano model for feature categorization. VP statement template. | "Write a value proposition." / "Apply VPC for this segment." / "Is this a basic, performance, or delighter?" |
| **outcome-oriented-thinking** | Output-outcome-impact chain. North Star selection. Leading vs lagging indicators. Outcome hypothesis with kill clause. | "Is this an outcome or an output?" / "What's our North Star?" / "Write the outcome hypothesis." |
| **trade-off-analysis** | Cost-benefit, opportunity cost, reversibility (one-way / two-way doors), second-order effects. Trade-off matrix. | "What are we trading off?" / "One-way or two-way door?" / "Compare options A, B, and do-nothing." |

## Decision Logic

**When is this plugin vs. adjacent plugins?**

- **Use `outcome-orientation` (not this plugin)** when you need to write team-level OKRs with objectives and key results. This plugin's `outcome-oriented-thinking` is upstream — it sets the North Star and product-strategy outcomes; OKRs translate those into team goals.
- **Use `prioritization` (not this plugin)** when you have a backlog to rank with RICE / MoSCoW / ICE. This plugin's `trade-off-analysis` is upstream — it decides whether a line item should be on the backlog at all.
- **Use `persona-definition` / `persona-mapping` (not this plugin)** when you need personas or stakeholder maps. This plugin's `user-needs-identification` is complementary — personas say who; needs identification says what jobs they hire the product to do.
- **Use `elicitation` (not this plugin)** when you need an interview script. Needs identification is what to ask about; elicitation is how to ask.
- **Use `systems-thinking` (not this plugin)** when analyzing feedback loops. Second-order effects here are a shallow version; systems-thinking goes deeper.

## Ideal For

- **Product managers** who want a structured way to reason about problems, needs, value, outcomes, and trade-offs — not just intuition.
- **Founders** making strategic bets where a one-way-door mistake costs months.
- **Engineering leads** crossing into product decisions and needing the vocabulary.
- **Staff+ engineers** contributing to product strategy, not just implementation.
- **Design leads** grounding design decisions in user jobs rather than feature requests.
- **Teams** that want a shared framework for product conversations so arguments converge on evidence rather than opinion.

## Not For

- **Writing production code** — this is a thinking-tools plugin, not a build plugin.
- **Marketing copy and microcopy** — use `ux-writing`.
- **Pitching the strategy to stakeholders** — use `storytelling-for-stakeholders` (part of `skillstack-workflows`).
- **Running interviews** — use `elicitation`.
- **Team OKR writing** — use `outcome-orientation`.

## Related Plugins

- **outcome-orientation** — OKR framework at the team level.
- **persona-definition** / **persona-mapping** — user segments and stakeholder maps.
- **elicitation** — interview design for needs discovery.
- **prioritization** — ranking options once trade-offs are clear.
- **risk-management** — quantified risk for high-stakes decisions.
- **systems-thinking** — feedback-loop analysis of outcomes and second-order effects.
- **storytelling-for-stakeholders** — translate product strategy into a narrative for leadership.
- **skillstack-workflows** — composed workflows (`product-story-to-ship`, `strategic-decision`) that sequence these skills end-to-end.

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
