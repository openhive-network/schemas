from __future__ import annotations

from pydantic import Field

from typing import Annotated

__all__ = [
    "Uint8t",
    "Int16t",
    "Uint16t",
    "Uint32t",
    "Int64t",
    "Uint64t",
]

Uint8t = Annotated[int, Field(ge=0, le=255)]

Int16t = Annotated[int, Field(ge=-32768, le=32767)]

Uint16t = Annotated[int, Field(ge=0, le=65535)]

Uint32t = Annotated[int, Field(ge=0, le=4294967295)]

Int64t = Annotated[int, Field(ge=-9223372036854775808, le=9223372036854775807)]

Uint64t = Annotated[int, Field(ge=0, le=18446744073709554615)]

class ShareType(Int64t):
    """Identical data-type as Int64t"""


class UShareType(Uint64t):
    """Identical data-type as Uint64t"""
