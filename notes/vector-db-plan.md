# Plan: Vector Database for Electrical Code Reference

## Goal

Build a searchable vector database from the "Illustrated Guide to the National Electrical Code 6th Edition" PDF so we can quickly look up code sections, ampacity tables, installation requirements, etc. during the project.

## Source

- **File:** `Illustrated Guide to the National Electrical Code 6th Edition by Charles R. Miller (1).pdf`
- **Size:** ~61MB
- **Location:** `/Users/ian/Development/garage_work/`

## Steps

### 1. Extract text from PDF
- Use a Python PDF library (PyPDF2, pdfplumber, or pymupdf/fitz) to extract text page by page
- Preserve page numbers for citation back to source
- Handle tables (ampacity charts, etc.) — these may need special extraction

### 2. Chunk the text
- Split into chunks of ~500-1000 tokens each
- Chunk by section/heading where possible (NEC articles are naturally structured)
- Include overlap between chunks (~100 tokens) to avoid losing context at boundaries
- Tag each chunk with metadata: page number, chapter/article if detectable

### 3. Generate embeddings
- Use an embedding model to convert each chunk to a vector
- Options:
  - **OpenAI `text-embedding-3-small`** — good quality, requires API key
  - **Sentence-transformers (local)** — free, runs locally, e.g. `all-MiniLM-L6-v2`
  - **Anthropic Voyage** — if available
- Store embeddings alongside the chunk text and metadata

### 4. Store in a vector database
- Options:
  - **ChromaDB** — simple, local, Python-native, good for small projects
  - **FAISS** — Facebook's library, fast, local
  - **SQLite + numpy** — minimal dependencies, just cosine similarity search
  - **LanceDB** — local, no server needed
- ChromaDB is probably the sweet spot: easy setup, persistent storage, built-in embedding support

### 5. Build a query interface
- A Python script or Claude Code skill that:
  1. Takes a natural language query
  2. Embeds the query
  3. Searches the vector DB for top-k similar chunks
  4. Returns the relevant chunks with page numbers
- Could integrate with the existing `/lookup` skill

## Tech Stack (Recommended)

```
Python 3.9+
pymupdf (fitz) — PDF text extraction (handles tables better than PyPDF2)
chromadb — vector storage and search
sentence-transformers — local embeddings (no API key needed)
```

## Directory Structure

```
garage_work/
├── nec_vectordb/
│   ├── ingest.py          — extract PDF, chunk, embed, store
│   ├── query.py           — search the vector DB
│   ├── requirements.txt   — dependencies
│   └── chroma_db/         — persistent ChromaDB storage (gitignored)
```

## Open Questions

- [ ] Does pymupdf extract tables from this PDF cleanly, or do we need OCR?
- [ ] What embedding model to use? (local sentence-transformers avoids API costs)
- [ ] Should the vector DB be gitignored (large) or committed (portable)?
- [ ] Do we want a Claude Code skill (`/nec`) to query it inline?

## Alternatives Considered

- **Just use Claude's knowledge** — works for common code sections but can't cite specific pages, and we've seen it get numbers wrong (e.g., the ampacity table earlier)
- **Full-text search (grep)** — works if text extracts cleanly, but no semantic understanding
- **Manual index** — too labor intensive for a 600+ page book
