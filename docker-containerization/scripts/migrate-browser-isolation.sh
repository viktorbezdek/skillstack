#!/bin/bash

# Browser Isolation Migration Script
# Adds --isolated=true flag to chrome-devtools-mcp in existing worktrees

set -e

SKILL_DIR="$HOME/.claude/skills/worktree-management"
WORKTREES_JSON="$SKILL_DIR/worktrees.json"

echo "🔧 Browser Isolation Migration"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "This script adds --isolated=true to chrome-devtools-mcp"
echo "in all existing worktrees to prevent browser interference."
echo ""

# Check if worktrees exist
if [ ! -f "$WORKTREES_JSON" ]; then
    echo "❌ No worktrees found. Nothing to migrate."
    exit 0
fi

worktree_count=$(jq '.worktrees | length' "$WORKTREES_JSON")

if [ "$worktree_count" -eq 0 ]; then
    echo "ℹ️  No worktrees found. Nothing to migrate."
    exit 0
fi

echo "Found $worktree_count worktree(s) to process..."
echo ""

migrated=0
skipped=0
errors=0

for i in $(seq 0 $((worktree_count - 1))); do
    worktree=$(jq -r ".worktrees[$i]" "$WORKTREES_JSON")
    name=$(echo "$worktree" | jq -r '.name')
    path=$(echo "$worktree" | jq -r '.path')
    mcp_file="$path/.mcp.json"

    echo "Processing: $name"
    echo "   Path: $path"

    # Check if worktree directory exists
    if [ ! -d "$path" ]; then
        echo "   ⚠️  Directory not found - skipping"
        skipped=$((skipped + 1))
        echo ""
        continue
    fi

    # Check if .mcp.json exists
    if [ ! -f "$mcp_file" ]; then
        echo "   ⚠️  .mcp.json not found - skipping"
        skipped=$((skipped + 1))
        echo ""
        continue
    fi

    # Check if already has --isolated flag
    if grep -q '"--isolated=true"' "$mcp_file" 2>/dev/null; then
        echo "   ℹ️  Already has --isolated flag - skipping"
        skipped=$((skipped + 1))
        echo ""
        continue
    fi

    # Create backup
    cp "$mcp_file" "$mcp_file.backup"
    echo "   📋 Created backup: .mcp.json.backup"

    # Check if using Docker-based or host-based chrome-devtools
    if grep -q '"command": "docker"' "$mcp_file" 2>/dev/null; then
        # Docker-based: Add --isolated after "chrome-devtools-mcp"
        if jq '.mcpServers["chrome-devtools"].args |= map(if . == "chrome-devtools-mcp" then (., "--isolated=true") else . end)' "$mcp_file" > "$mcp_file.tmp"; then
            mv "$mcp_file.tmp" "$mcp_file"
            echo "   ✅ Added --isolated flag (Docker-based)"
            migrated=$((migrated + 1))
        else
            echo "   ❌ Failed to update - restoring backup"
            mv "$mcp_file.backup" "$mcp_file"
            errors=$((errors + 1))
        fi
    else
        # Host-based: Add --isolated after "chrome-devtools-mcp@latest"
        if jq '.mcpServers["chrome-devtools"].args |= map(if . == "chrome-devtools-mcp@latest" then (., "--isolated=true") else . end)' "$mcp_file" > "$mcp_file.tmp"; then
            mv "$mcp_file.tmp" "$mcp_file"
            echo "   ✅ Added --isolated flag (host-based)"
            migrated=$((migrated + 1))
        else
            echo "   ❌ Failed to update - restoring backup"
            mv "$mcp_file.backup" "$mcp_file"
            errors=$((errors + 1))
        fi
    fi

    echo ""
done

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Migration Complete!"
echo ""
echo "📊 Summary:"
echo "   Migrated: $migrated"
echo "   Skipped:  $skipped"
echo "   Errors:   $errors"
echo ""

if [ $migrated -gt 0 ]; then
    echo "🎯 Next Steps:"
    echo "   1. Restart Claude Code sessions in affected worktrees"
    echo "   2. Test browser automation to verify isolation"
    echo "   3. If issues occur, restore from .mcp.json.backup"
    echo ""
    echo "💡 Verification:"
    echo "   In each worktree, check .mcp.json:"
    echo "   grep --isolated=true .mcp.json"
    echo ""
fi

if [ $errors -gt 0 ]; then
    echo "⚠️  Some migrations failed. Check error messages above."
    echo "   Backups are preserved as .mcp.json.backup"
    exit 1
fi
