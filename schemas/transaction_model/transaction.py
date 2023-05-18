from __future__ import annotations

from typing import Any

from schemas.__private.hive_fields_basic_schemas import HiveDateTime, HiveInt
from schemas.__private.hive_fields_custom_schemas import Signature
from schemas.__private.operations import Hf26OperationRepresentationType, LegacyOperationRepresentationType
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class TransactionCommon(PreconfiguredBaseModel):
    ref_block_num: HiveInt
    ref_block_prefix: HiveInt
    expiration: HiveDateTime
    extensions: list[Any]
    signatures: Signature


class Hf26Transaction(TransactionCommon):
    operations: list[Hf26OperationRepresentationType]


class LegacyTransaction(TransactionCommon):
    operations: list[LegacyOperationRepresentationType]
