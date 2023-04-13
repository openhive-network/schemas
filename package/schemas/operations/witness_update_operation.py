from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, PublicKey, LegacyChainProperties, AssetHive, LegacyAssetHive
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class WitnessUpdateOperation(PreconfiguredBaseModel):
    owner: AccountName
    url: str
    block_signing_key: PublicKey
    props: LegacyChainProperties
    fee: AssetHive | LegacyAssetHive  # currently ignored but validated
