---
name: plugin-research
description: Validates a plugin idea by surveying the marketplace, reading authoritative Anthropic sources, and deciding build-vs-fork-vs-skip before writing any code. Use when you want to research existing Claude Code plugins, check whether there is already a plugin for X, decide whether to build a new plugin or fork an existing one, run a marketplace survey before starting work, find authoritative documentation on a Claude Code feature, or gather primary sources for a plugin design. Covers the marketplace survey methodology, the canonical list of authoritative Anthropic URLs (code.claude.com, docs.claude.com, platform.claude.com, github.com/anthropics/claude-code, github.com/anthropics/skills, the Complete Guide PDF), community pattern discovery, and the build-vs-fork-vs-skip decision gate. NOT for deciding whether an idea is worth pursuing (use plugin-ideation) or for designing component layout (use plugin-architecture).
---

# Plugin Research

> **Validate an idea before building. Most plugin ideas die at research time, and that is a success not a failure.** Shipping a plugin that duplicates existing work is a waste for everyone. Shipping a plugin built on outdated assumptions is worse — it ships broken.

---

## When to use this skill

- You have a plugin idea that passed `plugin-ideation` and need to validate it
- You want to check if there's already a plugin for X before starting
- You're deciding whether to build from scratch or fork an existing plugin
- You need authoritative docs on a Claude Code feature before designing around it
- You're writing a PRD for a plugin and need to cite sources

## When NOT to use this skill

- **Deciding if the idea is worth pursuing** → `plugin-ideation`
- **Designing component layout** → `plugin-architecture`
- **Building the plugin** → `skill-creator`, `plugin-hooks`, `plugin-composition`

---

## The research loop

```
1. Marketplace survey    → is this already solved?
2. Authoritative docs    → what does Anthropic say about this?
3. Community patterns    → how are real plugins solving similar problems?
4. Decision              → build / fork / contribute / skip
```

Each step can kill the project. **Killing the project is a good outcome.**

---

## Step 1: Marketplace survey

Search, in order:

1. **Anthropic's bundled plugins** (the ones shipped by default with Claude Code). `skill-creator`, `debug`, etc. — these are curated and high-quality. If Anthropic covers your use case, use their plugin instead.
2. **The skillstack marketplace** and other known marketplaces/collections:
   - `github.com/viktorbezdek/skillstack`
   - `github.com/anthropics/skills` (official skills repo)
   - Community plugin collections (search "claude code plugin" on GitHub)
3. **GitHub search** — look for repos with `.claude-plugin/plugin.json` and descriptions that match your domain.
4. **The Claude Code docs plugin directory** (if maintained) at `code.claude.com/docs/en/plugins`.

### What to look for

- Exact match → skip building, install the existing plugin
- Close match → consider fork or contribution
- Adjacent but not matching → note the pattern, design around it so yours composes well
- Nothing → proceed to step 2

### What to record

For each existing plugin you found that's relevant, write down:
- Plugin name + URL
- What it covers
- What it does NOT cover (the gap)
- Last updated (abandonment signal)
- Install count / stars (adoption signal)

---

## Step 2: Authoritative sources

Before building, read the canonical Anthropic docs for the features you plan to use. Don't rely on Stack Overflow answers, old blog posts, or someone's tutorial — those are frequently out of date.

Full list with descriptions: `references/authoritative-sources.md`. The critical ones:

| URL | What it covers |
|---|---|
| `https://code.claude.com/docs/en/plugins` | Plugin structure, manifest, components |
| `https://code.claude.com/docs/en/hooks` | All 24+ hook events, handler types, exit codes |
| `https://code.claude.com/docs/en/skills` | Skill authoring, frontmatter, progressive disclosure |
| `https://code.claude.com/docs/en/mcp` | MCP server authoring (if relevant) |
| `https://github.com/anthropics/claude-code` | Source code + examples |
| `https://github.com/anthropics/skills` | Official skill examples |
| `https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf` | PDF guide to skill authoring |

**Rule**: every design decision in your plugin should trace back to a documented behavior. If you can't find a reference, assume the behavior is undocumented and subject to change — don't depend on it.

---

## Step 3: Community patterns

Once you know what Anthropic says, check how the community actually builds similar plugins. This surfaces:

- Conventions that aren't documented but are widely followed
- Workarounds for documented-but-broken features
- Anti-patterns the community has already learned to avoid

### Sources

- Existing plugins you found in Step 1 — read their `hooks.json`, `SKILL.md`, `plugin.json`
- `skillstack` plugins in this repo as references
- `superpowers`, `oh-my-claudecode`, other opinionated plugin collections
- GitHub code search for specific patterns (`language:json filename:hooks.json`)

### What to record

Keep a small "patterns file" with snippets you found useful. Don't copy them verbatim — adapt them — but reference them when explaining design decisions later.

---

## Step 4: Decision gate

You now have enough information to decide. Full decision tree: `references/build-vs-fork-decision.md`. Summary:

### Build from scratch when

- No existing plugin covers the use case OR existing plugins are abandoned (no commits in 6+ months)
- Your requirements don't fit the existing architecture
- You need control over the roadmap
- The existing plugin has a license you can't use

### Fork when

- Existing plugin is close but has gaps
- Upstream is inactive or unresponsive
- You have diverging vision

### Contribute when

- Existing plugin is close and actively maintained
- Your change fits upstream's roadmap
- You want long-term shared maintenance

### Skip when

- Existing plugin already covers the use case
- Your idea doesn't pass the `plugin-ideation` 7-criteria checklist
- The maintenance cost exceeds the value
- You'd be rebuilding for the sake of building

---

## When research kills the project

This is the most common outcome. Expect it. You went in planning to build, and you came out realizing you don't need to. Record what you learned:

1. **Which criterion killed it?** ("already solved", "undocumented behavior", "too broad")
2. **What did you find?** Links to the alternatives or the docs that clarified things.
3. **Did you install the alternative?** Often the result of research is "install someone else's plugin and move on".

Killing a project at research time costs a day. Killing it after building costs a week.

---

## From research to build

If research gives you the green light, hand off to:

1. **`plugin-architecture`** — decide component decomposition based on your findings
2. **`plugin-composition`** — layout and integration (if multi-component)
3. **`plugin-hooks`** — hook authoring (if hooks involved)
4. **`skill-creator`** — single-skill authoring (Anthropic's bundled skill)
5. **`plugin-validation`** — structural checks
6. **`plugin-evaluation`** — trigger and output evals before shipping

---

## References

| File | Contents |
|---|---|
| `references/authoritative-sources.md` | Canonical Anthropic URLs with descriptions — the primary sources you should cite in your plugin |
| `references/build-vs-fork-decision.md` | The decision tree with specific criteria for each branch and worked examples |

---

> *Plugin-Dev Authoring Toolkit by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
