from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.fundamental_schemas import Str

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class PublicKey(CustomSchema):
    def _define_schema(self) -> Schema:
        # See `wif_to_key` implementation in `fc` library for more information about this regex:
        wif_private_key_regex = r'^(?:STM|TST)[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{7,51}$'
        return Str(pattern=wif_private_key_regex)
