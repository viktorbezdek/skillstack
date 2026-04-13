# GWS CLI

> **v1.0.0** | Development | 1 iteration

Google Workspace CLI (gws) skill for managing Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and 11 more Workspace APIs from the command line. Dynamic Discovery-based commands, helper shortcuts, schema introspection, and cross-service workflows.

## What Problem Does This Solve

Automating Google Workspace tasks normally requires context-switching between the Drive web UI, Gmail, Sheets, Calendar, and Admin Console -- or writing bespoke API integration code for each service. The `gws` CLI solves this by generating commands at runtime from Google's Discovery Service, giving you a single composable interface for all 18 Workspace APIs that stays current without manual updates and pipes naturally with `jq` and shell scripts.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install gws-cli@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

Single-skill plugin with a comprehensive SKILL.md, 3 reference files, and an examples directory.

### SKILL.md (30,000+ words)

| Section | What It Covers |
|---|---|
| **Overview** | 18 services, dynamic command generation, helper shortcuts, output formats, cross-service workflows |
| **Quick Reference** | Command syntax patterns, global flags (`--params`, `--json`, `--format`, `--page-all`, `--dry-run`), services table with aliases, exit codes |
| **Authentication** | OAuth setup flow, scope presets (default/readonly/full/custom), AES-256-GCM credential storage, auth precedence, environment variables |
| **Schema Introspection** | `gws schema` for discovering method parameters, request body structure, response shape, and required OAuth scopes |
| **Drive** | File list/search/get/download/export/create/move/delete, `+upload` helper, Drive query syntax, MIME type reference |
| **Gmail** | Message list/search/get/label/trash/thread, `+send`/`+reply`/`+forward`/`+triage`/`+watch` helpers, Gmail search operators |
| **Sheets** | Spreadsheet get/read/batch-read/write/append/create/clear, `+read`/`+append` helpers, single-quote escaping for range names |
| **Calendar** | Event list/get/insert/patch/delete/quickAdd, `+agenda` (today/tomorrow/week/days) and `+insert` helpers with Meet and attendee support |

### Reference Files

| File | What It Covers |
|---|---|
| `auth-and-setup.md` | Google Cloud Project prerequisites, `gws auth setup` walkthrough, scope presets, token caching, credential storage |
| `helper-commands.md` | Complete reference for all `+` prefixed helper shortcuts across services |
| `query-syntax.md` | Drive query operators and Gmail search operators with examples |

### Examples

| File | What It Covers |
|---|---|
| `daily-workflows.md` | Morning triage routine, standup report generation, meeting preparation, email-to-task workflows |

## How to Use

**Direct invocation:**

```
Use the gws-cli skill to list all files in my Drive matching "Q1 report"
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`google-workspace` · `gws` · `drive` · `gmail` · `sheets` · `calendar`

## Usage Scenarios

**1. Morning triage in three commands.** Start your day by running `gws gmail +triage` to see unread emails sorted by priority, `gws calendar +agenda --today` to check today's meetings, and `gws tasks tasks list` to review open tasks -- all from the terminal without opening a browser.

**2. Sending an email with an attachment.** Use `gws gmail +send --to alice@example.com --subject "Q1 Report" --body "Attached." --attachment ./report.pdf` instead of writing a multi-step Gmail API integration or switching to the web UI.

**3. Building a cross-service standup report.** Run `gws workflow +standup-report` to automatically pull today's calendar events and open tasks into a single formatted report, ready to paste into Slack or a standup channel.

**4. Discovering API parameters you have never used.** You want to filter calendar events by attendee but do not know the parameter name. Run `gws schema calendar.events.list --resolve-refs` to see every parameter, its type, and whether it is required -- without leaving the terminal or reading API docs.

**5. Automating a spreadsheet update pipeline.** Read data from one sheet with `gws sheets +read --spreadsheet-id ID --range "Sheet1!A1:D100" --format csv`, pipe it through a transformation script, and write results back with `gws sheets +append` -- composing the entire ETL pipeline in a shell script.

## When to Use / When NOT to Use

**Use when:** You need to manage Google Workspace resources (Drive files, Gmail messages, Sheets data, Calendar events, Tasks, Chat, Docs, or any of the 18 supported services) from the command line or in automation scripts.

**Do NOT use for:**
- **Building MCP servers** -- use [mcp-server](../mcp-server/)
- **General API design patterns** -- use [api-design](../api-design/)
- **GCP infrastructure** -- use [cicd-pipelines](../cicd-pipelines/)

## Related Plugins in SkillStack

- **[API Design](../api-design/)** -- REST, GraphQL, gRPC, and Python library API design patterns
- **[MCP Server](../mcp-server/)** -- Build MCP servers in Python or TypeScript for Claude Code integration
- **[Workflow Automation](../workflow-automation/)** -- Workflow orchestration and release automation
- **[Frontend Design](../frontend-design/)** -- UI/UX design systems, component libraries, and accessibility

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
