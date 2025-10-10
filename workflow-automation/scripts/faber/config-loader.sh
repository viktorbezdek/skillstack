#!/bin/bash
# FABER Core: Configuration Loader
# Loads and parses FABER configuration file (TOML → JSON)

set -euo pipefail

# Configuration file path
CONFIG_PATH="${1:-.faber.config.toml}"

# Check if config file exists
if [ ! -f "$CONFIG_PATH" ]; then
    echo "Error: Configuration file not found: $CONFIG_PATH" >&2
    echo "Run '/faber-init' to create a configuration file" >&2
    exit 3
fi

# Convert TOML to JSON using Python
# We use Python because it has good TOML support and is widely available
config_json=$(python3 - "$CONFIG_PATH" <<'PYTHON_EOF'
import sys
import json

try:
    import tomllib  # Python 3.11+
except ImportError:
    try:
        import tomli as tomllib  # Fallback for Python <3.11
    except ImportError:
        # If neither available, try using toml
        try:
            import toml as tomllib
        except ImportError:
            print('Error: No TOML library found. Install tomli: pip install tomli', file=sys.stderr)
            sys.exit(3)

config_path = sys.argv[1]

try:
    with open(config_path, 'rb') as f:
        if hasattr(tomllib, 'load'):
            config = tomllib.load(f)
        else:
            # For the 'toml' library
            f.close()
            with open(config_path, 'r') as f:
                config = tomllib.load(f)

    # Output as compact JSON
    print(json.dumps(config, separators=(',', ':')))
except FileNotFoundError:
    print(f'Error: Configuration file not found: {config_path}', file=sys.stderr)
    sys.exit(3)
except Exception as e:
    print(f'Error parsing configuration: {e}', file=sys.stderr)
    sys.exit(3)
PYTHON_EOF
)

if [ $? -ne 0 ]; then
    echo "Error: Failed to parse configuration file" >&2
    exit 3
fi

# Validate required fields
if ! echo "$config_json" | jq -e '.project.name' >/dev/null 2>&1; then
    echo "Error: Invalid configuration - missing project.name" >&2
    exit 3
fi

if ! echo "$config_json" | jq -e '.project.issue_system' >/dev/null 2>&1; then
    echo "Error: Invalid configuration - missing project.issue_system" >&2
    exit 3
fi

# Output validated JSON
echo "$config_json"
exit 0
