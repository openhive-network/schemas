from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import HiveInt
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class EnumVirtualOpsFundament(PreconfiguredBaseModel):
    ops: list[int]
    ops_by_block: list[int]
    next_block_range_begin: HiveInt
    next_operation_begin: HiveInt
