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

    class AssetConfig:
        testnet_asset: ClassVar[bool] = False

    def get_symbol(self, testnet: bool | None = None) -> str:
        if testnet is not None:
            return self.symbol[int(testnet)]
        return self.symbol[int(AssetInfo.AssetConfig.testnet_asset)]
