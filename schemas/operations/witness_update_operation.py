from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    LegacyChainProperties,
    PublicKey,
)
from schemas.operation import Operation


class _WitnessUpdateOperation(Operation, GenericModel, Generic[AssetHive]):
    __operation_name__ = "witness_update"

    owner: AccountName
    url: str
    block_signing_key: PublicKey
    props: LegacyChainProperties[AssetHiveHF26]
    fee: AssetHive  # currently ignored but validated


class WitnessUpdateOperation(_WitnessUpdateOperation[AssetHiveHF26]):
    ...


class WitnessUpdateOperationLegacy(_WitnessUpdateOperation[AssetHiveLegacy]):
    ...
