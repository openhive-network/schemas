from __future__ import annotations

from schemas.fields.resolvables import AnyAsset
from schemas.virtual_operation import VirtualOperation


class ConsolidateTreasuryBalanceOperation(VirtualOperation, kw_only=True):
    total_moved: list[AnyAsset]

    @classmethod
    def get_name(cls) -> str:
        return "consolidate_treasury_balance"

    @classmethod
    def vop_offset(cls) -> int:
        return 21
