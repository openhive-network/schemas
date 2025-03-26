from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.hex import TransactionId
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.operations import (
    AnyHf26Operation,
    AnyLegacyOperation,
    Hf26OperationRepresentation,
    Hf26VirtualOperationRepresentation,
    LegacyOperationRepresentation,
    LegacyVirtualOperationRepresentation,
)


class ApiOperationObjectCommons(PreconfiguredBaseModel):
    trx_id: TransactionId
    block: HiveInt
    trx_in_block: HiveInt
    op_in_trx: HiveInt
    virtual_op: bool
    operation_id: HiveInt
    timestamp: HiveDateTime


class Hf26ApiOperationObject(ApiOperationObjectCommons):
    op: Hf26OperationRepresentation


class LegacyApiOperationObject(ApiOperationObjectCommons):
    op: LegacyOperationRepresentation


class Hf26ApiVirtualOperationObject(ApiOperationObjectCommons):
    op: Hf26VirtualOperationRepresentation


class LegacyApiVirtualOperationObject(ApiOperationObjectCommons):
    op: LegacyVirtualOperationRepresentation


class Hf26ApiAllOperationObject(ApiOperationObjectCommons):
    op: AnyHf26Operation


class LegacyApiAllOperationObject(ApiOperationObjectCommons):
    op: AnyLegacyOperation
