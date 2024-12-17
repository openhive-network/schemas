from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic.generics import GenericModel

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

OperationT = TypeVar("OperationT", bound=Hf26OperationRepresentationType | LegacyOperationRepresentationType)
# ApiOperationObjectT = TypeVar("ApiOperationObjectT", bound=Hf26ApiOperationObject | LegacyApiOperationObject)
# ApiVirtualOperationObjectT = TypeVar(
#     "ApiVirtualOperationObjectT", bound=Hf26ApiVirtualOperationObject | LegacyApiVirtualOperationObject
# )


class EnumVirtualOpsModel(PreconfiguredBaseModel):
    ops: Hf26ApiVirtualOperationObject | LegacyApiVirtualOperationObject
    ops_by_block: list[EnumVirtualOpsFieldFundament]
    next_block_range_begin: HiveInt
    next_operation_begin: HiveInt


# class GetAccountHistoryModel(
#     PreconfiguredBaseModel, GenericModel, Generic[ApiOperationObjectT, ApiVirtualOperationObjectT]
# ):
#     history: list[tuple[HiveInt, ApiOperationObjectT | ApiVirtualOperationObjectT]]


# class GetOpsInBlockModel(
#     PreconfiguredBaseModel, GenericModel, Generic[ApiOperationObjectT, ApiVirtualOperationObjectT]
# ):
#     ops: list[ApiOperationObjectT | ApiVirtualOperationObjectT]


class GetTransactionModel(PreconfiguredBaseModel):
    block_num: HiveInt
    expiration: HiveDateTime
    extensions: list[Any]
    operations: list[Hf26OperationRepresentationType | LegacyOperationRepresentationType]
    ref_block_num: HiveInt
    ref_block_prefix: HiveInt
    signatures: list[Signature]
    transaction_id: TransactionId
    transaction_num: HiveInt


EnumVirtualOps = EnumVirtualOpsModel
# GetAccountHistory = GetAccountHistoryModel[Hf26ApiOperationObject, Hf26ApiVirtualOperationObject]
# GetOpsInBlock = GetOpsInBlockModel[Hf26ApiOperationObject, Hf26ApiVirtualOperationObject]
GetTransaction = GetTransactionModel
