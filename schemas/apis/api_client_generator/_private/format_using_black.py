from __future__ import annotations

import black
from black.mode import Mode


def format_using_black(code: str) -> str:
    """
    Format code using Black.

    Args:
        code: The code to format.

    Returns:
        str: The formatted code.
    """
    return black.format_str(code, mode=Mode())
