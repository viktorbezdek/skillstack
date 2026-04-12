# `plugin.json` Manifest Reference

> Full schema for `.claude-plugin/plugin.json`. Sourced from [https://code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins) plus the working manifests of Anthropic's bundled plugins and this repo's plugins.

---

## Minimum viable manifest

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "One-sentence description of the plugin's purpose.",
  "author": {
    "name": "Your Name",
    "url": "https://github.com/you"
  }
}
```

These four fields are the minimum for a plugin to be accepted by a marketplace and validated by `validate_plugin.py`.

---

## Full field reference

### `name` — required, string

Kebab-case identifier. Must match the plugin directory name and, for single-skill plugins, the skill's `name` in SKILL.md frontmatter.

Rules:
- Lowercase letters, digits, and hyphens only
- Starts with a letter
- No reserved names (`claude`, `anthropic`, `plugin`, `system`)
- Globally unique within a marketplace

### `version` — required, string

Semantic version (MAJOR.MINOR.PATCH). Bump:
- PATCH for bug fixes and documentation improvements
- MINOR for additive changes (new skill, new reference, expanded description)
- MAJOR for breaking changes (renaming a skill, removing a component type, incompatible frontmatter restructure)

### `description` — required, string

One-sentence summary of the plugin's purpose. This appears in marketplace listings and is NOT the same as the SKILL.md description — this is plugin-level, skill descriptions are skill-level.

**Length**: 60-200 characters is the sweet spot. Longer descriptions get truncated in marketplace UIs.

### `author` — required, object

```json
"author": {
  "name": "Your Name",
  "url": "https://github.com/you",
  "email": "you@example.com"
}
```

| Field | Required | Purpose |
|---|---|---|
| `name` | yes | Human-readable author name |
| `url` | yes | GitHub profile, personal site, or company homepage |
| `email` | no | Contact email (rarely used; prefer issue tracker) |

### `license` — recommended, string

SPDX license identifier. Common values: `MIT`, `Apache-2.0`, `BSD-3-Clause`, `GPL-3.0`. If omitted, the marketplace may mark the plugin "license unknown" and deprioritize it.

### `repository` — recommended, string

Full URL to the source repository. For plugins inside a monorepo, link to the subdirectory:

```json
"repository": "https://github.com/you/repo/tree/main/my-plugin"
```

### `homepage` — optional, string

Full URL to the plugin's landing page or documentation. Defaults to `repository` if not set.

### `keywords` — recommended, array of strings

Search keywords for marketplace discovery. 5-15 is the sweet spot. Include both domain terms and trigger phrases.

```json
"keywords": [
  "claude-code",
  "plugin-development",
  "skill-authoring",
  "hooks",
  "mcp",
  "evaluation",
  "validation"
]
```

### `engines` — optional, object

Version constraints for Claude Code or specific runtimes:

```json
"engines": {
  "claude-code": ">=1.2.0",
  "node": ">=18"
}
```

Use only when your plugin depends on a specific version. Overly strict `engines` blocks adoption.

---

## Component declaration (advanced)

By default, Claude Code auto-discovers components from the standard directory layout (`skills/`, `hooks/`, `agents/`, `commands/`, `.mcp.json`). You usually don't need to declare them explicitly.

The manifest may override discovery with explicit paths:

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "...",
  "author": {"name": "...", "url": "..."},
  "skills": {
    "custom-skill": "./path/to/custom-skill"
  },
  "hooks": "./custom/hooks.json",
  "agents": "./custom/agents",
  "commands": "./custom/commands",
  "mcp": "./custom/.mcp.json"
}
```

**Use this sparingly.** Non-standard layouts are harder to validate, harder to debug, and often cause the auto-discovery to miss components.

---

## Multi-skill plugins

For plugins with multiple skills, keep `plugin.json` at the plugin root:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          ← one manifest
└── skills/
    ├── skill-a/SKILL.md
    ├── skill-b/SKILL.md
    └── skill-c/SKILL.md
```

Each skill has its own frontmatter in its own SKILL.md. The manifest does NOT list skills individually — Claude Code walks `skills/*/` automatically.

---

## Validation rules (from `validate_plugin.py`)

The structural validator enforces:

1. `.claude-plugin/plugin.json` exists and is valid JSON
2. `name`, `version`, `description`, `author.name`, `author.url` are all present
3. `name` matches the plugin directory name
4. For single-skill plugins: `skills/<name>/SKILL.md` exists and its frontmatter `name` matches `plugin.json:name`
5. For multi-skill plugins: each `skills/*/SKILL.md` has valid frontmatter
6. `README.md` exists at plugin root

Additional checks: frontmatter length (description 60-1024 chars), trigger phrase front-loading (first 250 chars), no `<>` placeholders, no dead `references/X.md` citations.

---

## Example manifests (real)

### Single-skill plugin

```json
{
  "name": "skill-creator",
  "version": "1.0.0",
  "description": "Authors new Claude Code skills with progressive disclosure and activation testing.",
  "author": {"name": "Anthropic", "url": "https://anthropic.com"},
  "license": "MIT"
}
```

### Multi-skill plugin

```json
{
  "name": "plugin-dev",
  "version": "1.0.0",
  "description": "End-to-end Claude Code plugin authoring toolkit — ideation, research, architecture, hooks, composition, validation, evaluation.",
  "author": {"name": "Viktor Bezdek", "url": "https://github.com/viktorbezdek"},
  "license": "MIT",
  "repository": "https://github.com/viktorbezdek/skillstack/tree/main/plugin-dev",
  "keywords": ["claude-code", "plugin-authoring", "hooks", "mcp", "evaluation", "validation"]
}
```

### Plugin with hooks + skills

```json
{
  "name": "security-guidance",
  "version": "2.1.0",
  "description": "Security guardrails via PreToolUse hooks + a secure-coding methodology skill.",
  "author": {"name": "acme-sec", "url": "https://github.com/acme/security-guidance"},
  "license": "Apache-2.0",
  "repository": "https://github.com/acme/security-guidance",
  "keywords": ["security", "guardrails", "sast", "owasp"]
}
```

Notice: the manifest doesn't describe the hooks or the skill individually. They are auto-discovered from `hooks/hooks.json` and `skills/secure-coding/SKILL.md`.

---

## Common mistakes

### Missing `author.url`

The validator will reject the plugin. Even if you're the only user, set a URL — use your GitHub profile or the repo URL.

### `version` not bumped on change

Marketplaces cache by version. If you ship a fix without bumping version, users never see the update. Bump PATCH for every release.

### `description` duplicated from SKILL.md

The plugin description is shown in marketplace listings alongside many other plugins. It should be distinct from the skill description — focus on what the plugin delivers as a whole, not how a specific skill activates.

### Using camelCase or snake_case for `name`

`name` must be kebab-case. `myPlugin` and `my_plugin` are invalid — use `my-plugin`.

### Placing `plugin.json` at the repo root for a monorepo

`plugin.json` must be at the plugin directory root, inside `.claude-plugin/`. For monorepos, each plugin has its own `.claude-plugin/plugin.json` inside its subdirectory.
