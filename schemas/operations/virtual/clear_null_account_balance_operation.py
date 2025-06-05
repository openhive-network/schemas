from __future__ import annotations

from schemas.fields.resolvables import AnyAsset
from schemas.virtual_operation import VirtualOperation


class _ClearNullAccountBalanceOperation(VirtualOperation, kw_only=True):
    total_cleared: list[AnyAsset]

    @classmethod
    def get_name(cls) -> str:
        return "clear_null_account_balance"

    @classmethod
    def vop_offset(cls) -> int:
        return 15


class ClearNullAccountBalanceOperation(_ClearNullAccountBalanceOperation):
    ...


class ClearNullAccountBalanceOperationLegacy(_ClearNullAccountBalanceOperation):
    ...
