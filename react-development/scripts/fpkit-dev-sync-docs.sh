#!/usr/bin/env bash
#
# sync-docs.sh - Sync documentation from fpkit package to skill references
#
# Usage:
#   ./scripts/sync-docs.sh              # Sync all docs
#   ./scripts/sync-docs.sh --check      # Check which docs need updating
#   ./scripts/sync-docs.sh --guide css-variables.md  # Sync specific guide
#

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="$SKILL_DIR/config.json"

# Load config
if [[ ! -f "$CONFIG_FILE" ]]; then
  echo -e "${RED}✗ Config file not found: $CONFIG_FILE${NC}"
  exit 1
fi

# Parse config (requires jq, fallback to manual parsing if not available)
if command -v jq &> /dev/null; then
  FPKIT_DOCS_PATH=$(jq -r '.fpkitDocsPath' "$CONFIG_FILE")
  LOCAL_DOCS_PATH=$(jq -r '.localDocsPath' "$CONFIG_FILE")
  GUIDES=($(jq -r '.availableGuides[]' "$CONFIG_FILE"))
else
  # Fallback: manual parsing (basic)
  FPKIT_DOCS_PATH="../../packages/fpkit/docs/guides"
  LOCAL_DOCS_PATH="./references"
  GUIDES=("css-variables.md" "composition.md" "accessibility.md" "architecture.md" "testing.md" "storybook.md")
fi

# Resolve paths
SOURCE_DIR="$SKILL_DIR/$FPKIT_DOCS_PATH"
DEST_DIR="$SKILL_DIR/$LOCAL_DOCS_PATH"

# Check if source directory exists
if [[ ! -d "$SOURCE_DIR" ]]; then
  echo -e "${RED}✗ Source directory not found: $SOURCE_DIR${NC}"
  echo -e "${YELLOW}  Make sure you're running this from within the fpkit monorepo${NC}"
  exit 1
fi

# Create destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Function to check if file needs updating
needs_update() {
  local src="$1"
  local dest="$2"

  if [[ ! -f "$dest" ]]; then
    return 0  # Destination doesn't exist, needs update
  fi

  # Compare modification times
  if [[ "$src" -nt "$dest" ]]; then
    return 0  # Source is newer
  fi

  return 1  # Up to date
}

# Function to sync a single guide
sync_guide() {
  local guide="$1"
  local src="$SOURCE_DIR/$guide"
  local dest="$DEST_DIR/$guide"

  if [[ ! -f "$src" ]]; then
    echo -e "${RED}✗ Guide not found: $guide${NC}"
    return 1
  fi

  if needs_update "$src" "$dest"; then
    cp "$src" "$dest"
    echo -e "${GREEN}✓ Synced: $guide${NC}"
    return 0
  else
    echo -e "${BLUE}→ Up to date: $guide${NC}"
    return 2
  fi
}

# Parse arguments
CHECK_ONLY=false
SPECIFIC_GUIDE=""

while [[ $# -gt 0 ]]; do
  case $1 in
    --check)
      CHECK_ONLY=true
      shift
      ;;
    --guide)
      SPECIFIC_GUIDE="$2"
      shift 2
      ;;
    -h|--help)
      echo "Usage: $0 [OPTIONS]"
      echo ""
      echo "Options:"
      echo "  --check          Check which docs need updating (don't sync)"
      echo "  --guide <file>   Sync specific guide only"
      echo "  -h, --help       Show this help message"
      echo ""
      echo "Examples:"
      echo "  $0                          # Sync all docs"
      echo "  $0 --check                  # Check status"
      echo "  $0 --guide testing.md       # Sync testing.md only"
      exit 0
      ;;
    *)
      echo -e "${RED}Unknown option: $1${NC}"
      exit 1
      ;;
  esac
done

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  fpkit Documentation Sync${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "Source: ${YELLOW}$SOURCE_DIR${NC}"
echo -e "Destination: ${YELLOW}$DEST_DIR${NC}"
echo ""

# Sync guides
SYNCED=0
UP_TO_DATE=0
ERRORS=0

if [[ -n "$SPECIFIC_GUIDE" ]]; then
  # Sync specific guide
  if sync_guide "$SPECIFIC_GUIDE"; then
    SYNCED=$((SYNCED + 1))
  elif [[ $? -eq 2 ]]; then
    UP_TO_DATE=$((UP_TO_DATE + 1))
  else
    ERRORS=$((ERRORS + 1))
  fi
else
  # Sync all guides
  for guide in "${GUIDES[@]}"; do
    if [[ "$CHECK_ONLY" == true ]]; then
      src="$SOURCE_DIR/$guide"
      dest="$DEST_DIR/$guide"
      if needs_update "$src" "$dest"; then
        echo -e "${YELLOW}⚠ Needs update: $guide${NC}"
        SYNCED=$((SYNCED + 1))
      else
        echo -e "${GREEN}✓ Up to date: $guide${NC}"
        UP_TO_DATE=$((UP_TO_DATE + 1))
      fi
    else
      if sync_guide "$guide"; then
        SYNCED=$((SYNCED + 1))
      elif [[ $? -eq 2 ]]; then
        UP_TO_DATE=$((UP_TO_DATE + 1))
      else
        ERRORS=$((ERRORS + 1))
      fi
    fi
  done
fi

# Summary
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
if [[ "$CHECK_ONLY" == true ]]; then
  echo -e "${YELLOW}Check Summary:${NC}"
  echo -e "  ${YELLOW}Needs update: $SYNCED${NC}"
  echo -e "  ${GREEN}Up to date: $UP_TO_DATE${NC}"
else
  echo -e "${GREEN}Sync Summary:${NC}"
  echo -e "  ${GREEN}Synced: $SYNCED${NC}"
  echo -e "  ${BLUE}Up to date: $UP_TO_DATE${NC}"
  if [[ $ERRORS -gt 0 ]]; then
    echo -e "  ${RED}Errors: $ERRORS${NC}"
  fi
fi
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

exit 0
