from __future__ import annotations

from schemas.fields.assets._base import AssetBase
from schemas.fields.assets.asset_info import AssetInfo
from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT

__all__ = [
    # TYPE VARS
    "AssetHiveT",
    "AssetHbdT",
    "AssetVestsT",
    # HF26 ASSETS
    "AssetHiveHF26",
    "AssetHbdHF26",
    "AssetVestsHF26",
    # LEGACY ASSETS
    "AssetHiveLegacy",
    "AssetHbdLegacy",
    "AssetVestsLegacy",
    # OTHER
    "AssetInfo",
    "AssetBase",
]
