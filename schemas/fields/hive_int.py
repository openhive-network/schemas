from __future__ import annotations

from typing import TYPE_CHECKING, Any

import msgspec
from typing_extensions import Self

from schemas.fields._init_validators import InitValidator

__all__ = [
    "HiveInt",
]


class HiveIntFactory(int, InitValidator[int]):
    def __new__(cls, obj: Any, *, skip_validation: bool = False) -> Self:
        if not skip_validation:
            cls.validate(obj)
        return super().__new__(cls, obj)

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
    def validate(cls, value: Any) -> Self:
        error_template = msgspec.ValidationError("The value could only be int or string that can be converted to int!")
        if not isinstance(value, (HiveIntFactory, str)) and type(value) is not int:
            raise error_template
        try:
            return super().validate(int(value))
        except ValueError as error:
            raise error_template from error


if TYPE_CHECKING:  # nofmt
    HiveInt = int
else:
    HiveInt = HiveIntFactory.factory("HiveInt", msgspec.Meta())
