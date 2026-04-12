# Authoritative Sources

> The canonical list of primary sources for Claude Code plugin development. **Always check the live URL before relying on cached content** — Anthropic's docs evolve. This file is a directory, not a substitute for actually reading the docs.

Last verified: 2026-04-12. If today is significantly later, re-check each URL.

---

## Official Anthropic documentation

### Claude Code CLI docs — `code.claude.com/docs/en/*`

The definitive reference for Claude Code features. Evolves with each release.

| URL | What it covers |
|---|---|
| `https://code.claude.com/docs/en/` | Docs index — start here for navigation |
| `https://code.claude.com/docs/en/plugins` | Plugin system: manifest, components, directory layout, install/update |
| `https://code.claude.com/docs/en/plugins-guide` | Plugin authoring walkthrough |
| `https://code.claude.com/docs/en/hooks` | **All documented hook events**, handler types, exit codes, matcher syntax, decision JSON schema |
| `https://code.claude.com/docs/en/hooks-guide` | Hook authoring walkthrough with worked examples |
| `https://code.claude.com/docs/en/skills` | Skill system: frontmatter, progressive disclosure, activation |
| `https://code.claude.com/docs/en/mcp` | MCP server integration with Claude Code |
| `https://code.claude.com/docs/en/slash-commands` | Slash command system |
| `https://code.claude.com/docs/en/subagents` | Subagent definitions and lifecycle |
| `https://code.claude.com/docs/en/settings` | Settings files, precedence, environment variables |

**Note**: `docs.claude.com/en/docs/claude-code/*` redirects to `code.claude.com/docs/en/*`. Both forms appear in the wild — the canonical form is `code.claude.com`.

### Model docs — `platform.claude.com/docs/en/*` (historically `docs.anthropic.com/en/docs/*`)

The Claude API and model-level documentation. Relevant when your plugin uses MCP, tool use, or programmatic model calls.

| URL | What it covers |
|---|---|
| `https://platform.claude.com/docs/en/` | Platform docs index |
| `https://platform.claude.com/docs/en/tool-use/overview` | Tool use schema and semantics |
| `https://platform.claude.com/docs/en/models/overview` | Model capabilities, IDs, versioning |
| `https://platform.claude.com/docs/en/prompt-caching` | Prompt caching (relevant for plugin MCPs) |

### MCP protocol spec

| URL | What it covers |
|---|---|
| `https://modelcontextprotocol.io/` | Protocol homepage |
| `https://modelcontextprotocol.io/specification` | Spec documents |
| `https://modelcontextprotocol.io/docs/concepts/servers` | Building an MCP server |

---

## GitHub repositories

### Anthropic-maintained

| URL | What it covers |
|---|---|
| `https://github.com/anthropics/claude-code` | Source code for Claude Code CLI — look here for undocumented behaviors and examples |
| `https://github.com/anthropics/skills` | Official skill examples — the reference for best-practice skill authoring |
| `https://github.com/anthropics/prompt-eng-interactive-tutorial` | Prompt engineering tutorial |
| `https://github.com/anthropics/courses` | Curated Anthropic learning content |

### Community

| URL | What it covers |
|---|---|
| `https://github.com/viktorbezdek/skillstack` | This repo — 52+ plugins with working SKILL.md, hooks, multi-skill plugins |
| `https://github.com/obra/superpowers` | Opinionated workflow plugin collection |
| (search `github.com` for `filename:.claude-plugin/plugin.json`) | All public Claude Code plugins |

---

## Long-form guides and PDFs

| URL | What it covers |
|---|---|
| `https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf` | The Complete Guide to Building Skill for Claude — the canonical PDF on skill authoring; covers frontmatter, activation, description patterns, progressive disclosure, eval-driven iteration |
| `https://www.anthropic.com/engineering` | Anthropic engineering blog — occasional Claude Code deep dives |
| `https://www.anthropic.com/news` | Release announcements — new features, version bumps |

---

## Example: tracing a hook-related decision

Suppose you're designing a hook and wonder: "Can `PreToolUse` modify the tool's input before it runs?"

1. **Primary**: read `code.claude.com/docs/en/hooks` → search for "updatedInput" → find the decision schema
2. **Cross-check**: check `github.com/anthropics/claude-code` for example hooks that use `updatedInput`
3. **Community**: search GitHub for `"updatedInput" in:file filename:hooks.json` to see how real plugins use it
4. **PDF**: search `The-Complete-Guide-to-Building-Skill-for-Claude.pdf` for any cross-references (this PDF is skill-focused, hooks are peripheral)

If all four agree, you have a reliable design anchor. If they disagree, trust the most recent (usually `code.claude.com/docs/en/hooks`).

---

## Red flags — sources to NOT rely on

| Source | Why |
|---|---|
| Random blog posts older than 6 months | Anthropic's docs change faster than blogs update |
| Stack Overflow answers without a date | Same reason |
| Cached copies of docs you found via search | Always click through to the canonical URL |
| Claude Code behavior you observed in one version | Not the same as documented behavior — test on current version |
| AI-generated tutorials (including from earlier Claude versions) | High hallucination rate on specific APIs and field names |

---

## Citing sources in your plugin

When your SKILL.md, references, or README reference a fact from the docs, link the exact URL. Three benefits:

1. Future-you can re-verify when the docs change
2. Reviewers can trace the reasoning
3. Users who want depth can read the primary source

**Example citation pattern** (from this plugin's own references):

```markdown
> Authoritative source: [https://code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks)
```

Put the citation at the top of the reference file and again next to any specific claim that depends on a source.

---

## Keeping this list current

This file names ≥18 URLs. When a URL moves or a new primary source lands:

1. Update the URL and the last-verified date at the top
2. Re-run any SKILL.md or reference files that cite the old URL
3. Commit the update with a clear message ("docs: update authoritative sources 2026-MM-DD")

A broken link in a reference file is a silent failure — readers may not notice, but the reliability of the skill depends on it.
