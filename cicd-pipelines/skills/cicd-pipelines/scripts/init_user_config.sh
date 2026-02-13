#!/bin/bash
# Canonical version lives in workflow-automation
exec "$(dirname "$0")/../../workflow-automation/scripts/release/init_user_config.sh" "$@"
