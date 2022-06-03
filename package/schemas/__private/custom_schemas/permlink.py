from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.fundamental_schemas import Str


if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class Permlink(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(maxLength=256)
