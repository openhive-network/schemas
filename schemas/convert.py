from __future__ import annotations

from typing import Any

import msgspec


def to_builtins(obj: Any, **kwargs: Any) -> Any:
    """Convert a msgspec Struct (or any object) to built-in Python types.

    Thin wrapper around msgspec.to_builtins() — use this instead of importing msgspec directly.
    """
    return msgspec.to_builtins(obj, **kwargs)
