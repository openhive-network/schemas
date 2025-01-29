from __future__ import annotations

from schemas.fields.hive_string_int import HiveStringInt

__all__ = [
    "HiveStringUint",
]


class HiveStringUint(HiveStringInt):
    """
    Amount in HF26 have to be serialized as str, to be properly recognized by c++
    """

    ge = 0
