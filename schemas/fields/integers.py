from __future__ import annotations

from typing import Annotated, Any

import msgspec

from schemas.fields.hive_int import HiveInt

__all__ = [
    "Uint8t",
    "Int16t",
    "Uint16t",
    "Uint32t",
    "Int64t",
    "Uint64t",
]

Uint8t = Annotated[int, msgspec.Meta(ge=0, le=255)]

Int16t = Annotated[int, msgspec.Meta(ge=-32768, le=32767)]

Uint16t = Annotated[int, msgspec.Meta(ge=0, le=65535)]

Uint32t = Annotated[int, msgspec.Meta(ge=0, le=4294967295)]


class Int64t(HiveInt):
    def _validate(self, value: Any) -> int:
        max_int64_value = 9223372036854775807
        min_int64_value = -9223372036854775808
        value_validated = super()._validate(value)
        if value < min_int64_value or value > max_int64_value:
            raise ValueError("Int64 out of range.")
        return value_validated


class Uint64t(HiveInt):
    def _validate(self, value: Any) -> int:
        max_uint64_value = 18446744073709554615
        value_validated = super()._validate(value)
        if value < 0 or value > max_uint64_value:
            raise ValueError("Int64 out of range.")
        return value_validated


ShareType = Int64t

UShareType = Uint64t
