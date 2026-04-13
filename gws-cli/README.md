# GWS CLI

> **v1.0.0** | Development | 1 iteration

> Manage all 18 Google Workspace APIs from the terminal -- Drive, Gmail, Sheets, Calendar, Docs, Chat, Tasks, and more -- with one dynamically-generated CLI that stays current without updates.

## The Problem

Google Workspace is the operational backbone of most organizations, yet interacting with it programmatically requires navigating 18 separate APIs, each with its own authentication flow, parameter formats, pagination patterns, and documentation. A developer who wants to automate a simple workflow -- "get today's calendar events and create a task for each one" -- must learn the Calendar API v3 event listing parameters, the Tasks API v1 task insertion format, handle OAuth2 scopes for both services, and write pagination logic twice with different token field names.

For AI agents, the problem is worse. When Claude needs to interact with Google Workspace on behalf of a user, it must construct raw API calls from memory, which means hallucinating parameter names, guessing at query syntax, and producing commands that fail silently or with cryptic error messages. Without a structured reference, agents waste turns on trial-and-error API construction.

The cost is measured in context switches. Developers flip between 18 different API reference pages, each with its own conventions for parameter naming, request body structure, and error codes. Common operations like "search Gmail for emails from Alice with attachments" require knowing Gmail's specific query syntax (`from:alice has:attachment`), which is different from Drive's query syntax (`name contains 'report'`), which is different from Calendar's time-range filtering pattern. There is no single interface that unifies these conventions.

## The Solution

This plugin teaches Claude how to use the `gws` CLI -- a single command-line interface for all 18 Google Workspace APIs. Commands are dynamically generated from Google's Discovery Service, so they stay current without CLI updates. The skill provides the complete reference: command syntax, global flags, authentication setup, per-service command examples (Drive, Gmail, Sheets, Calendar, Docs, Tasks, Chat, Slides, People, Forms, Apps Script, Admin Reports, Meet, Keep, Classroom, Events, Model Armor, Workflow), helper shortcuts for common operations, query syntax for each service, output formatting options, piping patterns, and troubleshooting guides.

The plugin ships one SKILL.md with the full CLI reference, 3 reference files (authentication and setup, helper commands, query syntax), 2 example files (daily workflows and an index), 13 trigger eval cases, and 3 output quality eval cases.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Navigate 18 separate API docs to find parameter names and query syntax | One CLI reference covering all 18 services with consistent command structure |
| OAuth2 setup requires separate scope configuration per service | Unified auth with scope presets: `gws auth login -s drive,gmail,sheets` |
| Query syntax differs per service (Gmail's `from:`, Drive's `name contains`, Calendar's `timeMin`) | Per-service query syntax documented with examples in one place |
| Pagination implemented differently per API (pageToken vs nextPageToken vs different field names) | `--page-all` flag handles pagination automatically across all services |
| Multi-service workflows require separate scripts per API | Cross-service `workflow` commands: standup report, meeting prep, email-to-task |
| Claude guesses at API parameters and fails silently | Claude has the complete `gws schema` introspection flow to discover valid parameters before constructing commands |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install gws-cli@skillstack
```

**Prerequisites:** The `gws` CLI must be installed separately:

```bash
npm install -g @googleworkspace/cli    # npm (recommended)
brew install googleworkspace-cli       # Homebrew
```

Then authenticate:

```bash
gws auth login -s drive,gmail,sheets,calendar,tasks
```

## Quick Start

1. Install the plugin and `gws` CLI using the commands above
2. Authenticate with `gws auth login`
3. Type: `List my 10 most recent Drive files`
4. Claude constructs: `gws drive files list --params '{"pageSize": 10, "q": "trashed = false"}'`
5. Next, try: `Send an email to alice@example.com with the subject "Weekly Update"`

---

## System Overview

```
User prompt (Google Workspace operation)
        |
        v
+------------------+     +-------------------------------+
|  gws-cli skill   |---->| Service routing               |
|  (SKILL.md)      |     | (18 services + workflow)      |
+------------------+     +-------------------------------+
        |                         |
        v                         v
  Command construction:     Reference files (3):
  - gws <service>            - auth-and-setup.md
    <resource> <method>       - helper-commands.md
    [--params] [--json]       - query-syntax.md
        |
        v                   Example files (2):
  Output formatting:        - daily-workflows.md
  --format json/table/      - INDEX.md
    yaml/csv
  --page-all
  --output <file>

  18 Services:
  drive | gmail | sheets | calendar | docs | slides
  tasks | people | chat | classroom | forms | keep
  meet | events | admin-reports | script | modelarmor | workflow
```

Single-skill plugin with 3 references and 2 example files. The skill contains the complete CLI reference for all 18 services plus the synthetic `workflow` service.

## What's Inside

| Component | Type | What It Provides |
|---|---|---|
| **gws-cli** | Skill | Complete CLI reference: command syntax, global flags, per-service examples, query syntax, troubleshooting |
| **auth-and-setup.md** | Reference | Authentication setup, OAuth2 configuration, scope presets, credential storage |
| **helper-commands.md** | Reference | Ergonomic `+` prefixed helper commands for common operations |
| **query-syntax.md** | Reference | Per-service query syntax (Drive `q`, Gmail search operators, Calendar time ranges) |
| **daily-workflows.md** | Example | Common daily workflow patterns |
| **INDEX.md** | Example | Example file index |
| **trigger-evals** | Eval | 13 trigger eval cases (8 positive, 5 negative) |
| **output-evals** | Eval | 3 output quality eval cases |

### Component Spotlights

#### gws-cli (skill)

**What it does:** Activates when you mention Google Workspace, `gws` CLI, Drive, Gmail, Sheets, Calendar, or any Workspace API operation. Provides the exact command syntax for any operation across 18 services, including authentication, schema introspection, query construction, output formatting, and cross-service workflows.

**Input -> Output:** You describe a Google Workspace operation in natural language -> The skill produces the exact `gws` command(s) with correct parameters, flags, and query syntax.

**When to use:**
- Listing, searching, creating, or modifying files in Google Drive
- Sending, searching, or triaging Gmail messages
- Reading or writing Google Sheets data
- Managing Calendar events (listing, creating, updating)
- Working with Docs, Slides, Tasks, Chat, Forms, Contacts, or any other Workspace service
- Building cross-service automations (email-to-task, standup reports, meeting prep)
- Introspecting API schemas to discover available parameters

**When NOT to use:**
- Building MCP servers -> use [mcp-server](../mcp-server/)
- General API design patterns -> use [api-design](../api-design/)
- GCP infrastructure (Compute Engine, Cloud Run, etc.) -> use [cicd-pipelines](../cicd-pipelines/)

**Try these prompts:**

```
List my unread Gmail messages from the last week with attachments
```

```
Create a Calendar event for tomorrow at 2pm with Alice and Bob, include a Google Meet link
```

```
Read the data from Sheet1 cells A1:D10 in my budget spreadsheet and show it as a table
```

```
Upload this report PDF to my Q2 folder in Drive
```

```
Run my morning standup: show today's calendar agenda and open tasks
```

**Key references:**

| Reference | Topic |
|---|---|
| `auth-and-setup.md` | OAuth2 setup, scope presets, credential storage, environment variables |
| `helper-commands.md` | `+send`, `+reply`, `+triage`, `+agenda`, `+upload`, `+read`, `+append` and more |
| `query-syntax.md` | Drive `q` parameter, Gmail search operators, Sheets range notation, Calendar time filters |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Check my email" | "List my 10 most recent unread Gmail messages with subject lines" |
| "What's on my calendar?" | "Show my calendar agenda for tomorrow with attendees and locations" |
| "Find a file" | "Search Drive for spreadsheets with 'budget' in the name modified in the last 30 days" |
| "Send a message" | "Send an email to team@example.com with subject 'Sprint Review' and attach ./report.pdf" |
| "Manage my tasks" | "Create a task 'Review PR #42' with due date April 15 in my Sprint 42 task list" |

### Structured Prompt Templates

**For Drive operations:**
```
[List / search / upload / download / share] [files / folders] in Drive. [Search criteria: name, type, date, owner]. [Output format: table / json / csv].
```

**For Gmail operations:**
```
[Send / reply / search / triage] [email]. To: [recipient]. Subject: [subject]. [Attachment: path]. [Search criteria: from, date, has attachment].
```

**For cross-service workflows:**
```
[Standup report / meeting prep / email-to-task / weekly digest]. [Any overrides: specific calendar, task list, time range].
```

### Prompt Anti-Patterns

- **Missing userId for Gmail:** Gmail methods require `"userId": "me"` in params -- Claude knows this from the skill but if you are constructing commands manually, this is the most common omission.
- **Using double quotes for Sheets ranges:** Shell interprets `!` in double quotes as history expansion. Always use single quotes: `'Sheet1!A1:C10'`.
- **Forgetting `trashed = false` for Drive:** `files.list` returns trashed files by default. Always add this filter unless you specifically want trashed files.

## Real-World Walkthrough

You are a project manager running a distributed team. Every morning you need to: check today's calendar, scan unread email for action items, and create tasks for anything requiring follow-up. Previously this meant opening three browser tabs and manually copying information between them.

**Step 1: Morning standup.** You ask Claude: **"Run my morning standup -- show today's calendar and open tasks."**

Claude constructs: `gws workflow +standup-report`. This cross-service command hits the Calendar API for today's events and the Tasks API for open items, returning a unified summary:

```
Today's Meetings (3):
- 09:00 Team Standup (Conference Room A)
- 11:00 1:1 with Alice (Google Meet)
- 14:00 Sprint Review (Conference Room B)

Open Tasks (5):
- Review PR #42 (due today)
- Update Q2 budget spreadsheet (due tomorrow)
- ...
```

**Step 2: Email triage.** You then ask: **"Show my unread emails from the last 24 hours."**

Claude constructs: `gws gmail users messages list --params '{"userId": "me", "q": "is:unread after:2026/04/11", "maxResults": 10}'`. You see 3 messages that need action.

**Step 3: Email to task.** For the most important email, you say: **"Convert this email to a task in my Sprint 42 list."**

Claude runs: `gws workflow +email-to-task --message-id MSG_ID --tasklist TASKLIST_ID`. The email subject becomes the task title, the email body becomes the task notes, and the task is created in the correct list.

**Step 4: Meeting prep.** Before your 11:00 meeting with Alice, you ask: **"Prep for my next meeting."**

Claude runs: `gws workflow +meeting-prep`. This fetches the next calendar event, lists attendees, and finds linked Drive documents attached to the event. You see: "1:1 with Alice -- Attendees: alice@example.com. Linked docs: Q2 OKR Review (Google Doc), Performance Dashboard (Google Sheet)."

**Step 5: Data update.** Finally, you need to update the budget spreadsheet. You ask: **"Append a new row to my budget spreadsheet: 'April, Marketing, 15000'."**

Claude constructs: `gws sheets +append --spreadsheet SHEET_ID --values "April,Marketing,15000"`. The row is added to the end of the sheet.

Your entire morning routine -- calendar check, email triage, task creation, meeting prep, and data update -- is completed through natural language commands without opening a single browser tab.

## Usage Scenarios

### Scenario 1: Automating daily email triage

**Context:** You receive 50+ emails daily and need to identify action items quickly without reading each one in the browser.

**You say:** "Triage my inbox -- show unread messages grouped by importance. Flag anything from my manager or with 'urgent' in the subject."

**The skill provides:**
- `gws gmail +triage` for the unread summary
- Search command with Gmail query syntax: `from:manager@company.com OR subject:urgent`
- Commands to apply labels or archive processed messages
- Option to convert flagged emails to tasks

**You end up with:** A triaged inbox where important messages are identified and action items are converted to tasks -- all from the terminal.

### Scenario 2: Building a reporting pipeline from Sheets data

**Context:** You have weekly metrics in a Google Sheet and need to read the data, process it, and distribute a summary.

**You say:** "Read the Q2 metrics from my 'Weekly KPIs' spreadsheet, Sheet1 rows A1:F52, and format as a table"

**The skill provides:**
- Exact read command with proper range notation (single-quoted for shell safety)
- Table formatting with `--format table`
- Piping to jq for data processing: `| jq '.values[] | select(.[2] > "1000")'`
- Command to append summary data back to a different sheet

**You end up with:** A pipeline that reads metrics, filters to interesting rows, and can write summaries back -- all composable with standard Unix pipes.

### Scenario 3: Cross-service meeting automation

**Context:** You host a weekly team meeting and want to automate the prep: pull the agenda doc, check who confirmed, and send a reminder email.

**You say:** "Prep for my weekly team meeting: get the agenda doc, list confirmed attendees, and send a reminder to anyone who hasn't responded"

**The skill provides:**
- Calendar event fetch with attendee response status
- Drive doc content retrieval for the linked agenda
- Gmail send command for the reminder, templated with attendee names
- Chain commands showing how to compose these into a single script

**You end up with:** A repeatable meeting prep script that runs in 30 seconds instead of 5 minutes of browser tab switching.

---

## Decision Logic

The skill routes requests to one of 18 services (plus the synthetic `workflow` service) based on the Google Workspace domain mentioned:

| You mention... | Service used | Common commands |
|---|---|---|
| Files, folders, Drive, upload, download | `drive` | `files list`, `files get`, `+upload` |
| Email, inbox, send, reply, Gmail | `gmail` | `users messages list`, `+send`, `+reply`, `+triage` |
| Spreadsheet, cells, rows, Sheets | `sheets` | `spreadsheets values get`, `+read`, `+append` |
| Calendar, events, meetings, agenda | `calendar` | `events list`, `+agenda`, `+insert` |
| Documents, Docs | `docs` | `documents get`, `+write` |
| Tasks, todo | `tasks` | `tasks list`, `tasks insert` |
| Chat, spaces, messages | `chat` | `spaces messages list`, `+send` |
| Standup, meeting prep, email-to-task | `workflow` | `+standup-report`, `+meeting-prep`, `+email-to-task` |

For unknown parameters, use `gws schema <service.resource.method>` to discover valid parameters before constructing commands.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Auth expired or missing scopes | Exit code 2, "credentials not found" or "insufficient scopes" | Run `gws auth login -s drive,gmail,sheets,calendar,tasks` with the required service scopes |
| Chat API scope missing | 403 on chat commands even after auth | Chat requires explicit `--scopes` flag: `gws auth login --scopes "https://www.googleapis.com/auth/chat.messages"`. Clear `~/.config/gws/token_cache.json` after scope changes |
| API not enabled in GCP project | 403 with `accessNotConfigured` | Click the `enable_url` in the error output to enable the API in your GCP project |
| Shell escaping for Sheets ranges | Bash expands `!` in double quotes | Always use single quotes for ranges: `'Sheet1!A1:C10'` |
| Binary download goes to terminal | Garbled output instead of file content | Add `--output ./file.pdf` for binary downloads; without it, binary content goes to stdout |

## Ideal For

- **Developers automating Workspace operations** who need a single CLI for all 18 APIs instead of separate scripts per service
- **AI agent builders** who need Claude to interact with Google Workspace reliably -- the skill provides the exact command syntax instead of hallucinated API calls
- **Project managers** who want terminal-based workflows for email triage, meeting prep, and task management
- **Data teams** who read from and write to Google Sheets programmatically as part of data pipelines

## Not For

- **Building MCP servers** that wrap Google APIs -- use [mcp-server](../mcp-server/) for server development
- **General API design patterns** -- use [api-design](../api-design/) for REST/GraphQL/gRPC design
- **GCP infrastructure** (Compute Engine, Cloud Run, Cloud Functions) -- use [cicd-pipelines](../cicd-pipelines/) for infrastructure

## Related Plugins

- **[MCP Server](../mcp-server/)** -- Build MCP servers that expose Google Workspace operations as agent tools
- **[API Design](../api-design/)** -- Design APIs that integrate with Google Workspace services
- **[Workflow Automation](../workflow-automation/)** -- Orchestrate multi-step automations that include Workspace operations
- **[CI/CD Pipelines](../cicd-pipelines/)** -- Automate Workspace operations in CI/CD pipelines

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
