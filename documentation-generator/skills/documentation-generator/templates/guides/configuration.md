# Configuration Guide

Complete reference for configuring {{PROJECT_NAME}}.

## Configuration Methods

{{PROJECT_NAME}} can be configured through:

1. **Configuration file** - `{{CONFIG_FILE}}`
2. **Environment variables** - Prefixed with `{{ENV_PREFIX}}_`
3. **Command-line flags** - Override at runtime
4. **Programmatic API** - Set in code

**Priority order:** CLI flags > Environment variables > Config file > Defaults

## Configuration File

### Location

{{PROJECT_NAME}} looks for configuration in these locations (in order):

1. Path specified by `--config` flag
2. `{{ENV_PREFIX}}_CONFIG` environment variable
3. `./{{CONFIG_FILE}}` (current directory)
4. `~/.{{PROJECT_NAME}}/{{CONFIG_FILE}}` (user home)
5. `/etc/{{PROJECT_NAME}}/{{CONFIG_FILE}}` (system-wide)

### File Formats

Supported formats:

| Format | Extensions | Example |
|--------|------------|---------|
| YAML | `.yaml`, `.yml` | `config.yaml` |
| JSON | `.json` | `config.json` |
| TOML | `.toml` | `config.toml` |

### Complete Configuration Example

```yaml
# {{CONFIG_FILE}}
# Complete configuration example with all options

{{CONFIG_SECTION_1}}:
  {{OPTION_1}}: {{VALUE_1}}  # {{OPTION_1_DESC}}
  {{OPTION_2}}: {{VALUE_2}}  # {{OPTION_2_DESC}}
  {{OPTION_3}}:              # {{OPTION_3_DESC}}
    - {{LIST_VALUE_1}}
    - {{LIST_VALUE_2}}

{{CONFIG_SECTION_2}}:
  {{OPTION_4}}: {{VALUE_4}}
  {{OPTION_5}}:
    {{NESTED_OPTION_1}}: {{NESTED_VALUE_1}}
    {{NESTED_OPTION_2}}: {{NESTED_VALUE_2}}

{{CONFIG_SECTION_3}}:
  {{OPTION_6}}: {{VALUE_6}}
  {{OPTION_7}}: {{VALUE_7}}
```

## Environment Variables

All configuration options can be set via environment variables.

**Naming convention:** `{{ENV_PREFIX}}_SECTION_OPTION`

| Config Path | Environment Variable | Example |
|-------------|---------------------|---------|
{{#ENV_VARS}}
| `{{CONFIG_PATH}}` | `{{ENV_VAR}}` | `{{EXAMPLE_VALUE}}` |
{{/ENV_VARS}}

### Using a .env File

```bash
# .env
{{ENV_PREFIX}}_{{OPTION_1}}={{VALUE_1}}
{{ENV_PREFIX}}_{{OPTION_2}}={{VALUE_2}}
{{ENV_PREFIX}}_{{SECTION}}_{{OPTION_3}}={{VALUE_3}}
```

Load with:
```bash
source .env && {{PROJECT_NAME}} start
```

## Configuration Reference

### {{SECTION_1_NAME}}

Settings for {{SECTION_1_PURPOSE}}.

| Option | Type | Default | Environment | Description |
|--------|------|---------|-------------|-------------|
{{#SECTION_1_OPTIONS}}
| `{{NAME}}` | `{{TYPE}}` | `{{DEFAULT}}` | `{{ENV_VAR}}` | {{DESCRIPTION}} |
{{/SECTION_1_OPTIONS}}

**Example:**

```yaml
{{SECTION_1_KEY}}:
  {{EXAMPLE_CONFIG_1}}
```

### {{SECTION_2_NAME}}

Settings for {{SECTION_2_PURPOSE}}.

| Option | Type | Default | Environment | Description |
|--------|------|---------|-------------|-------------|
{{#SECTION_2_OPTIONS}}
| `{{NAME}}` | `{{TYPE}}` | `{{DEFAULT}}` | `{{ENV_VAR}}` | {{DESCRIPTION}} |
{{/SECTION_2_OPTIONS}}

**Example:**

```yaml
{{SECTION_2_KEY}}:
  {{EXAMPLE_CONFIG_2}}
```

### {{SECTION_3_NAME}}

Settings for {{SECTION_3_PURPOSE}}.

| Option | Type | Default | Environment | Description |
|--------|------|---------|-------------|-------------|
{{#SECTION_3_OPTIONS}}
| `{{NAME}}` | `{{TYPE}}` | `{{DEFAULT}}` | `{{ENV_VAR}}` | {{DESCRIPTION}} |
{{/SECTION_3_OPTIONS}}

### Logging

Control log output and verbosity.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `log.level` | `string` | `info` | Log level: `debug`, `info`, `warn`, `error` |
| `log.format` | `string` | `text` | Output format: `text`, `json` |
| `log.output` | `string` | `stdout` | Output destination: `stdout`, `stderr`, filepath |
| `log.timestamp` | `bool` | `true` | Include timestamps |

```yaml
log:
  level: debug
  format: json
  output: /var/log/{{PROJECT_NAME}}.log
```

### Security

Security-related configuration.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `security.tls.enabled` | `bool` | `false` | Enable TLS |
| `security.tls.cert` | `string` | - | Path to TLS certificate |
| `security.tls.key` | `string` | - | Path to TLS key |
| `security.cors.origins` | `[]string` | `["*"]` | Allowed CORS origins |
| `security.rateLimit` | `int` | `100` | Requests per minute |

```yaml
security:
  tls:
    enabled: true
    cert: /etc/ssl/certs/server.crt
    key: /etc/ssl/private/server.key
  cors:
    origins:
      - https://example.com
      - https://app.example.com
  rateLimit: 1000
```

## Configuration Profiles

### Development Profile

```yaml
# config.development.yaml
{{DEV_CONFIG}}
```

### Production Profile

```yaml
# config.production.yaml
{{PROD_CONFIG}}
```

### Testing Profile

```yaml
# config.test.yaml
{{TEST_CONFIG}}
```

**Using profiles:**

```bash
# Set profile via environment
export {{ENV_PREFIX}}_PROFILE=production

# Or via flag
{{PROJECT_NAME}} start --profile production
```

## Dynamic Configuration

### Hot Reloading

{{PROJECT_NAME}} supports configuration hot reloading:

```yaml
config:
  watchInterval: 30s  # Check for changes every 30 seconds
  hotReload: true     # Apply changes without restart
```

**Note:** Some settings require restart:
- {{RESTART_REQUIRED_1}}
- {{RESTART_REQUIRED_2}}

### Configuration via API

```{{CODE_LANGUAGE}}
// Get current configuration
{{GET_CONFIG_EXAMPLE}}

// Update configuration at runtime
{{SET_CONFIG_EXAMPLE}}
```

## Secrets Management

### Using Environment Variables

```bash
export {{ENV_PREFIX}}_DB_PASSWORD="$(cat /run/secrets/db_password)"
```

### Using Secret Files

```yaml
secrets:
  files:
    - /run/secrets/api_key
    - /run/secrets/db_password
```

### Integration with Secret Managers

**HashiCorp Vault:**
```yaml
secrets:
  vault:
    address: https://vault.example.com
    path: secret/data/{{PROJECT_NAME}}
```

**AWS Secrets Manager:**
```yaml
secrets:
  aws:
    region: us-east-1
    secretName: {{PROJECT_NAME}}-secrets
```

## Validation

### Validate Configuration

```bash
{{PROJECT_NAME}} config validate
```

### Show Effective Configuration

```bash
{{PROJECT_NAME}} config show
```

### Generate Default Configuration

```bash
{{PROJECT_NAME}} config init > {{CONFIG_FILE}}
```

## Troubleshooting

### Configuration Not Loading

1. Check file exists and is readable
2. Verify file format (YAML/JSON/TOML syntax)
3. Run validation: `{{PROJECT_NAME}} config validate`

### Environment Variables Not Working

1. Verify naming: `{{ENV_PREFIX}}_SECTION_OPTION`
2. Check for typos (case-sensitive)
3. Ensure variables are exported: `export VAR=value`

### Priority Issues

Remember the priority order:
1. CLI flags (highest)
2. Environment variables
3. Config file
4. Defaults (lowest)

Use `{{PROJECT_NAME}} config show` to see effective values and their sources.
