# GWS CLI Daily Workflow Examples

## Morning Triage Routine

```bash
# 1. Check unread emails
gws gmail +triage

# 2. Review today's calendar
gws calendar +agenda --today

# 3. Check open tasks
gws tasks tasks list --params '{"tasklist": "@default"}'
```

## Standup Report

```bash
# One-command standup (meetings + tasks)
gws workflow +standup-report

# Or build custom standup:
# Today's meetings
gws calendar +agenda --today --format yaml

# Open tasks
gws tasks tasks list --params '{"tasklist": "@default"}' --format table
```

## Meeting Preparation

```bash
# Auto-prep for next meeting (attendees, agenda, linked docs)
gws workflow +meeting-prep

# Manual alternative:
# 1. Get next event details
gws calendar events list --params '{
  "calendarId": "primary",
  "timeMin": "2026-04-02T00:00:00Z",
  "maxResults": 1,
  "singleEvents": true,
  "orderBy": "startTime"
}'

# 2. Look up attendee details
gws people people get --params '{"resourceName": "people/PERSON_ID", "personFields": "names,emailAddresses,organizations"}'
```

## Email-to-Task Pipeline

```bash
# 1. Find actionable emails
gws gmail users messages list --params '{"userId": "me", "q": "is:unread label:action-required", "maxResults": 5}'

# 2. Read the email
gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'

# 3. Convert to task
gws workflow +email-to-task --message-id MSG_ID

# 4. Mark email as read
gws gmail users messages modify --params '{"userId": "me", "id": "MSG_ID"}' --json '{"removeLabelIds": ["UNREAD"]}'
```

## End-of-Day Digest

```bash
# Weekly summary
gws workflow +weekly-digest

# Or check remaining tasks
gws tasks tasks list --params '{"tasklist": "@default", "showCompleted": false}' --format table
```

## File Sharing Workflow

```bash
# 1. Find the file
FILE_ID=$(gws drive files list --params '{"q": "name = '\''Q1 Report'\'' and trashed = false", "pageSize": 1}' | jq -r '.files[0].id')

# 2. Share with a user
gws drive permissions create --params '{"fileId": "'$FILE_ID'"}' \
  --json '{"role": "commenter", "type": "user", "emailAddress": "reviewer@example.com"}'

# 3. Announce in Chat
gws workflow +file-announce --file-id "$FILE_ID" --space SPACE_ID --message "Q1 Report ready for review"

# 4. Notify via email
gws gmail +send --to "reviewer@example.com" --subject "Q1 Report shared" \
  --body "I've shared the Q1 Report with you. Please review by Friday."
```

## Sheets Data Pipeline

```bash
# 1. Create a tracking spreadsheet
SHEET_ID=$(gws sheets spreadsheets create --json '{"properties": {"title": "Daily Metrics"}}' | jq -r '.spreadsheetId')

# 2. Add headers
gws sheets +append --spreadsheet "$SHEET_ID" --values "Date,Metric,Value,Notes"

# 3. Append daily data
gws sheets +append --spreadsheet "$SHEET_ID" --values "2026-04-02,Signups,142,Above target"
gws sheets +append --spreadsheet "$SHEET_ID" --values "2026-04-02,Revenue,8500,On track"

# 4. Read back
gws sheets +read --spreadsheet "$SHEET_ID" --range 'A1:D10' --format table

# 5. Upload to Drive folder
gws drive files update --params '{"fileId": "'$SHEET_ID'", "addParents": "FOLDER_ID"}'
```

## Bulk Calendar Event Creation

```bash
# Create multiple events from a loop
for day in 07 08 09 10 11; do
  gws calendar +insert \
    --summary "Daily Standup" \
    --start "2026-04-${day}T09:00:00" \
    --end "2026-04-${day}T09:15:00" \
    --attendee "alice@example.com" \
    --attendee "bob@example.com" \
    --meet
done
```

## Search Across Services

```bash
# Find all traces of a project:

# 1. Emails about it
gws gmail users messages list --params '{"userId": "me", "q": "subject:project-phoenix", "maxResults": 10}'

# 2. Drive files
gws drive files list --params '{"q": "name contains '\''phoenix'\'' and trashed = false", "pageSize": 10}'

# 3. Tasks
gws tasks tasks list --params '{"tasklist": "@default"}' | jq '.items[] | select(.title | test("phoenix"; "i"))'

# 4. Calendar events
gws calendar events list --params '{"calendarId": "primary", "q": "phoenix", "timeMin": "2026-01-01T00:00:00Z", "singleEvents": true}'
```
