# GWS Helper Commands Reference

Helper commands are ergonomic wrappers prefixed with `+` that never collide with Discovery API method names.

## Gmail Helpers

### `gws gmail +send`
Send an email with optional CC, BCC, and attachments.

| Flag | Required | Description |
|---|---|---|
| `--to` | yes | Recipient email |
| `--subject` | yes | Email subject |
| `--body` | yes | Email body text |
| `--cc` | no | CC recipient(s) |
| `--bcc` | no | BCC recipient(s) |
| `--attachment` | no | File path to attach |

### `gws gmail +reply`
Reply to a message (auto-threads).

| Flag | Required | Description |
|---|---|---|
| `--message-id` | yes | Message ID to reply to |
| `--body` | yes | Reply body text |
| `--attachment` | no | File path to attach |

### `gws gmail +reply-all`
Reply-all to a message.

| Flag | Required | Description |
|---|---|---|
| `--message-id` | yes | Message ID to reply to |
| `--body` | yes | Reply body text |
| `--attachment` | no | File path to attach |

### `gws gmail +forward`
Forward a message.

| Flag | Required | Description |
|---|---|---|
| `--message-id` | yes | Message ID to forward |
| `--to` | yes | Forward recipient |
| `--body` | no | Optional body text |

### `gws gmail +triage`
Show unread inbox summary: sender, subject, date.

No flags required.

### `gws gmail +watch`
Watch for new emails via Pub/Sub, stream as NDJSON.

| Flag | Required | Description |
|---|---|---|
| `--project` | yes | GCP project ID |
| `--topic` | yes | Pub/Sub topic name |
| `--subscription` | no | Pub/Sub subscription name |
| `--labels` | no | Filter by label IDs |
| `--once` | no | Exit after first message |
| `--cleanup` | no | Delete subscription on exit |
| `--no-ack` | no | Don't acknowledge messages |
| `--poll-interval` | no | Poll interval in seconds |
| `--max-messages` | no | Max messages per pull |

---

## Calendar Helpers

### `gws calendar +agenda`
Show upcoming events across all calendars.

| Flag | Required | Description |
|---|---|---|
| `--today` | no | Today's events |
| `--tomorrow` | no | Tomorrow's events |
| `--week` | no | This week's events |
| `--days <N>` | no | Next N days |
| `--calendar` | no | Specific calendar ID |
| `--timezone` / `--tz` | no | Override timezone |

### `gws calendar +insert`
Create a new calendar event.

| Flag | Required | Description |
|---|---|---|
| `--summary` | yes | Event title |
| `--start` | yes | Start datetime (ISO 8601) |
| `--end` | yes | End datetime (ISO 8601) |
| `--calendar` | no | Calendar ID (default: primary) |
| `--location` | no | Event location |
| `--description` | no | Event description |
| `--attendee` | no | Attendee email (repeatable) |
| `--meet` | no | Attach Google Meet link |

---

## Drive Helpers

### `gws drive +upload`
Upload a file with auto MIME detection.

| Flag | Required | Description |
|---|---|---|
| `<file>` | yes | File path (positional) |
| `--parent` | no | Parent folder ID |
| `--name` | no | Override file name |

---

## Sheets Helpers

### `gws sheets +read`
Read values from a spreadsheet.

| Flag | Required | Description |
|---|---|---|
| `--spreadsheet` | yes | Spreadsheet ID |
| `--range` | yes | Cell range (e.g., `'Sheet1!A1:C10'`) |

### `gws sheets +append`
Append row(s) to a spreadsheet.

| Flag | Required | Description |
|---|---|---|
| `--spreadsheet` | yes | Spreadsheet ID |
| `--values` | no | Comma-separated values for single row |
| `--json-values` | no | JSON array(s) for single or multi row |
| `--range` | no | Target range (default: A1) |

---

## Docs Helpers

### `gws docs +write`
Append text to end of document body.

| Flag | Required | Description |
|---|---|---|
| `--document` | yes | Document ID |
| `--text` | yes | Text to append |

---

## Chat Helpers

### `gws chat +send`
Send a plain text message to a space.

| Flag | Required | Description |
|---|---|---|
| `--space` | yes | Space ID |
| `--text` | yes | Message text |

---

## Script Helpers

### `gws script +push`
Upload local files to an Apps Script project. Replaces ALL files.

| Flag | Required | Description |
|---|---|---|
| `--script` | yes | Script project ID |
| `--dir` | no | Directory to upload from |

Uploads `.gs`, `.js`, `.html`, and `appsscript.json`.

---

## Events Helpers

### `gws events +subscribe`
Subscribe to Workspace events, stream as NDJSON.

| Flag | Required | Description |
|---|---|---|
| `--target` | yes | Target resource (e.g., `//docs.googleapis.com/documents/DOC_ID`) |
| `--event-types` | yes | Event type(s) |
| `--project` | yes | GCP project ID |
| `--subscription` | no | Pub/Sub subscription name |
| `--max-messages` | no | Max messages per pull |
| `--poll-interval` | no | Poll interval |
| `--once` | no | Exit after first event |
| `--cleanup` | no | Cleanup on exit |
| `--no-ack` | no | Don't acknowledge |
| `--output-dir` | no | Save events to files |

### `gws events +renew`
Renew expiring subscriptions.

| Flag | Required | Description |
|---|---|---|
| `--name` | no | Specific subscription name |
| `--all` | no | Renew all subscriptions |
| `--within` | no | Renew if expiring within duration |

---

## Workflow Helpers (Cross-Service)

### `gws workflow +standup-report`
Today's meetings + open tasks as standup summary.

| Flag | Required | Description |
|---|---|---|
| `--format` | no | Output format |

### `gws workflow +meeting-prep`
Prepare for next meeting: agenda, attendees, linked docs.

| Flag | Required | Description |
|---|---|---|
| `--calendar` | no | Calendar ID |
| `--format` | no | Output format |

### `gws workflow +email-to-task`
Convert a Gmail message into a Google Tasks entry.

| Flag | Required | Description |
|---|---|---|
| `--message-id` | yes | Gmail message ID |
| `--tasklist` | no | Target task list ID |

### `gws workflow +weekly-digest`
Weekly summary: this week's meetings + unread email count.

| Flag | Required | Description |
|---|---|---|
| `--format` | no | Output format |

### `gws workflow +file-announce`
Announce a Drive file in a Chat space.

| Flag | Required | Description |
|---|---|---|
| `--file-id` | yes | Drive file ID |
| `--space` | yes | Chat space ID |
| `--message` | no | Custom announcement text |
| `--format` | no | Output format |

---

## Model Armor Helpers

### `gws modelarmor +sanitize-prompt`
Sanitize user prompt through Model Armor template.

| Flag | Required | Description |
|---|---|---|
| `--template` | yes | Model Armor template resource name |
| `--text` | no | Text to sanitize (or use `--json` or stdin) |
| `--json` | no | JSON input |

### `gws modelarmor +sanitize-response`
Sanitize model response through Model Armor template.

Same flags as `+sanitize-prompt`.

### `gws modelarmor +create-template`
Create a new Model Armor template.

| Flag | Required | Description |
|---|---|---|
| `--project` | yes | GCP project ID |
| `--location` | yes | GCP location |
| `--template-id` | yes | Template ID |
| `--preset` | no | Preset name (e.g., `basic`) |
| `--json` | no | Custom template JSON |
