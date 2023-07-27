from __future__ import annotations

from schemas.hive_fields_basic_schemas import AccountName, Uint32t
from schemas.preconfigured_base_model import Operation


class WitnessBlockApproveOperation(Operation):
    witness: AccountName
    block_id: Uint32t
