from __future__ import annotations

from typing import Any

from schemas._operation_objects import (
    Hf26ApiAllOperationObject,
    Hf26ApiOperationObject,
    Hf26ApiVirtualOperationObject,
)
from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.account_history_api.fundaments_of_responses import EnumVirtualOpsFieldFundament
from schemas.fields.hex import Signature, TransactionId
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.operations import Hf26OperationRepresentation


class EnumVirtualOps(PreconfiguredBaseModel):
    ops: list[Hf26ApiVirtualOperationObject]
    ops_by_block: list[EnumVirtualOpsFieldFundament]
    next_block_range_begin: HiveInt
    next_operation_begin: HiveInt


class GetAccountHistory(PreconfiguredBaseModel):
    history: list[tuple[HiveInt, Hf26ApiOperationObject]]


class GetOpsInBlock(PreconfiguredBaseModel):
    ops: list[Hf26ApiAllOperationObject]


class GetTransactionBase(PreconfiguredBaseModel):
    block_num: HiveInt
    expiration: HiveDateTime
    extensions: list[Any]
    ref_block_num: HiveInt
    ref_block_prefix: HiveInt
    signatures: list[Signature]
    transaction_id: TransactionId
    transaction_num: HiveInt


class GetTransaction(GetTransactionBase):
    operations: list[Hf26OperationRepresentation]
