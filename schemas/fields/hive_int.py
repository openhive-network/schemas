from __future__ import annotations

from typing import Annotated, Any

from pydantic import Field


__all__ = [
    "HiveInt",
]

HiveInt = Annotated[int, Field(description="The value could only be int or a string that can be converted to int!")]


def validate_hive_int(value: Any) -> int:
    error_template = ValueError("The value could only be int or string that can be converted to int!")

    if isinstance(value, (float, bool)):
        raise error_template

    if isinstance(value, (int, HiveInt)):
        return value

    if isinstance(value, str):
        try:
            return int(value)
        except (ValueError, TypeError) as error:
            raise error_template from error

    raise error_template
