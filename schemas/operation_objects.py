from __future__ import annotations

from typing import Any

from pydantic import root_validator

from schemas.hive_fields_basic_schemas import (
    HiveDateTime,
    HiveInt,
)
from schemas.hive_fields_custom_schemas import TransactionId
from schemas.operations._operation_representation_types import (
    Hf26AllOperationRepresentationType,
    Hf26OperationRepresentationType,
    Hf26VirtualOperationRepresentationType,
    LegacyAllOperationRepresentationType,
    LegacyOperationRepresentationType,
    LegacyVirtualOperationRepresentationType,
    get_legacy_representation,
)
from schemas.preconfigured_base_model import PreconfiguredBaseModel


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

    @root_validator(pre=True)
    @classmethod
    def check_operation(cls, values: dict[str, Any]) -> dict[str, Any]:
        type_of_operation = values["op"][0]
        value_of_operation = values["op"][1]
        values["op"] = get_legacy_representation(type_of_operation)(type=type_of_operation, value=value_of_operation)
        return values


class Hf26ApiVirtualOperationObject(ApiOperationObjectCommons):
    op: Hf26VirtualOperationRepresentationType  # type: ignore


class LegacyApiVirtualOperationObject(LegacyApiOperationObject):
    op: LegacyVirtualOperationRepresentationType  # type: ignore


class Hf26ApiAllOperationObject(ApiOperationObjectCommons):
    op: Hf26AllOperationRepresentationType  # type: ignore


class LegacyApiAllOperationObject(LegacyApiOperationObject):
    op: LegacyAllOperationRepresentationType  # type: ignore