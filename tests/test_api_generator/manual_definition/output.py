from __future__ import annotations

from typing import Any

from .input import TestCustomType

VALID_PARAMS_FOR_FIRST_AND_SECOND_ENDPOINT: dict[str, Any] = {
    "return": str,
    "some_custom_type": TestCustomType,
    "some_string": str,
    "some_int": int,
}

VALID_PARAMS_FOR_THIRD_ENDPOINT: dict[str, Any] = {
    "return": list[str],
    "some_custom_type": TestCustomType,
    "some_string": str,
    "some_int": int,
}
