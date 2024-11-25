from __future__ import annotations

from typing import Annotated, Any

from pydantic import Field, AfterValidator


__all__ = [
    "HiveInt",
]

def validate_hive_int(value: Any) -> int:
    error_template = ValueError("The value could only be int or string that can be converted to int!")

    if isinstance(value, (float, bool)):
        raise error_template

    if isinstance(value, (int)):
        return value

    if isinstance(value, str):
        try:
            return int(value)
        except (ValueError, TypeError) as error:
            raise error_template from error

    raise error_template

HiveInt = Annotated[int, AfterValidator(validate_hive_int)]
