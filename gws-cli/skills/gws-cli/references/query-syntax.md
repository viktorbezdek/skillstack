# GWS CLI Query Syntax Reference

## Drive Query Syntax (for `q` parameter)

Used with `gws drive files list --params '{"q": "..."}'`

### Operators

| Operator | Example | Description |
|---|---|---|
| `name contains 'X'` | `name contains 'report'` | Name includes substring |
| `name = 'X'` | `name = 'Budget 2026.xlsx'` | Exact name match |
| `fullText contains 'X'` | `fullText contains 'quarterly'` | Content search |
| `mimeType = 'X'` | `mimeType = 'application/pdf'` | Filter by MIME type |
| `'EMAIL' in owners` | `'alice@example.com' in owners` | Files owned by user |
| `'EMAIL' in writers` | `'bob@example.com' in writers` | Files writable by user |
| `'EMAIL' in readers` | `'team@example.com' in readers` | Files readable by user |
| `modifiedTime > 'DATE'` | `modifiedTime > '2026-01-01T00:00:00'` | Modified after date |
| `modifiedTime < 'DATE'` | `modifiedTime < '2026-04-01T00:00:00'` | Modified before date |
| `createdTime > 'DATE'` | `createdTime > '2026-03-01T00:00:00'` | Created after date |
| `trashed = false` | `trashed = false` | Exclude trashed files |
| `trashed = true` | `trashed = true` | Only trashed files |
| `starred = true` | `starred = true` | Only starred files |
| `'ID' in parents` | `'FOLDER_ID' in parents` | Files in folder |
| `sharedWithMe` | `sharedWithMe = true` | Shared with me |
| `visibility = 'anyoneCanFind'` | | Publicly discoverable |

### Combining Queries

Use `and`, `or`, `not`:

```
name contains 'report' and mimeType = 'application/pdf' and trashed = false
```

```
(name contains 'budget' or name contains 'forecast') and modifiedTime > '2026-01-01'
```

### Common MIME Types

| Type | MIME |
|---|---|
| Google Doc | `application/vnd.google-apps.document` |
| Google Sheet | `application/vnd.google-apps.spreadsheet` |
| Google Slides | `application/vnd.google-apps.presentation` |
| Google Form | `application/vnd.google-apps.form` |
| Folder | `application/vnd.google-apps.folder` |
| PDF | `application/pdf` |
| CSV | `text/csv` |
| JPEG | `image/jpeg` |
| PNG | `image/png` |

### Examples

```bash
# All PDFs modified this month
gws drive files list --params '{"q": "mimeType = '\''application/pdf'\'' and modifiedTime > '\''2026-04-01T00:00:00'\'' and trashed = false"}'

# All spreadsheets in a folder
gws drive files list --params '{"q": "'\''FOLDER_ID'\'' in parents and mimeType = '\''application/vnd.google-apps.spreadsheet'\''", "pageSize": 50}'

# Files shared with me containing "budget"
gws drive files list --params '{"q": "sharedWithMe = true and name contains '\''budget'\''", "pageSize": 10}'
```

---

## Gmail Search Syntax (for `q` parameter)

Used with `gws gmail users messages list --params '{"userId": "me", "q": "..."}'`

### Operators

| Operator | Example | Description |
|---|---|---|
| `from:` | `from:alice@example.com` | From sender |
| `to:` | `to:team@example.com` | To recipient |
| `cc:` | `cc:manager@example.com` | CC recipient |
| `bcc:` | `bcc:log@example.com` | BCC recipient |
| `subject:` | `subject:weekly report` | Subject contains |
| `has:attachment` | `has:attachment` | Has attachment |
| `filename:` | `filename:pdf` | Attachment filename |
| `is:unread` | `is:unread` | Unread messages |
| `is:read` | `is:read` | Read messages |
| `is:starred` | `is:starred` | Starred messages |
| `is:important` | `is:important` | Important messages |
| `is:snoozed` | `is:snoozed` | Snoozed messages |
| `in:inbox` | `in:inbox` | In inbox |
| `in:sent` | `in:sent` | In sent |
| `in:trash` | `in:trash` | In trash |
| `in:spam` | `in:spam` | In spam |
| `in:anywhere` | `in:anywhere` | All mail including spam/trash |
| `label:` | `label:work` | Has label |
| `after:` | `after:2026/03/01` | After date |
| `before:` | `before:2026/04/01` | Before date |
| `newer_than:` | `newer_than:7d` | Within last N days |
| `older_than:` | `older_than:1y` | Older than N years |
| `larger:` | `larger:5M` | Larger than size |
| `smaller:` | `smaller:1M` | Smaller than size |
| `{...}` or `OR` | `{from:alice from:bob}` | OR grouping |
| `-` | `-from:noreply` | Exclude |

### Examples

```bash
# Unread emails from specific sender this week
gws gmail users messages list --params '{"userId": "me", "q": "from:alice@example.com is:unread newer_than:7d"}'

# Emails with PDF attachments
gws gmail users messages list --params '{"userId": "me", "q": "has:attachment filename:pdf"}'

# Important emails about project
gws gmail users messages list --params '{"userId": "me", "q": "subject:project-alpha is:important after:2026/03/01"}'

# Emails from alice OR bob
gws gmail users messages list --params '{"userId": "me", "q": "{from:alice@example.com from:bob@example.com}"}'
```

---

## Calendar Query Notes

Calendar events don't use a `q` parameter. Instead, use time-range filters:

```bash
gws calendar events list --params '{
  "calendarId": "primary",
  "timeMin": "2026-04-01T00:00:00Z",
  "timeMax": "2026-04-30T23:59:59Z",
  "singleEvents": true,
  "orderBy": "startTime",
  "q": "standup"
}'
```

The `q` parameter for Calendar is a free-text search across event fields (summary, description, location).

---

## Sheets Range Notation

Used with `--range` parameter. Always use **single quotes** to prevent bash `!` expansion.

### Format

```
'SheetName!CellRange'
```

### Examples

| Range | Selects |
|---|---|
| `'Sheet1!A1'` | Single cell |
| `'Sheet1!A1:C10'` | Rectangular range |
| `'Sheet1!A:C'` | Entire columns A-C |
| `'Sheet1!1:5'` | Entire rows 1-5 |
| `'Sheet1'` | Entire sheet |
| `'A1:C10'` | First sheet, range A1:C10 |

### Named Ranges

Use named ranges directly: `'MyNamedRange'`
