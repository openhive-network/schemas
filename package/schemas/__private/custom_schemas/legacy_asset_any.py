from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.legacy_asset_hbd import LegacyAssetHbd
from schemas.__private.custom_schemas.legacy_asset_hive import LegacyAssetHive
from schemas.__private.custom_schemas.legacy_asset_vests import LegacyAssetVests
from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.fundamental_schemas import AnyOf

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class LegacyAssetAny(CustomSchema):
    def _define_schema(self) -> Schema:
        return AnyOf(
            LegacyAssetHbd(),
            LegacyAssetHive(),
            LegacyAssetVests(),
        )
