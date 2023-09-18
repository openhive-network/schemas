from __future__ import annotations

from typing import TypeVar

from schemas.fields.assets._base import AssetHF26, AssetLegacy
from schemas.fields.assets._symbol import VestsSymbolType
from schemas.fields.assets.asset_info import AssetInfo
from schemas.fields.hive_int import HiveInt

__all__ = [
    "AssetVestsHF26",
    "AssetVestsLegacy",
    "AssetVestsT",
]


class AssetVestsHF26(AssetHF26):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return VestsSymbolType.get_asset_information()

    precision: HiveInt = get_asset_information().precision
    nai: str = get_asset_information().nai


class AssetVestsLegacy(AssetLegacy):
    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return VestsSymbolType.get_asset_information()


AssetVestsT = TypeVar("AssetVestsT", AssetVestsHF26, AssetVestsLegacy)
