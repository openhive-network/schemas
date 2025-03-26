from __future__ import annotations

from typing import Any

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


class SignedBlockLegacy(GetBlockHeaderFundament):
    transactions: list[TransactionLegacy]


class BlockLogUtilSignedBlockBase(GetBlockHeaderFundament):
    block_id: TransactionId
    signing_key: PublicKey
    witness_signature: Signature
    transactions: list[Transaction | TransactionLegacy]


class BlockHF26(SignedBlockHF26):
    block_id: TransactionId
    signing_key: PublicKey
    transaction_ids: list[TransactionId]


class BlockLegacy(SignedBlockLegacy):
    block_id: TransactionId
    signing_key: PublicKey
    transaction_ids: list[TransactionId]


class Hf26Block(BlockHF26):
    witness_signature: Signature


class LegacyBlock(BlockLegacy):
    witness_signature: Signature


class EmptyModel(PreconfiguredBaseModel):
    """get_block and get_block_header can be an empty model or in format below"""
