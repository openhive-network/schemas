from __future__ import annotations

from dataclasses import dataclass

from schemas.fields.hive_int import HiveInt

__all__ = [
    "AssetInfo",
]


@dataclass
class AssetInfo:
    precision: HiveInt
    nai: str
    symbol: tuple[str, str]
