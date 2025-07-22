from __future__ import annotations

from typing import Any, Final

from msgspec import field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import LegacyChainProperties
from schemas.fields.hex import TransactionId
from schemas.fields.integers import Uint32t, Uint64t
from schemas.operation import Operation

DEFAULT_FILL_OR_KILL: Final[bool] = False


class Pow2Input(PreconfiguredBaseModel):
    worker_account: AccountName
    prev_block: TransactionId
    nonce: Uint64t = field(default_factory=lambda: 0)


class Pow2(PreconfiguredBaseModel):
    input_: Pow2Input = field(name="input")
    pow_summary: Uint32t = field(default_factory=lambda: 0)


class EquihashPow(PreconfiguredBaseModel, kw_only=True):
    input_: Pow2Input = field(name="input")
    proof: Any
    prev_block: TransactionId
    pow_summary: Uint32t


class Pow2WorkPow2(PreconfiguredBaseModel, kw_only=True, tag="pow2"):
    value: Pow2


class Pow2WorkEquihashPow(PreconfiguredBaseModel, kw_only=True, tag="equihash_pow"):
    value: EquihashPow


class Pow2Operation(Operation):
    work: Pow2WorkPow2 | Pow2WorkEquihashPow
    props: LegacyChainProperties
    new_owner_key: PublicKey | None = None

    @classmethod
    def get_name(cls) -> str:
        return "pow2"

    @classmethod
    def offset(cls) -> int:
        return 30
