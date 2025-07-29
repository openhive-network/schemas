from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from schemas.fields.hive_int import HiveInt

__all__ = [
    "AssetInfo",
]


@dataclass
class AssetInfo:
    precision: HiveInt
    nai: str
    symbol: tuple[str, str]
    testnet: bool

    class AssetConfig:
        testnet_asset: ClassVar[bool | None] = None

    def get_symbol(self, testnet: bool | None = None) -> str:
        testnet = AssetInfo.AssetConfig.testnet_asset or testnet or self.testnet
        return self.symbol[int(testnet)]
