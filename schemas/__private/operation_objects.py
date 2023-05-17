from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import (
    HiveDateTime,
    HiveInt,
)
from schemas.__private.hive_fields_custom_schemas import TransactionId
from schemas.__private.operations import (
    Hf26OperationRepresentationType,  # pyright: ignore
    LegacyOperationRepresentationType,  # pyright: ignore
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
