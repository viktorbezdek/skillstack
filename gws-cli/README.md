# Gws Cli

> **v1.0.0** | Development | 0 iterations

Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace APIs from the command line. Dynamic Discovery-based commands, helper shortcuts, schema introspection, and cross-service workflows.

## What Problem Does This Solve

Automating Google Workspace tasks normally requires context-switching between the Drive web UI, Gmail, Sheets, Calendar, and Admin Console — or writing bespoke API integration code for each service. The `gws` CLI solves this by generating commands at runtime from Google's Discovery Service, giving you a single composable interface for all 18 Workspace APIs that stays current without manual updates and pipes naturally with `jq` and shell scripts.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "List all files in a Drive folder matching a name pattern" | `gws drive files list` with `q` query syntax reference and Drive query operator table |
| "Send an email with an attachment from the command line" | `gws gmail +send` helper with `--to`, `--subject`, `--body`, `--attachment` flags |
| "Read a range from a Google Sheet and output as CSV" | `gws sheets +read` with `--format csv` and single-quote escaping rule for `!` in range names |
| "Create a Calendar event with attendees and a Google Meet link" | `gws calendar +insert` with `--attendee` and `--meet` flags |
| "Build a standup report combining today's meetings and open tasks" | `gws workflow +standup-report` cross-service helper |
| "I'm not sure what parameters a method accepts" | `gws schema drive.files.list --resolve-refs` introspection command showing parameters, body schema, and required OAuth scopes |

## When NOT to Use This Skill

- building MCP servers -- use [mcp-server](../mcp-server/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install gws-cli@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the gws-cli skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `google-workspace`
- `gws`
- `drive`
- `gmail`
- `sheets`
- `calendar`

## What's Inside

- **Overview** -- Service listing (18 APIs), command generation model, helper shortcuts, output formats, and the time-savings rationale for a unified CLI.
- **Quick Reference** -- Command syntax patterns, global flags table (--params, --json, --format, --page-all, --dry-run, etc.), services table with aliases, and exit code reference.
- **Authentication** -- OAuth setup flow, scope presets (default/readonly/full/custom), AES-256-GCM credential storage, auth precedence order, and environment variable reference.
- **Schema Introspection** -- `gws schema` usage for discovering method parameters, request body structure, response shape, and required scopes before constructing commands.
- **Drive** -- Raw API methods for list, search, get, download, export, create, move, delete; `+upload` helper; Drive query syntax operator table; common MIME type reference.
- **Gmail** -- Raw API methods for list, search, get, label, trash, thread; `+send`, `+reply`, `+reply-all`, `+forward`, `+triage`, `+watch` helpers; Gmail search operator table.
- **Sheets** -- Raw API methods for get, read, batch-read, write, append, create, clear; `+read` and `+append` helpers; single-quote escaping rule for range names containing `!`.
- **Calendar** -- Raw API methods for list, get, insert, patch, delete, quickAdd; `+agenda` (today/tomorrow/week/days) and `+insert` helpers with meet and attendee support.

## Key Capabilities

- **18 services**
- **Dynamic commands**
- **Helper shortcuts**
- **Schema introspection**
- **Output formats**
- **Cross-service workflows**

## Related Skills

- **[Api Design](../api-design/)** -- Comprehensive API design skill for REST, GraphQL, gRPC, and Python library architectures. Design endpoints, schemas, aut...
- **[Debugging](../debugging/)** -- Comprehensive debugging skill combining systematic debugging methodology, browser DevTools automation, E2E testing with ...
- **[Frontend Design](../frontend-design/)** -- Comprehensive Frontend Design (UI/UX) skill combining UI design systems, component libraries, CSS/Tailwind styling, acce...
- **[Mcp Server](../mcp-server/)** -- Comprehensive MCP (Model Context Protocol) server development skill. Build, configure, and manage MCP servers using Pyth...
- **[Nextjs Development](../nextjs-development/)** -- Comprehensive Next.js development skill covering App Router (13+/15/16), Server Components, Server Actions, Cache Compon...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
