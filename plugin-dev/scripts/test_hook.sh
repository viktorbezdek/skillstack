#!/usr/bin/env bash
# test_hook.sh — mock-stdin hook tester for Claude Code hooks.
#
# Pipes a JSON event payload to a hook script on stdin, captures exit code
# and stdout/stderr, then asserts expectations.
#
# Usage:
#   bash test_hook.sh SCRIPT_PATH EVENT_JSON [OPTIONS]
#
# Options:
#   --expect-exit N        Assert hook exits with code N (default: 0)
#   --expect-output PATH   Assert jq expression evaluates to truthy
#                          Example: --expect-output '.ok == true'
#   --expect-stderr TEXT   Assert TEXT appears in hook's stderr
#   --timeout SECONDS      Override timeout (default: ${TEST_HOOK_TIMEOUT:-15})
#
# Exit codes:
#   0  All assertions pass
#   1  Assertion failed
#   2  Hook script not found or not executable
#   3  Timeout exceeded
#
# Environment:
#   TEST_HOOK_TIMEOUT  Override default 15-second timeout
#
# Examples:
#   bash test_hook.sh ./hooks/format.sh '{"tool_name":"Edit","tool_input":{"file_path":"foo.ts"}}' --expect-exit 0
#   bash test_hook.sh ./hooks/block.sh '{"tool_name":"Bash","tool_input":{"command":"rm -rf /"}}' --expect-exit 2 --expect-stderr "blocked"

set -euo pipefail

SCRIPT_PATH=""
EVENT_JSON=""
EXPECT_EXIT=0
EXPECT_OUTPUT=""
EXPECT_STDERR=""
TIMEOUT_SECONDS="${TEST_HOOK_TIMEOUT:-15}"

# ---------------------------------------------------------------------------
# Parse arguments
# ---------------------------------------------------------------------------
if [ $# -lt 2 ]; then
    echo "Usage: test_hook.sh SCRIPT_PATH EVENT_JSON [OPTIONS]" >&2
    echo "Run 'bash test_hook.sh --help' for details." >&2
    exit 1
fi

if [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
    grep "^#" "$0" | sed 's/^# \{0,1\}//' | head -40
    exit 0
fi

SCRIPT_PATH="$1"
EVENT_JSON="$2"
shift 2

while [ $# -gt 0 ]; do
    case "$1" in
        --expect-exit)
            EXPECT_EXIT="$2"
            shift 2
            ;;
        --expect-output)
            EXPECT_OUTPUT="$2"
            shift 2
            ;;
        --expect-stderr)
            EXPECT_STDERR="$2"
            shift 2
            ;;
        --timeout)
            TIMEOUT_SECONDS="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1" >&2
            exit 1
            ;;
    esac
done

# ---------------------------------------------------------------------------
# Validate inputs
# ---------------------------------------------------------------------------
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "Error: hook script not found: $SCRIPT_PATH" >&2
    exit 2
fi

if [ ! -x "$SCRIPT_PATH" ]; then
    echo "Error: hook script is not executable: $SCRIPT_PATH" >&2
    echo "Fix with: chmod +x $SCRIPT_PATH" >&2
    exit 2
fi

# ---------------------------------------------------------------------------
# Detect timeout command (GNU coreutils on macOS needs gtimeout)
# ---------------------------------------------------------------------------
TIMEOUT_CMD=""
if command -v timeout > /dev/null 2>&1; then
    TIMEOUT_CMD="timeout"
elif command -v gtimeout > /dev/null 2>&1; then
    TIMEOUT_CMD="gtimeout"
else
    echo "Error: 'timeout' command not found." >&2
    echo "On macOS: brew install coreutils (provides gtimeout, also symlinked as timeout)" >&2
    echo "On Linux: should be available by default (GNU coreutils)" >&2
    exit 2
fi

# ---------------------------------------------------------------------------
# Run the hook
# ---------------------------------------------------------------------------
STDOUT_FILE="$(mktemp /tmp/test_hook_stdout.XXXXXX)"
STDERR_FILE="$(mktemp /tmp/test_hook_stderr.XXXXXX)"

cleanup() {
    rm -f "$STDOUT_FILE" "$STDERR_FILE"
}
trap cleanup EXIT

ACTUAL_EXIT=0
"$TIMEOUT_CMD" "$TIMEOUT_SECONDS" \
    bash -c "printf '%s' \"\$EVENT_JSON\" | \"$SCRIPT_PATH\"" \
    > "$STDOUT_FILE" 2> "$STDERR_FILE" || ACTUAL_EXIT=$?

# Timeout returns 124.
if [ "$ACTUAL_EXIT" -eq 124 ]; then
    echo "FAIL: hook timed out after ${TIMEOUT_SECONDS}s" >&2
    echo "  Hook: $SCRIPT_PATH" >&2
    exit 3
fi

# ---------------------------------------------------------------------------
# Assertions
# ---------------------------------------------------------------------------
FAILED=0

# Exit code check.
if [ "$ACTUAL_EXIT" -ne "$EXPECT_EXIT" ]; then
    echo "FAIL: expected exit $EXPECT_EXIT, got $ACTUAL_EXIT" >&2
    if [ -s "$STDERR_FILE" ]; then
        echo "  stderr: $(cat "$STDERR_FILE")" >&2
    fi
    FAILED=1
fi

# JSON output check via jq.
if [ -n "$EXPECT_OUTPUT" ]; then
    if ! command -v jq > /dev/null 2>&1; then
        echo "WARNING: jq not found — skipping JSON output assertion ($EXPECT_OUTPUT)" >&2
        echo "  Install with: brew install jq (macOS) or apt-get install jq (Linux)"
    else
        STDOUT_CONTENT="$(cat "$STDOUT_FILE")"
        if [ -z "$STDOUT_CONTENT" ]; then
            echo "FAIL: expected JSON output matching '$EXPECT_OUTPUT' but stdout is empty" >&2
            FAILED=1
        elif ! echo "$STDOUT_CONTENT" | jq -e "$EXPECT_OUTPUT" > /dev/null 2>&1; then
            echo "FAIL: jq expression '$EXPECT_OUTPUT' not satisfied" >&2
            echo "  stdout: $STDOUT_CONTENT" >&2
            FAILED=1
        fi
    fi
fi

# Stderr substring check.
if [ -n "$EXPECT_STDERR" ]; then
    STDERR_CONTENT="$(cat "$STDERR_FILE")"
    if ! echo "$STDERR_CONTENT" | grep -qF "$EXPECT_STDERR"; then
        echo "FAIL: expected '$EXPECT_STDERR' in stderr" >&2
        echo "  actual stderr: $STDERR_CONTENT" >&2
        FAILED=1
    fi
fi

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
if [ "$FAILED" -eq 0 ]; then
    echo "OK: all assertions passed (exit=$ACTUAL_EXIT)"
    exit 0
else
    exit 1
fi
