from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.asset_hbd import AssetHbd
from schemas.__private.custom_schemas.asset_hive import AssetHive
from schemas.__private.custom_schemas.asset_vests import AssetVests
from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.fundamental_schemas import AnyOf

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class AssetAny(CustomSchema):
    def _define_schema(self) -> Schema:
        return AnyOf(
            AssetHbd(),
            AssetHive(),
            AssetVests(),
        )
