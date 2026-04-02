# GWS CLI Authentication and Setup Reference

## Prerequisites

1. **Google Cloud Project** -- create at https://console.cloud.google.com
2. **OAuth Consent Screen** -- configure under APIs & Services > OAuth consent screen
3. **OAuth Client ID** -- create as "Desktop app" type (NOT web app)
4. **API Enablement** -- enable each Workspace API you want to use
5. **Test Users** -- add your email under OAuth consent > Test users (for unverified apps)

## Quick Start

```bash
# Option 1: Interactive setup (requires gcloud CLI)
gws auth setup

# Option 2: Manual (place client_secret.json, then login)
cp ~/Downloads/client_secret_*.json ~/.config/gws/client_secret.json
gws auth login
```

## Auth Commands

### `gws auth setup`
Interactive GCP project setup. Creates Cloud project, enables APIs, configures OAuth, and logs in. Requires `gcloud` CLI.

### `gws auth login`
Opens browser for OAuth2 authorization.

**Scope Presets:**

| Flag | Scopes |
|---|---|
| (none) | drive, spreadsheets, gmail.modify, calendar, documents, presentations, tasks |
| `--readonly` | Read-only versions of the above |
| `--full` | All default + pubsub + cloud-platform |
| `-s drive,gmail` | Only specified service scopes |
| `--scopes <urls>` | Custom scope URLs |

### `gws auth status`
Show current auth state as JSON: method, token validity, scopes, user, storage.

### `gws auth export`
Print decrypted credentials to stdout.

| Flag | Description |
|---|---|
| `--unmasked` | Show secrets in clear text |

### `gws auth logout`
Clear saved credentials and token cache.

## Credential Storage

- **Location:** `~/.config/gws/` (override with `GOOGLE_WORKSPACE_CLI_CONFIG_DIR`)
- **Encryption:** AES-256-GCM at rest
- **Key Storage:** OS keyring (macOS Keychain, Linux Secret Service, Windows Credential Manager)
- **Fallback:** `~/.config/gws/.encryption_key` when `GOOGLE_WORKSPACE_CLI_KEYRING_BACKEND=file`

### Files

| File | Purpose |
|---|---|
| `client_secret.json` | OAuth client configuration |
| `credentials.enc` | Encrypted OAuth credentials |
| `credentials.json` | Plaintext fallback (not recommended) |
| `.encryption_key` | Fallback encryption key (when keyring=file) |

## Auth Precedence (highest to lowest)

1. `GOOGLE_WORKSPACE_CLI_TOKEN` -- pre-obtained access token
2. `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` -- credentials JSON file path
3. Encrypted credentials from `gws auth login`
4. Plaintext `~/.config/gws/credentials.json`

## Environment Variables

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
| `GOOGLE_WORKSPACE_PROJECT_ID` | GCP project ID override |

All variables can also be set in a `.env` file.

## Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `redirect_uri_mismatch` | OAuth client not "Desktop app" type | Recreate client in Cloud Console as Desktop app |
| `Access blocked` | Test user not added | Add email under OAuth consent > Test users |
| `accessNotConfigured (403)` | API not enabled | Click `enable_url` in error output, or enable in Console |
| Token expired | Refresh token invalid | Run `gws auth login` again |
| Keyring error | OS keyring unavailable | Set `GOOGLE_WORKSPACE_CLI_KEYRING_BACKEND=file` |

## CI/CD and Headless Environments

For non-interactive environments:

```bash
# Use environment variable with pre-obtained token
export GOOGLE_WORKSPACE_CLI_TOKEN="ya29...."

# Or use service account credentials
export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE="/path/to/service-account.json"
```

## Scope Notes

- Unverified OAuth apps are limited to ~25 scopes
- Use `-s service1,service2` to limit scope selection
- The CLI picks the first (broadest) scope from a method's scope list
- Using restrictive scopes like `gmail.metadata` can block query parameters even when broader scopes are also granted
