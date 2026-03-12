#!/bin/bash

# MCP Browser Isolation Setup Script
# One-time setup to configure browser MCP containers with shared volume for worktree isolation

set -e

echo "🔧 Setting up MCP Browser Isolation"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if Docker is running
if ! docker info &>/dev/null; then
    echo "❌ Error: Docker is not running"
    echo "   Please start Docker Desktop and try again"
    exit 1
fi

echo "📦 Step 1: Creating shared browser profiles volume..."
if docker volume inspect browser-profiles &>/dev/null; then
    echo "   ℹ️  Volume 'browser-profiles' already exists"
else
    docker volume create browser-profiles
    echo "   ✅ Created volume 'browser-profiles'"
fi
echo ""

# Function to restart a container with volume mount
restart_container_with_volume() {
    local container_name=$1
    local image=$2
    local command=$3

    echo "🔄 Processing container: $container_name"

    # Check if container exists
    if docker ps -a --format '{{.Names}}' | grep -q "^${container_name}$"; then
        echo "   Stopping existing container..."
        docker stop $container_name &>/dev/null || true
        docker rm $container_name &>/dev/null || true
        echo "   ✅ Removed old container"
    fi

    echo "   Starting new container with volume mount..."
    docker run -d \
        --name $container_name \
        -v browser-profiles:/browser-data \
        --restart unless-stopped \
        $image \
        $command

    echo "   ✅ Container $container_name running with isolation"
    echo ""
}

echo "📦 Step 2: Restarting MCP containers with shared volume..."
echo ""

# Playwright MCP
restart_container_with_volume \
    "playwright-mcp" \
    "mcr.microsoft.com/playwright:v1.48.0-jammy" \
    "tail -f /dev/null"

# Chrome DevTools MCP
restart_container_with_volume \
    "chrome-devtools-mcp" \
    "zenika/alpine-chrome:latest" \
    "tail -f /dev/null"

# Puppeteer MCP
restart_container_with_volume \
    "puppeteer-mcp" \
    "ghcr.io/puppeteer/puppeteer:latest" \
    "tail -f /dev/null"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ MCP Browser Isolation Setup Complete!"
echo ""
echo "📋 Summary:"
echo "   • Shared volume 'browser-profiles' created"
echo "   • playwright-mcp: Running with /browser-data mount"
echo "   • chrome-devtools-mcp: Running with /browser-data mount"
echo "   • puppeteer-mcp: Running with /browser-data mount"
echo ""
echo "🎯 Next Steps:"
echo "   1. Existing worktrees: Unchanged (will use old paths)"
echo "   2. New worktrees: Will automatically use isolated browser profiles"
echo "   3. Test: Create two worktrees and try parallel browsing"
echo ""
echo "💡 Verification:"
echo "   docker volume inspect browser-profiles"
echo "   docker exec -it playwright-mcp ls -la /browser-data/"
echo ""
