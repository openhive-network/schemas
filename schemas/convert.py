from __future__ import annotations

from typing import Any

import msgspec

UNSET = msgspec.UNSET
"""Sentinel value for optional fields that are not set in a msgspec Struct response."""


def to_builtins(obj: Any, **kwargs: Any) -> Any:
    """Convert a msgspec Struct (or any object) to built-in Python types.

    Thin wrapper around msgspec.to_builtins() — use this instead of importing msgspec directly.
    """
    return msgspec.to_builtins(obj, **kwargs)


def json_encode(obj: Any, **kwargs: Any) -> bytes:
    """Encode an object to JSON bytes using msgspec.

    Thin wrapper around msgspec.json.encode() — use this instead of importing msgspec directly.
    """
    return msgspec.json.encode(obj, **kwargs)
