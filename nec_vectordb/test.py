#!/usr/bin/env python3
"""
Validation suite for the NEC vector database.

Runs golden query test cases and content extraction checks.

Usage:
    python nec_vectordb/test.py
    python nec_vectordb/test.py --verbose
"""

import argparse
import json
import os
import sys

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


# --- Config ---
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "nec_guide"
DB_PATH = os.path.join(os.path.dirname(__file__), "chroma_db")
TEST_CASES_PATH = os.path.join(os.path.dirname(__file__), "test_cases.json")


def load_collection():
    embedding_fn = SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    client = chromadb.PersistentClient(path=DB_PATH)
    return client.get_collection(name=COLLECTION_NAME, embedding_function=embedding_fn)


def run_query_tests(collection, verbose=False):
    """Run golden query test cases."""
    with open(TEST_CASES_PATH) as f:
        test_cases = json.load(f)

    passed = 0
    failed = 0
    results_detail = []

    for i, tc in enumerate(test_cases):
        query = tc["query"]
        expected_pages = tc.get("expected_pages", [])
        must_contain = tc.get("must_contain", "")
        top_k = tc.get("top_k", 5)

        results = collection.query(query_texts=[query], n_results=top_k)
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        result_pages = [m["page"] for m in metadatas]
        combined_text = " ".join(documents)

        errors = []

        # Check expected pages (if specified)
        if expected_pages:
            found_pages = [p for p in expected_pages if p in result_pages]
            if not found_pages:
                errors.append(
                    f"Expected page(s) {expected_pages} not in results {result_pages}"
                )

        # Check must_contain (if specified)
        if must_contain and must_contain not in combined_text:
            errors.append(f'Text "{must_contain}" not found in results')

        if errors:
            failed += 1
            status = "FAIL"
        else:
            passed += 1
            status = "PASS"

        results_detail.append(
            {
                "index": i + 1,
                "query": query,
                "status": status,
                "errors": errors,
                "result_pages": result_pages,
            }
        )

        if verbose or errors:
            print(f"  [{status}] {i + 1}. {query}")
            if errors:
                for e in errors:
                    print(f"         {e}")
            if verbose:
                print(f"         Pages returned: {result_pages}")
        elif status == "PASS":
            print(f"  [PASS] {i + 1}. {query}")

    return passed, failed, results_detail


def run_content_checks(collection, verbose=False):
    """Check that key NEC content was extracted from the PDF."""
    checks = [
        {
            "name": "Table 310.15(B)(16) present",
            "search": "310.15(B)(16)",
            "expect_min_chunks": 3,
        },
        {
            "name": "Article 210 receptacle outlets present",
            "search": "210.52",
            "expect_min_chunks": 3,
        },
        {
            "name": "Article 250 grounding present",
            "search": "250.122",
            "expect_min_chunks": 1,
        },
        {
            "name": "Article 334 NM cable present",
            "search": "334.10",
            "expect_min_chunks": 1,
        },
        {
            "name": "Article 625 EV charging present",
            "search": "625",
            "expect_min_chunks": 1,
        },
    ]

    passed = 0
    failed = 0

    for check in checks:
        results = collection.get(where_document={"$contains": check["search"]})
        matching = results["documents"]

        if len(matching) >= check["expect_min_chunks"]:
            passed += 1
            status = "PASS"
        else:
            failed += 1
            status = "FAIL"

        print(
            f"  [{status}] {check['name']} "
            f"(found {len(matching)} chunks, need {check['expect_min_chunks']})"
        )

    return passed, failed


def run_chunk_stats(collection, verbose=False):
    """Report chunk size statistics."""
    all_data = collection.get()
    documents = all_data["documents"]
    lengths = [len(d) for d in documents]

    total = len(lengths)
    avg = sum(lengths) / total
    shortest = min(lengths)
    longest = max(lengths)
    too_short = sum(1 for l in lengths if l < 50)
    too_long = sum(1 for l in lengths if l > 1500)

    print(f"  Total chunks: {total}")
    print(f"  Avg length: {avg:.0f} chars")
    print(f"  Range: {shortest}-{longest} chars")
    print(f"  Too short (<50 chars): {too_short}")
    print(f"  Too long (>1500 chars): {too_long}")

    issues = 0
    if too_short > total * 0.05:
        print(f"  [WARN] {too_short} chunks are very short — may be low quality")
        issues += 1
    if too_long > total * 0.05:
        print(f"  [WARN] {too_long} chunks are very long — may dilute search results")
        issues += 1

    return issues


def main():
    parser = argparse.ArgumentParser(description="Validate NEC vector database")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show all results")
    args = parser.parse_args()

    if not os.path.exists(DB_PATH):
        print(f"Error: Database not found at {DB_PATH}")
        print("Run ingest.py first.")
        sys.exit(1)

    collection = load_collection()

    print("\n=== Golden Query Tests ===")
    q_passed, q_failed, _ = run_query_tests(collection, verbose=args.verbose)

    print("\n=== Content Extraction Checks ===")
    c_passed, c_failed = run_content_checks(collection, verbose=args.verbose)

    print("\n=== Chunk Quality Stats ===")
    warnings = run_chunk_stats(collection, verbose=args.verbose)

    print("\n=== Summary ===")
    total_passed = q_passed + c_passed
    total_failed = q_failed + c_failed
    print(f"  Queries: {q_passed}/{q_passed + q_failed} passed")
    print(f"  Content: {c_passed}/{c_passed + c_failed} passed")
    print(f"  Warnings: {warnings}")
    print()

    if total_failed > 0:
        print(f"RESULT: {total_failed} FAILURES")
        sys.exit(1)
    else:
        print("RESULT: ALL PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
