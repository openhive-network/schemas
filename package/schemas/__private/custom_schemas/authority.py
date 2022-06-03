from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.fundamental_schemas import Array, ArrayStrict, Int, Map, Str
from schemas.__private.custom_schemas.public_key import PublicKey


if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class Authority(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            'weight_threshold': Int(),
            'account_auths': Array(
                ArrayStrict(
                    Str(),
                    Int(),
                )
            ),
            'key_auths': Array(
                ArrayStrict(
                    PublicKey(),
                    Int(),
                )
            ),
        })
