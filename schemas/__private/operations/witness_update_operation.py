from __future__ import annotations

from schemas.__private.hive_fields_schemas import (
    AccountName,
    AssetHive,
    LegacyChainProperties,
    PublicKey,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class WitnessUpdateOperation(PreconfiguredBaseModel):
    owner: AccountName
    url: str
    block_signing_key: PublicKey
    props: LegacyChainProperties
    fee: AssetHive  # currently ignored but validated
