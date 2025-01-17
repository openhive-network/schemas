from __future__ import annotations
from typing import Annotated

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


# class Uint8t(ConstrainedInt):
#     ge = 0
#     le = 255

Uint8t = Annotated[int, msgspec.Meta(ge=0, le=255)]

# class Int16t(ConstrainedInt):
#     ge = -32768
#     le = 32767

Int16t = Annotated[int, msgspec.Meta(ge=-32768, le=32767)]

# class Uint16t(ConstrainedInt):
#     ge = 0
#     le = 65535

Uint16t = Annotated[int, msgspec.Meta(ge=0, le=65535)]

# class Uint32t(ConstrainedInt):
#     ge = 0
#     le = 4294967295

Uint32t = Annotated[int, msgspec.Meta(ge=0, le=4294967295)]

class Int64t(HiveInt):
    def _validate(self):
        if int(self.value) < -9223372036854775808 or int(self.value) > 9223372036854775807:
            raise ValueError("Int64 out of range.")


# Int64t = Annotated[int, msgspec.Meta(ge=-9223372036854775808, le=9223372036854775807)]

class Uint64t(HiveInt):
    def _validate(self):
        if int(self.value) < 0 or int(self.value) > 18446744073709554615:
            raise ValueError("Int64 out of range.")


# Uint64t = Annotated[int, msgspec.Meta(ge=0, le=18446744073709554615)]

ShareType = Int64t

UShareType = Uint64t
