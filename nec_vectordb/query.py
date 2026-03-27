#!/usr/bin/env python3
"""
Query the NEC guide vector database.

Usage:
    python nec_vectordb/query.py "what wire size for 100 amp feeder"
    python nec_vectordb/query.py --top 10 "GFCI requirements for garages"
"""

import argparse
import os
import sys

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


# --- Config ---
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "nec_guide"
DB_PATH = os.path.join(os.path.dirname(__file__), "chroma_db")


def query(query_text: str, top_k: int = 5):
    """Search the vector DB and print results."""
    if not os.path.exists(DB_PATH):
        print(f"Error: Database not found at {DB_PATH}")
        print("Run ingest.py first to build the database.")
        sys.exit(1)

    embedding_fn = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    client = chromadb.PersistentClient(path=DB_PATH)

    try:
        collection = client.get_collection(
            name=COLLECTION_NAME,
            embedding_function=embedding_fn,
        )
    except ValueError:
        print(f"Error: Collection '{COLLECTION_NAME}' not found.")
        print("Run ingest.py first to build the database.")
        sys.exit(1)

    results = collection.query(
        query_texts=[query_text],
        n_results=top_k,
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    print(f"Query: {query_text}")
    print(f"Results: {len(documents)} (top {top_k})")
    print("=" * 80)

    for i, (doc, meta, dist) in enumerate(zip(documents, metadatas, distances)):
        similarity = 1 - dist  # ChromaDB returns L2 distance by default
        print(f"\n--- Result {i + 1} | Page {meta['page']} | Score: {similarity:.3f} ---")
        print(doc.strip())
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query the NEC guide vector DB")
    parser.add_argument("query", help="Natural language query")
    parser.add_argument("--top", type=int, default=5, help="Number of results (default: 5)")
    args = parser.parse_args()
    query(args.query, args.top)
