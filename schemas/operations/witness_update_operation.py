from __future__ import annotations

from typing import Generic

from pydantic import validator
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import (
    AccountName,
    PublicKey,
    WitnessUrl,
)
from schemas.fields.compound import LegacyChainProperties
from schemas.operation import Operation


class _WitnessUpdateOperation(Operation):
    __operation_name__ = "witness_update"
    __offset__ = 11

    owner: AccountName
    url: WitnessUrl
    block_signing_key: PublicKey
    props: LegacyChainProperties
    fee: AssetHive | None


class WitnessUpdateOperation(_WitnessUpdateOperation):
    fee: AssetHive | None = None

    @validator("fee", always=True)
    @classmethod
    def validate_fee(cls, v: AssetHive | None) -> AssetHive:
        if v is None:
            return AssetHive(amount=0)
        return v


class WitnessUpdateOperationLegacy(_WitnessUpdateOperation):
    fee: AssetHive | None = None

    @validator("fee", always=True)
    @classmethod
    def validate_fee(cls, v: AssetHive | None) -> AssetHive:
        if v is None:
            return AssetHive("0.000 HIVE")
        return v
