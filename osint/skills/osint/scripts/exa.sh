#!/bin/bash
# Exa AI — semantic search, company research, people search, deep research
# Usage: exa.sh search "query"
#        exa.sh company "company name"
#        exa.sh people "person name"
#        exa.sh crawl "url"
#        exa.sh deep "research prompt"
set -euo pipefail

CMD="${1:?Usage: exa.sh search|company|people|crawl|deep <query>}"
QUERY="${2:?Missing query}"
EXA_API_KEY="${EXA_API_KEY:-}"

if [ -n "$EXA_API_KEY" ]; then
  BASE="https://api.exa.ai"
else
  echo "⚠️  No EXA_API_KEY, cannot proceed" >&2
  exit 1
fi

case "$CMD" in
  search)
    curl -s "$BASE/search" \
      -H "x-api-key: $EXA_API_KEY" \
      -H "Content-Type: application/json" \
      -d "{
        \"query\": \"$QUERY\",
        \"type\": \"auto\",
        \"numResults\": 10,
        \"contents\": {\"text\": {\"maxCharacters\": 500}}
      }" | python3 -c "
import json, sys
d = json.load(sys.stdin)
for r in d.get('results', [])[:10]:
    print(f'🔗 {r.get(\"title\",\"\")}')
    print(f'   {r.get(\"url\",\"\")}')
    txt = r.get('text','')[:200]
    if txt: print(f'   {txt}')
    print()
"
    ;;
  company)
    curl -s "$BASE/search" \
      -H "x-api-key: $EXA_API_KEY" \
      -H "Content-Type: application/json" \
      -d "{
        \"query\": \"$QUERY company information about\",
        \"type\": \"auto\",
        \"numResults\": 10,
        \"contents\": {\"text\": {\"maxCharacters\": 1000}},
        \"category\": \"company\"
      }" | python3 -c "
import json, sys
d = json.load(sys.stdin)
for r in d.get('results', [])[:10]:
    print(f'🏢 {r.get(\"title\",\"\")}')
    print(f'   {r.get(\"url\",\"\")}')
    txt = r.get('text','')[:300]
    if txt: print(f'   {txt}')
    print()
"
    ;;
  people)
    curl -s "$BASE/search" \
      -H "x-api-key: $EXA_API_KEY" \
      -H "Content-Type: application/json" \
      -d "{
        \"query\": \"$QUERY\",
        \"type\": \"auto\",
        \"numResults\": 10,
        \"contents\": {\"text\": {\"maxCharacters\": 500}},
        \"category\": \"personal site\"
      }" | python3 -c "
import json, sys
d = json.load(sys.stdin)
for r in d.get('results', [])[:10]:
    print(f'👤 {r.get(\"title\",\"\")}')
    print(f'   {r.get(\"url\",\"\")}')
    txt = r.get('text','')[:200]
    if txt: print(f'   {txt}')
    print()
"
    ;;
  crawl)
    curl -s "$BASE/contents" \
      -H "x-api-key: $EXA_API_KEY" \
      -H "Content-Type: application/json" \
      -d "{
        \"urls\": [\"$QUERY\"],
        \"text\": {\"maxCharacters\": 5000}
      }" | python3 -c "
import json, sys
d = json.load(sys.stdin)
for r in d.get('results', []):
    print(f'📄 {r.get(\"title\",\"\")}')
    print(f'   {r.get(\"url\",\"\")}')
    print(r.get('text','')[:3000])
"
    ;;
  deep)
    echo "🔬 Exa Deep Research — use MCP or dashboard for this"
    echo "   MCP endpoint: https://mcp.exa.ai/mcp?tools=deep_researcher_start,deep_researcher_check"
    ;;
  *)
    echo "Unknown command: $CMD (use search|company|people|crawl|deep)" >&2; exit 1
    ;;
esac
