from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.fundamental_schemas import Str

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class AccountName(CustomSchema):
    def _define_schema(self) -> Schema:
        name_segment = r'[a-z][a-z0-9\-]+[a-z0-9]'
        return Str(
            pattern=fr'^{name_segment}(?:\.{name_segment})*$',
            minLength=3,
            maxLength=16
        )
