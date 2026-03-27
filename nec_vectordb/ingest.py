#!/usr/bin/env python3
"""
Ingest the NEC guide PDF into a ChromaDB vector database.

Usage:
    python nec_vectordb/ingest.py <path_to_pdf>

This script:
1. Extracts text from each page of the PDF
2. Chunks the text into ~500 token segments with overlap
3. Embeds each chunk using sentence-transformers (all-MiniLM-L6-v2)
4. Stores everything in a persistent ChromaDB database

Run once. The database is stored in nec_vectordb/chroma_db/
"""

import argparse
import os
import sys

import fitz  # pymupdf
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from text_normalize import replace_ligatures


# --- Config ---
CHUNK_SIZE = 800  # characters (~200 tokens)
CHUNK_OVERLAP = 150  # characters overlap between chunks
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "nec_guide"
DB_PATH = os.path.join(os.path.dirname(__file__), "chroma_db")
STRIP_PHRASES_PATH = os.path.join(os.path.dirname(__file__), "strip_phrases.txt")
DEFAULT_PDF = os.path.join(
    os.path.dirname(__file__),
    "Illustrated Guide to the National Electrical Code 6th Edition by Charles R. Miller (1).pdf",
)


def load_strip_phrases() -> list[str]:
    """Load phrases to strip from extracted text."""
    if not os.path.exists(STRIP_PHRASES_PATH):
        return []
    with open(STRIP_PHRASES_PATH) as f:
        return [line.strip() for line in f if line.strip()]


def extract_pages(pdf_path: str) -> list[dict]:
    """Extract text from each page of the PDF.

    TODO: Parse chapter/section/unit headings from extracted text and attach
    as metadata (e.g., "Section 2: One-Family Dwellings", "Unit 8: Branch
    Circuits and Feeders"). This would improve search by letting us filter
    or boost results by section, and provide better citations in query output.

    TODO: Figures are currently extracted as raw label text (e.g., "A", "B",
    "C" callouts) which lacks context without the image. Two improvements:
    1. Convert figure text/captions into readable prose that stands alone.
    2. Extract each figure as an image and generate a text description
       (e.g., via a vision model) so the diagram content is searchable.
    """
    strip_phrases = load_strip_phrases()
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text()
        text = replace_ligatures(text)
        for phrase in strip_phrases:
            text = text.replace(phrase, "")
        if text.strip():
            pages.append({"page": i + 1, "text": text})
    doc.close()
    print(f"Extracted text from {len(pages)} pages (of {total_pages} total)")
    return pages


def chunk_text(text: str, page_num: int) -> list[dict]:
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunk = text[start:end]

        # Try to break at a sentence boundary
        if end < len(text):
            # Look for last period, newline, or semicolon in the chunk
            for sep in ["\n\n", ".\n", ". ", "\n"]:
                last_sep = chunk.rfind(sep)
                if last_sep > CHUNK_SIZE // 2:
                    chunk = chunk[: last_sep + len(sep)]
                    end = start + len(chunk)
                    break

        chunk = chunk.strip()
        if chunk:
            chunks.append(
                {
                    "text": chunk,
                    "page": page_num,
                    "start_char": start,
                }
            )
        start = end - CHUNK_OVERLAP

    return chunks


def ingest(pdf_path: str):
    """Main ingestion pipeline."""
    if not os.path.exists(pdf_path):
        print(f"Error: PDF not found: {pdf_path}")
        sys.exit(1)

    print(f"PDF: {pdf_path}")
    print(f"DB path: {DB_PATH}")
    print(f"Embedding model: {EMBEDDING_MODEL}")
    print(f"Chunk size: {CHUNK_SIZE} chars, overlap: {CHUNK_OVERLAP} chars")
    print()

    # Extract text
    print("Extracting text from PDF...")
    pages = extract_pages(pdf_path)

    # Chunk
    print("Chunking text...")
    all_chunks = []
    for page_data in pages:
        chunks = chunk_text(page_data["text"], page_data["page"])
        all_chunks.extend(chunks)
    print(f"Created {len(all_chunks)} chunks")

    # Initialize ChromaDB with sentence-transformer embedding
    print(f"Initializing ChromaDB at {DB_PATH}...")
    embedding_fn = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)

    # Remove existing DB for clean rebuild
    client = chromadb.PersistentClient(path=DB_PATH)
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_fn,
        metadata={"description": "Illustrated Guide to the NEC 6th Edition"},
    )

    # Batch insert (ChromaDB has a batch limit)
    batch_size = 100
    total = len(all_chunks)
    for i in range(0, total, batch_size):
        batch = all_chunks[i : i + batch_size]
        collection.add(
            ids=[f"chunk_{i + j}" for j in range(len(batch))],
            documents=[c["text"] for c in batch],
            metadatas=[{"page": c["page"], "start_char": c["start_char"]} for c in batch],
        )
        print(f"  Embedded and stored {min(i + batch_size, total)}/{total} chunks")

    print()
    print(f"Done. {total} chunks stored in {DB_PATH}")
    print(f"Collection: {COLLECTION_NAME}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest NEC guide PDF into vector DB")
    parser.add_argument("pdf_path", nargs="?", default=DEFAULT_PDF, help="Path to the PDF file")
    args = parser.parse_args()
    ingest(args.pdf_path)
