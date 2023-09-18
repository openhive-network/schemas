from __future__ import annotations

from typing import TypeVar

from schemas.fields.assets._base import AssetHF26, AssetLegacy
from schemas.fields.assets._symbol import HiveSymbolType
from schemas.fields.assets.asset_info import AssetInfo
from schemas.fields.hive_int import HiveInt

__all__ = [
    "AssetHiveHF26",
    "AssetHiveLegacy",
    "AssetHiveT",
]


class AssetHiveHF26(AssetHF26):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return HiveSymbolType.get_asset_information()

    precision: HiveInt = get_asset_information().precision
    nai: str = get_asset_information().nai


class AssetHiveLegacy(AssetLegacy):
    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return HiveSymbolType.get_asset_information()


AssetHiveT = TypeVar("AssetHiveT", AssetHiveHF26, AssetHiveLegacy)
