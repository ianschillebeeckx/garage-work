Look up electrical code requirements using the NEC vector database and web search.

## Instructions

1. Read `plan.md` to understand the full project scope and current status.
2. Read the relevant files in `permits/` for existing research on the topic.
3. The user's query is: $ARGUMENTS

### Step 1: Query the NEC Vector Database

First, check that the venv is activated by running:
```bash
python3 -c "import chromadb" 2>/dev/null || echo "VENV_NOT_ACTIVE"
```

If the venv is not active, tell the user to activate it:
```bash
source .venv/bin/activate
```

Then query the NEC guide vector database. Run **6 queries** — the user's raw question plus 5 reformulations that ask the same thing in different ways (different terminology, more specific, more general, focusing on different aspects). This improves recall since vector search is sensitive to phrasing.

**Run all 6 queries in parallel** by making 6 separate Bash tool calls in a single message:

```bash
python3 nec_vectordb/query.py "the raw user question" --top 3
```
```bash
python3 nec_vectordb/query.py "reformulation 1" --top 3
```
```bash
python3 nec_vectordb/query.py "reformulation 2" --top 3
```
```bash
python3 nec_vectordb/query.py "reformulation 3" --top 3
```
```bash
python3 nec_vectordb/query.py "reformulation 4" --top 3
```
```bash
python3 nec_vectordb/query.py "reformulation 5" --top 3
```

### Step 2: Assess Vector DB Results

After running all 6 queries, assess the quality of results:

**Strong results** — the returned chunks directly discuss the topic, cite specific NEC sections, and similarity scores are above 0.6. These are **high confidence** findings from a trusted source.

**Weak or no results** — the returned chunks are tangentially related or similarity scores are below 0.5. This is a signal that the topic may be **newer than the book** (the NEC guide is 6th edition, pre-2020 NEC). Flag this clearly.

### Step 3: Web Search

The purpose of web search depends on the vector DB result quality:

**If vector DB returned strong results:**
- Web search is supplementary — use it to check if the 2020 or 2023 NEC **changed, expanded, or overrode** the sections found in the vector DB
- Look for NEC code cycle changes (2020, 2023) that affect those sections
- Check San Francisco local amendments (SF Electrical Code, Section 89)

**If vector DB returned weak or no results:**
- This topic is likely newer code not in the book. Web search is the primary source.
- Search specifically for the relevant NEC article text
- Look for which NEC cycle introduced the requirement (2020? 2023?)
- Check California Electrical Code (CEC) adoption status

### Step 4: Synthesize with Source Tiers

Present findings to the user with clear source attribution using these tiers:

**Tier 1 — NEC Guide (vector DB):** High confidence. Cite the NEC section number AND the page number from the guide (e.g., "NEC 210.8(A)(2), p.160 of Illustrated Guide to the NEC"). This is the trusted baseline.

**Tier 2 — Web-confirmed update:** The vector DB had the base requirement, and web search confirmed the current NEC cycle preserves or expands it. Cite both sources.

**Tier 3 — Web-only (newer code):** Not found in the NEC guide. This is likely a 2020 or 2023 NEC addition. Cite the URL and note the NEC cycle. Flag to the user: *"Not found in the NEC guide (pre-2020 edition). The following is from web sources and reflects [2020/2023] NEC additions."*

**Conflict:** If web results contradict the vector DB, present both positions. The newer NEC cycle may override, but the user should see the discrepancy and understand what changed.

### Step 5: Update Project Files

After researching, update the relevant file(s) in `permits/` or `decisions/` with what you found. Mark each finding with its source tier and citation.

## Tips

- This skill is for **electrical code only**. For plumbing, building, or other codes, use web search directly.
- The vector DB contains the "Illustrated Guide to the National Electrical Code 6th Edition" — it explains NEC requirements with illustrations and examples, but is not the NEC text itself. It predates the 2020 NEC cycle.
- San Francisco has adopted the California Electrical Code (CEC), which is based on the NEC with California amendments.
- The NEC guide PDF pages are offset by +14 from the printed page numbers (PDF page 200 = printed page 186).
- When in doubt, the vector DB reduces **false positives** (it won't make things up) while web search reduces **false negatives** (it catches newer requirements). Use both.
