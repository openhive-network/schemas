from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, Any

import msgspec
from pydantic import ConstrainedInt

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator

__all__ = [
    "HiveInt",
]

# HiveInt = Annotated[str, msgspec.Meta(pattern=r"^[0-9]+$")]
class HiveInt():
    def __init__(self, value: int | str):
        self.value = str(value)
        self._validate()

    def __int__(self):
        return int(self.value)
    
    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

    def _validate(self):
        pass

    # @classmethod
    # def __get_validators__(cls) -> CallableGenerator:
    #     yield cls.validate
    #     yield from super().__get_validators__()

    # @classmethod
    # def validate(cls, value: Any) -> int:
    #     error_template = ValueError("The value could only be int or string that can be converted to int!")

    #     if isinstance(value, float | bool):
    #         raise error_template

    #     if isinstance(value, int | HiveInt):
    #         return value

    #     if isinstance(value, str):
    #         try:
    #             return int(value)
    #         except (ValueError, TypeError) as error:
    #             raise error_template from error
    #     raise error_template
