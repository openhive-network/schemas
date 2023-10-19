from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import ConstrainedInt

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator

__all__ = [
    "HiveInt",
]


class HiveInt(ConstrainedInt):
    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate
        yield from super().__get_validators__()

    @classmethod
    def validate(cls, value: Any) -> int:
        error_template = ValueError("The value could only be int or string that can be converted to int!")

        if isinstance(value, float | bool):
            raise error_template

        if isinstance(value, int | HiveInt):
            return value

        if isinstance(value, str):
            try:
                return int(value)
            except (ValueError, TypeError) as error:
                raise error_template from error
        raise error_template
