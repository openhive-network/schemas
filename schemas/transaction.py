from __future__ import annotations

from typing import Any, TypeVar

from pydantic import validator

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.hex import Signature, TransactionId
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.operations.representation_types import (
    Hf26OperationRepresentationType,
    LegacyOperationRepresentationType,
)
from schemas.operations.representations import get_legacy_operation_representation

__all__ = [
    "Transaction",
    "TransactionLegacy",
    "TransactionT",
]


class TransactionCommon(PreconfiguredBaseModel):
    ref_block_num: HiveInt
    ref_block_prefix: HiveInt
    expiration: HiveDateTime
    extensions: list[Any]
    signatures: list[Signature]


class Transaction(TransactionCommon):
    operations: list[Hf26OperationRepresentationType]


class TransactionLegacy(TransactionCommon):
    operations: list[LegacyOperationRepresentationType]
    block_num: HiveInt
    transaction_id: TransactionId
    transaction_num: HiveInt

    # TODO[pydantic]: We couldn't refactor the `validator`, please replace it by `field_validator` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-validators for more information.
    @validator("operations", pre=True, always=True)
    @classmethod
    def operations_converter(cls, value: Any) -> list[LegacyOperationRepresentationType]:
        assert isinstance(value, list)
        return [
            get_legacy_operation_representation(op_name)(type=op_name, value=op_value) for op_name, op_value in value
        ]


TransactionT = TypeVar("TransactionT", bound=Transaction | TransactionLegacy)
