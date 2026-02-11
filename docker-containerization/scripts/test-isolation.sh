#!/bin/bash

# Test script for worktree browser isolation
# Validates that multiple worktrees can run browser automation without interference

set -e

SKILL_DIR="$HOME/.claude/skills/worktree-management"

echo "🧪 Worktree Browser Isolation Test Suite"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

pass_count=0
fail_count=0

test_pass() {
    echo -e "${GREEN}✓ PASS${NC}: $1"
    ((pass_count++))
}

test_fail() {
    echo -e "${RED}✗ FAIL${NC}: $1"
    ((fail_count++))
}

test_warn() {
    echo -e "${YELLOW}⚠ WARN${NC}: $1"
}

echo "📦 Test 1: Verify shared volume exists"
if docker volume inspect browser-profiles &>/dev/null; then
    test_pass "Shared volume 'browser-profiles' exists"
else
    test_fail "Shared volume 'browser-profiles' not found"
    echo "   Run: $SKILL_DIR/scripts/setup-mcp-isolation.sh"
fi
echo ""

echo "📦 Test 2: Verify MCP containers have volume mounted"
for container in playwright-mcp chrome-devtools-mcp puppeteer-mcp; do
    if docker inspect $container 2>/dev/null | grep -q "browser-profiles"; then
        test_pass "Container '$container' has volume mounted"
    else
        test_fail "Container '$container' missing volume mount"
        echo "   Run: $SKILL_DIR/scripts/setup-mcp-isolation.sh"
    fi
done
echo ""

echo "📦 Test 3: Verify containers can access /browser-data"
for container in playwright-mcp chrome-devtools-mcp puppeteer-mcp; do
    if docker exec $container ls -la /browser-data &>/dev/null; then
        test_pass "Container '$container' can access /browser-data"
    else
        test_fail "Container '$container' cannot access /browser-data"
    fi
done
echo ""

echo "🔒 Test 4: Port allocation locking"
if grep -q "flock" "$SKILL_DIR/scripts/worktree-manager.sh"; then
    test_pass "Port allocation uses flock locking"
else
    test_fail "Port allocation missing flock locking"
fi
echo ""

echo "🔧 Test 5: MCP template uses container paths"
if grep -q "/browser-data/{{WORKTREE_NAME}}" "$SKILL_DIR/assets/mcp.template.json"; then
    test_pass "MCP template uses container-accessible paths"
else
    test_fail "MCP template still uses host paths"
fi
echo ""

echo "🌐 Test 6: Browser debugging ports configured"
template_content=$(cat "$SKILL_DIR/assets/mcp.template.json")
if echo "$template_content" | grep -q "PLAYWRIGHT_PORT"; then
    test_pass "Playwright debugging port configured"
else
    test_fail "Playwright debugging port missing"
fi

if echo "$template_content" | grep -q "CHROME_DEVTOOLS_PORT"; then
    test_pass "Chrome DevTools debugging port configured"
else
    test_fail "Chrome DevTools debugging port missing"
fi

if echo "$template_content" | grep -q "PUPPETEER_PORT"; then
    test_pass "Puppeteer debugging port configured"
else
    test_fail "Puppeteer debugging port missing"
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Test Results Summary"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo -e "  ${GREEN}Passed: $pass_count${NC}"
echo -e "  ${RED}Failed: $fail_count${NC}"
echo ""

if [ $fail_count -eq 0 ]; then
    echo -e "${GREEN}✅ All tests passed! Browser isolation is properly configured.${NC}"
    echo ""
    echo "🎯 Next Steps:"
    echo "   1. Create two test worktrees:"
    echo "      @worktree create test-iso-1"
    echo "      @worktree create test-iso-2"
    echo ""
    echo "   2. In separate terminals, launch Claude in each:"
    echo "      Terminal 1: cd ../SoftTrak-test-iso-1 && claude"
    echo "      Terminal 2: cd ../SoftTrak-test-iso-2 && claude"
    echo ""
    echo "   3. Test browser automation in both sessions simultaneously"
    echo "      Both should work without interference"
    echo ""
    exit 0
else
    echo -e "${RED}❌ Some tests failed. Please fix the issues above.${NC}"
    echo ""
    echo "🔧 Quick Fix:"
    echo "   $SKILL_DIR/scripts/setup-mcp-isolation.sh"
    echo ""
    exit 1
fi
