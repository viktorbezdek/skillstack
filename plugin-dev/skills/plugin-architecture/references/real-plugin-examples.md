# Real Plugin Examples

> Architectural breakdowns of real Claude Code plugins. Each entry answers: **what components does it use, why, and what would a different decomposition look like?** Source: this repo (`skillstack`), Anthropic's bundled plugins, and the community plugins referenced in the research phase of plugin-dev's PRD.

Each example shows the decomposition the author chose — not necessarily the only correct one.

---

## 1. Anthropic `skill-creator` (single skill)

**Components**: 1 skill + scripts + evals. No hooks, no MCP, no subagents, no commands.

**Layout**:
```
skill-creator/
├── .claude-plugin/plugin.json
├── README.md
└── skills/skill-creator/
    ├── SKILL.md
    ├── references/ (progressive disclosure)
    ├── scripts/run_loop.py
    └── evals/ (trigger-evals.json + evals.json)
```

**Why this decomposition**: The capability is "teach the model how to author a new skill with proper progressive disclosure". That is pure methodology — model-judgment triggered, no events, no external systems. Skill is the obvious choice. Scripts handle the repeatable eval loop; no need for an MCP server because the loop runs locally.

**Alternative**: could have shipped as a slash command (`/create-skill`). Chose skill because the user doesn't need to remember to invoke it — any query about authoring a skill activates it.

---

## 2. `plugin-dev` (this plugin — multi-skill)

**Components**: 7 skills + shared scripts. No hooks, no MCP, no subagents, no commands.

**Layout**:
```
plugin-dev/
├── .claude-plugin/plugin.json
├── README.md
├── scripts/  (shared across skills: validate_plugin.py, scaffold_plugin.py, run_eval.py, test_hook.sh)
└── skills/
    ├── plugin-ideation/
    ├── plugin-research/
    ├── plugin-architecture/
    ├── plugin-hooks/
    ├── plugin-composition/
    ├── plugin-validation/
    └── plugin-evaluation/
```

**Why this decomposition**: Each phase of the plugin-authoring lifecycle is a distinct methodology with distinct trigger phrases. A single monolithic skill would have 7x overlapping trigger patterns and confuse the model about which aspect of plugin development to apply. Separating into 7 skills lets each have a tight, front-loaded description and activate on the specific phase the user is in.

**Alternative**: could have shipped as 7 separate plugins. Chose single multi-skill plugin because the user's install-and-discovery cost is 7x higher that way, and the shared `scripts/` directory (validate, scaffold, run_eval, test_hook) is genuinely shared across all skills.

---

## 3. `skillstack-workflows` (composed-workflow multi-skill)

**Components**: 9 skills. No hooks, no MCP.

**Layout**:
```
skillstack-workflows/
├── .claude-plugin/plugin.json
├── README.md
└── skills/
    ├── skill-bug-triage/
    ├── skill-feature-design/
    ├── skill-code-review-gate/
    └── ... (6 more)
```

**Why this decomposition**: Each skill is a workflow that composes several OTHER skills (e.g. `skill-bug-triage` references `debugging` + `test-driven-development` + `code-review`). The purpose of this plugin is meta: it doesn't add new methodologies, it orchestrates existing ones for common use cases.

**Alternative**: could have been slash commands (`/bug-triage`). Chose skills because users already have mental models for "what to do when a bug comes in" — a skill activates on natural phrasing, a command requires knowing the name.

---

## 4. Hypothetical `repo-linter` (hook-first plugin)

**Components**: Hooks + 1 skill. No MCP, no commands.

**Layout**:
```
repo-linter/
├── .claude-plugin/plugin.json
├── README.md
├── hooks/
│   ├── hooks.json               # PostToolUse after Edit|Write
│   └── scripts/run-linter.sh
└── skills/lint-fixing/
    └── SKILL.md                  # methodology for fixing lint errors
```

**Why this decomposition**: The core capability is "lint runs automatically after every edit" — that is purely event-driven, purely Hook territory. But when the linter finds errors, the user needs guidance to fix them — that's Skill territory. Two components, each doing what it's good at.

**Alternative**: hook-only with a heavy script that fixes errors itself. Chose the skill for fixing because methodology-driven fixes benefit from model reasoning on context, which a shell script can't replicate.

---

## 5. Hypothetical `customer-data` (MCP-first plugin)

**Components**: MCP server + 1 skill.

**Layout**:
```
customer-data/
├── .claude-plugin/plugin.json
├── README.md
├── .mcp.json
├── mcp-server/                  # Node.js process
│   ├── package.json
│   └── server.js                # exposes crm.search_customers, crm.get_ticket
└── skills/customer-lookup/
    └── SKILL.md                  # methodology for querying, formatting, follow-up
```

**Why this decomposition**: Accessing the CRM requires persistent auth state and network calls — that's MCP. Knowing WHEN to query it and HOW to present the results is methodology — that's Skill. The skill's body explicitly references the MCP tool names so the model knows to use them when the skill activates.

**Alternative**: MCP-only. Chose to add the skill because without it, users have to know that the MCP tool exists and call it by name. With the skill, natural queries like "who's the customer for ticket #123" automatically activate the methodology that then calls the MCP tool.

---

## 6. Hypothetical `security-guardrails` (hook + skill)

**Components**: Hooks (multiple events) + 1 skill.

**Layout**:
```
security-guardrails/
├── .claude-plugin/plugin.json
├── hooks/
│   ├── hooks.json               # PreToolUse Bash, UserPromptSubmit, Stop
│   └── scripts/
│       ├── block-secrets.sh
│       ├── audit-prompt.sh
│       └── log-session.sh
└── skills/secure-coding/
    └── SKILL.md
```

**Why this decomposition**: Guardrails are event-driven — "block X before it runs" — which is Hook territory. Teaching secure coding patterns is methodology — that's Skill territory. The hook blocks the dangerous action; the skill teaches the user/model how to do it safely next time.

---

## 7. Community: `superpowers` (multi-skill + subagents)

**Components**: Many skills + subagent definitions.

**Reference**: [github.com/obra/superpowers](https://github.com/obra/superpowers) (community-maintained)

**Why this decomposition**: Each skill teaches a development workflow (TDD, debugging, refactoring). Some workflows are long-running and benefit from a dedicated subagent context (e.g. multi-step refactoring). Skills activate on user intent; subagents are invoked by the skill's body when the workflow needs isolation.

---

## 8. Community: `ralph-wiggum` (hook-driven persistence)

**Components**: Hooks (SessionStart, PostToolUse, Stop) + 1 skill.

**Why this decomposition**: The core capability is "keep Claude working on a task until it's actually done", which is fundamentally a loop-control problem — you can't implement "keep going" as a skill because skills only trigger on user queries. Stop hook keeps the session alive; SessionStart hook re-injects the task state after compaction; a skill teaches the methodology of using the loop correctly.

---

## 9. Community: `hookify` (reference hooks plugin)

**Components**: Hooks only. No skill, no MCP.

**Why this decomposition**: The plugin ships pre-built hook examples (the exit-code-1 blocker, the SessionStart direnv loader, the FileChanged .envrc watcher). Users install it as a learning resource and a starting point. There's no methodology to teach beyond "look at the hooks.json and copy what you need" — no skill needed.

**Alternative**: could have been a skill that teaches hooks with references. But the value is in the running examples, not the docs — users want to see the actual hook files they can copy.

---

## 10. Anthropic `pr-review-toolkit` (composed-workflow example)

**Components**: Skills (code review, risk assessment, nitpick filtering) + slash command (`/review-pr`) + hooks for automation.

**Why this decomposition**: PR review is a workflow with multiple phases. Each phase is a skill (easy to discover, activates on intent). A slash command orchestrates the whole workflow end-to-end when the user wants the full pipeline. Hooks automate steps that should run without asking.

---

## Pattern summary

| Decomposition | Use when | Example |
|---|---|---|
| **Single skill** | Pure methodology, one domain | `skill-foundry` |
| **Multi-skill** | Multiple related methodologies | `plugin-dev`, `skillstack-workflows` |
| **Hook + skill** | Event-triggered action + methodology for the follow-up | `repo-linter`, `security-guardrails` |
| **MCP + skill** | External system access + methodology around it | `customer-data` |
| **Hook-only** | Event-triggered automation with no teachable surface | `hookify` |
| **Skill + subagent** | Methodology that sometimes needs isolated execution | `superpowers` |
| **Composed workflow (skill + command + hook)** | Multi-phase workflow with user-triggered and automatic parts | `pr-review-toolkit` |

---

## When in doubt

Ask: "When does this capability become useful?"

- Useful when the user asks about it → **Skill**
- Useful when the system does something → **Hook**
- Useful when the model needs external data → **MCP**
- Useful when the user remembers the command name → **Command**
- Useful when another agent needs isolated context → **Subagent**

If the answer is "more than one of the above", the plugin needs more than one component. That's normal — most non-trivial plugins do.
