from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.fundamental_schemas import Map


if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class Price(CustomSchema):
    def __init__(self, base, quote):
        super().__init__()
        self.base = base
        self.quote = quote

    def _define_schema(self) -> Schema:
        return Map({
            'base': self.base,
            'quote': self.quote,
        })
