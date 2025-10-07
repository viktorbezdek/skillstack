# Getting Started with {{PROJECT_NAME}}

This guide will help you get {{PROJECT_NAME}} up and running in under 5 minutes.

## What You'll Need

Before starting, make sure you have:

{{#PREREQUISITES}}
- [ ] {{PREREQUISITE}}
{{/PREREQUISITES}}

## Installation

### Step 1: Get the Code

```bash
{{CLONE_COMMAND}}
cd {{PROJECT_NAME}}
```

### Step 2: Install Dependencies

{{#INSTALL_OPTIONS}}
#### Option {{INDEX}}: {{OPTION_NAME}}

```bash
{{INSTALL_COMMAND}}
```
{{/INSTALL_OPTIONS}}

### Step 3: Configure Your Environment

```bash
# Copy the example configuration
cp {{ENV_EXAMPLE}} {{ENV_FILE}}
```

Open `{{ENV_FILE}}` and set these required values:

| Variable | Description | Example |
|----------|-------------|---------|
{{#REQUIRED_ENV_VARS}}
| `{{VAR_NAME}}` | {{VAR_DESCRIPTION}} | `{{VAR_EXAMPLE}}` |
{{/REQUIRED_ENV_VARS}}

### Step 4: Start the Application

```bash
{{START_COMMAND}}
```

You should see:

```
{{EXPECTED_OUTPUT}}
```

## Verify It's Working

{{VERIFICATION_STEPS}}

## Next Steps

Now that you're set up:

1. **Explore the features** - See [User Guide](./user-guide.md)
2. **Learn the API** - Check [API Reference](./api/README.md)
3. **Customize it** - Read [Configuration](./configuration.md)

## Common Setup Issues

### {{ISSUE_1_TITLE}}

**Symptom:** {{ISSUE_1_SYMPTOM}}

**Solution:** {{ISSUE_1_SOLUTION}}

### {{ISSUE_2_TITLE}}

**Symptom:** {{ISSUE_2_SYMPTOM}}

**Solution:** {{ISSUE_2_SOLUTION}}

## Getting Help

- 📖 [Full Documentation](./README.md)
- 💬 [Community Discord]({{DISCORD_URL}})
- 🐛 [Report an Issue]({{ISSUES_URL}})
