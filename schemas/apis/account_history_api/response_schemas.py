from __future__ import annotations

from typing import Any, Generic, TypeVar

from schemas._operation_objects import (
    Hf26ApiOperationObject,
    Hf26ApiVirtualOperationObject,
    LegacyApiOperationObject,
    LegacyApiVirtualOperationObject,
)
from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.account_history_api.fundaments_of_responses import EnumVirtualOpsFieldFundament
from schemas.fields.hex import Signature, TransactionId
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.operations.representation_types import (
    Hf26OperationRepresentationType,
    LegacyOperationRepresentationType,
)
from pydantic import BaseModel

OperationT = TypeVar("OperationT", bound=Hf26OperationRepresentationType | LegacyOperationRepresentationType)
ApiOperationObjectT = TypeVar("ApiOperationObjectT", bound=Hf26ApiOperationObject | LegacyApiOperationObject)
ApiVirtualOperationObjectT = TypeVar(
    "ApiVirtualOperationObjectT", bound=Hf26ApiVirtualOperationObject | LegacyApiVirtualOperationObject
)


class EnumVirtualOpsModel(PreconfiguredBaseModel, BaseModel, Generic[ApiVirtualOperationObjectT]):
    ops: list[ApiVirtualOperationObjectT]
    ops_by_block: list[EnumVirtualOpsFieldFundament]
    next_block_range_begin: HiveInt
    next_operation_begin: HiveInt


class GetAccountHistoryModel(
    PreconfiguredBaseModel, BaseModel, Generic[ApiOperationObjectT, ApiVirtualOperationObjectT]
):
    history: list[tuple[HiveInt, ApiOperationObjectT | ApiVirtualOperationObjectT]]


class GetOpsInBlockModel(
    PreconfiguredBaseModel, BaseModel, Generic[ApiOperationObjectT, ApiVirtualOperationObjectT]
):
    ops: list[ApiOperationObjectT | ApiVirtualOperationObjectT]


class GetTransactionModel(PreconfiguredBaseModel, BaseModel, Generic[OperationT]):
    block_num: HiveInt
    expiration: HiveDateTime
    extensions: list[Any]
    operations: list[OperationT]
    ref_block_num: HiveInt
    ref_block_prefix: HiveInt
    signatures: list[Signature]
    transaction_id: TransactionId
    transaction_num: HiveInt


EnumVirtualOps = EnumVirtualOpsModel[Hf26ApiVirtualOperationObject]
GetAccountHistory = GetAccountHistoryModel[Hf26ApiOperationObject, Hf26ApiVirtualOperationObject]
GetOpsInBlock = GetOpsInBlockModel[Hf26ApiOperationObject, Hf26ApiVirtualOperationObject]
GetTransaction = GetTransactionModel[Hf26OperationRepresentationType]
