from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.fields.hive_int import HiveInt

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator

__all__ = [
    "HiveStringInt",
]


class HiveStringInt(HiveInt):
    """
    Amount in HF26 have to be serialized as str, to be properly recognized by c++
    """

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield from super().__get_validators__()
        yield cls.__stringify

    @classmethod
    def __stringify(cls, value: int | str) -> str:
        return str(value)
