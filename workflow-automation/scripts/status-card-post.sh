#!/bin/bash
# FABER Core: Status Card Poster
# Posts formatted status cards to work tracking systems

set -euo pipefail

# Check arguments
if [ $# -lt 5 ]; then
    echo "Usage: $0 <work_id> <issue_id> <stage> <message> <options_json>" >&2
    exit 2
fi

WORK_ID="$1"
ISSUE_ID="$2"
STAGE="$3"
MESSAGE="$4"
OPTIONS_JSON="$5"

# Load configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_JSON=$("$SCRIPT_DIR/config-loader.sh")

if [ $? -ne 0 ]; then
    echo "Error: Failed to load configuration" >&2
    exit 3
fi

# Get configuration values
ISSUE_SYSTEM=$(echo "$CONFIG_JSON" | jq -r '.project.issue_system')
POST_STATUS_CARDS=$(echo "$CONFIG_JSON" | jq -r '.notifications.post_status_cards // true')
STATUS_CARD_STYLE=$(echo "$CONFIG_JSON" | jq -r '.notifications.status_card_style // "detailed"')
INCLUDE_METADATA=$(echo "$CONFIG_JSON" | jq -r '.notifications.include_session_metadata // true')

# Check if status cards are enabled
if [ "$POST_STATUS_CARDS" != "true" ]; then
    echo "Status cards are disabled in configuration" >&2
    exit 0
fi

# Load workflow state to get context
STATE_FILE=".fractary/plugins/faber/state.json"

if [ ! -f "$STATE_FILE" ]; then
    echo "Warning: State file not found, posting without workflow context" >&2
    STATE_JSON='{}'
else
    STATE_JSON=$(cat "$STATE_FILE")
fi

# Create timestamp
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Get stage emoji
case "$STAGE" in
    frame) STAGE_EMOJI="📋" ;;
    architect) STAGE_EMOJI="📐" ;;
    build) STAGE_EMOJI="🔨" ;;
    evaluate) STAGE_EMOJI="🧪" ;;
    release) STAGE_EMOJI="🚀" ;;
    *) STAGE_EMOJI="⚙️" ;;
esac

# Format options as markdown list
OPTIONS_MD=$(echo "$OPTIONS_JSON" | jq -r '.[] | "- `\(.)`"' | tr '\n' '\n')

# Load status card template
TEMPLATE_PATH="$SCRIPT_DIR/../templates/status-card.template.md"
if [ ! -f "$TEMPLATE_PATH" ]; then
    # Use default template if not found
    STATUS_CARD="**FABER** ${STAGE_EMOJI} Stage: ${STAGE}

$MESSAGE

**Options:** $OPTIONS_MD

\`\`\`yaml
work_id: $WORK_ID
stage: $STAGE
timestamp: $TIMESTAMP
\`\`\`"
else
    # Use template with variable substitution
    STATUS_CARD=$(cat "$TEMPLATE_PATH" | \
        sed "s/{stage_emoji}/$STAGE_EMOJI/g" | \
        sed "s/{stage}/$STAGE/g" | \
        sed "s/{message}/$MESSAGE/g" | \
        sed "s/{options}/$OPTIONS_MD/g" | \
        sed "s/{work_id}/$WORK_ID/g" | \
        sed "s/{timestamp}/$TIMESTAMP/g")
fi

# Add metadata if enabled and style is detailed
if [ "$INCLUDE_METADATA" = "true" ] && [ "$STATUS_CARD_STYLE" = "detailed" ]; then
    DOMAIN=$(echo "$STATE_JSON" | jq -r '.domain // "unknown"')
    AUTONOMY=$(echo "$STATE_JSON" | jq -r '.autonomy // "unknown"')

    STATUS_CARD="$STATUS_CARD

**Domain:** $DOMAIN | **Autonomy:** $AUTONOMY"
fi

# Post to work tracking system based on issue_system
case "$ISSUE_SYSTEM" in
    github)
        # Post comment to GitHub issue using gh CLI
        echo "$STATUS_CARD" | gh issue comment "$ISSUE_ID" --body-file -
        if [ $? -ne 0 ]; then
            echo "Error: Failed to post status card to GitHub issue #$ISSUE_ID" >&2
            exit 1
        fi
        echo "Status card posted to GitHub issue #$ISSUE_ID"
        ;;

    jira)
        echo "Error: Jira support not yet implemented" >&2
        exit 1
        ;;

    linear)
        echo "Error: Linear support not yet implemented" >&2
        exit 1
        ;;

    manual)
        # For manual tracking, just output the status card
        echo "Status card (manual mode):"
        echo "$STATUS_CARD"
        ;;

    *)
        echo "Error: Unknown issue system: $ISSUE_SYSTEM" >&2
        exit 1
        ;;
esac

exit 0
