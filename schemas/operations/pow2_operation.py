from __future__ import annotations

from typing import Any, Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import LegacyChainProperties
from schemas.fields.hex import Sha256, TransactionId
from schemas.fields.integers import Uint32t, Uint64t
from schemas.operation import Operation

DEFAULT_FILL_OR_KILL: Final[bool] = False
from msgspec import field


class Pow2Input(PreconfiguredBaseModel):
    worker_account: AccountName
    prev_block: TransactionId
    nonce: Uint64t = field(default_factory=lambda: Uint64t(0))


class Pow2(PreconfiguredBaseModel, tag="pow2"):
    input_: Pow2Input = field(name="input")
    pow_summary: Uint32t = field(default_factory=lambda: Uint32t(0))


class EquihashPow(PreconfiguredBaseModel, kw_only=True, tag="equihaszpow"):
    input_: Sha256 = field(name="input")
    proof: Any
    prev_block: TransactionId
    pow_summary: Uint32t


class Pow2Work(PreconfiguredBaseModel, kw_only=True):
    type_: str = field(name="type")
    value: Pow2 | EquihashPow


class _Pow2Operation(Operation):
    work: Pow2Work
    props: LegacyChainProperties
    new_owner_key: PublicKey | None = None

    @classmethod
    def get_name(cls):
        return "pow2"
    
    @classmethod
    def offset(cls):
        return 30

class Pow2Operation(_Pow2Operation):
    ...


class Pow2OperationLegacy(_Pow2Operation):
    ...
