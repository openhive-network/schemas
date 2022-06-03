from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.custom_schemas.hardfork_version import HardforkVersion
from schemas.__private.custom_schemas.hex import Hex
from schemas.__private.custom_schemas.sha_256 import Sha256
from schemas.__private.fundamental_schemas import Map, Str

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class HiveVersion(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            'blockchain_version': HardforkVersion(),
            'hive_revision': Hex(minLength=40, maxLength=40),
            'fc_revision': Hex(minLength=40, maxLength=40),
            'chain_id': Sha256(),
            'node_type': Str(pattern=r'^(mainnet|testnet|mirrornet)$')
        })
