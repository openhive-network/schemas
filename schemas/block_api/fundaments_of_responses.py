from __future__ import annotations

from typing import Any

from schemas.__private.hive_fields_basic_schemas import AccountName, HiveDateTime, PublicKey
from schemas.__private.hive_fields_custom_schemas import Signature, TransactionId
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.transaction_model.transaction import Hf26Transaction, LegacyTransaction


class Block(PreconfiguredBaseModel):
    block_id: TransactionId
    extensions: list[Any]
    previous: TransactionId
    signing_key: PublicKey
    timestamp: HiveDateTime
    transaction_ids: list[TransactionId]
    transaction_merkle_root: TransactionId
    transactions: list[Hf26Transaction | LegacyTransaction]
    witness: AccountName
    witness_signature: Signature


class EmptyModel(PreconfiguredBaseModel):
    """get_block and get_block_header can be an empty model or in format below"""


class GetBlockFundament(PreconfiguredBaseModel):
    """Second possible format of get_block model"""

    block: Block


class GetBlockHeaderFundament(PreconfiguredBaseModel):
    """as model above get_block_header can also be empty, so it is second possible format of this response"""

    extensions: list[Any]
    previous: TransactionId
    timestamp: HiveDateTime
    transaction_merkle_root: TransactionId
    witness: AccountName
