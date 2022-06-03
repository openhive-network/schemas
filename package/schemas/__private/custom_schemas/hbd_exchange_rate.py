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


class HbdExchangeRate(CustomSchema):
    def __init__(self, legacy_format=False):
        """
        A field similar to the `Price` type, with the difference that it is allowed to return a value by this field:
          {
            base: Hbd or Hive
            quote: Hive
          }
        Explanation. When creating a new witness, the `update_witnesses_operation` completes the field
        `hbd_exchange_rate` with default value (base: HIVE, quote: HIVE). Which is inconsistent with the `Price` field.
        This is because the pointer in hive must be set to an existing value. Cannot be a null pointer.
        :param legacy_format: Set to `True` to validate `HbdExchangeRate` in legacy format.
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
        return Map({
            'base': AnyOf(AssetHbd(), AssetHive()) if self.__legacy_format is False else AnyOf(LegacyAssetHbd(),
                                                                                               LegacyAssetHive()),
            'quote': AssetHive() if self.__legacy_format is self.__legacy_format is False else LegacyAssetHive(),
        })