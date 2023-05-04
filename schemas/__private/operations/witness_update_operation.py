from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private import LegacyChainProperties
from schemas.__private.hive_fields_schemas import (
    AccountName,
    AssetHive,
    PublicKey,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class WitnessUpdateOperation(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    owner: AccountName
    url: str
    block_signing_key: PublicKey
    props: LegacyChainProperties
    fee: AssetHive  # currently ignored but validated
