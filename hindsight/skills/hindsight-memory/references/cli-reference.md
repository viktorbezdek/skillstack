# Hindsight CLI reference (for this integration)

The `hindsight` CLI (verify: `hindsight version`) is the transport for this
plugin. It resolves the API endpoint from `HINDSIGHT_API_URL` / `HINDSIGHT_API_KEY`
or a named profile (`-p <name>`). Global flags: `-o pretty|json|yaml` (default
`pretty`; use `json` when parsing), `-v` verbose, `-p` profile.

Only the commands the integration actually uses are documented here. For any
subcommand, `hindsight <group> <cmd> --help` is authoritative.

## memory — the day-to-day surface

```bash
# recall: semantic search → ranked hits (this is what the UserPromptSubmit hook runs)
hindsight memory recall <BANK_ID> <QUERY> [OPTIONS]
#   -t, --fact-type <world|experience|opinion>   (repeatable; default: all three)
#   -b, --budget <low|mid|high>                  thinking budget (latency knob)
#       --max-tokens <N>                         cap on result size (default 4096)
#       --tags <a,b>  --tags-match <any|all|any_strict|all_strict>
#       --query-timestamp <ISO8601>              reference time for recency
#       --include-chunks                         also return source chunks

# reflect: synthesized ANSWER in the bank's voice (reasons over recalled memories)
hindsight memory reflect <BANK_ID> <QUERY> [-b low|mid|high] [-m MAX_TOKENS] [-c CONTEXT]

# retain: store one memory
hindsight memory retain <BANK_ID> <CONTENT> [-d DOC_ID] [-c CONTEXT] [--async] [-t TIMESTAMP]
#   -d/--doc-id: stable id → re-retain REPLACES (idempotent). Omit → auto-generated.
#   --async:     queue for background fact extraction (what the Stop hook uses)

# inspect / maintain
hindsight memory list <BANK_ID>            # list memory units (paginated)
hindsight memory get <MEMORY_ID>
hindsight memory history <MEMORY_ID>       # observation history for a unit
hindsight memory retain-files <BANK_ID> <FILES...>   # bulk import
hindsight memory delete <MEMORY_ID>
hindsight memory clear <BANK_ID>           # destructive: wipe all memories
```

**recall vs reflect:** `recall` returns evidence (`text`, `type`, `mentioned_at`);
`reflect` returns a conclusion synthesized from that evidence. Want the raw
facts → recall. Want an answer → reflect.

## bank — isolated memory stores ("brains")

```bash
hindsight bank list
hindsight bank create <BANK_ID> [-n NAME] [-m MISSION]
hindsight bank stats <BANK_ID>             # counts: memories, entities, etc.
hindsight bank disposition <BANK_ID>       # profile + disposition traits
hindsight bank mission <BANK_ID> <TEXT>    # identity/purpose used during recall
hindsight bank graph <BANK_ID>             # memory graph data
hindsight bank consolidate <BANK_ID>       # build/update observations from memories
hindsight bank export-template <BANK_ID>   # config + mental models + directives
hindsight bank import-template <FILE>
hindsight bank delete <BANK_ID>            # destructive: bank + all data
```

## entity / mental-model / directive — curation

```bash
hindsight entity list <BANK_ID>            # entities extracted from memories
hindsight entity get <ENTITY_ID>
hindsight entity regenerate <ENTITY_ID>    # rebuild an entity's profile

hindsight mental-model ...                 # user-curated summaries (see --help)
hindsight directive ...                    # behavioral rules for the bank (see --help)
```

## documents & operations

```bash
hindsight document list <BANK_ID>          # raw retained documents (pre-extraction)
hindsight document get <DOC_ID>
hindsight operation list                   # async jobs (e.g. queued retains)
hindsight operation get <OP_ID>
```

## system & interactive

```bash
hindsight health                           # API + DB reachability (SessionStart hook)
hindsight version
hindsight explore                          # k9s-style TUI over banks/memories/entities
hindsight ui                               # web control-plane
hindsight configure                        # set API URL / key
hindsight profile list                     # named connection profiles
```

## Destructive commands — handle with care

`memory clear`, `memory delete`, `bank delete`, `document delete` permanently
remove data. Never run them as part of recall/retain automation; reserve them
for explicit, confirmed user requests.
