from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import LegacyChainProperties, LegacyChainPropertiesLegacy
from schemas.operation import Operation


class _WitnessUpdateOperation(Operation, GenericModel, Generic[AssetHiveT]):
    __operation_name__ = "witness_update"
    __offset__ = 11

    owner: AccountName
    url: str
    block_signing_key: PublicKey
    fee: AssetHiveT  # currently ignored but validated


class WitnessUpdateOperation(_WitnessUpdateOperation[AssetHiveHF26]):
    props: LegacyChainProperties


class WitnessUpdateOperationLegacy(_WitnessUpdateOperation[AssetHiveLegacy]):
    props: LegacyChainPropertiesLegacy
