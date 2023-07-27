from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import (
    AccountName,
    AssetHive,
    AssetHiveHF26,
    LegacyChainProperties,
    PublicKey,
)
from schemas.preconfigured_base_model import Operation


class WitnessUpdateOperation(Generic[AssetHive], GenericModel, Operation):
    owner: AccountName
    url: str
    block_signing_key: PublicKey
    props: LegacyChainProperties[AssetHiveHF26]
    fee: AssetHive  # currently ignored but validated
