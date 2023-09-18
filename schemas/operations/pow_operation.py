from __future__ import annotations

from typing import Any, Final

from pydantic import Field

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    PublicKey,
    Uint16t,
    Uint32t,
    Uint64t,
)
from schemas.__private.hive_fields_custom_schemas import (
    Sha256,
    Signature,
    TransactionId,
)
from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.operation import Operation

DEFAULT_FILL_OR_KILL: Final[bool] = False


class LegacyChainProperties(PreconfiguredBaseModel):
    __operation_name__ = "legacy_chain_properties"

    maximum_block_size: Uint32t
    hbd_interest_rate: Uint16t
    account_creation_fee: Any


class Work(PreconfiguredBaseModel):
    __operation_name__ = "work"

    worker: PublicKey
    input_: Sha256 = Field(alias="input")
    signature: Signature
    work: Sha256


class PowOperation(Operation):
    __operation_name__ = "pow"

    worker_account: AccountName
    block_id: TransactionId
    nonce: Uint64t
    props: LegacyChainProperties
    work: Work
