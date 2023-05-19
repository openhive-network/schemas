from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import (
    HiveDateTime,
    HiveInt,
)
from schemas.__private.hive_fields_custom_schemas import TransactionId
from schemas.__private.operations import (
    Hf26OperationRepresentationType,  # pyright: ignore
    Hf26VirtualOperationRepresentationType,  # pyright: ignore
    LegacyOperationRepresentationType,  # pyright: ignore
    LegacyVirtualOperationRepresentationType,  # pyright: ignore
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class ApiOperationObjectCommons(PreconfiguredBaseModel):
    trx_id: TransactionId
    block: HiveInt
    trx_in_block: HiveInt
    op_in_trx: HiveInt
    virtual_op: bool
    operation_id: HiveInt
    timestamp: HiveDateTime


class Hf26ApiOperationObject(ApiOperationObjectCommons):
    op: Hf26OperationRepresentationType  # type: ignore


class LegacyApiOperationObject(ApiOperationObjectCommons):
    op: LegacyOperationRepresentationType  # type: ignore


class Hf26ApiVirtualOperationObject(ApiOperationObjectCommons):
    op: Hf26VirtualOperationRepresentationType  # type: ignore


class LegacyApiVirtualOperationObject(ApiOperationObjectCommons):
    op: LegacyVirtualOperationRepresentationType  # type: ignore


class Hf26ApiAllOperationObject(ApiOperationObjectCommons):
    op: Hf26OperationRepresentationType | Hf26VirtualOperationRepresentationType


class LegacyApiAllOperationObject(ApiOperationObjectCommons):
    op: LegacyOperationRepresentationType | LegacyVirtualOperationRepresentationType
