from __future__ import annotations

from typing import Any, Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import (
    AccountName,
    HiveDateTime,
    PublicKey,
)
from schemas.hive_fields_custom_schemas import Signature, TransactionId
from schemas.preconfigured_base_model import PreconfiguredBaseModel
from schemas.transaction_model.transaction import (
    Hf26Transaction,
    LegacyTransaction,
    TransactionT,
)


class GetBlockHeaderFundament(PreconfiguredBaseModel):
    """as model above get_block_header can also be empty, so it is second possible format of this response"""

    extensions: list[Any]
    previous: TransactionId
    timestamp: HiveDateTime
    transaction_merkle_root: TransactionId
    witness: AccountName


class SignedBlock(GetBlockHeaderFundament, GenericModel, Generic[TransactionT]):
    witness_signature: Signature
    transactions: list[TransactionT]


class Block(SignedBlock[TransactionT], GenericModel, Generic[TransactionT]):
    block_id: TransactionId
    signing_key: PublicKey
    transaction_ids: list[TransactionId]


Hf26Block = Block[Hf26Transaction]
LegacyBlock = Block[LegacyTransaction]


class EmptyModel(PreconfiguredBaseModel):
    """get_block and get_block_header can be an empty model or in format below"""
