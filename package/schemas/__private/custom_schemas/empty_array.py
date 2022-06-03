from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.fundamental_schemas import Any_, Array


if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class EmptyArray(CustomSchema):
    def _define_schema(self) -> Schema:
        return Array(Any_(), maxItems=0)
