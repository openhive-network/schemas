from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import HiveDateTime, HiveInt
from schemas.__private.operation_objects import Hf26ApiAllOperationObject, LegacyApiAllOperationObject
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class EnumVirtualOpsFieldFundament(PreconfiguredBaseModel):
    """This is a field for ops_by_block field in EnumVirtualOps model"""

    block: HiveInt
    timestamp: HiveDateTime
    irreversible: bool
    ops: list[Hf26ApiAllOperationObject | LegacyApiAllOperationObject]
