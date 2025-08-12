from __future__ import annotations

from typing import Final

from msgspec import field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import LegacyChainProperties
from schemas.fields.hex import BlockId, Sha256, Signature
from schemas.fields.integers import Uint64t
from schemas.operation import Operation

DEFAULT_FILL_OR_KILL: Final[bool] = False


class Work(PreconfiguredBaseModel, kw_only=True):
    __operation_name__ = "work"

    worker: PublicKey
    input_: Sha256 = field(name="input")
    signature: Signature
    work: Sha256


class PowOperation(Operation):
    worker_account: AccountName
    block_id: BlockId
    nonce: Uint64t
    props: LegacyChainProperties
    work: Work

    @classmethod
    def get_name(cls) -> str:
        return "pow"

    @classmethod
    def offset(cls) -> int:
        return 14
