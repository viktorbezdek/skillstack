---
name: plugin-validation
description: Validates the structural correctness of Claude Code plugins — plugin.json manifest fields, SKILL.md YAML frontmatter, reference cross-references, skill name-to-directory consistency, and plugin structure conventions. Use when checking whether a plugin is well-formed before shipping, when debugging "plugin won't load" errors, when setting up CI for a plugin repo, or when reviewing a third-party plugin for issues. NOT for functional evaluation (whether skills activate or produce correct output — use plugin-evaluation for that). NOT for single-skill SKILL.md quality review (use skill-forge for that).
---

# Plugin Validation

> A plugin that passes `claude plugin validate` can still fail to activate in production. Structural validation eliminates stupid failures; it doesn't guarantee quality. This skill covers both what the official validator checks and the additional contract the skillstack validator enforces.

---

## When to use this skill

- "My plugin won't install" or "plugin fails to load" — structural errors
- "I want to add CI to my plugin repo" — validation tooling
- "Is my plugin.json correct?" — manifest fields
- "Why is my SKILL.md frontmatter invalid?" — frontmatter rules
- "How do I check cross-references?" — referenced files that don't exist

## When NOT to use this skill

- Checking whether a skill activates correctly → `plugin-evaluation`
- Checking whether a skill's instructions are good → `skill-forge`
- Debugging hook behavior → `plugin-hooks`

---

## Core principle

Structural validation is necessary but not sufficient. A structurally valid plugin can still fail because the frontmatter description doesn't trigger reliably, the skills are too long, or the hooks use exit code 1 instead of exit code 2. Structure is table stakes; evaluation is the real test.

---

## What `claude plugin validate` checks

`claude plugin validate .` (run from the plugin directory) checks:

- `plugin.json` JSON syntax and schema violations — missing required `name` field, invalid component path types
- `SKILL.md` YAML frontmatter syntax — unclosed quotes, missing `---` delimiters, invalid `name` format
- `hooks/hooks.json` syntax — invalid JSON
- Directory-structure errors — components inside `.claude-plugin/` instead of plugin root

What it **does NOT** check:
- Whether `name` in frontmatter matches the skill directory name
- Whether files cited in SKILL.md (references, scripts) actually exist on disk
- Whether `description` meets quality criteria (third-person, first 250 chars, trigger phrases)
- Orphan catalog entries in `marketplace.json`
- Version drift across `plugin.json`/`registry.json`/`marketplace.json`

---

## What the skillstack validator adds

`python3 plugin-dev/scripts/validate_plugin.py --plugin-dir ./your-plugin/` covers the gaps:

- Frontmatter `name` matches the skill directory name (common drift source)
- Every reference file cited in SKILL.md body (any `references/` link) exists on disk
- Plugin `name` in `plugin.json` matches the plugin directory name
- Multi-skill plugins: validates each sub-skill independently with `plugin/skill` scoped errors

Run this before every `git push` or CI commit. See `references/validation-checklist.md` for the pre-ship checklist.

---

## Running validation

```bash
# Official validator (inside your plugin directory)
claude plugin validate .

# Skillstack validator (any plugin, from repo root)
python3 plugin-dev/scripts/validate_plugin.py --plugin-dir ./my-plugin/

# JSON output for CI integration
python3 plugin-dev/scripts/validate_plugin.py --plugin-dir ./my-plugin/ --json

# Strict mode (fail on warnings too)
python3 plugin-dev/scripts/validate_plugin.py --plugin-dir ./my-plugin/ --strict
```

Exit codes: 0 = all pass, 1 = errors found, 2 = validator crashed, 3 = `--strict` mode warnings present.

---

## Interpreting common errors

| Error | Cause | Fix |
|---|---|---|
| `plugin.json name 'X' does not match directory 'Y'` | plugin.json `name` field differs from directory | Set `name` to match directory (kebab-case) |
| `SKILL.md frontmatter name 'A' does not match skill directory 'B'` | Frontmatter drift | Update frontmatter `name:` field |
| `SKILL.md cites <reference> which does not exist` | A link to a references/ file in the SKILL.md body points to a file that doesn't exist | Create the file at that path or remove the citation |
| `missing entry in registry.json` | Plugin not catalog-registered | Add entry to `.claude-plugin/registry.json` |
| `version drift: plugin.json=X vs registry.json=Y` | Version mismatch | Make all three version strings byte-equal |
| `missing skills/ directory` | Plugin has no skills | Create `skills/` with at least one skill |

---

## CI integration

Add this to your GitHub Actions workflow (mirror `.github/workflows/ci.yml` `plugin-validation` job):

```yaml
- name: Validate plugin structure
  run: python3 .github/scripts/validate_plugins.py  # repo-level
  # or for your own plugin repo:
  # python3 plugin-dev/scripts/validate_plugin.py --plugin-dir . --strict
```

See `references/validation-checklist.md` for the full pre-ship checklist.

---

> *Plugin-Dev Authoring Toolkit by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
