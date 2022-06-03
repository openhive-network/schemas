from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.custom_schemas.hex import Hex

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class Sha256(CustomSchema):
    def _define_schema(self) -> Schema:
        return Hex(minLength=64, maxLength=64)
