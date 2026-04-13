# GWS CLI

> **v1.0.0** | Development | 1 iteration

> Manage all 18 Google Workspace APIs from the terminal -- Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and more -- with one dynamically-generated CLI that stays current without updates.

## The Problem

Automating Google Workspace tasks means choosing between two bad options. Option one: open five browser tabs (Drive, Gmail, Sheets, Calendar, Admin Console), click through each web UI, copy data between them manually, and repeat tomorrow. Option two: write bespoke API integration code for each service -- separate OAuth flows, separate client libraries, separate error handling, separate pagination logic -- and maintain it all when Google changes the API.

Both options scale poorly. A morning triage routine that checks unread email, reviews today's calendar, and pulls open tasks requires three separate interactions (or three separate API integrations). A workflow that reads data from a spreadsheet, transforms it, and writes results back requires understanding the Sheets API's peculiar range notation, batch update semantics, and value rendering options. And discovering what parameters an API method accepts means reading Google's documentation website -- which is comprehensive but not accessible from a terminal session.

The result is that most teams either do Workspace operations manually (slow, error-prone, not scriptable) or build one-off integrations for specific tasks (expensive to build, expensive to maintain, fragile when APIs change). There is no general-purpose command-line tool that works across all Workspace services with a consistent interface.

## The Solution

The `gws` CLI provides a single command-line interface for all 18 Google Workspace APIs. Commands are generated dynamically at runtime from Google's Discovery Service, so they stay current without CLI updates -- when Google adds a new API method, `gws` picks it up automatically. Helper shortcuts (`+send`, `+triage`, `+agenda`, `+upload`, `+read`, `+append`) wrap the most common operations in ergonomic commands. Schema introspection (`gws schema`) lets you discover method parameters, request body structure, response shapes, and required OAuth scopes without leaving the terminal.

This plugin gives Claude deep knowledge of the `gws` CLI so it can help you compose commands, build cross-service workflows, troubleshoot authentication, discover API parameters, and automate Workspace operations. The SKILL.md covers all 18 services with complete command syntax, helper command reference, query syntax for Drive and Gmail search, authentication setup and scope management, and worked examples for daily workflows.

The practical outputs are ready-to-run `gws` commands for any Workspace operation, shell scripts that compose multiple services into workflows (morning triage, standup reports, meeting preparation, email-to-task), and schema introspection commands that replace reading API documentation.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Morning triage means opening Gmail, Calendar, and Tasks in separate browser tabs and scanning each manually | Three commands: `gws gmail +triage`, `gws calendar +agenda --today`, `gws tasks tasks list` |
| Sending an email with an attachment requires the Gmail web UI or a multi-step API integration | One command: `gws gmail +send --to alice@example.com --subject "Report" --attachment ./report.pdf` |
| Discovering API parameters means reading Google's documentation website in a browser | `gws schema calendar.events.list --resolve-refs` shows every parameter, type, and whether it is required |
| Automating a spreadsheet read-transform-write pipeline requires a custom Sheets API integration | Pipe `gws sheets +read` output through `jq`, write back with `gws sheets +append` -- all in a shell script |
| Each Google service requires separate OAuth setup and scope management | One `gws auth login` with scope presets (default/readonly/full/custom) covers all services |
| Cross-service workflows (calendar + tasks + email) are manual or require custom glue code | Built-in workflow commands: `gws workflow +standup-report`, `gws workflow +meeting-prep` |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install gws-cli@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention Google Workspace, gws, Drive, Gmail, Sheets, Calendar, or any of the 18 supported services.

### Prerequisites

- **`gws` CLI** must be installed and available on PATH
- **Google Cloud Project** with OAuth credentials configured
- Run `gws auth setup` to complete the initial authentication flow

## Quick Start

1. Install the plugin using the commands above
2. Ensure `gws` is installed and authenticated (`gws auth status` should show `token_valid: true`)
3. Type: `List all PDF files in my Drive modified this week`
4. Claude produces: `gws drive files list --params '{"q": "mimeType=\"application/pdf\" and modifiedTime > \"2026-04-06T00:00:00\"", "fields": "files(id,name,modifiedTime)"}'`
5. Next, try: `Send an email to the team with the Q1 report attached` to see the `+send` helper in action

## What's Inside

Single-skill plugin with one comprehensive SKILL.md (30,000+ words), 3 reference files, 1 examples directory, 13 trigger eval cases, and 3 output eval cases.

| Section | What It Covers |
|---|---|
| **Overview** | 18 services, dynamic command generation, helper shortcuts, output formats, cross-service workflows |
| **Quick Reference** | Command syntax, global flags (`--params`, `--json`, `--format`, `--page-all`, `--dry-run`), services table with aliases, exit codes |
| **Authentication** | OAuth setup flow, scope presets (default/readonly/full/custom), AES-256-GCM credential storage, environment variables |
| **Schema Introspection** | `gws schema` for discovering method parameters, request body structure, response shape, and required scopes |
| **Drive** | File list/search/get/download/export/create/move/delete, `+upload` helper, Drive query syntax, MIME type reference |
| **Gmail** | Message list/search/get/label/trash/thread, `+send`/`+reply`/`+forward`/`+triage`/`+watch` helpers, search operators |
| **Sheets** | Spreadsheet get/read/batch-read/write/append/create/clear, `+read`/`+append` helpers, range notation |
| **Calendar** | Event list/get/insert/patch/delete/quickAdd, `+agenda`/`+insert` helpers with Meet and attendee support |

### Reference Files

| Reference | Topic |
|---|---|
| `auth-and-setup.md` | Google Cloud Project prerequisites, `gws auth setup` walkthrough, scope presets, token caching, credential storage |
| `helper-commands.md` | Complete reference for all `+` prefixed helper shortcuts across services |
| `query-syntax.md` | Drive query operators and Gmail search operators with examples |

### Examples

| File | Topic |
|---|---|
| `daily-workflows.md` | Morning triage routine, standup report generation, meeting preparation, email-to-task workflows |

### gws-cli

**What it does:** Activates when you ask about Google Workspace operations, `gws` commands, Drive file management, Gmail automation, Sheets data operations, Calendar event management, or any of the 18 supported Workspace APIs. Produces ready-to-run `gws` commands with correct syntax, flags, and parameters, and composes multi-service workflows for automation.

**Try these prompts:**

```
List all shared Drive files that haven't been modified in 6 months so I can clean up stale shares
```

```
Send a meeting recap email to all attendees of my 2pm meeting today with the action items from our doc
```

```
Read the budget data from our Q1 spreadsheet, column A through F, and export it as CSV
```

```
What parameters does the Calendar events.insert method accept? I want to create an event with a Google Meet link and specific attendees
```

```
Build a shell script that runs every morning: check unread email, show today's calendar, and list overdue tasks
```

```
Set up gws authentication with read-only scopes for Drive and Gmail -- I just need to read, not write
```

## Real-World Walkthrough

You are a team lead at a mid-size company and your mornings start the same way: open Gmail to scan for urgent messages, switch to Calendar to check what meetings are today, open Google Tasks to review what is due, then open the team's shared spreadsheet to check project status. By the time you have context on your day, 20 minutes have passed and you have not started any actual work.

You decide to automate this with `gws`. You start by asking Claude: **"Build me a morning triage script using gws that checks email, calendar, and tasks."**

Claude activates the gws-cli skill and produces a shell script:

```bash
#!/bin/bash
echo "=== UNREAD EMAIL (priority) ==="
gws gmail +triage

echo ""
echo "=== TODAY'S CALENDAR ==="
gws calendar +agenda --today

echo ""
echo "=== OPEN TASKS ==="
gws tasks tasks list --params '{"tasklist": "@default", "showCompleted": false}' \
  --format table
```

You run it and get a clean terminal output: 7 unread emails sorted by importance, 4 meetings today with times and attendees, and 5 open tasks with due dates. Morning context in 10 seconds instead of 20 minutes.

Next, you notice an email from a client asking for the latest project status. The data lives in a Google Sheet. You ask Claude: **"Read the status column from our project tracker spreadsheet and send it to the client."**

Claude composes two commands. First, read the spreadsheet:

```bash
gws sheets +read \
  --spreadsheet-id "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms" \
  --range "Projects!A1:D20" \
  --format table
```

This outputs the project names, statuses, owners, and due dates in a clean table. You review it, then send the email:

```bash
gws gmail +send \
  --to "client@acme.com" \
  --subject "Project Status Update - Week of April 7" \
  --body "Hi Sarah, here's the current project status:

Project Alpha: On Track (due April 15)
Project Beta: At Risk (blocked on API integration)
Project Gamma: Complete

Let me know if you have questions." \
  --cc "pm@mycompany.com"
```

Two commands replace: opening the spreadsheet, copying the data, opening Gmail, composing a message, pasting the data, and sending. And because it is all in the terminal, you can save it as a script and run it weekly.

Later, you need to schedule a design review meeting. You want to know what parameters the Calendar API accepts for creating events with Google Meet links. You ask Claude: **"What parameters do I need to create a Calendar event with a Meet link and specific attendees?"**

Claude runs `gws schema calendar.events.insert --resolve-refs` and explains the key parameters:

- `conferenceData` with `createRequest.requestId` to auto-generate a Meet link
- `attendees` array with email addresses and optional `responseStatus`
- `start` and `end` with `dateTime` in RFC 3339 format and `timeZone`
- `conferenceDataVersion=1` must be set in query params to enable Meet

Then Claude produces the ready-to-run command:

```bash
gws calendar +insert \
  --summary "Design Review: Dashboard Redesign" \
  --start "2026-04-14T14:00:00" \
  --end "2026-04-14T15:00:00" \
  --attendees "designer@mycompany.com,pm@mycompany.com,eng@mycompany.com" \
  --meet \
  --description "Review the new dashboard mockups. Figma link: https://..."
```

The `+insert` helper handles the conferenceData setup, attendee formatting, and timezone handling automatically. One command instead of clicking through the Calendar web UI, manually adding each attendee, enabling Meet, and typing the description.

By the end of the day, you have a morning triage script that runs in 10 seconds, a reusable status-report-and-email workflow, and a pattern for creating meetings from the terminal. You save the scripts in your dotfiles and share them with the team. The next morning, your triage takes 10 seconds instead of 20 minutes, and the team starts adopting the same patterns for their own workflows.

## Usage Scenarios

### Scenario 1: Morning email and calendar triage

**Context:** You start every day scanning email and calendar manually across two browser tabs. You want this in one terminal command.

**You say:** "Build a morning triage command that shows my unread emails, today's meetings, and overdue tasks"

**The skill provides:**
- `gws gmail +triage` for priority-sorted unread emails
- `gws calendar +agenda --today` for today's schedule
- `gws tasks tasks list` with filters for incomplete tasks
- A composable shell script combining all three

**You end up with:** A single script that gives you full morning context in under 10 seconds.

### Scenario 2: Automating a spreadsheet ETL pipeline

**Context:** Every week you manually copy data from one Google Sheet, transform it in Excel, and paste results into another sheet. You want to automate this.

**You say:** "Read data from the sales sheet, calculate totals by region, and write the summary to the dashboard sheet"

**The skill provides:**
- `gws sheets +read` with range notation and CSV output for extraction
- `jq` pipe for transformation (or Python script for complex logic)
- `gws sheets +append` for writing results back
- A complete shell script composing the pipeline

**You end up with:** A reusable ETL script that runs the entire pipeline in one command.

### Scenario 3: Discovering API parameters without reading docs

**Context:** You want to create a Calendar event with a specific recurrence pattern but do not know the parameter name or format.

**You say:** "What parameters does the Calendar API accept for recurring events?"

**The skill provides:**
- `gws schema calendar.events.insert --resolve-refs` output showing the `recurrence` field
- Explanation of RRULE format (`RRULE:FREQ=WEEKLY;BYDAY=MO,WE,FR`)
- Ready-to-run command with the recurrence parameter filled in
- Helper command alternative if available

**You end up with:** A working command for creating recurring events without having visited the Google Calendar API documentation.

### Scenario 4: Managing Drive files at scale

**Context:** Your shared Drive has accumulated hundreds of stale files. You need to find files not modified in 6 months and move them to an archive folder.

**You say:** "Find all Drive files older than 6 months and move them to the Archive folder"

**The skill provides:**
- `gws drive files list` with Drive query syntax: `modifiedTime < '2025-10-12T00:00:00'`
- `--page-all` for auto-pagination through large result sets
- `gws drive files update` with `addParents`/`removeParents` for moving files
- A shell script that lists, confirms, and moves in batch

**You end up with:** An automated cleanup script that finds and archives stale files without manual Drive UI browsing.

### Scenario 5: Setting up authentication for a new team member

**Context:** A new developer joins the team and needs to set up `gws` with appropriate scopes for their role (read-only access to Drive and Sheets, full access to Calendar).

**You say:** "Set up gws auth for a new developer with read-only Drive and Sheets but full Calendar access"

**The skill provides:**
- `gws auth setup` walkthrough for Google Cloud Project prerequisites
- Custom scope configuration: `gws auth login --scopes drive.readonly,sheets.readonly,calendar`
- Verification steps: `gws auth status` to confirm scopes
- Troubleshooting for common auth issues (expired tokens, missing scopes, scope upgrades)

**You end up with:** A properly authenticated `gws` installation with least-privilege scopes for the developer's role.

## Ideal For

- **Developers who live in the terminal** -- one CLI for all 18 Workspace APIs eliminates context-switching to browser UIs
- **Teams automating repetitive Workspace tasks** -- composable commands with pipes and scripts replace manual copy-paste workflows
- **Ops teams building internal automation** -- cross-service workflows (email + calendar + sheets + tasks) in shell scripts
- **Anyone who needs to discover API parameters quickly** -- `gws schema` replaces browsing Google's API documentation website
- **Power users managing shared Drives at scale** -- batch operations with auto-pagination and Drive query syntax

## Not For

- **Building MCP servers for Claude Code** -- this plugin teaches you to use the `gws` CLI, not to build protocol servers. Use [mcp-server](../mcp-server/) for MCP server development
- **General REST API design patterns** -- this is specific to Google Workspace APIs. Use [api-design](../api-design/) for general API design guidance
- **GCP infrastructure and cloud operations** -- use [cicd-pipelines](../cicd-pipelines/) for Terraform, cloud infrastructure, and CI/CD pipelines

## How It Works Under the Hood

The plugin is a single-skill architecture with a comprehensive SKILL.md (30,000+ words) and 3 reference files. The SKILL.md is structured around the `gws` CLI's own architecture:

1. **Quick Reference** -- command syntax patterns, global flags, services table, exit codes
2. **Authentication** -- OAuth setup, scope presets, credential storage, troubleshooting
3. **Schema Introspection** -- `gws schema` for parameter discovery without leaving the terminal
4. **Per-Service Sections** -- Drive, Gmail, Sheets, Calendar each with complete command reference, helper shortcuts, and worked examples
5. **Cross-Service Workflows** -- built-in workflow commands for common multi-service operations

The three reference files provide focused depth: `auth-and-setup.md` covers the full Google Cloud Project setup and OAuth configuration, `helper-commands.md` documents all `+` prefixed shortcuts, and `query-syntax.md` covers Drive query operators and Gmail search operators. The examples directory provides daily workflow scripts.

The `gws` CLI itself uses Google's Discovery Service to generate commands at runtime, which means the CLI stays current without updates. The plugin's SKILL.md teaches Claude how to compose these dynamically-generated commands with the correct syntax, flags, and parameters.

## Related Plugins

- **[API Design](../api-design/)** -- REST, GraphQL, gRPC, and Python library API design patterns
- **[MCP Server](../mcp-server/)** -- Build MCP servers in Python or TypeScript for Claude Code integration
- **[Workflow Automation](../workflow-automation/)** -- Workflow orchestration and release automation for multi-step processes
- **[CI/CD Pipelines](../cicd-pipelines/)** -- GitHub Actions, GitLab CI, and infrastructure as code

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
