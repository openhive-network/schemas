from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, Uint32t
from schemas.__private.operation import Operation


class WitnessBlockApproveOperation(Operation):
    witness: AccountName
    block_id: Uint32t
