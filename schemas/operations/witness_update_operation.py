from __future__ import annotations

from typing import Generic

from pydantic import validator
from pydantic.generics import GenericModel

from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import LegacyChainProperties
from schemas.operation import Operation


class _WitnessUpdateOperation(Operation, GenericModel, Generic[AssetHiveT]):
    __operation_name__ = "witness_update"
    __offset__ = 11

    owner: AccountName
    url: str
    block_signing_key: PublicKey
    props: LegacyChainProperties[AssetHiveHF26]
    fee: AssetHiveT | None


class WitnessUpdateOperation(_WitnessUpdateOperation[AssetHiveHF26]):
    fee: AssetHiveHF26 | None = None

    @validator("fee", always=True)
    @classmethod
    def validate_fee(cls, v: AssetHiveHF26 | None) -> AssetHiveHF26:
        if v is None:
            return AssetHiveHF26(amount=0)
        return v


class WitnessUpdateOperationLegacy(_WitnessUpdateOperation[AssetHiveLegacy]):
    fee: AssetHiveLegacy | None = None

    @validator("fee", always=True)
    @classmethod
    def validate_fee(cls, v: AssetHiveLegacy | None) -> AssetHiveLegacy:
        if v is None:
            return AssetHiveLegacy("0.000 HIVE")
        return v
