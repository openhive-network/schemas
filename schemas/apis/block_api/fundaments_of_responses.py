from __future__ import annotations

from typing import Any, Generic

from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.hex import Signature, TransactionId
from schemas.fields.hive_datetime import HiveDateTime
from schemas.transaction import (
    Transaction,
    TransactionLegacy,
    TransactionT,
)


class GetBlockHeaderFundament(PreconfiguredBaseModel):
    """as model above get_block_header can also be empty, so it is second possible format of this response"""

    extensions: list[Any]
    previous: TransactionId
    timestamp: HiveDateTime
    transaction_merkle_root: TransactionId
    witness: AccountName


class SignedBlock(GetBlockHeaderFundament):
    witness_signature: Signature
    transactions: list[Transaction | TransactionLegacy]


class BlockLogUtilSignedBlock(GetBlockHeaderFundament):
    block_id: TransactionId
    signing_key: PublicKey
    witness_signature: Signature
    transactions: list[Transaction | TransactionLegacy]


class Block(SignedBlock):
    block_id: TransactionId
    signing_key: PublicKey
    transaction_ids: list[TransactionId]


Hf26Block = Block
LegacyBlock = Block


class EmptyModel(PreconfiguredBaseModel):
    """get_block and get_block_header can be an empty model or in format below"""
