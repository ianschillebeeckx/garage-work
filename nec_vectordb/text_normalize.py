"""Shared text normalization utilities for extraction and testing."""

LIGATURES = {
    "\ufb01": "fi",
    "\ufb02": "fl",
    "\ufb00": "ff",
    "\ufb03": "ffi",
    "\ufb04": "ffl",
}


def replace_ligatures(text: str) -> str:
    """Replace Unicode ligature characters with their ASCII equivalents."""
    for lig, replacement in LIGATURES.items():
        text = text.replace(lig, replacement)
    return text
