#!/usr/bin/env python3
"""
Spot-check PDF text extraction by comparing extract_pages() output
against known-good reference text files.

Validation files live in nec_vectordb/validation_sets/ and are named
extraction_p{PAGE}.txt — each contains the expected text for that page.

Usage:
    python nec_vectordb/test_extraction.py <path_to_pdf>
    python nec_vectordb/test_extraction.py <path_to_pdf> --verbose
"""

import argparse
import os
import re
import sys

from ingest import extract_pages, DEFAULT_PDF
from text_normalize import replace_ligatures


VALIDATION_DIR = os.path.join(os.path.dirname(__file__), "validation_sets")


def load_validation_cases():
    """Load all extraction_p{PAGE}.txt files from the validation directory."""
    cases = []
    pattern = re.compile(r"^extraction_p(\d+)\.txt$")

    for filename in sorted(os.listdir(VALIDATION_DIR)):
        match = pattern.match(filename)
        if match:
            page_num = int(match.group(1))
            filepath = os.path.join(VALIDATION_DIR, filename)
            with open(filepath) as f:
                expected_text = f.read()
            cases.append({
                "page": page_num,
                "file": filename,
                "expected_text": expected_text,
            })

    return cases


def normalize(text):
    """Normalize whitespace, ligatures, and bullet spacing for comparison."""
    text = replace_ligatures(text)
    # Normalize bullet characters — fitz sometimes drops space after bullets
    text = text.replace("▸", "▸ ")
    return " ".join(text.split())


def run_extraction_checks(pdf_path, verbose=False):
    """Extract pages from PDF and compare against validation files."""
    cases = load_validation_cases()
    if not cases:
        print(f"  No validation files found in {VALIDATION_DIR}/")
        print(f"  Add files named extraction_p{{PAGE}}.txt")
        return 0, 0

    print(f"  Extracting pages from PDF...")
    pages = extract_pages(pdf_path)
    page_map = {p["page"]: p["text"] for p in pages}

    passed = 0
    failed = 0

    for tc in cases:
        page_num = tc["page"]
        expected = tc["expected_text"]
        filename = tc["file"]

        if page_num not in page_map:
            failed += 1
            print(f"  [FAIL] {filename} — page {page_num} not extracted from PDF")
            continue

        actual = page_map[page_num]

        # Check that each non-empty line from the validation file
        # appears in the extracted text (normalized whitespace)
        missing_lines = []
        for line in expected.strip().splitlines():
            line = line.strip()
            if not line:
                continue
            if normalize(line) not in normalize(actual):
                missing_lines.append(line)

        if not missing_lines:
            passed += 1
            print(f"  [PASS] {filename} — all lines found on page {page_num}")
        else:
            failed += 1
            print(f"  [FAIL] {filename} — {len(missing_lines)} lines missing from page {page_num}")
            for line in missing_lines[:5]:
                print(f"         Missing: \"{line[:80]}\"")
            if len(missing_lines) > 5:
                print(f"         ... and {len(missing_lines) - 5} more")

        if verbose:
            total_lines = len([l for l in expected.strip().splitlines() if l.strip()])
            matched = total_lines - len(missing_lines)
            print(f"         Matched {matched}/{total_lines} lines")
            preview = normalize(actual)[:120]
            print(f"         Extracted preview: \"{preview}...\"")

    return passed, failed


def main():
    parser = argparse.ArgumentParser(description="Validate PDF text extraction")
    parser.add_argument("pdf_path", nargs="?", default=DEFAULT_PDF, help="Path to the PDF file")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    if not os.path.exists(args.pdf_path):
        print(f"Error: PDF not found: {args.pdf_path}")
        sys.exit(1)

    print("\n=== Page Extraction Spot Checks ===")
    passed, failed = run_extraction_checks(args.pdf_path, verbose=args.verbose)

    print(f"\n=== Summary ===")
    print(f"  {passed}/{passed + failed} passed")
    print()

    if failed > 0:
        print(f"RESULT: {failed} FAILURES")
        sys.exit(1)
    else:
        print("RESULT: ALL PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
