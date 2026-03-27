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

```bash
python3 nec_vectordb/query.py "the raw user question" --top 3
python3 nec_vectordb/query.py "reformulation 1" --top 3
python3 nec_vectordb/query.py "reformulation 2" --top 3
python3 nec_vectordb/query.py "reformulation 3" --top 3
python3 nec_vectordb/query.py "reformulation 4" --top 3
python3 nec_vectordb/query.py "reformulation 5" --top 3
```

Review all results. Note the **page numbers** and any **section/unit headings** visible in the text. Deduplicate results that appear across multiple queries. If no relevant results are returned from any query, tell the user that nothing was found in the NEC guide for this topic.

### Step 2: Web Search

Use web search to supplement the vector DB results with:
- The specific NEC article text (if the vector DB returned a section number but not the full text)
- San Francisco local electrical code amendments (SF Electrical Code, Section 89)
- California Electrical Code (CEC) differences from the NEC
- Inspection requirements and what electrical inspectors typically look for

### Step 3: Synthesize and Cite

Combine findings from the vector DB and web search. For every code reference:
- Cite the **NEC section number** (e.g., 210.8(A)(2))
- Cite the **page number** from the NEC guide (e.g., "p.160 of Illustrated Guide to the NEC")
- Cite the **URL** for web-sourced findings

### Step 4: Update Project Files

After researching, update the relevant file(s) in `permits/` or `decisions/` with what you found. Clearly mark sourced information with the NEC section and page number or URL.

## Tips

- This skill is for **electrical code only**. For plumbing, building, or other codes, use web search directly.
- The vector DB contains the "Illustrated Guide to the National Electrical Code 6th Edition" — it explains NEC requirements with illustrations and examples, but is not the NEC text itself.
- San Francisco has adopted the California Electrical Code (CEC), which is based on the NEC with California amendments.
- The NEC guide PDF pages are offset by +14 from the printed page numbers (PDF page 200 = printed page 186).
