from __future__ import annotations

from schemas.fields.resolvables import AnyAsset
from schemas.virtual_operation import VirtualOperation


class _ConsolidateTreasuryBalanceOperation(VirtualOperation, kw_only=True):
    total_moved: list[AnyAsset]

    @classmethod
    def get_name(cls) -> str:
        return "consolidate_treasury_balance"

    @classmethod
    def offset(cls) -> int:
        return 21


class ConsolidateTreasuryBalanceOperation(_ConsolidateTreasuryBalanceOperation):
    ...


class ConsolidateTreasuryBalanceOperationLegacy(_ConsolidateTreasuryBalanceOperation):
    ...
