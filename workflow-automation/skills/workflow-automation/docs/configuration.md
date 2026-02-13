# FABER Configuration Reference

Complete reference for `.faber.config.toml` configuration file.

## Quick Start

```bash
# Copy example configuration
cp plugins/fractary-faber/config/faber.example.toml .faber.config.toml

# Or use init command (/fractary-faber:init) command
/fractary-faber:init
```

## Configuration Sections

### [project]

Project-level settings.

```toml
[project]
name = "my-project"              # Project name
issue_system = "github"          # Issue tracker: github | jira | linear | manual
source_control = "github"        # Source control: github | gitlab | bitbucket
file_system = "r2"               # File storage: r2 | s3 | local
```

### [auth]

Authentication credentials. Use `env:VAR_NAME` to read from environment variables.

```toml
[auth]
ISSUE_TOKEN = "env:GITHUB_TOKEN"          # Issue tracker auth
GIT_TOKEN = "env:GITHUB_TOKEN"            # Git auth
CI_TOKEN = "env:GITHUB_TOKEN"             # CI system auth
FILE_STORAGE_TOKEN = "env:R2_TOKEN"       # Storage auth
```

### [defaults]

Default workflow settings.

```toml
[defaults]
preset = "software-guarded"                    # Workflow preset
autonomy = "guarded"                           # Autonomy level
branch_naming = "feat/{issue_id}-{slug}"       # Branch naming pattern
```

**Autonomy Levels:**
- `dry-run`: Simulate only, make no changes
- `assist`: Open PRs/drafts, never merge/deploy
- `guarded`: Proceed until gates, pause for approvals (recommended)
- `autonomous`: No pauses, full automation

**Branch Naming Variables:**
- `{issue_id}`: External issue ID
- `{work_id}`: FABER work ID
- `{slug}`: URL-friendly title slug
- `{work_type}`: Work type (feature, bug, chore, patch)

### [director]

Director agent configuration.

```toml
[director]
type = "default"                               # default | custom
agent_ref = "agents/faber-director.md"         # Agent file path
model = "claude-3.7"                           # AI model
max_tokens = 4096                              # Max response tokens
```

### [safety]

Safety and protection settings.

```toml
[safety]
protected_paths = [
    "secrets/**",
    "infra/prod/**",
    ".env*"
]
require_confirm_for = ["release", "deploy", "tag", "merge_to_main"]
```

### [workflow]

Workflow behavior settings.

```toml
[workflow]
max_evaluate_retries = 3           # Max Build-Evaluate retry loops
auto_merge = false                 # Auto-merge PRs after Evaluate
auto_close_work_item = false       # Auto-close issues after Release
```

### [systems.work_config]

Work tracking system configuration (varies by `issue_system`).

**GitHub:**
```toml
[systems.work_config]
repo = "owner/repo"
api_url = "https://api.github.com"
labels_feature = ["feature", "enhancement"]
labels_bug = ["bug", "fix"]
labels_chore = ["chore", "maintenance"]
labels_patch = ["patch", "hotfix"]
```

**Jira:**
```toml
[systems.work_config]
jira_url = "https://your-domain.atlassian.net"
jira_project = "PROJ"
```

**Linear:**
```toml
[systems.work_config]
linear_team = "your-team"
linear_workspace = "your-workspace"
```

### [systems.repo_config]

Repository configuration.

```toml
[systems.repo_config]
default_branch = "main"
protected_branches = ["main", "master", "production"]
require_signed_commits = false
```

### [systems.file_config]

File storage configuration (varies by `file_system`).

**Cloudflare R2:**
```toml
[systems.file_config]
account_id = "your-account-id"
bucket_name = "faber-artifacts"
public_url = "https://your-bucket.r2.dev"
```

**AWS S3:**
```toml
[systems.file_config]
s3_bucket = "your-bucket"
s3_region = "us-east-1"
s3_endpoint = ""  # Optional: for S3-compatible services
```

**Local:**
```toml
[systems.file_config]
local_storage_path = ".faber/artifacts"
```

### [session] (DEPRECATED in v2.0)

**NOTE:** Session management has been replaced by state management in FABER v2.0.

In v2.0, workflow state is stored in `.fractary/plugins/faber/state.json` instead of per-work-id session files. This provides:
- Single source of truth for current workflow
- Simpler state management
- Better integration with fractary-logs plugin for historical tracking

For v2.0 configuration, see the main FABER configuration documentation.

### [notifications]

Notification and status card settings.

```toml
[notifications]
post_status_cards = true
status_card_style = "detailed"  # detailed | minimal
include_session_metadata = true

notify_on_frame = true
notify_on_architect = true
notify_on_build = true
notify_on_evaluate = true
notify_on_release = true
notify_on_error = true
```

### [logging]

Logging configuration.

```toml
[logging]
log_level = "info"  # debug | info | warn | error
log_file = ".faber/logs/faber.log"
log_rotation = "daily"
max_log_size_mb = 100
```

## Presets

Presets provide predefined configuration bundles.

### software-basic

Minimal workflow with no gates.

```toml
[presets.software-basic]
autonomy = "assist"
auto_merge = false
max_evaluate_retries = 2
require_confirm_for = []
```

### software-guarded

Workflow with approval gates (recommended).

```toml
[presets.software-guarded]
autonomy = "guarded"
auto_merge = false
max_evaluate_retries = 3
require_confirm_for = ["release", "deploy"]
protected_paths = ["secrets/**", "infra/prod/**"]
```

### software-autonomous

Fully autonomous workflow.

```toml
[presets.software-autonomous]
autonomy = "autonomous"
auto_merge = true
max_evaluate_retries = 3
require_confirm_for = []
auto_close_work_item = true
```

## Environment Variables

Recommended environment variables:

```bash
# GitHub
export GITHUB_TOKEN="ghp_..."

# Jira
export JIRA_TOKEN="..."
export JIRA_EMAIL="user@example.com"

# Linear
export LINEAR_API_KEY="lin_..."

# Cloudflare R2
export R2_ACCESS_KEY_ID="..."
export R2_SECRET_ACCESS_KEY="..."
export R2_ACCOUNT_ID="..."

# AWS S3
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
```

## Validation

Configuration is validated when loaded by `config-loader.sh`. Required fields:
- `project.name`
- `project.issue_system`
- `project.source_control`
- `project.file_system`

## Examples

### Minimal Configuration

```toml
[project]
name = "my-app"
issue_system = "github"
source_control = "github"
file_system = "local"

[auth]
ISSUE_TOKEN = "env:GITHUB_TOKEN"
GIT_TOKEN = "env:GITHUB_TOKEN"

[systems.work_config]
repo = "owner/my-app"
```

### Production Configuration

```toml
[project]
name = "production-app"
issue_system = "github"
source_control = "github"
file_system = "r2"

[defaults]
preset = "software-guarded"
autonomy = "guarded"

[safety]
protected_paths = ["secrets/**", "infra/prod/**", "terraform/**"]
require_confirm_for = ["release", "deploy", "tag", "merge_to_main"]

[workflow]
max_evaluate_retries = 3
auto_merge = false
auto_close_work_item = false

[notifications]
post_status_cards = true
status_card_style = "detailed"
```
