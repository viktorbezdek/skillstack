## Status Cards Specification

Status cards are formatted messages posted to work tracking systems (GitHub, Jira, Linear) to communicate the progress of FABER workflows.

### Format

Status cards follow a consistent markdown format:

```markdown
**FABER** {emoji} Stage: {stage_name}

{status_message}

**Options:**
- `option1`
- `option2`
- `option3`

```yaml
session: {session_id}
stage: {stage_name}
timestamp: {iso8601_timestamp}
```
```

### Stage Emojis

- 📋 **Frame**: Work item fetched and classified
- 📐 **Architect**: Specification generated
- 🔨 **Build**: Implementation in progress
- 🧪 **Evaluate**: Testing and review
- 🚀 **Release**: Deployment and PR creation

### Options

Options represent available actions the user can take in response to a status card:

**Frame Stage:**
- `proceed` - Continue to Architect stage
- `cancel` - Cancel the workflow

**Architect Stage:**
- `proceed` - Continue to Build stage
- `revise` - Regenerate specification
- `cancel` - Cancel the workflow

**Build Stage:**
- `proceed` - Continue to Evaluate stage
- `cancel` - Cancel the workflow

**Evaluate Stage:**
- `ship` - Proceed to Release stage
- `hold` - Pause for manual review
- `retry` - Re-run Build stage
- `reject` - Cancel the workflow

**Release Stage:**
- `merge` - Merge the pull request
- `hold` - Keep PR open for review
- `close` - Close PR without merging

### Metadata

The YAML block contains:
- `session`: Work/session identifier
- `stage`: Current FABER stage
- `timestamp`: ISO8601 UTC timestamp
- Optional fields based on configuration

### Configuration

Status cards can be configured in `.faber.config.toml`:

```toml
[notifications]
post_status_cards = true
status_card_style = "detailed"  # detailed | minimal
include_session_metadata = true
```

### Usage

Status cards are posted automatically by the `director` at key transition points in the workflow. Manual posting is also supported via `status-card-post.sh` script.
