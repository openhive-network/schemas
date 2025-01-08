from __future__ import annotations

from pydantic import validator

from schemas.fields.assets._base import AssetHive, AssetNaiAmount
from schemas.fields.basic import (
    AccountName,
    PublicKey,
    WitnessUrl,
)
from schemas.fields.compound import LegacyChainProperties
from schemas.operation import Operation


class _WitnessUpdateOperation(Operation):
    owner: AccountName
    url: WitnessUrl
    block_signing_key: PublicKey
    props: LegacyChainProperties
    fee: AssetHive | None

    @classmethod
    def get_name(cls) -> str:
        return "witness_update"

    @classmethod
    def offset(cls) -> int:
        return 11


class WitnessUpdateOperation(_WitnessUpdateOperation):
    fee: AssetHive | None = None

    @validator("fee", always=True)
    @classmethod
    def validate_fee(cls, v: AssetHive | None) -> AssetHive:
        if v is None:
            return AssetHive(amount=AssetNaiAmount(0))
        return v


class WitnessUpdateOperationLegacy(_WitnessUpdateOperation):
    fee: AssetHive | None = None

    @validator("fee", always=True)
    @classmethod
    def validate_fee(cls, v: AssetHive | None) -> AssetHive:
        if v is None:
            return AssetHive(AssetNaiAmount("0.000 HIVE"))
        return v
