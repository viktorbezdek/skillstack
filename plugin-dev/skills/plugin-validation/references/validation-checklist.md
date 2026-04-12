# Validation Checklist

> A pre-ship checklist for Claude Code plugins. Run through every item before publishing to a marketplace or committing to CI. Items marked `[auto]` are checked by `python3 plugin-dev/scripts/validate_plugin.py`. Items marked `[manual]` require human verification.

---

## Before you start building

- [ ] **[manual]** Identified 2-3 concrete use cases the plugin should enable
- [ ] **[manual]** Reviewed existing marketplace for plugins that already do this
- [ ] **[manual]** Decided on component decomposition (skill vs hook vs MCP vs agent vs command)
- [ ] **[manual]** Plugin directory named in kebab-case, no spaces or underscores
- [ ] **[manual]** Decided whether this is a single-skill or multi-skill plugin

---

## During development

### plugin.json

- [ ] **[auto]** File exists at `.claude-plugin/plugin.json`
- [ ] **[auto]** Valid JSON (no trailing commas, no syntax errors)
- [ ] **[auto]** `name` field present and kebab-case
- [ ] **[auto]** `name` matches the plugin directory name
- [ ] **[manual]** `version` follows semantic versioning (`1.0.0`)
- [ ] **[manual]** `description` is useful for humans browsing the marketplace
- [ ] **[manual]** `author` object has `name` and `url`
- [ ] **[manual]** `license` specified if open source
- [ ] **[manual]** `keywords` include terms users would search for

### SKILL.md frontmatter (for each skill)

- [ ] **[auto]** File exists at exactly `SKILL.md` (case-sensitive, not `skill.md` or `SKILL.MD`)
- [ ] **[auto]** YAML frontmatter present with `---` delimiters
- [ ] **[auto]** `name` field present, kebab-case, matches skill directory name
- [ ] **[auto]** `description` field present and non-empty
- [ ] **[manual]** Description is third-person (no "I", "my", "we")
- [ ] **[manual]** Description front-loads key use case in first 250 characters
- [ ] **[manual]** Description includes specific trigger phrases users would actually say
- [ ] **[manual]** Description includes "NOT for X (use Y instead)" boundary clause
- [ ] **[manual]** No XML angle brackets `<` or `>` in description
- [ ] **[manual]** Description is ≤1024 characters

### SKILL.md body

- [ ] **[manual]** SKILL.md body is ≤500 lines
- [ ] **[manual]** Detailed content moved to `references/` files
- [ ] **[auto]** Every `references/X.md` cited in SKILL.md exists on disk
- [ ] **[manual]** References are one level deep (SKILL.md → reference, not SKILL.md → ref → deeper)
- [ ] **[manual]** Long references (>100 lines) have a `## Contents` section at the top

### Directory structure

- [ ] **[manual]** Only `plugin.json` is inside `.claude-plugin/` — nothing else
- [ ] **[manual]** Skills in `skills/`, hooks in `hooks/`, commands in `commands/`, agents in `agents/`
- [ ] **[manual]** Scripts use `${CLAUDE_PLUGIN_ROOT}` for paths, not relative `./` paths
- [ ] **[auto]** Plugin README.md exists at plugin root

---

## Before upload / publish

### Validation tools

- [ ] Run `claude plugin validate .` — zero errors
- [ ] Run `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir .` — zero errors
- [ ] Run `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir . --strict` — zero warnings

### Catalog consistency (for skillstack-hosted plugins)

- [ ] **[auto]** Entry in `.claude-plugin/registry.json` at correct alphabetical position
- [ ] **[auto]** Entry in `.claude-plugin/marketplace.json`
- [ ] **[auto]** `version` string is byte-equal across `plugin.json`, `registry.json`, `marketplace.json`
- [ ] **[auto]** `path_in_repo` in `registry.json` points to plugin root (for multi-skill plugins) not a skill subdirectory

### Testing (triggering)

- [ ] **[manual]** Tested with ≥5 prompts that SHOULD activate the skill — all activate
- [ ] **[manual]** Tested with ≥3 prompts that should NOT activate the skill — all correctly reject
- [ ] **[manual]** Tested with paraphrased versions of the trigger phrases — still activates
- [ ] **[manual]** Plugin activates on mobile/different device (description loading confirmed)

### Testing (functional)

- [ ] **[manual]** Each skill produces correct outputs for 2-3 representative tasks
- [ ] **[manual]** Error handling works (MCP connection failure, missing files, etc.)
- [ ] **[manual]** Tested against a baseline (with vs without skill) — skill helps

### After upload

- [ ] **[manual]** Test in a real Claude Code session with `/plugin install name@marketplace`
- [ ] **[manual]** Monitor first 10 uses for undertriggering (skill never loads) or overtriggering (loads for everything)
- [ ] **[manual]** Update `version` field in `plugin.json` when releasing changes
- [ ] **[manual]** Add version to CHANGELOG or README Version History section

---

## CI checklist (for skillstack-integrated plugins)

```bash
# Run these locally before every commit:
python3 .github/scripts/validate_plugins.py          # repo-level validator
python3 plugin-dev/scripts/validate_plugin.py \
  --plugin-dir ./your-plugin/ --strict              # per-plugin validator
cd plugin-dev/scripts && pytest tests/ -q && cd -   # script tests
find . -name "*.sh" -not -path "./.git/*" \
  | xargs shellcheck --severity=error               # shell scripts
```

---

## Further reading

- [Plugins reference — Claude Code Docs](https://code.claude.com/docs/en/plugins-reference)
- [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

---

> *Plugin-Dev Authoring Toolkit by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
