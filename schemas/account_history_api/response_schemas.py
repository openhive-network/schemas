from __future__ import annotations

from typing import Any

from schemas.__private.hive_fields_basic_schemas import HiveDateTime, HiveInt
from schemas.__private.hive_fields_custom_schemas import Signature, TransactionId
from schemas.__private.operation_objects import Hf26ApiOperationObject
from schemas.__private.operations import Hf26OperationRepresentationType  # pyright: ignore
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.account_history_api.fundaments_of_responses import EnumVirtualOpsFieldFundament


class EnumVirtualOps(PreconfiguredBaseModel):
    ops: list[Hf26ApiOperationObject]
    ops_by_block: list[EnumVirtualOpsFieldFundament]
    next_block_range_begin: HiveInt
    next_operation_begin: HiveInt


class GetAccountHistory(PreconfiguredBaseModel):
    history: list[tuple[HiveInt, Hf26ApiOperationObject]]


class GetOpsInBlock(PreconfiguredBaseModel):
    ops: list[Hf26ApiOperationObject]


class GetTransaction(PreconfiguredBaseModel):
    block_num: HiveInt
    expiration: HiveDateTime
    extensions: list[Any]
    operations: list[Hf26OperationRepresentationType]
    ref_block_num: HiveInt
    ref_block_prefix: HiveInt
    signatures: list[Signature]
    transaction_id: TransactionId
    transaction_num: HiveInt
