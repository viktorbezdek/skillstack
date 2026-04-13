# Outcome Orientation

> **v1.0.10** | Strategic Thinking | 11 iterations

Focus on measurable outcomes using OKRs, results-driven thinking, and outcome vs output distinction.

## What Problem Does This Solve

Teams routinely confuse delivering outputs -- features shipped, meetings held, documents written -- with achieving outcomes that actually matter to users and the business. Roadmaps fill with activity that looks productive but moves no meaningful metrics. A team ships ten features in a quarter but user retention stays flat because nobody asked "so what?" about any of them. OKRs get written as glorified task lists ("Launch feature X") instead of measurable change ("Reduce time-to-value by 30%"). This skill provides the frameworks (OKRs, results chains, leading/lagging metrics) and the "so what?" discipline needed to define goals in terms of measurable change rather than completed tasks.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Help me write OKRs for my team" | OKR structure template with Objective and Key Results table (baseline/target/current), plus good vs bad OKR examples showing the difference between task-based and outcome-based goals |
| "How do I know if my goal is an output or an outcome?" | Outputs vs outcomes comparison table and the "so what?" chain to trace activities to real value |
| "What metrics should I track to measure product success?" | Outcome metrics table with lagging results (revenue, NPS, defect rate) paired with leading predictors (pipeline, activation rate, test coverage) |
| "My roadmap is full of features but leadership wants to see business impact" | Results chain model mapping Activities to Outputs to Outcomes to Impact |
| "We completed everything we planned but the metric didn't move" | Outputs vs outcomes framing to diagnose whether the work was tied to the right leading indicators |

## When NOT to Use This Skill

- Prioritizing features or ranking backlog items -- use [prioritization](../prioritization/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install outcome-orientation@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the outcome-orientation skill to write OKRs for our Q3 product goals
```

```
Use the outcome-orientation skill to convert our feature roadmap into outcome-based goals
```

```
Use the outcome-orientation skill to identify leading metrics for our adoption targets
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`okrs` · `outcomes` · `metrics`

## What's Inside

### Skill: outcome-orientation

Single-skill plugin with no reference files -- all content is in the main SKILL.md.

| Component | Description |
|---|---|
| **SKILL.md** | Complete outcome orientation guide covering outcomes vs outputs distinction, OKR framework with template, outcome metrics with leading/lagging pairs, results chain model, and outcome definition checklist |
| **evals/** | Trigger evaluation and output quality evaluation test suites |

### Key content areas

- **Outcomes vs Outputs** -- Side-by-side table contrasting output activities (features shipped, docs written, meetings held, code deployed) with the outcomes they should drive (user problems solved, users successful, decisions made, revenue generated), plus the "so what?" question chain
- **OKR Framework** -- OKR structural definition (Objective = qualitative goal, Key Results = quantitative measures) with a fill-in template including Objective, Key Results table (baseline/target/current columns), and Initiatives section
- **Good vs Bad OKRs** -- Concrete comparison: "Launch feature X" (bad, task-based) vs "Reduce time-to-value by 30%" (good, outcome-based); "Write 10 docs" vs "90% of users complete onboarding"; "Conduct 5 interviews" vs "Identify top 3 user pain points"
- **Outcome Metrics** -- Four metric categories (revenue, adoption, quality, satisfaction) each with a lagging result metric paired with its leading predictor (e.g., monthly revenue paired with pipeline created, defect rate paired with test coverage)
- **Results Chain** -- Four-stage model: Activities (do) produce Outputs (produce) which achieve Outcomes (achieve) which create Impact (change)
- **Outcome Definition Checklist** -- Five criteria for validating that a goal qualifies as a genuine outcome: describes end state (not activity), measurable and time-bound, within influence, valuable to user/business, achievable but stretching

## Usage Scenarios

1. **Writing quarterly OKRs for a product team.** Use the OKR template to structure each objective with three measurable key results. Apply the good vs bad OKR comparison to catch task-based key results ("Ship search feature") and reframe them as outcomes ("Reduce average time-to-find from 45s to 15s"). Use the outcome definition checklist to validate each key result.

2. **Converting a feature roadmap into outcome-based goals for leadership.** Walk each planned feature through the "so what?" chain until you reach user or business value. Map the result onto the results chain (Activity > Output > Outcome > Impact) and present the Outcome and Impact layers to leadership instead of the Activity layer.

3. **Identifying metrics to track product health.** Use the outcome metrics table to select lagging indicators (revenue, active users, defect rate, NPS) and pair each with its leading predictor (pipeline, activation rate, test coverage, support tickets). Leading metrics are what you can act on; lagging metrics tell you whether the actions worked.

4. **Diagnosing why completed work didn't move the target metric.** Apply the outputs vs outcomes framing: the team completed activities and produced outputs, but were those outputs connected to the right leading indicators? If test coverage went up but defect rate didn't change, the tests might not be covering the code paths that produce defects.

## Version History

- `1.0.10` fix(strategy+ux): optimize descriptions for outcome, prioritization, risk, systems, journey, ux-writing (9661735)
- `1.0.9` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.0.8` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.7` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.6` docs: update README and install commands to marketplace format (af9e39c)
- `1.0.5` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.0.4` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.0.3` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.0.2` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)
- `1.0.1` docs: improve strategic skill descriptions (f59b24a)

## Related Skills

- **[Prioritization](../prioritization/)** -- RICE, MoSCoW, ICE scoring to rank the initiatives that drive outcomes
- **[Risk Management](../risk-management/)** -- Risk assessment for the initiatives supporting outcome goals
- **[Systems Thinking](../systems-thinking/)** -- Feedback loop analysis to understand why outcomes do or don't respond to outputs
- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate breakthrough approaches when conventional outputs fail to move outcomes
- **[Critical Intuition](../critical-intuition/)** -- Pattern detection and bias exposure for evaluating whether goals are genuine outcomes

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
