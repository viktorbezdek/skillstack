---
name: gws-cli
description: >-
  Google Workspace CLI (gws) for managing all 18 Workspace APIs from the terminal.
  Use when running gws commands, listing Drive files, sending Gmail, reading Sheets,
  creating Calendar events, managing Tasks, querying Chat, pushing Apps Script,
  building cross-service automations, or when user mentions gws or Google Workspace CLI.
  NOT for building MCP servers (use mcp-server), NOT for general API design (use api-design),
  NOT for GCP infrastructure (use cicd-pipelines).
---

# Google Workspace CLI (gws)

Single CLI for all 18 Google Workspace APIs. Commands built at runtime from Discovery Service.

## When to Use / Not Use

**Use when:**
- Running any `gws` command or asking about Google Workspace operations
- Working with Drive, Gmail, Sheets, Calendar, Docs, Slides, Tasks, Chat, People, Forms, Keep, Meet, Classroom, Events, Apps Script, Admin Reports, Model Armor
- Building cross-service workflows (standup reports, meeting prep, email-to-task)
- Introspecting API schemas to discover valid parameters

**Do NOT use when:**
- Building MCP servers -> use `mcp-server`
- General API design patterns -> use `api-design`
- GCP infrastructure (Compute Engine, Cloud Run) -> use `cicd-pipelines`

## Decision Tree

```
What Google Workspace operation do you need?
├── File/folder operations
│   ├── List/search files -> gws drive files list --params '{"q": "..."}'
│   ├── Upload file -> gws drive +upload ./file [--parent FOLDER_ID]
│   ├── Download/export -> gws drive files get --params '{"fileId": "ID", "alt": "media"}' --output ./file
│   └── Create folder -> gws drive files create --json '{"name": "X", "mimeType": "...folder"}'
├── Email
│   ├── Send email -> gws gmail +send --to X --subject Y --body Z
│   ├── Search inbox -> gws gmail users messages list --params '{"userId": "me", "q": "..."}'
│   ├── Reply/forward -> gws gmail +reply / +forward
│   └── Triage unread -> gws gmail +triage
├── Spreadsheets
│   ├── Read data -> gws sheets +read --spreadsheet ID --range 'Sheet1!A1:D10'
│   ├── Append data -> gws sheets +append --spreadsheet ID --values "A,B,C"
│   ├── Write/overwrite -> gws sheets spreadsheets values update
│   └── REMEMBER: single-quote ranges ('Sheet1!A1:C10') to avoid bash ! expansion
├── Calendar
│   ├── View agenda -> gws calendar +agenda --today/--week
│   ├── Create event -> gws calendar +insert --summary X --start T --end T
│   └── With Meet link -> add --meet flag to +insert
├── Tasks
│   ├── List task lists -> gws tasks tasklists list
│   ├── Create task -> gws tasks tasks insert --params '{"tasklist": "ID"}' --json '{...}'
│   └── Complete task -> gws tasks tasks patch ... --json '{"status": "completed"}'
├── Chat
│   └── Send message -> gws chat +send --space ID --text "message"
├── Cross-service workflow
│   ├── Morning standup -> gws workflow +standup-report
│   ├── Meeting prep -> gws workflow +meeting-prep
│   ├── Email to task -> gws workflow +email-to-task --message-id ID
│   └── Weekly digest -> gws workflow +weekly-digest
├── Unknown parameters?
│   └── Introspect first -> gws schema <service.resource.method> [--resolve-refs]
└── Other service (Docs, Slides, People, Forms, Script, Reports, Meet, Keep, Classroom, Events, ModelArmor)
    └── See references/command-reference.md for full examples
```

## Command Syntax

```
gws <service> <resource> [sub-resource] <method> [flags]
gws <service> +<helper> [flags]
gws schema <service.resource.method> [--resolve-refs]
gws auth <login|status|export|logout|setup>
```

## Global Flags

| Flag | Short | Description | Default |
|---|---|---|---|
| `--params <JSON>` | -- | URL/query parameters as JSON | -- |
| `--json <JSON>` | -- | Request body as JSON | -- |
| `--upload <PATH>` | -- | File to upload (multipart) | -- |
| `--upload-content-type <MIME>` | -- | MIME type override for upload | auto-detect |
| `--output <PATH>` | `-o` | Save binary response to file | stdout |
| `--format <FMT>` | -- | `json`, `table`, `yaml`, `csv` | `json` |
| `--api-version <VER>` | -- | Override API version | service default |
| `--dry-run` | -- | Validate locally, don't send | false |
| `--sanitize <TEMPLATE>` | -- | Model Armor template for response | -- |
| `--page-all` | -- | Auto-paginate (NDJSON output) | off |
| `--page-limit <N>` | -- | Max pages with `--page-all` | 10 |
| `--page-delay <MS>` | -- | Delay between pages (ms) | 100 |

## Services

| Service | Aliases | Key Helpers |
|---|---|---|
| `drive` | -- | `+upload`, `files list/get/create/update/delete` |
| `gmail` | -- | `+send`, `+reply`, `+triage`, `+watch` |
| `sheets` | -- | `+read`, `+append` |
| `calendar` | -- | `+agenda`, `+insert` |
| `docs` | -- | `+write` |
| `slides` | -- | `presentations get/create/batchUpdate` |
| `tasks` | -- | `tasklists list`, `tasks insert/list/patch` |
| `people` | -- | `searchContacts`, `createContact` |
| `chat` | -- | `+send`, `spaces messages list/create` |
| `classroom` | -- | `courses list/students/courseWork` |
| `forms` | -- | `forms get`, `responses list` |
| `keep` | -- | `notes list/get` |
| `meet` | -- | `conferenceRecords list/participants` |
| `events` | -- | `+subscribe`, `+renew` |
| `admin-reports` | `reports` | `activities list` |
| `script` | -- | `+push`, `scripts run` |
| `modelarmor` | -- | `+sanitize-prompt`, `+sanitize-response`, `+create-template` |
| `workflow` | `wf` | `+standup-report`, `+meeting-prep`, `+email-to-task`, `+weekly-digest`, `+file-announce` |

## Authentication

```bash
gws auth setup                    # Interactive setup (requires gcloud CLI)
gws auth login                    # Opens browser for OAuth
gws auth login -s drive,gmail     # Login with specific service scopes
gws auth login --readonly         # Read-only scopes
gws auth login --full             # All scopes including cloud-platform
gws auth status                   # Check credentials and scopes
```

**Auth precedence** (highest to lowest): `GOOGLE_WORKSPACE_CLI_TOKEN` env -> `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` env -> encrypted credentials from `gws auth login` -> plaintext `~/.config/gws/credentials.json`

**Credential storage:** AES-256-GCM encrypted at rest, key in OS keyring. Config dir: `~/.config/gws/`

### Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_WORKSPACE_CLI_TOKEN` | Pre-obtained OAuth2 access token |
| `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` | Path to credentials JSON |
| `GOOGLE_WORKSPACE_CLI_CLIENT_ID` | OAuth client ID |
| `GOOGLE_WORKSPACE_CLI_CLIENT_SECRET` | OAuth client secret |
| `GOOGLE_WORKSPACE_CLI_CONFIG_DIR` | Override config directory |
| `GOOGLE_WORKSPACE_CLI_KEYRING_BACKEND` | `keyring` (default) or `file` |
| `GOOGLE_WORKSPACE_CLI_LOG` | Log level (e.g., `gws=debug`) |
| `GOOGLE_WORKSPACE_CLI_LOG_FILE` | JSON log file directory |
| `GOOGLE_WORKSPACE_CLI_PROJECT_ID` | GCP project ID override |

## Schema Introspection

```bash
gws schema drive.files.list              # View method parameters and body schema
gws schema drive.files.list --resolve-refs  # Resolve all $ref types inline
gws schema drive.File                    # View a specific type definition
```

Use schema before constructing `--params` or `--json`, when a command fails, or for undocumented features.

## Exit Codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 1 | API error (4xx/5xx) |
| 2 | Auth error (missing/expired credentials) |
| 3 | Validation error (bad args, unknown service) |
| 4 | Discovery error (can't fetch schema) |
| 5 | Internal error |

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Missing `userId: "me"` in Gmail params | Gmail API requires userId; most common omission | Always include `"userId": "me"` in `--params` for Gmail methods |
| Double-quoting Sheets ranges | Bash expands `!` in double quotes as history expansion | Always single-quote: `'Sheet1!A1:C10'` |
| Forgetting `trashed = false` in Drive | `files.list` returns trashed files by default | Add `"q": "trashed = false"` unless you want trashed files |
| Binary download without `--output` | Binary content dumps to terminal (garbled) | Always add `--output ./file.pdf` for media downloads |
| Missing Chat API scope | 403 on chat commands even after auth | Chat requires explicit scope: `gws auth login --scopes "https://www.googleapis.com/auth/chat.messages"` |
| Guessing parameters instead of introspecting | Wrong param names cause exit code 3 | Run `gws schema <service.resource.method>` before constructing commands |

## Common Errors

| Error | Cause | Fix |
|---|---|---|
| `accessNotConfigured (403)` | API not enabled | Click `enable_url` in error output |
| `redirect_uri_mismatch` | Wrong OAuth client type | Recreate as "Desktop app" in Cloud Console |
| `Access blocked` | Test user not added | Add email under OAuth consent > Test users |
| Exit code 2 | Auth expired/missing | Run `gws auth login` |
| Exit code 3 | Bad params | Check `gws schema <method>` for valid params |
| Exit code 4 | Discovery fetch failed | Check network; retry (cached 24h) |

## Version Override / Any Google API

```bash
gws drive:v2 files list                    # Use Drive v2 instead of v3
gws youtube:v3 search list --params '...'  # Access ANY Google API, not just 18 listed
```

## Installation

```bash
npm install -g @googleworkspace/cli        # npm (recommended)
brew install googleworkspace-cli            # Homebrew
cargo install --git https://github.com/googleworkspace/cli --locked  # From source
gws --version                              # Verify
```

**Prerequisites:** Google Cloud project with OAuth credentials (Desktop app type), OAuth consent screen with test users, APIs enabled for desired services.

## Reference Directory

| Topic | Reference |
|---|---|
| Per-service command examples (all 18 services) | `references/command-reference.md` |
| Authentication and setup details | `references/auth-and-setup.md` |
| Helper commands (+send, +reply, etc.) | `references/helper-commands.md` |
| Per-service query syntax | `references/query-syntax.md` |
| Daily workflow examples | `examples/daily-workflows.md` |

## Integration

- **mcp-server** -- Build MCP servers that expose gws operations as agent tools
- **workflow-automation** -- Orchestrate multi-step automations including Workspace operations
- **cicd-pipelines** -- Use gws in CI/CD for automated Workspace operations
