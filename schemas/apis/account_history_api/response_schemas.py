from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic.generics import GenericModel

from schemas._operation_objects import (
    Hf26ApiOperationObject,
    Hf26ApiVirtualOperationObject,
    LegacyApiOperationObject,
    LegacyApiVirtualOperationObject,
)
from schemas.operations import AnyOperationRepresentation, AnyLegacyOperationRepresentation, AnyEveryOperation

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.account_history_api.fundaments_of_responses import EnumVirtualOpsFieldFundament
from schemas.fields.hex import Signature, TransactionId
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
# from schemas.operations.representation_types import (
#     Hf26OperationRepresentationType,
#     LegacyOperationRepresentationType,
# )

# OperationT = TypeVar("OperationT", bound=Hf26OperationRepresentationType | LegacyOperationRepresentationType)
# ApiOperationObjectT = TypeVar("ApiOperationObjectT", bound=Hf26ApiOperationObject | LegacyApiOperationObject)
# ApiVirtualOperationObjectT = TypeVar(
#     "ApiVirtualOperationObjectT", bound=Hf26ApiVirtualOperationObject | LegacyApiVirtualOperationObject
# )


class EnumVirtualOps(PreconfiguredBaseModel):
    ops: list[Hf26ApiVirtualOperationObject]
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
    operations: list[AnyOperationRepresentation]
    ref_block_num: HiveInt
    ref_block_prefix: HiveInt
    signatures: list[Signature]
    transaction_id: TransactionId
    transaction_num: HiveInt
