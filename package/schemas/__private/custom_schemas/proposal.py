from __future__ import annotations

from typing import Any, Optional, TYPE_CHECKING

from schemas.__private.custom_schemas.asset_hbd import AssetHbd
from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.custom_schemas.legacy_asset_hbd import LegacyAssetHbd
from schemas.__private.fundamental_schemas import Date, Int, Map, Str


if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class Proposal(CustomSchema):
    def __init__(self, *, legacy_format: [Optional] = False, **options: Any):
        super().__init__(**options)
        self.__legacy_format = legacy_format
        self.__data = Map({
            'id': Int(),
            'proposal_id': Int(),
            'creator': Str(),
            'receiver': Str(),
            'start_date': Date(),
            'end_date': Date(),
            'daily_pay': LegacyAssetHbd() if self.__legacy_format else AssetHbd(),
            'subject': Str(),
            'permlink': Str(),
            'total_votes': Int(),
            'status': Str(),
        })

    def __setitem__(self, key: str, schema: Schema):
        self.__data[key] = schema

    def __delitem__(self, key):
        del self.__data[key]

    @property
    def legacy_format(self):
        return self.__legacy_format

    @legacy_format.setter
    def legacy_format(self, value: bool):
        self.__legacy_format = value
        self.__data['daily_pay'] = LegacyAssetHbd() if self.__legacy_format else AssetHbd()

    def _define_schema(self) -> Schema:
        return self.__data
