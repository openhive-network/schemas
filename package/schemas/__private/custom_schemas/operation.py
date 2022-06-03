from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.hive_operation_parser import adapt_hive_operations_to_schema

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class Operation(CustomSchema):
    def _define_schema(self) -> Schema:
        return adapt_hive_operations_to_schema()
