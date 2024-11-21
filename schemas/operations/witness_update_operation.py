from __future__ import annotations

from typing import Generic

from pydantic import BaseModel, validator

from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
    PublicKey,
    WitnessUrl,
)
from schemas.fields.compound import LegacyChainProperties
from schemas.operation import Operation


class _WitnessUpdateOperation(Operation, BaseModel, Generic[AssetHiveT]):
    __operation_name__ = "witness_update"
    __offset__ = 11

    owner: AccountName
    url: WitnessUrl
    block_signing_key: PublicKey
    props: LegacyChainProperties[AssetHiveHF26]
    fee: AssetHiveT | None


class WitnessUpdateOperation(_WitnessUpdateOperation[AssetHiveHF26]):
    fee: AssetHiveHF26 | None = None

    # TODO[pydantic]: We couldn't refactor the `validator`, please replace it by `field_validator` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-validators for more information.
    @validator("fee", always=True)
    @classmethod
    def validate_fee(cls, v: AssetHiveHF26 | None) -> AssetHiveHF26:
        if v is None:
            return AssetHiveHF26(amount=0)
        return v


class WitnessUpdateOperationLegacy(_WitnessUpdateOperation[AssetHiveLegacy]):
    fee: AssetHiveLegacy | None = None

    # TODO[pydantic]: We couldn't refactor the `validator`, please replace it by `field_validator` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-validators for more information.
    @validator("fee", always=True)
    @classmethod
    def validate_fee(cls, v: AssetHiveLegacy | None) -> AssetHiveLegacy:
        if v is None:
            return AssetHiveLegacy("0.000 HIVE")
        return v
