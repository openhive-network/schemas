from __future__ import annotations

from typing import Any, Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHive,
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
from schemas.__private.preconfigured_base_model import Operation, PreconfiguredBaseModel

DEFAULT_FILL_OR_KILL: Final[bool] = False


class LegacyChainProperties(PreconfiguredBaseModel):
    maximum_block_size: Uint32t
    hbd_interest_rate: Uint16t
    account_creation_fee: Any


class Work(PreconfiguredBaseModel):
    worker: PublicKey
    input_: Sha256 = Field(alias="input")
    signature: Signature
    work: Sha256


class PowOperation(Operation):
    worker_account: AccountName
    block_id: TransactionId
    nonce: Uint64t
    props: LegacyChainProperties
    work: Work
