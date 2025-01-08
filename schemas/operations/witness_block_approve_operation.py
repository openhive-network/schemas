from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation


class WitnessBlockApproveOperation(Operation):
    witness: AccountName
    block_id: Uint32t

    @classmethod
    def get_name(cls) -> str:
        return "witness_block_approve"

    @classmethod
    def offset(cls) -> int:
        return 16
