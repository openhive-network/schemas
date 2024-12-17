from __future__ import annotations

from typing import Any, TypeVar

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.hex import Signature, TransactionId
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.operations import Hf26OperationRepresentation, LegacyOperationRepresentation

__all__ = [
    "Transaction",
    "TransactionLegacy",
    "TransactionT",
]


class TransactionCommon(PreconfiguredBaseModel):
    ref_block_num: HiveInt
    ref_block_prefix: HiveInt
    expiration: HiveDateTime
    extensions: list[Any]
    signatures: list[Signature]


class Transaction(TransactionCommon):
    operations: list[Hf26OperationRepresentation]


class TransactionLegacy(TransactionCommon):
    operations: list[LegacyOperationRepresentation]
    block_num: HiveInt
    transaction_id: TransactionId
    transaction_num: HiveInt


TransactionT = TypeVar("TransactionT", bound=Transaction | TransactionLegacy)
