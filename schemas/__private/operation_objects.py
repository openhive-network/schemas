from __future__ import annotations

from typing import Any

from pydantic import root_validator

from schemas.__private.hive_fields_basic_schemas import (
    HiveDateTime,
    HiveInt,
)
from schemas.__private.hive_fields_custom_schemas import TransactionId
from schemas.__private.operations import (
    Hf26OperationRepresentationType,  # pyright: ignore
    Hf26VirtualOperationRepresentationType,  # pyright: ignore
    LegacyAllOperationRepresentationType,  # pyright: ignore
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

    @root_validator(pre=True)
    @classmethod
    def check_operation(cls, values: dict[str, Any]) -> dict[str, Any]:
        type_of_operation = values["op"][0]
        value_of_operation = values["op"][1]
        result = {"type": type_of_operation, "value": value_of_operation}

        values["op"] = result
        return values


class Hf26ApiVirtualOperationObject(ApiOperationObjectCommons):
    op: Hf26VirtualOperationRepresentationType  # type: ignore


class LegacyApiVirtualOperationObject(LegacyApiOperationObject):
    op: LegacyVirtualOperationRepresentationType  # type: ignore


class Hf26ApiAllOperationObject(ApiOperationObjectCommons):
    op: Hf26OperationRepresentationType | Hf26VirtualOperationRepresentationType


class LegacyApiAllOperationObject(LegacyApiOperationObject):
    op: LegacyAllOperationRepresentationType  # type: ignore
