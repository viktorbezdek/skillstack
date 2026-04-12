# Ideation Anti-Patterns

> The 7 ways plugin ideas go wrong at birth, with case studies and fixes. Every one of these has produced a plugin that got built and then abandoned.

---

## 1. Building for yourself only

**Symptom**: The plugin hardcodes your personal paths, your preferred tools, your specific workflow. Nobody else can install it without rewriting half of it.

**Case study**: A plugin that opens your personal Obsidian vault at `/Users/you/Documents/vault/`, appends a note to "Daily/2026-04-12.md", and tags it with your email. Nobody else has this directory, this file format, or this email. The plugin is functionally useless outside your laptop.

**Fix**: Generalize. Make paths configurable via `.claude/settings.json`. Make tool choices pluggable (any vault, not just Obsidian). Or — if the plugin is deeply personal — accept that it should live in your private `~/.claude/` and not be published.

**The test**: read your plugin's README aloud. If it requires "you must have X installed at Y running on Z", the plugin is for you only.

---

## 2. Tool vs problem confusion

**Symptom**: The idea starts with "I want to build a plugin using hooks" or "I want to try the MCP system". The tool is the goal, not the problem.

**Case study**: Someone wants to learn `PreToolUse` hooks, so they write a plugin that intercepts every tool call and logs it to a file. What does it solve? Nothing specific. What does the user gain? A log they never read.

**Fix**: Flip the order. Start with a problem ("I need to audit which tools Claude uses during security reviews"). Pick the right tool for the problem (hook), not the problem that fits the tool.

**The test**: Can you describe the idea without naming a Claude Code feature? If your one-sentence pitch is "a hook that…" or "an MCP that…", you led with the tool.

---

## 3. Scope creep at ideation time

**Symptom**: Your one-sentence idea grew into seven bullet points of features before you even wrote a line of code. The plugin will take 3x longer to build and 10x longer to maintain.

**Case study**: Started with "Skill that helps review PRs". Grew to: review PRs, run tests, check CI status, post Slack updates, generate release notes, enforce commit format, run security scans, audit dependencies, warn on breaking changes, suggest refactorings, auto-merge trivial PRs. That's not a plugin — that's an engineering team.

**Fix**: Cut back to the smallest version of the idea that is still useful. If "review PRs" alone is useful, build that first. Additional features become v2, v3 — maybe never.

**The test**: Can you trim to one verb? "Review PRs" is one verb. "Review PRs, run tests, check CI…" is many.

---

## 4. Engineering-exercise plugins

**Symptom**: You're building it because you want to learn a Claude Code feature, not because you have a problem. The plugin's real purpose is your education.

**Case study**: "Let me build a plugin that combines hooks, MCP, subagents, and slash commands to see how they all work together." The result is a Frankenstein plugin that demonstrates features but doesn't solve anything for anyone.

**Fix**: It's fine to build for learning — call it what it is. Keep the plugin in your private repo, don't publish it, move on once you've learned the feature. Don't dress it up as a real plugin.

**The test**: Would you install this plugin if you were a stranger? If not, it's a learning exercise.

---

## 5. Already-solved

**Symptom**: Someone else shipped this plugin 6 months ago. You didn't check before starting.

**Case study**: You're about to build a "skill-authoring helper". Anthropic ships `skill-creator` in the default install.

**Fix**: Always run the `plugin-research` pass before building. Search the marketplace, search community plugin collections, search GitHub. If something similar exists, decide: fork / contribute / skip.

**The test**: Can you name 3 places you checked? If not, you haven't checked.

---

## 6. One-off dressed as repeatable

**Symptom**: Your plugin idea is really a single project's migration or cleanup, not a repeatable pain.

**Case study**: "A plugin that migrates our app from React 17 to React 18." React 18 migrations are a one-time event — once you've done yours, you never need the plugin again. The investment in packaging doesn't pay back.

**Fix**: For one-offs, write a detailed prompt or a subagent run, not a plugin. Plugins are for repeatable workflows, not for specific projects.

**The test**: After using the plugin N times, are you done forever? If yes, it's a one-off. A repeatable plugin is one you'd still use in 12 months.

---

## 7. Shiny technology

**Symptom**: Claude Code ships a new feature, and you're searching for a problem that "justifies" using it.

**Case study**: New `WorktreeCreate` hook event drops. You build a plugin that hooks `WorktreeCreate` to do… something. You're not sure what, but the hook is cool.

**Fix**: Wait. Let the feature mature, watch real use cases emerge, and pick one that matches a real pain you have. Being first with a feature isn't valuable if the plugin solves nothing.

**The test**: Could you describe the idea BEFORE you knew the feature existed? If not, the feature came first.

---

## Bonus: signals your idea is NOT one of these

The idea passes the seven criteria, AND:

- You can point to ≥3 moments in the last month when you suffered this pain
- You can describe the desired behavior without naming a Claude Code feature
- You can name ≥1 other person who would use it, unprompted
- You've checked ≥3 existing plugin sources and found nothing equivalent
- You're willing to maintain it for a year

If all of these hold, you probably have a real plugin idea. Hand off to `plugin-research` to validate.

---

## How to kill a bad idea gracefully

Killing an idea is a success, not a failure. Most plugin ideas *should* be killed — the ones that survive are better for it. Kill rituals:

1. **Write down the idea and why you killed it.** Future-you will thank you when the same idea pops up again.
2. **Note which criterion killed it.** If it's always "not repeatable", you have a pattern to watch for.
3. **Salvage the insight.** Even a bad plugin idea often contains a good CLAUDE.md entry, a good prompt snippet, or a good personal automation. Extract the salvage and discard the rest.

The best plugin authors have a long list of killed ideas. That list is proof the discipline is working.
