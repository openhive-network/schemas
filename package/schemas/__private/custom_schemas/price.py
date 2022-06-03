from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.asset_hbd import AssetHbd
from schemas.__private.custom_schemas.asset_hive import AssetHive
from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.custom_schemas.legacy_asset_hbd import LegacyAssetHbd
from schemas.__private.custom_schemas.legacy_asset_hive import LegacyAssetHive
from schemas.__private.fundamental_schemas import AnyOf, Map


if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class Price(CustomSchema):
    def __init__(self, legacy_format=False):
        """
        Valid values for the `Price` structures are:
         - `base: Hbd` and `quote: Hive`,
         - `base: Hive` and `quote: Hbd`.
        :param legacy_format: Set to `True` to validate `Price` in legacy format.
        """
        super().__init__()
        self.__legacy_format = legacy_format

    @property
    def legacy_format(self):
        return self.__legacy_format

    @legacy_format.setter
    def legacy_format(self, value: bool):
        self.__legacy_format = value

    def _define_schema(self) -> Schema:
        return AnyOf(
            Map({
                'base': AssetHbd() if self.__legacy_format is False else LegacyAssetHbd(),
                'quote': AssetHive() if self.__legacy_format is self.__legacy_format is False else LegacyAssetHive(),
            }),
            Map({
                'base': AssetHive() if self.__legacy_format is False else LegacyAssetHive(),
                'quote': AssetHbd() if self.__legacy_format is self.__legacy_format is False else LegacyAssetHbd(),
            }),
        )
