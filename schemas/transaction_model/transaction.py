from __future__ import annotations

from typing import Any, TypeVar

from pydantic import validator

from schemas.__private.hive_fields_basic_schemas import HiveDateTime, HiveInt
from schemas.__private.hive_fields_custom_schemas import Signature, TransactionId
from schemas.__private.operations.representation_types import (
    Hf26OperationRepresentationType,
    LegacyOperationRepresentationType,
)
from schemas.__private.operations.representations import get_legacy_representation
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class TransactionCommon(PreconfiguredBaseModel):
    ref_block_num: HiveInt
    ref_block_prefix: HiveInt
    expiration: HiveDateTime
    extensions: list[Any]
    signatures: list[Signature]


class Hf26Transaction(TransactionCommon):
    operations: list[Hf26OperationRepresentationType]


class LegacyTransaction(TransactionCommon):
    operations: list[LegacyOperationRepresentationType]
    block_num: HiveInt
    transaction_id: TransactionId
    transaction_num: HiveInt

    @validator("operations", pre=True, always=True)
    @classmethod
    def operations_converter(cls, value: Any) -> list[LegacyOperationRepresentationType]:
        assert isinstance(value, list)
        return [get_legacy_representation(op_name)(type=op_name, value=op_value) for op_name, op_value in value]


TransactionT = TypeVar("TransactionT", bound=Hf26Transaction | LegacyTransaction)
