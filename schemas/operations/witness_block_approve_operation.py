from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation


class WitnessBlockApproveOperation(Operation):
    __operation_name__ = "witness_block_approve"

    witness: AccountName
    block_id: Uint32t
