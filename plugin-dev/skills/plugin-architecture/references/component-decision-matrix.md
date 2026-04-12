# Component Decision Matrix

> The decision matrix for picking the right extension type. Source: the five-extension model documented at [https://code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins) plus concrete examples from working plugins.

---

## The matrix

Rows are extension types. Columns are properties of the capability you're implementing. A ✓ means the extension type is a good fit when the property holds.

| Property | Skill | Hook | MCP | Subagent | Command |
|---|:---:|:---:|:---:|:---:|:---:|
| Triggered by model judgment on user query | ✓ | | | | |
| Triggered by an event (tool call, session start, file change) | | ✓ | | | |
| Triggered by explicit user input (`/foo`) | | | | | ✓ |
| Triggered by another agent calling `Task(subagent_type=...)` | | | | ✓ | |
| Accesses external system (API, DB, file beyond project) | | | ✓ | | |
| Needs model-level reasoning to decide what to do | ✓ | | | ✓ | |
| Should run before/after every occurrence of X | | ✓ | | | |
| Should run once per session | | ✓* | | | ✓* |
| Needs persistent state across invocations | | ✓ | ✓ | | |
| Should block an action if a policy is violated | | ✓ | | | |
| Injects context that Claude reads | ✓ | ✓ | ✓ | | ✓ |
| Implemented mostly as shell commands / scripts | | ✓ | | | ✓ |
| Implemented mostly as model behavior | ✓ | | | ✓ | |
| Needs its own context window | | | | ✓ | |
| User types the trigger literally | | | | | ✓ |

*Once-per-session: via `SessionStart` hook or a slash command the user runs manually.

---

## How to read the matrix

You are not picking the type that has the most ✓. You are picking the type whose ✓'s match your capability's **required** properties.

### Example 1 — "Block rm -rf before it runs"

Required properties:
- Triggered by an event (specifically: `Bash` tool call) → Hook ✓
- Should block an action if policy violated → Hook ✓
- Implemented as a shell check → Hook ✓

All three point to Hook. Decision: `PreToolUse` hook with matcher `Bash`.

### Example 2 — "Help users debug failing tests"

Required properties:
- Triggered by model judgment (user describes a problem, model picks methodology) → Skill ✓
- Needs model-level reasoning → Skill ✓
- Injects context (debugging methodology) → Skill ✓

All three point to Skill. Decision: `skills/test-debugging/SKILL.md` with methodology and references.

### Example 3 — "Fetch customer data from our CRM"

Required properties:
- Accesses external system → MCP ✓
- Needs persistent state (auth token) → MCP ✓
- Implemented as a service → MCP ✓

All three point to MCP. Decision: MCP server exposing `crm.get_customer`, `crm.list_tickets`, etc.

### Example 4 — "Run our 3-step deployment workflow"

Required properties:
- User types the trigger literally (`/deploy`) → Command ✓
- Needs model reasoning to handle edge cases → Subagent ✓ (borderline)

Two candidates. If the workflow is deterministic with branching on outputs, use a slash command that calls agents/tools. If the workflow needs the agent to make judgment calls at each step, use a subagent. **If unsure, start with a slash command** — it's easier to refactor into a subagent later than the reverse.

---

## Common wrong turns

### "I'll make it a skill so the model triggers it automatically"

You want a skill when **user intent** should trigger the capability. You do NOT want a skill when a **system event** should trigger it. The skill triggering machinery runs once per user prompt — it cannot react to tool calls, file changes, or timers.

**Wrong**: "Skill that auto-formats code after every edit"
**Right**: `PostToolUse` hook with matcher `Edit|Write`

### "I'll make it a hook to reduce load on the model"

Hooks run for every occurrence of their trigger. A hook that runs on `PreToolUse` for `*` fires on every tool call — that can easily be 100+ times per session. If the hook is slow or calls an LLM, it kills interactivity.

**Wrong**: An `agent`-type hook on `PreToolUse` with matcher `*` that asks Claude to evaluate every tool call
**Right**: A narrow matcher (`Bash` only, or a regex on specific patterns) OR a skill the model triggers itself when it wants a second opinion

### "I'll make it a subagent so it has its own context"

Subagents are expensive — each one is a full model session. Reserve them for tasks that:
- Take many tool calls
- Have a clearly bounded goal
- Would pollute the main session context if run inline

**Wrong**: Subagent that formats a file
**Right**: Shell script run by a hook

### "I'll make it a slash command because it's easy"

Slash commands require the user to know the command name and type it. They don't surface automatically. If the capability is "I want this to happen when users ask about X", slash command is the wrong choice — use a skill.

**Wrong**: `/debug-tests` slash command for a methodology
**Right**: `test-debugging` skill

---

## Hybrid patterns

Most non-trivial plugins use **multiple** extension types. Examples:

### Skill + Hook

A skill teaches the methodology (e.g. `code-review`). A hook auto-runs the methodology on PR events (e.g. `PostToolUse` after `Bash` runs `git push`).

### Skill + MCP

A skill teaches how to query a data source. An MCP server exposes the actual query tool. The skill's description says "use when querying X data" and the SKILL.md body instructs the model to call the MCP tool.

### Hook + Subagent

A `SubagentStop` hook checks whether the subagent's output meets criteria; if not, it forces another iteration. Common in test-driven workflows.

### Slash command + Skill

A slash command (`/setup`) is a one-shot user-triggered workflow. A skill handles the day-to-day methodology the user will repeat manually after setup is complete.

---

## Red flags that your decomposition is wrong

1. **The skill never triggers** — your description doesn't match real queries. Either fix the description (use `plugin-evaluation`) or the capability isn't really skill-shaped.
2. **The hook fires too often** — matcher is too broad. Narrow to the specific tool or event.
3. **The MCP tool is never called** — no skill or instruction tells the model when to use it. Add a skill that references the MCP tool explicitly.
4. **The subagent runs for every query** — it shouldn't. Subagents should be invoked deliberately.
5. **The command is never typed** — users don't know it exists. Either advertise it in README / CLAUDE.md, or refactor into a skill that activates on intent.

If you see any of these after shipping, come back to this matrix and re-pick the type.
