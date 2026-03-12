#!/bin/bash
# Canonical version lives in workflow-automation
exec "$(dirname "$0")/../../workflow-automation/scripts/release/create_org_config.sh" "$@"
