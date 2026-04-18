# gws Command Reference — Per-Service Examples

Complete command examples for all 18 gws services. Use `gws schema <service.resource.method>` to discover parameters for any method not listed here.

## Drive

### Raw API Methods

```bash
# List files (10 most recent)
gws drive files list --params '{"pageSize": 10}'

# Search files by name
gws drive files list --params '{"q": "name contains '\''report'\'', "pageSize": 5}'

# Search by MIME type (spreadsheets only)
gws drive files list --params '{"q": "mimeType = '\''application/vnd.google-apps.spreadsheet'\'', "pageSize": 10}'

# Get file metadata
gws drive files get --params '{"fileId": "FILE_ID"}'

# Get file metadata with specific fields
gws drive files get --params '{"fileId": "FILE_ID", "fields": "id,name,mimeType,modifiedTime,size"}'

# Download file content
gws drive files get --params '{"fileId": "FILE_ID", "alt": "media"}' --output ./downloaded-file.pdf

# Export Google Doc as PDF
gws drive files export --params '{"fileId": "DOC_ID", "mimeType": "application/pdf"}' --output ./doc.pdf

# Create a folder
gws drive files create --json '{"name": "New Folder", "mimeType": "application/vnd.google-apps.folder"}'

# Move file to folder
gws drive files update --params '{"fileId": "FILE_ID", "addParents": "FOLDER_ID", "removeParents": "OLD_PARENT_ID"}'

# Delete file (trash)
gws drive files update --params '{"fileId": "FILE_ID"} ' --json '{"trashed": true}'

# Permanently delete
gws drive files delete --params '{"fileId": "FILE_ID"}'

# List shared drives
gws drive drives list

# List files in a shared drive
gws drive files list --params '{"driveId": "DRIVE_ID", "corpora": "drive", "includeItemsFromAllDrives": true, "supportsAllDrives": true}'
```

### Drive Helper

```bash
# Upload a file (auto-detects MIME type)
gws drive +upload ./report.pdf

# Upload to a specific folder
gws drive +upload ./report.pdf --parent FOLDER_ID

# Upload with custom name
gws drive +upload ./report.pdf --name "Q1 Report 2026.pdf"
```

### Drive Query Syntax (for `q` parameter)

| Operator | Example |
|---|---|
| `name contains 'X'` | Files with X in name |
| `name = 'X'` | Exact name match |
| `mimeType = 'X'` | Filter by type |
| `'EMAIL' in owners` | Files owned by user |
| `modifiedTime > '2026-01-01'` | Modified after date |
| `trashed = false` | Exclude trashed (default includes trashed!) |
| `'FOLDER_ID' in parents` | Files in specific folder |

Combine with `and`: `"name contains 'report' and mimeType = 'application/pdf' and trashed = false"`

### Common MIME Types

| Type | MIME |
|---|---|
| Google Doc | `application/vnd.google-apps.document` |
| Google Sheet | `application/vnd.google-apps.spreadsheet` |
| Google Slides | `application/vnd.google-apps.presentation` |
| Folder | `application/vnd.google-apps.folder` |
| PDF | `application/pdf` |

## Gmail

### Raw API Methods

```bash
# List messages (inbox)
gws gmail users messages list --params '{"userId": "me", "maxResults": 10}'

# Search messages
gws gmail users messages list --params '{"userId": "me", "q": "from:alice@example.com subject:report", "maxResults": 5}'

# Get message content
gws gmail users messages get --params '{"userId": "me", "id": "MESSAGE_ID"}'

# Get message in minimal format (just IDs and labels)
gws gmail users messages get --params '{"userId": "me", "id": "MESSAGE_ID", "format": "minimal"}'

# Get full message with raw MIME
gws gmail users messages get --params '{"userId": "me", "id": "MESSAGE_ID", "format": "raw"}'

# List labels
gws gmail users labels list --params '{"userId": "me"}'

# Apply label to message
gws gmail users messages modify --params '{"userId": "me", "id": "MESSAGE_ID"}' --json '{"addLabelIds": ["LABEL_ID"]}'

# Trash a message
gws gmail users messages trash --params '{"userId": "me", "id": "MESSAGE_ID"}'

# Get thread
gws gmail users threads get --params '{"userId": "me", "id": "THREAD_ID"}'

# List drafts
gws gmail users drafts list --params '{"userId": "me"}'
```

### Gmail Helpers

```bash
# Send an email
gws gmail +send --to "alice@example.com" --subject "Weekly Update" --body "Here is the update..."

# Send with CC and attachment
gws gmail +send --to "alice@example.com" --cc "bob@example.com" --bcc "log@example.com" \
  --subject "Report" --body "See attached." --attachment ./report.pdf

# Reply to a message (auto-threads)
gws gmail +reply --message-id MESSAGE_ID --body "Thanks for the update!"

# Reply with attachment
gws gmail +reply --message-id MESSAGE_ID --body "Here's the file." --attachment ./data.xlsx

# Reply all
gws gmail +reply-all --message-id MESSAGE_ID --body "Adding my thoughts..."

# Forward a message
gws gmail +forward --message-id MESSAGE_ID --to "manager@example.com" --body "FYI"

# Triage inbox (unread summary)
gws gmail +triage

# Watch for new emails (streams NDJSON)
gws gmail +watch --project my-gcp-project --topic my-topic
```

### Gmail Search Operators (for `q` parameter)

| Operator | Example |
|---|---|
| `from:` | `from:alice@example.com` |
| `to:` | `to:team@example.com` |
| `subject:` | `subject:weekly report` |
| `has:attachment` | Messages with attachments |
| `is:unread` | Unread messages |
| `is:starred` | Starred messages |
| `after:YYYY/MM/DD` | After date |
| `before:YYYY/MM/DD` | Before date |
| `label:` | `label:important` |
| `larger:5M` | Larger than 5MB |
| `filename:pdf` | Has PDF attachment |

Combine freely: `"from:alice@example.com subject:report after:2026/03/01 has:attachment"`

## Sheets

### Raw API Methods

```bash
# Get spreadsheet metadata
gws sheets spreadsheets get --params '{"spreadsheetId": "SHEET_ID"}'

# Get with specific fields
gws sheets spreadsheets get --params '{"spreadsheetId": "SHEET_ID", "fields": "sheets.properties.title,sheets.properties.sheetId"}'

# Read cell values
gws sheets spreadsheets values get --params '{"spreadsheetId": "SHEET_ID", "range": "Sheet1!A1:D10"}'

# Read values as table
gws sheets spreadsheets values get --params '{"spreadsheetId": "SHEET_ID", "range": "Sheet1!A1:D10"}' --format table

# Batch read multiple ranges
gws sheets spreadsheets values batchGet --params '{"spreadsheetId": "SHEET_ID", "ranges": ["Sheet1!A1:B5", "Sheet2!A1:C3"]}'

# Write values
gws sheets spreadsheets values update \
  --params '{"spreadsheetId": "SHEET_ID", "range": "Sheet1!A1", "valueInputOption": "USER_ENTERED"}' \
  --json '{"values": [["Name", "Score"], ["Alice", 95], ["Bob", 87]]}'

# Append values (add rows at end)
gws sheets spreadsheets values append \
  --params '{"spreadsheetId": "SHEET_ID", "range": "Sheet1!A1", "valueInputOption": "USER_ENTERED"}' \
  --json '{"values": [["Charlie", 92]]}'

# Create a new spreadsheet
gws sheets spreadsheets create --json '{"properties": {"title": "New Sheet"}}'

# Clear a range
gws sheets spreadsheets values clear --params '{"spreadsheetId": "SHEET_ID", "range": "Sheet1!A2:D100"}'
```

### Sheets Helpers

```bash
# Read values (simplified)
gws sheets +read --spreadsheet SHEET_ID --range 'Sheet1!A1:D10'

# Append a single row
gws sheets +append --spreadsheet SHEET_ID --values "Alice,95,Engineering"

# Append multiple rows (JSON)
gws sheets +append --spreadsheet SHEET_ID --json-values '[["Alice", 95], ["Bob", 87]]'

# Append to specific range
gws sheets +append --spreadsheet SHEET_ID --range 'Sheet1!A1' --values "Charlie,92,Marketing"
```

### Sheets Gotcha: Shell Escaping

Sheets ranges use `!` which bash interprets as history expansion. **Always use single quotes:**

```bash
# CORRECT
gws sheets +read --spreadsheet ID --range 'Sheet1!A1:C10'

# WRONG (bash expands !)
gws sheets +read --spreadsheet ID --range "Sheet1!A1:C10"
```

## Calendar

### Raw API Methods

```bash
# List calendars
gws calendar calendarList list

# List upcoming events (next 7 days)
gws calendar events list --params '{"calendarId": "primary", "timeMin": "2026-04-02T00:00:00Z", "timeMax": "2026-04-09T00:00:00Z", "singleEvents": true, "orderBy": "startTime"}'

# Get a specific event
gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'

# Create an event
gws calendar events insert --params '{"calendarId": "primary"}' --json '{
  "summary": "Team Standup",
  "location": "Conference Room A",
  "start": {"dateTime": "2026-04-03T09:00:00", "timeZone": "America/New_York"},
  "end": {"dateTime": "2026-04-03T09:30:00", "timeZone": "America/New_York"},
  "attendees": [{"email": "alice@example.com"}, {"email": "bob@example.com"}]
}'

# Update an event
gws calendar events patch --params '{"calendarId": "primary", "eventId": "EVENT_ID"}' \
  --json '{"summary": "Updated: Team Standup"}'

# Delete an event
gws calendar events delete --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'

# Quick add (natural language)
gws calendar events quickAdd --params '{"calendarId": "primary", "text": "Lunch with Alice tomorrow at noon"}'
```

### Calendar Helpers

```bash
# View today's agenda
gws calendar +agenda --today

# View tomorrow's agenda
gws calendar +agenda --tomorrow

# View this week
gws calendar +agenda --week

# View next N days
gws calendar +agenda --days 14

# View with timezone override
gws calendar +agenda --today --tz "Europe/Prague"

# Create an event (simplified)
gws calendar +insert --summary "Sprint Review" --start "2026-04-03T14:00:00" --end "2026-04-03T15:00:00"

# Create with attendees and Google Meet
gws calendar +insert --summary "1:1 with Alice" \
  --start "2026-04-03T10:00:00" --end "2026-04-03T10:30:00" \
  --attendee "alice@example.com" --meet

# Create with location and description
gws calendar +insert --summary "Offsite Planning" \
  --start "2026-04-05T09:00:00" --end "2026-04-05T17:00:00" \
  --location "WeWork, 5th Floor" --description "Q2 planning session"
```

## Docs

### Raw API Methods

```bash
# Get document content
gws docs documents get --params '{"documentId": "DOC_ID"}'

# Create a new document
gws docs documents create --json '{"title": "Meeting Notes"}'

# Update document content (batch update)
gws docs documents batchUpdate --params '{"documentId": "DOC_ID"}' --json '{
  "requests": [
    {
      "insertText": {
        "location": {"index": 1},
        "text": "Hello, World!\n"
      }
    }
  ]
}'
```

### Docs Helper

```bash
# Append text to end of document
gws docs +write --document DOC_ID --text "New section content here"
```

## Tasks

### Raw API Methods

```bash
# List task lists
gws tasks tasklists list

# List tasks in a list
gws tasks tasks list --params '{"tasklist": "TASKLIST_ID"}'

# Get a specific task
gws tasks tasks get --params '{"tasklist": "TASKLIST_ID", "task": "TASK_ID"}'

# Create a task
gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{
  "title": "Review PR #42",
  "notes": "Check test coverage",
  "due": "2026-04-05T00:00:00Z"
}'

# Complete a task
gws tasks tasks patch --params '{"tasklist": "TASKLIST_ID", "task": "TASK_ID"}' \
  --json '{"status": "completed"}'

# Delete a task
gws tasks tasks delete --params '{"tasklist": "TASKLIST_ID", "task": "TASK_ID"}'

# Create a new task list
gws tasks tasklists insert --json '{"title": "Sprint 42"}'
```

## Chat

### Raw API Methods

```bash
# List spaces
gws chat spaces list

# Get space details
gws chat spaces get --params '{"name": "spaces/SPACE_ID"}'

# List messages in a space
gws chat spaces messages list --params '{"parent": "spaces/SPACE_ID"}'

# Create a message
gws chat spaces messages create --params '{"parent": "spaces/SPACE_ID"}' \
  --json '{"text": "Hello from the CLI!"}'

# List members of a space
gws chat spaces members list --params '{"parent": "spaces/SPACE_ID"}'
```

### Chat Helper

```bash
# Send a message (simplified)
gws chat +send --space SPACE_ID --text "Deployment complete!"
```

## Slides

### Raw API Methods

```bash
# Get presentation
gws slides presentations get --params '{"presentationId": "PRES_ID"}'

# Get specific fields
gws slides presentations get --params '{"presentationId": "PRES_ID", "fields": "slides.objectId,slides.pageElements"}'

# Create presentation
gws slides presentations create --json '{"title": "Q2 Review"}'

# Batch update (add slide, insert text, etc.)
gws slides presentations batchUpdate --params '{"presentationId": "PRES_ID"}' --json '{
  "requests": [
    {"createSlide": {"insertionIndex": 1, "slideLayoutReference": {"predefinedLayout": "TITLE_AND_BODY"}}}
  ]
}'
```

## People (Contacts)

```bash
# List contacts
gws people people connections list --params '{"resourceName": "people/me", "personFields": "names,emailAddresses,phoneNumbers"}'

# Search contacts
gws people people searchContacts --params '{"query": "Alice", "readMask": "names,emailAddresses"}'

# Get current user profile
gws people people get --params '{"resourceName": "people/me", "personFields": "names,emailAddresses"}'

# Create a contact
gws people people createContact --json '{
  "names": [{"givenName": "Alice", "familyName": "Smith"}],
  "emailAddresses": [{"value": "alice@example.com"}]
}'
```

## Forms

```bash
# Get form
gws forms forms get --params '{"formId": "FORM_ID"}'

# List responses
gws forms forms responses list --params '{"formId": "FORM_ID"}'

# Get a specific response
gws forms forms responses get --params '{"formId": "FORM_ID", "responseId": "RESPONSE_ID"}'
```

## Apps Script

### Raw API Methods

```bash
# List script projects
gws script projects get --params '{"scriptId": "SCRIPT_ID"}'

# Get script content
gws script projects getContent --params '{"scriptId": "SCRIPT_ID"}'

# Create a new project
gws script projects create --json '{"title": "My Script"}'

# Update script content
gws script projects updateContent --params '{"scriptId": "SCRIPT_ID"}' --json '{
  "files": [
    {"name": "Code", "type": "SERVER_JS", "source": "function myFunction() { Logger.log(\"hello\"); }"},
    {"name": "appsscript", "type": "JSON", "source": "{\"timeZone\": \"America/New_York\", \"expirationDate\": \"2026-12-31\"}"}
  ]
}'

# Run a function
gws script scripts run --params '{"scriptId": "SCRIPT_ID"}' --json '{
  "function": "myFunction",
  "parameters": ["arg1", "arg2"]
}'
```

### Script Helper

```bash
# Push local files to Apps Script (replaces ALL files)
gws script +push --script SCRIPT_ID --dir ./my-script-project/
```

Uploads `.gs`, `.js`, `.html`, and `appsscript.json` files from the directory.

## Admin Reports

```bash
# List admin activities
gws admin-reports activities list --params '{"userKey": "all", "applicationName": "admin"}'

# List login activities
gws admin-reports activities list --params '{"userKey": "all", "applicationName": "login"}'

# List drive activities
gws admin-reports activities list --params '{"userKey": "all", "applicationName": "drive"}'

# Get usage report
gws admin-reports userUsageReport get --params '{"userKey": "all", "date": "2026-04-01"}'
```

## Meet

```bash
# List conference records
gws meet conferenceRecords list

# Get a specific conference
gws meet conferenceRecords get --params '{"name": "conferenceRecords/CONF_ID"}'

# List participants
gws meet conferenceRecords participants list --params '{"parent": "conferenceRecords/CONF_ID"}'
```

## Keep

```bash
# List notes
gws keep notes list

# Get a note
gws keep notes get --params '{"name": "notes/NOTE_ID"}'
```

## Classroom

```bash
# List courses
gws classroom courses list

# Get course details
gws classroom courses get --params '{"id": "COURSE_ID"}'

# List students
gws classroom courses students list --params '{"courseId": "COURSE_ID"}'

# List coursework
gws classroom courses courseWork list --params '{"courseId": "COURSE_ID"}'
```

## Events (Workspace Event Subscriptions)

### Event Helpers

```bash
# Subscribe to events (streams NDJSON)
gws events +subscribe --target "//docs.googleapis.com/documents/DOC_ID" \
  --event-types "google.workspace.documents.document.v1.updated" \
  --project my-gcp-project

# Renew expiring subscriptions
gws events +renew --all

# Renew specific subscription
gws events +renew --name "subscriptions/SUB_ID"
```

## Model Armor (Content Safety)

### Helpers

```bash
# Sanitize a prompt
gws modelarmor +sanitize-prompt --template "projects/P/locations/L/templates/T" --text "user input here"

# Sanitize from stdin
echo "user input" | gws modelarmor +sanitize-prompt --template "projects/P/locations/L/templates/T"

# Sanitize a model response
gws modelarmor +sanitize-response --template "projects/P/locations/L/templates/T" --text "model output"

# Create a template
gws modelarmor +create-template --project my-project --location us-central1 --template-id my-filter --preset basic

# Inline sanitization on any command
gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}' \
  --sanitize "projects/P/locations/L/templates/T"
```

## Workflow (Cross-Service)

The `workflow` (alias `wf`) service is synthetic -- no Discovery doc, only helper commands.

```bash
# Today's standup report (meetings + open tasks)
gws workflow +standup-report

# Meeting prep (agenda, attendees, linked docs for next meeting)
gws workflow +meeting-prep

# Convert email to task
gws workflow +email-to-task --message-id MSG_ID

# Convert email to task in specific list
gws workflow +email-to-task --message-id MSG_ID --tasklist TASKLIST_ID

# Weekly digest (this week's meetings + unread email count)
gws workflow +weekly-digest

# Announce a Drive file in Chat
gws workflow +file-announce --file-id FILE_ID --space SPACE_ID

# Announce with custom message
gws workflow +file-announce --file-id FILE_ID --space SPACE_ID --message "Please review by Friday"
```

## Piping and Composition

### Pipe gws output to jq

```bash
# Get file IDs and names
gws drive files list --params '{"pageSize": 5}' | jq '.files[] | {id, name}'

# Get unread message count
gws gmail users messages list --params '{"userId": "me", "q": "is:unread"}' | jq '.resultSizeEstimate'

# Extract event summaries
gws calendar +agenda --week | jq '.[].summary'
```

### Chain Commands

```bash
# Create a spreadsheet, then write to it
SHEET_ID=$(gws sheets spreadsheets create --json '{"properties": {"title": "Log"}}' | jq -r '.spreadsheetId')
gws sheets +append --spreadsheet "$SHEET_ID" --values "Timestamp,Event,Status"

# Find a file, then share it
FILE_ID=$(gws drive files list --params '{"q": "name = '\''Q1 Report'\'', "pageSize": 1}' | jq -r '.files[0].id')
gws drive permissions create --params '{"fileId": "'$FILE_ID'"}' --json '{"role": "reader", "type": "user", "emailAddress": "alice@example.com"}'
```

## Common Patterns

### Search then Act

```bash
# 1. Find the file
gws drive files list --params '{"q": "name contains '\''budget'\'' and mimeType = '\''application/vnd.google-apps.spreadsheet'\''", "pageSize": 1}'

# 2. Read its contents
gws sheets +read --spreadsheet FOUND_ID --range 'Sheet1!A1:Z100'

# 3. Append new data
gws sheets +append --spreadsheet FOUND_ID --values "2026-04-02,Marketing,15000"
```

### Email Workflow

```bash
# 1. Triage inbox
gws gmail +triage

# 2. Read specific message
gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'

# 3. Reply
gws gmail +reply --message-id MSG_ID --body "Done, see updated sheet."

# 4. Convert to task
gws workflow +email-to-task --message-id MSG_ID
```

### Meeting Preparation

```bash
# 1. Check today's agenda
gws calendar +agenda --today

# 2. Prep for next meeting
gws workflow +meeting-prep

# 3. Quick note to attendees
gws gmail +send --to "team@example.com" --subject "Meeting prep" --body "Pre-read: ..."
```

### Bulk Operations with Pagination

```bash
# List ALL files across pages
gws drive files list --params '{"pageSize": 100, "q": "trashed = false"}' --page-all --page-limit 50

# Process each page
gws drive files list --params '{"pageSize": 100}' --page-all | while read -r page; do
  echo "$page" | jq -r '.files[].name'
done
```

### Dry Run Before Execute

```bash
# Validate command locally first
gws calendar events insert --params '{"calendarId": "primary"}' \
  --json '{"summary": "Test", "start": {"dateTime": "2026-04-03T09:00:00Z"}, "end": {"dateTime": "2026-04-03T10:00:00Z"}}' \
  --dry-run

# If validation passes, remove --dry-run to execute
```
