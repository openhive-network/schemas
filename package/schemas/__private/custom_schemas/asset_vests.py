from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.fundamental_schemas import Int, Map, Str

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class AssetVests(CustomSchema):
    @staticmethod
    def Amount():
        return Int()

    @staticmethod
    def Precision():
        return Int(enum=[6])

    @staticmethod
    def Nai():
        return Str(pattern='@@000000037')

    def _define_schema(self) -> Schema:
        return Map({
            'amount': self.Amount(),
            'precision': self.Precision(),
            'nai': self.Nai(),
        })
