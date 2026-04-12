# Frontmatter Rules Reference

> Authoritative rules for `SKILL.md` YAML frontmatter. Every Claude Code skill must have a `---` fenced frontmatter block at the top of `SKILL.md` with at minimum `name` and `description`. Violating any of these rules causes either a validation error or a silent activation failure.

---

## Required fields

### `name`
- **Type:** string
- **Format:** kebab-case only — lowercase letters, digits, hyphens. No spaces, no underscores, no capitals.
- **Max length:** 64 characters
- **Must match:** the skill's directory name (e.g., `my-skill/` → `name: my-skill`)
- **Forbidden:** the strings `anthropic` or `claude` anywhere in the name (reserved by Anthropic)
- **Forbidden:** XML angle brackets `<` or `>`

```yaml
# ✅ correct
name: my-skill

# ❌ wrong — capitals
name: My-Skill

# ❌ wrong — spaces
name: my skill

# ❌ wrong — reserved word
name: claude-helper
```

### `description`
- **Type:** string
- **Max length:** 1024 characters
- **Must contain both:** what the skill does AND when to use it (trigger conditions)
- **Forbidden:** XML angle brackets `<` or `>`
- **Required:** third-person only — no "I", "my", "we", "our"
- **Critical:** front-load the key use case in the first 250 characters. Claude truncates descriptions to a budget (≥8000 chars across all active skills, scales at 1% of context window). Descriptions beyond 250 chars may be cut in the skill listing.
- **Include:** specific phrases users would actually say, not just abstract capabilities
- **Include:** "NOT for X (use Y)" boundary clauses to prevent over-triggering

---

## Optional fields

### `license`
Common values: `MIT`, `Apache-2.0`, `CC-BY-SA-4.0`

### `compatibility`
1-500 characters. Describe environment requirements (required packages, target platform, network access).

### `metadata`
Custom key-value pairs. Common conventions:

```yaml
metadata:
  author: Your Name
  version: 1.0.0
  mcp-server: server-name   # if skill assumes a specific MCP server
  category: productivity
  tags: [automation, code-generation]
```

### `allowed-tools`
Restrict which tools Claude can use when this skill is active. Syntax: space-separated tool names.

```yaml
allowed-tools: "Read Write Edit Bash"
```

### `disable-model-invocation`
Set to `true` to prevent Claude from auto-activating this skill. Only user-invoked via `/skill-name`. Description is not included in system context.

### `user-invocable`
Set to `false` to hide from the `/` command menu. Claude can still auto-activate; user cannot invoke directly.

### `paths`
Glob patterns limiting when the skill auto-activates:
```yaml
paths: "**/*.py"  # only activates when working with Python files
```

### `model`
Override the model for this skill: `claude-haiku-4-5`, `claude-sonnet-4-5`, `claude-opus-4-5`

### `effort`
Override thinking budget: `low`, `medium`, `high`

---

## Frontmatter security restrictions

The following are **forbidden** in frontmatter because the description is injected directly into Claude's system prompt:

- XML angle brackets `<` and `>` — could inject system prompt content
- Code execution in YAML — only YAML safe-parse mode is used
- Names starting with `claude` or `anthropic` — reserved for Anthropic's own skills

---

## Complete valid example

```yaml
---
name: pdf-processor
description: Extracts and processes text, tables, and metadata from PDF files. Use when the user uploads a .pdf, asks for "PDF processing", "extract tables from PDF", "parse PDF content", or "document extraction". Works with both digital and scanned PDFs (OCR). NOT for DOCX/Word files (use document-processor), NOT for image files.
license: MIT
compatibility: Requires pdfminer.six or PyMuPDF. Works on Claude.ai and Claude Code with Python 3.10+.
metadata:
  author: SkillStack
  version: 1.0.0
  category: document-processing
  tags: [pdf, extraction, ocr]
---
```

---

## Common validation errors and fixes

| Error | Cause | Fix |
|---|---|---|
| `name field: kebab-case, no spaces` | Uppercase or space in name | Change to lowercase-with-hyphens |
| `frontmatter name 'X' does not match directory 'Y'` | Name drift | Set `name:` equal to directory name |
| `description missing required field` | Empty or missing description | Add a non-empty `description:` |
| `XML tags in description` | Used `<` or `>` in description | Remove XML tags entirely |
| `description over 1024 characters` | Too long | Trim to ≤1024 chars |
| `Claude or Anthropic in name` | Reserved namespace | Choose a different name |

---

## Further reading

- [Claude Code Skills — Overview](https://code.claude.com/docs/en/skills) (frontmatter fields and behavior)
- [Claude Code Skills — Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) (pages 10-12)

---

> *Plugin-Dev Authoring Toolkit by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
