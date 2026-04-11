# Risk Management

> **v1.0.10** | Strategic Thinking | 11 iterations

Apply risk assessment frameworks, mitigation strategies, risk registers, and monitoring practices.

## What Problem Does This Solve

Projects fail predictably — third-party dependencies slip, key people leave, integrations break at the worst moment — yet most teams only react after the damage is done. Ad-hoc risk discussions produce vague worries without scores, owners, or response plans. This skill provides a structured register-based approach that turns gut-level concerns into tracked, scored risks with assigned owners and concrete mitigation strategies.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "What could go wrong with this project?" | Pre-mortem technique: imagine the project already failed, reverse-engineer what went wrong, convert answers to tracked risks |
| "Help me build a risk register for this initiative" | Risk register template with ID, category, likelihood/impact scoring, mitigation actions, owner, and status columns |
| "How serious is this risk — should we worry about it?" | Risk assessment matrix scoring Likelihood (1-3) x Impact (1-3) to classify risks as Low, Medium, High, or Critical |
| "What type of risk is this and how should we handle it?" | Five risk categories (Technical, Schedule, Resource, External, Organizational) and four response strategies (Avoid, Transfer, Mitigate, Accept) |
| "Write a response plan for this specific risk" | Risk response template capturing description, trigger warning signs, probability, impact, actions, owner, and review date |
| "How often should we review our risks?" | Monitoring cadence table with Daily (trigger checks), Weekly (active review), Monthly (score reassessment), and Quarterly (full register review) |

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install risk-management@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the risk-management skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `risk`
- `mitigation`
- `assessment`

## What's Inside

- **Risk Assessment Matrix** -- 3x3 Likelihood x Impact grid that maps combinations to Low, Medium, High, or Critical severity levels.
- **Risk Categories** -- Five risk types with examples: Technical (architecture, integration, performance), Schedule (dependencies, estimation), Resource (skills, turnover), External (vendors, regulations), and Organizational (priorities, funding, politics).
- **Risk Register Template** -- Markdown table template with columns for ID, description, category, likelihood, impact, calculated score, mitigation action, owner, and status.
- **Mitigation Strategies** -- Four response strategies (Avoid, Transfer, Mitigate, Accept) with guidance on when to apply each.
- **Risk Response Template** -- Structured plan for a single risk covering description, trigger warning signs, probability, impact consequence, response actions, owner, and review date.
- **Monitoring Practices** -- Recommended monitoring cadence from daily trigger checks through quarterly full-register reviews.
- **Pre-Mortem Technique** -- Three-question future-failure exercise that surfaces risks before a project starts by imagining it has already failed.

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

- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate breakthrough solutions through lateral thinking, first principles reasoning, game theory, and strategic reframi...
- **[Critical Intuition](../critical-intuition/)** -- Detect hidden patterns, expose blind spots, and deliver rigorous critical analysis with intuition-level depth.
- **[Outcome Orientation](../outcome-orientation/)** -- Focus on measurable outcomes using OKRs, results-driven thinking, and outcome vs output distinction.
- **[Prioritization](../prioritization/)** -- Apply prioritization frameworks including RICE, MoSCoW, ICE scoring, and effort-impact matrices for decision-making.
- **[Systems Thinking](../systems-thinking/)** -- Apply systems thinking principles including feedback loops, leverage points, and system dynamics to analyze complex prob...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
