from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import LegacyChainProperties
from schemas.fields.hex import Sha256, Signature, TransactionId
from schemas.fields.hive_int import HiveInt
from schemas.fields.integers import Uint64t
from schemas.operation import Operation

DEFAULT_FILL_OR_KILL: Final[bool] = False


class Work(PreconfiguredBaseModel, kw_only=True):
    __operation_name__ = "work"

    worker: PublicKey
    input_: Sha256 = Field(alias="input")
    signature: Signature
    work: Sha256


class _PowOperation(Operation):
    worker_account: AccountName
    block_id: TransactionId
    nonce: Uint64t
    props: LegacyChainProperties
    work: Work

    @classmethod
    def get_name(cls):
        return "pow"
    
    @classmethod
    def offset(cls):
        return 14

class PowOperation(_PowOperation):
    ...


class PowOperationLegacy(_PowOperation):
    ...
