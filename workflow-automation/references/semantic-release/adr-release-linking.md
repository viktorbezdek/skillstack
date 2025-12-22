**Skill**: [semantic-release](../SKILL.md)

# ADR/Design Spec Linking in Release Notes

Automatically include links to Architecture Decision Records (ADRs) and Design Specs in release notes.

## Overview

When semantic-release creates a release, the `generate-adr-notes.mjs` script detects changed ADRs/specs and appends clickable links to the release notes.

## How It Works

The script uses a **union approach** to detect ADRs:

1. **Git diff detection**: Files changed in `docs/adr/*.md` and `docs/design/*/spec.md` since the last release
2. **Commit message parsing**: References like `ADR: 2025-12-06-slug` in commit bodies
3. **Deduplication**: Both methods combined, deduplicated by ADR slug
4. **Full HTTPS URLs**: Required for GitHub release pages (relative links don't work)

## Configuration

### Step 1: Set Environment Variable

Before running semantic-release, set the `ADR_NOTES_SCRIPT` environment variable:

```bash
# For projects using the installed plugin
export ADR_NOTES_SCRIPT="${CLAUDE_PLUGIN_ROOT:-$HOME/.claude/plugins/marketplaces/cc-skills/plugins/itp}/skills/semantic-release/scripts/generate-adr-notes.mjs"

# Or for the cc-skills source repo itself
export ADR_NOTES_SCRIPT="./plugins/itp/skills/semantic-release/scripts/generate-adr-notes.mjs"
```

### Step 2: Configure `.releaserc.yml`

Add to your `.releaserc.yml` **before** `@semantic-release/changelog`:

```yaml
# ADR/Design Spec links via @semantic-release/exec
- - "@semantic-release/exec"
  - generateNotesCmd: 'node "$ADR_NOTES_SCRIPT" ${lastRelease.gitTag}'
```

If you already have an `@semantic-release/exec` entry (e.g., for `prepareCmd`), consolidate them:

```yaml
- - "@semantic-release/exec"
  - generateNotesCmd: 'node "$ADR_NOTES_SCRIPT" ${lastRelease.gitTag}'
    prepareCmd: "node scripts/sync-versions.mjs ${nextRelease.version}"
```

### Why Environment Variable?

**Important**: `@semantic-release/exec` uses [lodash templates](https://lodash.com/docs/4.17.15#template) to process commands. Lodash interprets `${...}` as JavaScript expressions, not shell variables.

| Syntax                             | What Lodash Does        | Result                                 |
| ---------------------------------- | ----------------------- | -------------------------------------- |
| `${lastRelease.gitTag}`            | Evaluates as JS         | ✅ Works (semantic-release context)    |
| `${CLAUDE_PLUGIN_ROOT:-$HOME/...}` | Tries to evaluate as JS | ❌ `SyntaxError: Unexpected token ':'` |
| `$ADR_NOTES_SCRIPT`                | Ignores (no braces)     | ✅ Passes through to bash              |

By using `$VAR` (no braces), lodash ignores it and bash expands it during execution.

## Output Format

The script appends this section to release notes (if ADRs are found):

```markdown
---

## Architecture Decisions

### ADRs

- [Centralized Version Management](https://github.com/owner/repo/blob/main/docs/adr/2025-12-05-centralized-version-management.md) (accepted)

### Design Specs

- [Centralized Version Management Spec](https://github.com/owner/repo/blob/main/docs/design/2025-12-05-centralized-version-management/spec.md)
```

## ADR Reference in Commits

To explicitly link an ADR in release notes (even if the ADR file wasn't modified), include this in your commit message body:

```
feat: add new authentication flow

Implements OAuth2 PKCE flow for mobile clients.

ADR: 2025-12-06-oauth2-pkce-mobile
```

The script will detect this reference and include the ADR in release notes.

## Edge Cases

| Scenario          | Behavior                                             |
| ----------------- | ---------------------------------------------------- |
| No ADRs changed   | Script exits silently (no section added)             |
| First release     | Uses `git ls-files` to find all tracked ADRs         |
| ADR deleted       | Excluded (git diff --diff-filter=ACMR excludes D)    |
| No H1 in ADR file | Uses slug as fallback title                          |
| Missing ADR file  | Referenced commits are skipped if file doesn't exist |

## Requirements

- **Directory structure**: `docs/adr/YYYY-MM-DD-slug.md` and `docs/design/YYYY-MM-DD-slug/spec.md`
- **Git remote**: Must have `origin` remote configured
- **Node.js**: ES modules support (Node 14+)

## Related

- [ADR Code Traceability](../../adr-code-traceability/SKILL.md) - Reference ADRs in code comments
- [Local Release Workflow](./local-release-workflow.md) - Complete release process
