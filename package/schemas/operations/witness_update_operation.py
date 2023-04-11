from __future__ import annotations

from schemas.package.schemas.predefined import AccountName, PublicKey, LegacyChainProperties, AssetHive, LegacyAssetHive
from preconfigure_base_model import PreconfiguredBaseModel


class WitnessUpdateOperation(PreconfiguredBaseModel):
    owner: AccountName
    url: str
    block_signing_key: PublicKey
    props: LegacyChainProperties
    fee: AssetHive | LegacyAssetHive  # currently ignored but validated
