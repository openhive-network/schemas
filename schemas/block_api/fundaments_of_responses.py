from __future__ import annotations

from typing import Any

from schemas.__private.hive_fields_basic_schemas import AccountName, HiveDateTime, PublicKey
from schemas.__private.hive_fields_custom_schemas import Signature, TransactionId
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class Block(PreconfiguredBaseModel):
    block_id: TransactionId
    extensions: list[Any]
    previous: TransactionId
    signing_key: PublicKey
    timestamp: HiveDateTime
    transaction_ids: TransactionId
    transaction_merkle_root: TransactionId
    transactions: list[Any]  # Here will be placed transaction model
    witness: AccountName
    witness_signature: Signature


class GetBlockEmptyModel(PreconfiguredBaseModel):
    """get_block can be an empty model or in format below"""


class GetBlockNotEmptyModel(PreconfiguredBaseModel):
    """Second possible format of get_block model"""

    block: Block


class GetBlockHeaderEmptyModel(PreconfiguredBaseModel):
    """as model above get_block_header can also be empty or in format below"""
