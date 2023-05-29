from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import HiveDateTime, HiveInt
from schemas.__private.hive_fields_custom_schemas import Signature, TransactionId
from schemas.__private.operation_objects import (
    Hf26ApiOperationObject,
    Hf26ApiVirtualOperationObject,
    LegacyApiOperationObject,
    LegacyApiVirtualOperationObject,
)
from schemas.__private.operations import Hf26OperationRepresentationType, LegacyOperationRepresentationType
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.account_history_api.fundaments_of_responses import EnumVirtualOpsFieldFundament

OperationT = TypeVar("OperationT", bound=Hf26OperationRepresentationType | LegacyOperationRepresentationType)
ApiOperationObjectT = TypeVar("ApiOperationObjectT", bound=Hf26ApiOperationObject | LegacyApiOperationObject)
ApiVirtualOperationObjectT = TypeVar(
    "ApiVirtualOperationObjectT", bound=Hf26ApiVirtualOperationObject | LegacyApiVirtualOperationObject
)


class EnumVirtualOps(PreconfiguredBaseModel, GenericModel, Generic[ApiVirtualOperationObjectT]):
    ops: list[ApiVirtualOperationObjectT]
    ops_by_block: list[EnumVirtualOpsFieldFundament]
    next_block_range_begin: HiveInt
    next_operation_begin: HiveInt


class GetAccountHistory(PreconfiguredBaseModel, GenericModel, Generic[ApiOperationObjectT, ApiVirtualOperationObjectT]):
    history: list[tuple[HiveInt, ApiOperationObjectT | ApiVirtualOperationObjectT]]


class GetOpsInBlock(PreconfiguredBaseModel, GenericModel, Generic[ApiOperationObjectT, ApiVirtualOperationObjectT]):
    ops: list[ApiOperationObjectT | ApiVirtualOperationObjectT]


class GetTransaction(PreconfiguredBaseModel, GenericModel, Generic[OperationT]):
    block_num: HiveInt
    expiration: HiveDateTime
    extensions: list[Any]
    operations: list[OperationT]
    ref_block_num: HiveInt
    ref_block_prefix: HiveInt
    signatures: list[Signature]
    transaction_id: TransactionId
    transaction_num: HiveInt
