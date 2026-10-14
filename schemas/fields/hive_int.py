from __future__ import annotations

from typing import TYPE_CHECKING, Any

import msgspec

from schemas.errors import FieldValidationError
from schemas.fields._init_validators import InitValidator

__all__ = [
    "HiveInt",
]


class HiveIntFactory(InitValidator[int], int):
    @classmethod
    def _covered_type(cls) -> type[int]:
        return int

    def serialize(self) -> Any:
        max_safe_int = (2**53) - 1
        min_safe_int = -(2**53) + 1
        if self >= min_safe_int and self <= max_safe_int:
            return int(self)
        return str(self)

    @classmethod
    def validate(cls, value: Any) -> int:
        if not isinstance(value, HiveIntFactory | str) and type(value) is not int:
            raise cls._invalid_value_error(value)
        try:
            as_int = int(value)
        except ValueError as error:
            raise cls._invalid_value_error(value) from error
        return super().validate(as_int)

    @staticmethod
    def _invalid_value_error(value: object) -> FieldValidationError:
        return FieldValidationError(
            "The value could only be int or string that can be converted to int!"
            f" Received `{value}` with type `{type(value)}`"
        )


if TYPE_CHECKING:  # nofmt
    HiveInt = int
else:
    HiveInt = HiveIntFactory.factory("HiveInt", msgspec.Meta())
