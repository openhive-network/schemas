from __future__ import annotations

from typing import Any

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.hex import BlockId, Signature, TransactionId
from schemas.fields.hive_datetime import HiveDateTime
from schemas.transaction import (
    Transaction,
    TransactionLegacy,
)


class GetBlockHeaderFundament(PreconfiguredBaseModel):
    """as model above get_block_header can also be empty, so it is second possible format of this response"""

    extensions: list[Any]
    previous: TransactionId
    timestamp: HiveDateTime
    transaction_merkle_root: TransactionId
    witness: AccountName


class SignedBlockHF26(GetBlockHeaderFundament):
    transactions: list[Transaction]
    witness_signature: Signature


class SignedBlockLegacy(GetBlockHeaderFundament):
    transactions: list[TransactionLegacy]
    witness_signature: Signature


class BlockLogUtilSignedBlockBaseTransaction(GetBlockHeaderFundament):
    block_id: BlockId
    signing_key: PublicKey
    witness_signature: Signature
    transactions: list[Transaction]


class BlockLogUtilSignedBlockBaseTransactionLegacy(GetBlockHeaderFundament):
    block_id: BlockId
    signing_key: PublicKey
    witness_signature: Signature
    transactions: list[TransactionLegacy]


class Hf26Block(SignedBlockHF26):
    block_id: BlockId
    signing_key: PublicKey
    transaction_ids: list[TransactionId]


class LegacyBlock(SignedBlockLegacy):
    block_id: BlockId
    signing_key: PublicKey
    transaction_ids: list[TransactionId]


class EmptyModel(PreconfiguredBaseModel):
    """get_block and get_block_header can be an empty model or in format below"""
