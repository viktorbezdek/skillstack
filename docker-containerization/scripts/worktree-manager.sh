#!/bin/bash

# Worktree Manager - Core Implementation
# Handles Git worktree creation with isolated Docker and MCP configuration

set -e

SKILL_DIR="$HOME/.claude/skills/worktree-management"
TEMPLATES_DIR="$SKILL_DIR/assets"
WORKTREES_JSON="$SKILL_DIR/worktrees.json"
PORTS_JSON="$SKILL_DIR/port-registry.json"

# Check bash version (informational only, script works with older versions now)
BASH_VERSION_MAJOR="${BASH_VERSION%%.*}"
if [ "$BASH_VERSION_MAJOR" -lt 4 ]; then
    echo "ℹ️  Note: Using bash $BASH_VERSION (older version)"
    echo "   Script has been updated to work with older bash versions"
fi

# Load jq for JSON manipulation
if ! command -v jq &> /dev/null; then
    echo "❌ Error: jq is required but not installed"
    echo "   Install: brew install jq"
    exit 1
fi

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Helper Functions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

get_main_project() {
    jq -r '.main_project' "$WORKTREES_JSON"
}

# Check if a specific port is available
# Args: $1 = port number, $2 = port name/description, $3 = quiet mode (optional)
# Returns: 0 if available, 1 if in use
check_port_available() {
    local port=$1
    local port_name=$2
    local quiet_mode=${3:-false}

    # Check if port is in use by any system process (using lsof)
    if lsof -Pi :$port -sTCP:LISTEN -t &>/dev/null; then
        if [ "$quiet_mode" != true ]; then
            echo "⚠️  Port $port ($port_name) is already in use" >&2
            local process_info=$(lsof -Pi :$port -sTCP:LISTEN | tail -1)
            echo "   Process: $process_info" >&2
        fi
        return 1  # Port is in use
    fi

    # Also check Docker containers
    if docker ps --format '{{.Ports}}' 2>/dev/null | grep -q ":$port->"; then
        if [ "$quiet_mode" != true ]; then
            echo "⚠️  Port $port ($port_name) is in use by Docker container" >&2
            local container=$(docker ps --format '{{.Names}}\t{{.Ports}}' | grep ":$port->" | cut -f1)
            echo "   Container: $container" >&2
        fi
        return 1  # Port is in use
    fi

    return 0  # Port is available
}

# Validate all required ports are available
# Args: $1-$7 = backend, frontend, db, redis, playwright, chrome, puppeteer ports
# Returns: 0 if all available, 1 if any conflicts
validate_all_ports() {
    local backend_port=$1
    local frontend_port=$2
    local db_port=$3
    local redis_port=$4
    local playwright_port=$5
    local chrome_port=$6
    local puppeteer_port=$7

    local all_ports_ok=true
    local conflicts=()

    echo "🔍 Validating port availability..."

    # Check each port and collect conflicts
    if ! check_port_available $backend_port "Backend" true; then
        conflicts+=("Backend:$backend_port")
        all_ports_ok=false
    fi

    if ! check_port_available $frontend_port "Frontend" true; then
        conflicts+=("Frontend:$frontend_port")
        all_ports_ok=false
    fi

    if ! check_port_available $db_port "Database" true; then
        conflicts+=("Database:$db_port")
        all_ports_ok=false
    fi

    if ! check_port_available $redis_port "Redis" true; then
        conflicts+=("Redis:$redis_port")
        all_ports_ok=false
    fi

    if ! check_port_available $playwright_port "Playwright" true; then
        conflicts+=("Playwright:$playwright_port")
        all_ports_ok=false
    fi

    if ! check_port_available $chrome_port "Chrome DevTools" true; then
        conflicts+=("Chrome DevTools:$chrome_port")
        all_ports_ok=false
    fi

    if ! check_port_available $puppeteer_port "Puppeteer" true; then
        conflicts+=("Puppeteer:$puppeteer_port")
        all_ports_ok=false
    fi

    # If conflicts found, show detailed error report
    if [ "$all_ports_ok" = false ]; then
        echo ""
        echo "❌ PORT CONFLICT DETECTED"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
        echo "The following ports are already in use:"
        for conflict in "${conflicts[@]}"; do
            # Show detailed info for each conflict
            local service=$(echo "$conflict" | cut -d: -f1)
            local port=$(echo "$conflict" | cut -d: -f2)

            echo "  • $conflict"

            # Get what's using it
            if lsof -Pi :$port -sTCP:LISTEN -t &>/dev/null; then
                local process=$(lsof -Pi :$port -sTCP:LISTEN | tail -1 | awk '{print $1}')
                echo "    └─ Used by: $process"
            elif docker ps --format '{{.Names}}\t{{.Ports}}' 2>/dev/null | grep -q ":$port->"; then
                local container=$(docker ps --format '{{.Names}}\t{{.Ports}}' | grep ":$port->" | cut -f1)
                echo "    └─ Container: $container"
            fi
        done

        echo ""
        echo "💡 RESOLUTION OPTIONS"
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo ""
        echo "Option 1: Stop Specific Containers"
        echo "  docker ps                    # View running containers"
        echo "  docker stop <container-name> # Stop conflicting container"
        echo ""
        echo "Option 2: Stop Main SoftTrak Project"
        echo "  cd /Users/{{POSTGRES_USERNAME}}/Github_Projects/SoftTrak"
        echo "  docker-compose down"
        echo ""
        echo "Option 3: Check Other Worktrees"
        echo "  @worktree list --status      # View active worktrees"
        echo "  cd <worktree-path>"
        echo "  docker-compose down          # Stop worktree services"
        echo ""
        echo "Option 4: Manual Service Startup (Recommended)"
        echo "  • Worktree will be created successfully"
        echo "  • Resolve conflicts above"
        echo "  • Start services manually: ./start-worktree.sh"
        echo ""

        return 1
    fi

    echo "   ✅ All ports available"
    echo ""
    echo "📊 Validated Ports:"
    echo "   Backend:        $backend_port ✓"
    echo "   Frontend:       $frontend_port ✓"
    echo "   Database:       $db_port ✓"
    echo "   Redis:          $redis_port ✓"
    echo "   Playwright:     $playwright_port ✓"
    echo "   Chrome DevTools: $chrome_port ✓"
    echo "   Puppeteer:      $puppeteer_port ✓"
    echo ""
    return 0
}

get_next_port() {
    local base_port=$1
    local port_name=$2

    # Get all allocated ports for this type from worktrees (registry-based)
    local allocated_ports=$(jq -r ".allocated_worktrees | .[] | .$port_name" "$PORTS_JSON" 2>/dev/null | grep -v null || echo "")

    # Start with base_port as the minimum (main project uses base_port)
    # First worktree should use base_port + 1
    local highest=$base_port

    # If there are allocated ports, find the highest
    if [ -n "$allocated_ports" ]; then
        local max_allocated=$(echo "$allocated_ports" | sort -n | tail -1)
        if [ "$max_allocated" -gt "$highest" ]; then
            highest=$max_allocated
        fi
    fi

    # Intelligent port scanning - find first actually available port
    local candidate_port=$((highest + 1))
    local max_scan_attempts=50
    local scan_attempts=0

    # Scan for first available port (checking both system processes and Docker)
    while [ $scan_attempts -lt $max_scan_attempts ]; do
        # Check if port is available (system + Docker)
        if check_port_available $candidate_port "$port_name" true; then
            # Port is free - return it
            echo $candidate_port
            return 0
        fi

        # Port in use, try next one
        candidate_port=$((candidate_port + 1))
        scan_attempts=$((scan_attempts + 1))
    done

    # If we exhausted scan attempts, warn user and fall back to registry-based allocation
    if [ $scan_attempts -ge $max_scan_attempts ]; then
        echo "⚠️  WARNING: Could not find available port after scanning $max_scan_attempts ports" >&2
        echo "   Port Name: $port_name" >&2
        echo "   Starting from: $((highest + 1))" >&2
        echo "   Using registry-based allocation (may conflict)" >&2
        echo "   You may need to manually adjust ports in docker-compose.worktree.yml" >&2
    fi

    # Fallback to registry-based allocation
    echo $((highest + 1))
}

allocate_ports() {
    local worktree_name=$1
    local lockfile="/tmp/worktree-ports.lock"

    # Use flock for atomic port allocation to prevent race conditions
    # when multiple worktrees are created simultaneously
    (
        # Acquire exclusive lock (200 is arbitrary file descriptor)
        flock -x 200

        local backend_base=$(jq -r '.base_ports.backend' "$PORTS_JSON")
        local frontend_base=$(jq -r '.base_ports.frontend' "$PORTS_JSON")
        local db_base=$(jq -r '.base_ports.database' "$PORTS_JSON")
        local redis_base=$(jq -r '.base_ports.redis' "$PORTS_JSON")
        local playwright_base=$(jq -r '.base_ports.playwright' "$PORTS_JSON")
        local chrome_base=$(jq -r '.base_ports.chrome_devtools' "$PORTS_JSON")
        local puppeteer_base=$(jq -r '.base_ports.puppeteer' "$PORTS_JSON")

        local backend_port=$(get_next_port $backend_base "backend")
        local frontend_port=$(get_next_port $frontend_base "frontend")
        local db_port=$(get_next_port $db_base "database")
        local redis_port=$(get_next_port $redis_base "redis")
        local playwright_port=$(get_next_port $playwright_base "playwright")
        local chrome_port=$(get_next_port $chrome_base "chrome_devtools")
        local puppeteer_port=$(get_next_port $puppeteer_base "puppeteer")

        # Update port registry atomically
        local temp_file=$(mktemp)
        jq ".allocated_worktrees[\"$worktree_name\"] = {
            \"backend\": $backend_port,
            \"frontend\": $frontend_port,
            \"database\": $db_port,
            \"redis\": $redis_port,
            \"playwright\": $playwright_port,
            \"chrome_devtools\": $chrome_port,
            \"puppeteer\": $puppeteer_port
        }" "$PORTS_JSON" > "$temp_file"
        mv "$temp_file" "$PORTS_JSON"

        # Return JSON with allocated ports
        echo "{\"backend\":$backend_port,\"frontend\":$frontend_port,\"database\":$db_port,\"redis\":$redis_port,\"playwright\":$playwright_port,\"chrome_devtools\":$chrome_port,\"puppeteer\":$puppeteer_port}"

    ) 200>"$lockfile"
}

free_ports() {
    local worktree_name=$1
    local temp_file=$(mktemp)
    jq "del(.allocated_worktrees[\"$worktree_name\"])" "$PORTS_JSON" > "$temp_file"
    mv "$temp_file" "$PORTS_JSON"
}

generate_from_template() {
    local template_file=$1
    local output_file=$2

    # Read all replacement arguments into an array
    shift 2
    local -a replacement_args=("$@")

    local content=$(cat "$template_file")

    # Process replacements in pairs: key value key value ...
    local i=0
    while [ $i -lt ${#replacement_args[@]} ]; do
        local key="${replacement_args[$i]}"
        local value="${replacement_args[$((i+1))]}"
        content="${content//\{\{$key\}\}/$value}"
        i=$((i+2))
    done

    echo "$content" > "$output_file"
}

worktree_exists() {
    local name=$1
    jq -e ".worktrees[] | select(.name == \"$name\")" "$WORKTREES_JSON" > /dev/null 2>&1
}

get_worktree_index() {
    local name=$1
    jq -r ".worktrees | map(.name) | index(\"$name\")" "$WORKTREES_JSON"
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CREATE WORKTREE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

create_worktree() {
    local worktree_name=$1
    local branch_name=$2
    local start_services=${3:-true}

    echo "🔧 Creating worktree: $worktree_name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    # Validation
    if worktree_exists "$worktree_name"; then
        echo "❌ Error: Worktree '$worktree_name' already exists"
        exit 1
    fi

    # Get main project path
    local main_project=$(get_main_project)
    cd "$main_project"

    # Convert worktree name to branch name if not provided
    if [ -z "$branch_name" ]; then
        # Auto-convert: feature-auth → feature/auth
        if [[ $worktree_name == feature-* ]]; then
            branch_name="feature/${worktree_name#feature-}"
        elif [[ $worktree_name == bugfix-* ]]; then
            branch_name="bugfix/${worktree_name#bugfix-}"
        elif [[ $worktree_name == docs-* ]]; then
            branch_name="docs/${worktree_name#docs-}"
        else
            branch_name="$worktree_name"
        fi
    fi

    echo "📦 Branch: $branch_name"

    # Calculate worktree path
    local worktree_path="${main_project%/*}/SoftTrak-$worktree_name"
    echo "📁 Path: $worktree_path"

    # Allocate ports
    echo ""
    echo "🔌 Allocating ports..."
    local ports_json=$(allocate_ports "SoftTrak-$worktree_name")
    local backend_port=$(echo "$ports_json" | jq -r '.backend')
    local frontend_port=$(echo "$ports_json" | jq -r '.frontend')
    local db_port=$(echo "$ports_json" | jq -r '.database')
    local redis_port=$(echo "$ports_json" | jq -r '.redis')
    local playwright_port=$(echo "$ports_json" | jq -r '.playwright')
    local chrome_port=$(echo "$ports_json" | jq -r '.chrome_devtools')
    local puppeteer_port=$(echo "$ports_json" | jq -r '.puppeteer')

    echo "   Backend:        $backend_port"
    echo "   Frontend:       $frontend_port"
    echo "   Database:       $db_port"
    echo "   Redis:          $redis_port"
    echo "   Playwright:     $playwright_port"
    echo "   Chrome DevTools: $chrome_port"
    echo "   Puppeteer:      $puppeteer_port"

    # Create Git worktree
    echo ""
    echo "🌳 Creating Git worktree..."
    if ! git worktree add "$worktree_path" -b "$branch_name" 2>&1; then
        echo "❌ Failed to create Git worktree"
        free_ports "SoftTrak-$worktree_name"
        exit 1
    fi

    # Get worktree index for unique container names
    local worktree_index=$(jq '.worktrees | length' "$WORKTREES_JSON")

    # Generate docker-compose.worktree.yml
    echo "🐳 Generating Docker Compose configuration..."
    generate_from_template \
        "$TEMPLATES_DIR/docker-compose.worktree.template.yml" \
        "$worktree_path/docker-compose.worktree.yml" \
        "WORKTREE_NAME" "$worktree_name" \
        "BRANCH_NAME" "$branch_name" \
        "WORKTREE_PATH" "$worktree_path" \
        "MAIN_PROJECT_PATH" "$main_project" \
        "BACKEND_PORT" "$backend_port" \
        "FRONTEND_PORT" "$frontend_port" \
        "DB_PORT" "$db_port" \
        "REDIS_PORT" "$redis_port" \
        "PLAYWRIGHT_PORT" "$playwright_port" \
        "CHROME_DEVTOOLS_PORT" "$chrome_port" \
        "PUPPETEER_PORT" "$puppeteer_port" \
        "WORKTREE_INDEX" "$worktree_index"

    # Generate .mcp.json
    echo "🔧 Generating MCP configuration..."
    generate_from_template \
        "$TEMPLATES_DIR/mcp.template.json" \
        "$worktree_path/.mcp.json" \
        "WORKTREE_NAME" "$worktree_name" \
        "BRANCH_NAME" "$branch_name" \
        "WORKTREE_PATH" "$worktree_path" \
        "MAIN_PROJECT_PATH" "$main_project" \
        "BACKEND_PORT" "$backend_port" \
        "FRONTEND_PORT" "$frontend_port" \
        "DB_PORT" "$db_port" \
        "REDIS_PORT" "$redis_port" \
        "PLAYWRIGHT_PORT" "$playwright_port" \
        "CHROME_DEVTOOLS_PORT" "$chrome_port" \
        "PUPPETEER_PORT" "$puppeteer_port" \
        "WORKTREE_INDEX" "$worktree_index"

    # Generate start-worktree.sh
    echo "📝 Generating startup script..."
    generate_from_template \
        "$TEMPLATES_DIR/start-worktree.template.sh" \
        "$worktree_path/start-worktree.sh" \
        "WORKTREE_NAME" "$worktree_name" \
        "BRANCH_NAME" "$branch_name" \
        "WORKTREE_PATH" "$worktree_path" \
        "MAIN_PROJECT_PATH" "$main_project" \
        "BACKEND_PORT" "$backend_port" \
        "FRONTEND_PORT" "$frontend_port" \
        "DB_PORT" "$db_port" \
        "REDIS_PORT" "$redis_port" \
        "PLAYWRIGHT_PORT" "$playwright_port" \
        "CHROME_DEVTOOLS_PORT" "$chrome_port" \
        "PUPPETEER_PORT" "$puppeteer_port" \
        "WORKTREE_INDEX" "$worktree_index"

    chmod +x "$worktree_path/start-worktree.sh"

    # Verify generated files
    echo "🔍 Verifying generated files..."
    local all_files_ok=true

    if [ ! -f "$worktree_path/docker-compose.worktree.yml" ]; then
        echo "   ⚠️  docker-compose.worktree.yml not found"
        all_files_ok=false
    else
        echo "   ✅ docker-compose.worktree.yml"
    fi

    if [ ! -f "$worktree_path/.mcp.json" ]; then
        echo "   ⚠️  .mcp.json not found"
        all_files_ok=false
    else
        echo "   ✅ .mcp.json"
    fi

    if [ ! -f "$worktree_path/start-worktree.sh" ]; then
        echo "   ⚠️  start-worktree.sh not found"
        all_files_ok=false
    else
        echo "   ✅ start-worktree.sh"
    fi

    if [ "$all_files_ok" = false ]; then
        echo ""
        echo "⚠️  Warning: Some configuration files were not generated properly"
        echo "   The worktree was created but may not be fully configured"
    fi

    # Update worktree registry
    echo "📊 Updating registry..."
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    local temp_file=$(mktemp)
    jq ".worktrees += [{
        \"name\": \"SoftTrak-$worktree_name\",
        \"path\": \"$worktree_path\",
        \"branch\": \"$branch_name\",
        \"created\": \"$timestamp\",
        \"ports\": {
            \"backend\": $backend_port,
            \"frontend\": $frontend_port,
            \"database\": $db_port,
            \"playwright\": $playwright_port,
            \"chrome_devtools\": $chrome_port,
            \"puppeteer\": $puppeteer_port
        },
        \"status\": \"active\",
        \"docker_running\": false
    }]" "$WORKTREES_JSON" > "$temp_file"
    mv "$temp_file" "$WORKTREES_JSON"

    # Add .gitignore entries
    echo "📝 Updating .gitignore..."
    cd "$worktree_path"
    if [ ! -f .gitignore ]; then
        cp "$main_project/.gitignore" .gitignore 2>/dev/null || touch .gitignore
    fi

    # Add worktree-specific ignores
    echo "" >> .gitignore
    echo "# Worktree-specific files (not committed)" >> .gitignore
    echo "docker-compose.worktree.yml" >> .gitignore
    echo "start-worktree.sh" >> .gitignore
    echo ".browser-data/" >> .gitignore

    # Copy .env files from main project
    echo "📋 Copying environment files..."
    if [ -f "$main_project/backend/.env" ]; then
        cp "$main_project/backend/.env" "$worktree_path/backend/.env"

        # Update CORS allowed origins to include worktree frontend port
        echo "🔧 Configuring CORS for worktree port $frontend_port..."
        if grep -q "ALLOWED_ORIGINS=" "$worktree_path/backend/.env"; then
            # Check if port already exists in ALLOWED_ORIGINS
            if ! grep "ALLOWED_ORIGINS=" "$worktree_path/backend/.env" | grep -q "localhost:$frontend_port"; then
                # Add worktree frontend port to ALLOWED_ORIGINS
                sed -i.bak "s|\(ALLOWED_ORIGINS=.*\)|\1,http://localhost:$frontend_port|" "$worktree_path/backend/.env"
                rm "$worktree_path/backend/.env.bak"
                echo "   ✅ Added http://localhost:$frontend_port to ALLOWED_ORIGINS"
            else
                echo "   ✅ Port $frontend_port already in ALLOWED_ORIGINS"
            fi
        else
            # ALLOWED_ORIGINS not found, add it with common ports + worktree port
            echo "" >> "$worktree_path/backend/.env"
            echo "# CORS Settings" >> "$worktree_path/backend/.env"
            echo "ALLOWED_ORIGINS=http://localhost:4000,http://localhost:4001,http://localhost:4002,http://localhost:4003,http://localhost:4004,http://localhost:5173,http://localhost:3000,http://localhost:$frontend_port" >> "$worktree_path/backend/.env"
            echo "   ✅ Created ALLOWED_ORIGINS with worktree port $frontend_port"
        fi

        # Also update cors.rb to include worktree frontend port in development defaults
        if [ -f "$worktree_path/backend/config/initializers/cors.rb" ]; then
            echo "🔧 Updating CORS initializer for worktree port $frontend_port..."
            # Check if the worktree port is already in the cors.rb defaults
            if ! grep -A2 "Rails.env.development?" "$worktree_path/backend/config/initializers/cors.rb" | grep -q "localhost:$frontend_port"; then
                # Find the line with the development defaults array and add the worktree port
                sed -i.bak "/allowed_origins = \[.*localhost:4003/s|\]|, \"http://localhost:$frontend_port\"]|" "$worktree_path/backend/config/initializers/cors.rb"
                rm "$worktree_path/backend/config/initializers/cors.rb.bak"
                echo "   ✅ Added http://localhost:$frontend_port to cors.rb development defaults"
            else
                echo "   ✅ Port $frontend_port already in cors.rb development defaults"
            fi
        else
            echo "   ⚠️  cors.rb not found - CORS may need manual configuration"
        fi

        echo "   ✅ Copied backend/.env"
    else
        echo "   ⚠️  backend/.env not found in main project"
    fi

    if [ -f "$main_project/frontend/.env" ]; then
        cp "$main_project/frontend/.env" "$worktree_path/frontend/.env"

        # Update VITE_API_BASE_URL to point to worktree backend port
        echo "🔧 Configuring frontend API URL for backend port $backend_port..."
        if grep -q "VITE_API_BASE_URL=" "$worktree_path/frontend/.env"; then
            sed -i.bak "s|VITE_API_BASE_URL=http://localhost:[0-9]*/api/v1|VITE_API_BASE_URL=http://localhost:$backend_port/api/v1|g" "$worktree_path/frontend/.env"
            rm "$worktree_path/frontend/.env.bak"
            echo "   ✅ Updated VITE_API_BASE_URL to http://localhost:$backend_port/api/v1"
        else
            echo "" >> "$worktree_path/frontend/.env"
            echo "# Worktree-specific API URL" >> "$worktree_path/frontend/.env"
            echo "VITE_API_BASE_URL=http://localhost:$backend_port/api/v1" >> "$worktree_path/frontend/.env"
            echo "   ✅ Added VITE_API_BASE_URL=http://localhost:$backend_port/api/v1"
        fi

        echo "   ✅ Copied frontend/.env"
    else
        echo "   ⚠️  frontend/.env not found in main project"
    fi

    # Also update frontend/.env.development if it exists
    if [ -f "$main_project/frontend/.env.development" ]; then
        cp "$main_project/frontend/.env.development" "$worktree_path/frontend/.env.development"

        echo "🔧 Configuring frontend/.env.development for backend port $backend_port..."
        if grep -q "VITE_API_BASE_URL=" "$worktree_path/frontend/.env.development"; then
            sed -i.bak "s|VITE_API_BASE_URL=http://localhost:[0-9]*/api/v1|VITE_API_BASE_URL=http://localhost:$backend_port/api/v1|g" "$worktree_path/frontend/.env.development"
            rm "$worktree_path/frontend/.env.development.bak"
            echo "   ✅ Updated .env.development VITE_API_BASE_URL to http://localhost:$backend_port/api/v1"
        else
            echo "" >> "$worktree_path/frontend/.env.development"
            echo "# Worktree-specific API URL" >> "$worktree_path/frontend/.env.development"
            echo "VITE_API_BASE_URL=http://localhost:$backend_port/api/v1" >> "$worktree_path/frontend/.env.development"
            echo "   ✅ Added VITE_API_BASE_URL to .env.development"
        fi

        echo "   ✅ Copied and configured frontend/.env.development"
    fi

    if [ -f "$main_project/.env" ]; then
        cp "$main_project/.env" "$worktree_path/.env"
        # Update the ports in the .env file to match allocated worktree ports
        sed -i.bak "s/^BACKEND_PORT=.*/BACKEND_PORT=$backend_port/" "$worktree_path/.env"
        sed -i.bak "s/^FRONTEND_PORT=.*/FRONTEND_PORT=$frontend_port/" "$worktree_path/.env"
        sed -i.bak "s/^DB_PORT=.*/DB_PORT=$db_port/" "$worktree_path/.env"
        sed -i.bak "s/^REDIS_PORT=.*/REDIS_PORT=$redis_port/" "$worktree_path/.env"
        rm "$worktree_path/.env.bak"
        echo "   ✅ Copied root .env (updated with worktree ports)"
    else
        # Create .env file with worktree-specific ports if it doesn't exist
        cat > "$worktree_path/.env" <<EOF
# Worktree-specific port configuration
BACKEND_PORT=$backend_port
FRONTEND_PORT=$frontend_port
DB_PORT=$db_port
REDIS_PORT=$redis_port

# Database credentials (same as main project)
POSTGRES_USERNAME={{POSTGRES_USERNAME}}
POSTGRES_PASSWORD={{POSTGRES_PASSWORD}}
EOF
        echo "   ✅ Created root .env with worktree ports"
    fi

    # Create browser isolation directory for MCP servers
    echo "🌐 Setting up browser isolation..."
    mkdir -p "$worktree_path/.browser-data"
    echo "   ✅ Created .browser-data directory for isolated browser profiles"

    # Start services if requested
    if [ "$start_services" = true ]; then
        echo ""

        # Pre-flight port validation before Docker startup
        if ! validate_all_ports $backend_port $frontend_port $db_port $redis_port \
                                $playwright_port $chrome_port $puppeteer_port; then
            # Validation failed - port conflicts detected
            echo ""
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo "⚠️  WORKTREE CREATED - SERVICES NOT STARTED"
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo ""
            echo "✅ Worktree setup completed successfully:"
            echo "   • Git worktree created"
            echo "   • Configuration files generated"
            echo "   • Ports allocated in registry"
            echo "   • Environment files copied"
            echo "   • Browser isolation configured"
            echo ""
            echo "❌ Docker services not started due to port conflicts"
            echo "   (See conflict details above)"
            echo ""
            echo "📍 Worktree Location:"
            echo "   $worktree_path"
            echo ""
            echo "🔧 Next Steps:"
            echo "   1. Resolve port conflicts using options above"
            echo "   2. Navigate to worktree: cd $worktree_path"
            echo "   3. Start services: ./start-worktree.sh"
            echo "   4. Launch Claude: claude"
            echo ""

            # Don't exit - worktree was created successfully
            # Registry stays as docker_running: false (default)
        else
            # Validation passed - proceed with Docker startup
            echo "🚀 Starting Docker services..."
            cd "$worktree_path"

            # Start Docker services with error handling
            if ./start-worktree.sh; then
                # Startup successful
                echo ""
                echo "✅ Docker services started successfully!"

                # Update registry
                local temp_file=$(mktemp)
                jq "(.worktrees[] | select(.name == \"SoftTrak-$worktree_name\") | .docker_running) = true" \
                    "$WORKTREES_JSON" > "$temp_file"
                mv "$temp_file" "$WORKTREES_JSON"
            else
                # Startup failed despite validation
                echo ""
                echo "⚠️  Docker startup encountered errors despite port validation"
                echo ""
                echo "This may indicate:"
                echo "  • Resource constraints (memory, disk space)"
                echo "  • Image pull failures"
                echo "  • Configuration issues"
                echo ""
                echo "📋 Troubleshooting:"
                echo "  1. Check Docker logs: docker-compose logs"
                echo "  2. Verify Docker is running: docker info"
                echo "  3. Try manual startup: cd $worktree_path && ./start-worktree.sh"
                echo ""

                # Registry stays as docker_running: false (default)
            fi
        fi
    fi

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "✅ Worktree created successfully!"
    echo ""
    echo "📍 Location: $worktree_path"
    echo "🌿 Branch: $branch_name"
    echo ""
    echo "🔌 Ports:"
    echo "   Backend:        http://localhost:$backend_port"
    echo "   Frontend:       http://localhost:$frontend_port"
    echo "   Database:       localhost:$db_port"
    echo "   Playwright:     localhost:$playwright_port"
    echo "   Chrome DevTools: localhost:$chrome_port"
    echo "   Puppeteer:      localhost:$puppeteer_port"
    echo ""
    echo "🚀 IMPORTANT: Next Steps"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "You are still in the ORIGINAL Claude Code session."
    echo "To work in the new worktree:"
    echo ""
    echo "1. Exit this Claude Code session (Ctrl+D or /exit)"
    echo "2. Navigate to worktree:"
    echo "   cd $worktree_path"
    if [ "$start_services" != true ]; then
        echo "3. Start services:"
        echo "   ./start-worktree.sh"
        echo "4. Launch NEW Claude Code session:"
    else
        echo "3. Launch NEW Claude Code session:"
    fi
    echo "   claude"
    echo ""
    echo "💡 Tip: You can run multiple Claude sessions in parallel:"
    echo "   - Terminal 1: Original project (main branch)"
    echo "   - Terminal 2: This worktree ($worktree_name)"
    echo "   - Terminal 3: Another worktree (different feature)"
    echo ""
    echo "Each session is completely isolated with its own:"
    echo "   ✓ Docker services (different ports)"
    echo "   ✓ Database (independent data)"
    echo "   ✓ Conversation history (fresh context)"
    echo ""

    # Add port validation status
    echo "🔍 Port Validation:"
    if [ "$start_services" = true ]; then
        if [ "$(jq -r ".worktrees[] | select(.name == \"SoftTrak-$worktree_name\") | .docker_running" "$WORKTREES_JSON")" = "true" ]; then
            echo "   ✅ All ports validated and services started"
        else
            echo "   ⚠️  Port conflicts detected - services not started"
            echo "   ℹ️  Run ./start-worktree.sh after resolving conflicts"
        fi
    else
        echo "   ℹ️  Services not auto-started (use --start-services)"
    fi
    echo ""
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LIST WORKTREES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

list_worktrees() {
    local show_status=${1:-false}

    echo "📋 Active Worktrees"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    local count=$(jq '.worktrees | length' "$WORKTREES_JSON")

    if [ "$count" -eq 0 ]; then
        echo "No worktrees found."
        echo ""
        echo "Create one with: @worktree create <name>"
        return
    fi

    for i in $(seq 0 $((count - 1))); do
        local worktree=$(jq -r ".worktrees[$i]" "$WORKTREES_JSON")
        local name=$(echo "$worktree" | jq -r '.name')
        local path=$(echo "$worktree" | jq -r '.path')
        local branch=$(echo "$worktree" | jq -r '.branch')
        local created=$(echo "$worktree" | jq -r '.created')
        local docker_running=$(echo "$worktree" | jq -r '.docker_running')
        local ports=$(echo "$worktree" | jq -r '.ports')

        echo ""
        echo "$((i + 1)). $name"
        echo "   Branch: $branch"
        echo "   Path:   $path"
        echo "   Created: $created"

        if [ "$show_status" = true ]; then
            if [ "$docker_running" = true ]; then
                echo "   Status: 🟢 Running"
            else
                echo "   Status: 🔴 Stopped"
            fi
        fi

        local backend=$(echo "$ports" | jq -r '.backend')
        local frontend=$(echo "$ports" | jq -r '.frontend')
        echo "   Ports:  Backend $backend, Frontend $frontend"
    done

    echo ""
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# REMOVE WORKTREE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

remove_worktree() {
    local worktree_name=$1
    local delete_branch=${2:-false}
    local force=${3:-false}

    echo "🗑️  Removing worktree: $worktree_name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    # Check if worktree exists
    if ! worktree_exists "SoftTrak-$worktree_name"; then
        echo "❌ Error: Worktree 'SoftTrak-$worktree_name' not found"
        exit 1
    fi

    # Get worktree info
    local worktree=$(jq -r ".worktrees[] | select(.name == \"SoftTrak-$worktree_name\")" "$WORKTREES_JSON")
    local path=$(echo "$worktree" | jq -r '.path')
    local branch=$(echo "$worktree" | jq -r '.branch')
    local docker_running=$(echo "$worktree" | jq -r '.docker_running')

    # Check for uncommitted changes
    if [ "$force" != true ]; then
        cd "$path"
        if ! git diff-index --quiet HEAD --; then
            echo "⚠️  Warning: Worktree has uncommitted changes"
            echo ""
            git status --short
            echo ""
            read -p "Continue with removal? [y/N] " -n 1 -r
            echo
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                echo "Aborted."
                exit 0
            fi
        fi
    fi

    # Stop Docker services - always attempt cleanup regardless of registry flag
    echo "🐳 Cleaning up Docker services..."
    cd "$path"

    # Remove containers specific to this worktree
    # Container names include the worktree name, so this is safe
    echo "   Removing worktree-specific containers..."
    for container in backend-$worktree_name frontend-$worktree_name db-$worktree_name redis-$worktree_name; do
        if docker ps -a --format '{{.Names}}' | grep -q "^${container}$"; then
            echo "   Removing container: $container"
            docker rm -f "$container" 2>/dev/null || true
        fi
    done

    # Remove worktree-specific volumes
    echo "   Removing worktree-specific volumes..."
    for volume in db_data_$worktree_name redis_data_$worktree_name; do
        if docker volume ls --format '{{.Name}}' | grep -q "^${volume}$"; then
            echo "   Removing volume: $volume"
            docker volume rm "$volume" 2>/dev/null || true
        fi
    done

    # Remove Git worktree
    echo "🌳 Removing Git worktree..."
    local main_project=$(get_main_project)
    cd "$main_project"
    git worktree remove "$path" --force

    # Delete branch if requested
    if [ "$delete_branch" = true ]; then
        echo "🌿 Deleting branch: $branch"
        git branch -D "$branch" 2>/dev/null || true
    fi

    # Free ports
    echo "🔌 Freeing ports..."
    free_ports "SoftTrak-$worktree_name"

    # Update registry
    echo "📊 Updating registry..."
    local temp_file=$(mktemp)
    jq "del(.worktrees[] | select(.name == \"SoftTrak-$worktree_name\"))" \
        "$WORKTREES_JSON" > "$temp_file"
    mv "$temp_file" "$WORKTREES_JSON"

    echo ""
    echo "✅ Worktree removed successfully!"
    echo ""
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MAIN COMMAND DISPATCHER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

main() {
    local command=$1
    shift

    case "$command" in
        create)
            local name=$1
            local branch=""
            local start_services=true

            shift
            while [[ $# -gt 0 ]]; do
                case $1 in
                    --branch=*)
                        branch="${1#*=}"
                        shift
                        ;;
                    --start-services)
                        start_services=true
                        shift
                        ;;
                    --no-start-services)
                        start_services=false
                        shift
                        ;;
                    *)
                        shift
                        ;;
                esac
            done

            create_worktree "$name" "$branch" "$start_services"
            ;;

        list)
            local show_status=false
            if [[ $1 == "--status" ]]; then
                show_status=true
            fi
            list_worktrees "$show_status"
            ;;

        remove)
            local name=$1
            local delete_branch=false
            local force=false

            shift
            while [[ $# -gt 0 ]]; do
                case $1 in
                    --delete-branch)
                        delete_branch=true
                        shift
                        ;;
                    --force)
                        force=true
                        shift
                        ;;
                    *)
                        shift
                        ;;
                esac
            done

            remove_worktree "$name" "$delete_branch" "$force"
            ;;

        *)
            echo "❌ Unknown command: $command"
            echo ""
            echo "Usage:"
            echo "  worktree-manager.sh create <name> [--branch=<branch>] [--start-services]"
            echo "  worktree-manager.sh list [--status]"
            echo "  worktree-manager.sh remove <name> [--delete-branch] [--force]"
            exit 1
            ;;
    esac
}

# Run main function
main "$@"
