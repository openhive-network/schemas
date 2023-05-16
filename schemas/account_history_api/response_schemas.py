from __future__ import annotations

from typing import Any

from schemas.__private.hive_fields_basic_schemas import HiveDateTime, HiveInt
from schemas.__private.hive_fields_custom_schemas import ApiOperationObject, OperationType, Signature, TransactionId
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.account_history_api.fundaments_of_responses import EnumVirtualOpsFieldFundament


class EnumVirtualOps(PreconfiguredBaseModel):
    ops: list[ApiOperationObject]
    ops_by_block: list[EnumVirtualOpsFieldFundament] | list[str]
    next_block_range_begin: HiveInt
    next_operation_begin: HiveInt


class GetAccountHistory(PreconfiguredBaseModel):
    history: list[tuple[HiveInt, ApiOperationObject]]


class GetOpsInBlock(PreconfiguredBaseModel):
    ops: list[ApiOperationObject]


class GetTransaction(PreconfiguredBaseModel):
    block_num: HiveInt
    expiration: HiveDateTime
    extensions: list[Any]
    operations: list[OperationType]
    ref_block_num: HiveInt
    ref_block_prefix: HiveInt
    signatures: list[Signature]
    transaction_id: TransactionId
    transaction_num: HiveInt
