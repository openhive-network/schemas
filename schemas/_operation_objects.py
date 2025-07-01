from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.hex import TransactionId
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.operations import (
    AnyHf26Operation,
    AnyLegacyOperation,
    Hf26VirtualOperationRepresentation,
    LegacyVirtualOperationRepresentation,
)


class ApiOperationObjectCommonsBase(PreconfiguredBaseModel):
    trx_id: TransactionId
    block: HiveInt
    trx_in_block: HiveInt
    op_in_trx: HiveInt
    virtual_op: bool
    timestamp: HiveDateTime


class ApiOperationObjectCommons(ApiOperationObjectCommonsBase):
    operation_id: HiveInt


class Hf26ApiOperationObject(ApiOperationObjectCommons):
    op: AnyHf26Operation


class LegacyApiOperationObject(ApiOperationObjectCommons):
    op: AnyLegacyOperation


class Hf26ApiVirtualOperationObject(ApiOperationObjectCommons):
    op: Hf26VirtualOperationRepresentation


class LegacyApiVirtualOperationObject(ApiOperationObjectCommons):
    op: LegacyVirtualOperationRepresentation


class Hf26ApiAllOperationObject(ApiOperationObjectCommons):
    op: AnyHf26Operation


class LegacyApiAllOperationObject(ApiOperationObjectCommonsBase):
    op: AnyLegacyOperation
