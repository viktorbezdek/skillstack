#!/bin/bash
# Canonical version lives in workflow-automation
exec "$(dirname "$0")/../../workflow-automation/scripts/git/cleanup_worktrees.sh" "$@"
