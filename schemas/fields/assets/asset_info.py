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
        if AssetInfo.AssetConfig.testnet_asset is None:
            if testnet is None:
                testnet = self.testnet
        else:
            testnet = AssetInfo.AssetConfig.testnet_asset
        return self.symbol[int(testnet)]
