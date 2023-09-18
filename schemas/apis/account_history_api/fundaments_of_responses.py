from __future__ import annotations

from schemas.__private.operation_objects import Hf26ApiAllOperationObject, LegacyApiAllOperationObject
from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import HiveDateTime, HiveInt


class EnumVirtualOpsFieldFundament(PreconfiguredBaseModel):
    """This is a field for ops_by_block field in EnumVirtualOps model"""

    block: HiveInt
    timestamp: HiveDateTime
    irreversible: bool
    ops: list[Hf26ApiAllOperationObject | LegacyApiAllOperationObject]
