from __future__ import annotations

from typing import Final, Generic

from pydantic import BaseModel, Field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import LegacyChainProperties
from schemas.fields.hex import Sha256, Signature, TransactionId
from schemas.fields.integers import Uint64t
from schemas.operation import Operation

DEFAULT_FILL_OR_KILL: Final[bool] = False


class Work(PreconfiguredBaseModel):
    __operation_name__ = "work"

    worker: PublicKey
    input_: Sha256 = Field(alias="input")
    signature: Signature
    work: Sha256


class _PowOperation(Operation, BaseModel, Generic[AssetHiveT]):
    __operation_name__ = "pow"
    __offset__ = 14

    worker_account: AccountName
    block_id: TransactionId
    nonce: Uint64t
    props: LegacyChainProperties[AssetHiveT]
    work: Work


class PowOperation(_PowOperation[AssetHiveHF26]):
    ...


class PowOperationLegacy(_PowOperation[AssetHiveLegacy]):
    ...
