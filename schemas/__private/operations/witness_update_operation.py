from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHive,
    AssetHiveHF26,
    LegacyChainProperties,
    PublicKey,
)
from schemas.__private.preconfigured_base_model import Operation


class WitnessUpdateOperation(Operation, GenericModel, Generic[AssetHive]):
    owner: AccountName
    url: str
    block_signing_key: PublicKey
    props: LegacyChainProperties[AssetHiveHF26]
    fee: AssetHive  # currently ignored but validated
