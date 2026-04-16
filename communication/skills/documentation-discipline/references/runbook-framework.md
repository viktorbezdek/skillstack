# Runbook Framework

A runbook is a step-by-step document for an operational task. It assumes the reader is competent but has never done this specific thing before. The discipline: every step has an expected result; every runbook has an owner; rollback is never "figure it out."

## Runbook anatomy

```markdown
# Runbook: [operation name]

**Owner:** [name / team]
**Last reviewed:** YYYY-MM-DD
**Next review:** YYYY-MM-DD
**Related:** [ADRs, other runbooks, dashboards]

## When to run this
[Trigger conditions — what event or schedule prompts this runbook?]

## Impact
[What changes in the system when this runs. Who notices.]

## Prerequisites
- [ ] [Access / permission needed]
- [ ] [Tool / CLI needed]
- [ ] [Other runbook that must have been run first]
- [ ] [Context the runner must understand]

## Steps

### 1. [Step name]
**Action:** [Exact command or action]
**Expected result:** [What you should see — screenshot, output, metric change]
**If this fails:** [Go to Troubleshooting section X, or 'stop here']

### 2. [Step name]
**Action:** ...
**Expected result:** ...
**If this fails:** ...

## Verification
- [ ] [Check 1 — readable signal that the operation succeeded]
- [ ] [Check 2]
- [ ] [Check 3]

## Rollback
[Step by step undo. If irreversible, state "irreversible after step N" and what
 validates before proceeding.]

## Troubleshooting
- **Symptom:** [what you see]
  - **Fix:** [what to do]
- **Symptom:** [what you see]
  - **Escalate:** [to whom, via what channel]

## Changelog
- YYYY-MM-DD: [what changed] — @author
- YYYY-MM-DD: [what changed] — @author
```

## Core rules

### 1. Every step has an expected result

A step without expected result is a wish. "Run `kubectl apply -f ...`" is incomplete. "Run `kubectl apply -f ...` — expected: `configured` output for each resource, pods become `Running` within 60 seconds" is a step.

The expected result is how a novice runner knows they're on track. Without it, the first sign of trouble is a failure several steps later.

### 2. Rollback is non-negotiable

Every runbook has either:
- A rollback section with explicit steps, OR
- An explicit note "Irreversible after step N" and what validates before step N.

Runbooks without rollback decay into crisis improvisation.

### 3. Owner, not orphan

Every runbook has a named owner — individual or team. The owner is responsible for:
- Accuracy (the steps still work)
- Review cadence (last reviewed within the declared window)
- Deprecation (when the operation changes, update the runbook)

Orphan runbooks are worse than no runbook — they mislead.

### 4. Review date visible

Every runbook shows last-reviewed AND next-review dates. Beyond the next-review date, the runbook is considered stale until re-validated.

| Volatility | Review cadence |
|---|---|
| High (changes monthly) | Every 3 months |
| Medium (changes quarterly) | Every 6 months |
| Low (changes yearly or less) | Every 12 months |

### 5. Changelog at the bottom

Track edits. When something goes wrong during a run, the changelog helps trace whether a recent edit caused the issue.

## Worked example

```markdown
# Runbook: Weekly Database Backup Verification

**Owner:** @data-platform-team (primary: @alex)
**Last reviewed:** 2026-03-10
**Next review:** 2026-06-10
**Related:** ADR-0003 (PostgreSQL primary datastore), [Backup dashboard](link)

## When to run this
Every Monday at 9am PT. Triggered by the weekly schedule in Ops calendar.
Also run after any incident that touched the backup pipeline.

## Impact
No user-facing impact. Generates an audit log entry and may page oncall
if a backup is found inconsistent.

## Prerequisites
- [ ] Access to `backup-ops` IAM role
- [ ] AWS CLI configured with `skillstack-prod` profile
- [ ] pg_restore 16 installed locally
- [ ] Understand what "WAL archive completeness" means (see ADR-0003)

## Steps

### 1. Pull latest backup manifest
**Action:** `aws s3 ls s3://skillstack-backups/weekly/ --recursive | tail -1`
**Expected result:** Lists a manifest file dated within the last 7 days.
**If this fails:** Backup pipeline may be broken — go to Troubleshooting "Missing backup."

### 2. Download manifest and verify checksum
**Action:**
```
aws s3 cp s3://skillstack-backups/weekly/YYYY-MM-DD/manifest.json ./
sha256sum manifest.json  # compare against s3://skillstack-backups/weekly/YYYY-MM-DD/manifest.json.sha256
```
**Expected result:** Checksums match exactly.
**If this fails:** Manifest corrupted — escalate to @data-platform-team.

### 3. Restore manifest to verification instance
**Action:** `./scripts/restore-to-verify.sh YYYY-MM-DD`
**Expected result:** Instance `backup-verify-YYYYMMDD` starts; pg_restore completes in under 45 minutes; no errors in `/var/log/restore.log`.
**If this fails:** Check CloudWatch for instance start errors. If pg_restore fails, attach log to an incident ticket.

### 4. Run row-count check
**Action:** `psql -h backup-verify-YYYYMMDD -f ./scripts/row-counts.sql`
**Expected result:** Counts within 0.5% of production for all checked tables (users, orders, line_items, events_last_7d).
**If this fails:** Backup data is inconsistent — page oncall immediately.

### 5. Cleanup verification instance
**Action:** `./scripts/teardown-verify.sh YYYY-MM-DD`
**Expected result:** Instance and EBS volumes deleted; confirmation in output.
**If this fails:** Manual cleanup in AWS Console. Open a ticket to investigate.

## Verification
- [ ] Row-count check passed for all 4 tables
- [ ] `/var/log/restore.log` has no ERROR lines
- [ ] Verification instance deleted (check EC2 console)
- [ ] Audit entry created in `backup_verifications` table

## Rollback
No rollback needed — this operation is read-only on production. The verify
instance is ephemeral. If the runbook is aborted mid-run, rerun from step 5
to clean up the verification instance.

## Troubleshooting

### Symptom: Missing backup (step 1 shows no recent file)
Check backup cron on `backup-orchestrator` instance. If cron is healthy
but no backup exists, backups are broken — page oncall and open a SEV-2
incident.

### Symptom: pg_restore fails with "unsupported extension"
Our PG 16 upgrade changed extension versions. Check if backup was taken
before PG 16 upgrade (see ADR-0015). If yes, use the legacy restore path:
`./scripts/restore-legacy.sh`.

### Symptom: Row-count check exceeds 0.5% threshold
Most common cause: backup was taken mid-transaction. Re-run the verification
on the next day's backup. If drift persists across two consecutive backups,
escalate to @data-platform-team — this is a real data consistency issue.

## Changelog
- 2026-03-10: Added PG 16 extension troubleshooting — @alex
- 2025-12-05: Increased row-count threshold from 0.1% to 0.5% after noisy alerts — @alex
- 2025-09-22: Initial version — @alex
```

## Runbook rot — how they decay

Runbooks decay in predictable patterns. Watch for:

1. **Commands that don't work anymore.** Infrastructure changed; the runbook didn't.
2. **Expected results that don't match reality.** Outputs shifted due to tool upgrades.
3. **Dead links.** Linked dashboards, ADRs, or tickets removed or moved.
4. **Missing owner.** The original owner left; nobody claimed it.
5. **Stale review dates.** Last reviewed 18 months ago; nobody has re-validated.

Defense:
- **Quarterly rot review** — walk through each runbook's prerequisites and step 1 to verify it still works.
- **Game-day exercises** — run the runbook as a drill before you need it under pressure.
- **Dry-run flag** — runbooks that support `--dry-run` let runners validate without making changes.

## Game-day exercises

For high-stakes runbooks (incident response, disaster recovery, critical ops):

1. Schedule a calendar day every quarter or half-year.
2. Walk through the runbook with a fresh runner (not the author).
3. Capture:
   - Steps that are unclear or missing.
   - Prerequisites that were wrong or out of date.
   - Commands that failed.
   - Expected results that didn't match.
4. Update the runbook within 24 hours of the exercise.

Game-days are expensive but pay back on the first real incident.

## Common mistakes

- **Steps without expected results.** Unverifiable, so decay is silent.
- **Rollback as "undo the changes."** Vague. Needs explicit commands.
- **Single points of failure in the runbook itself.** "If you see X, ask Alex" — Alex is on vacation; now what?
- **Running the runbook from memory.** The runbook is the source of truth; anyone running from memory is not using the runbook.
- **Not checking in changes.** Edits made during a run must be captured and committed. Otherwise the next runner sees stale steps.
- **Mixing context and steps.** Background belongs in Context or linked ADRs, not interleaved with steps.
- **Over-abstracted steps.** "Deploy the service." Which service? Which command? Be explicit.
