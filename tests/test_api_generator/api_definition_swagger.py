from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SecondEndpointResponseItem:
    some_string: str | None = None
    some_bool: bool | None = None


VALID_ENDPOINT_FROM_SWAGGER_PARAMS: dict[str, Any] = {
    "return": str,
    "some_string": str,
    "some_integer": int,
    "some_another_string": str,
}

VALID_ENDPOINT_FROM_SWAGGER_PARAMS_LIST_RETURN: dict[str, Any] = {
    "some_string": str,
    "some_integer": int,
    "some_another_string": str,
}
