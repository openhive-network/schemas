from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.fundamental_schemas import Int, Map


if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class Manabar(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            "current_mana": Int(),
            "last_update_time": Int(),
        })
