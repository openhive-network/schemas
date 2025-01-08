from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, Any
from typing_extensions import Self

import msgspec
from pydantic import ConstrainedInt

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator

__all__ = [
    "HiveInt",
]

# HiveInt = Annotated[str, msgspec.Meta(pattern=r"^[0-9]+$")]
class HiveInt():
    def __init__(self, value: int | str | Self):
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

    def __eq__(self, value: object) -> bool:
        if isinstance(value, int | float):
            return int(self.value) == value
        elif isinstance(value, str | HiveInt):
            return self.value == value
        return False
