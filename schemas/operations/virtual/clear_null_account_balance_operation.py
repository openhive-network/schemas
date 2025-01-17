from __future__ import annotations




from schemas.virtual_operation import VirtualOperation
from schemas.fields.resolvables import AnyAsset


class _ClearNullAccountBalanceOperation(VirtualOperation, kw_only=True):
    total_cleared: list[AnyAsset]


    @classmethod
    def get_name(cls):
        return "clear_null_account_balance"
    
    @classmethod
    def offset(cls):
        return 15

class ClearNullAccountBalanceOperation(_ClearNullAccountBalanceOperation):
    ...


class ClearNullAccountBalanceOperationLegacy(
    _ClearNullAccountBalanceOperation
):
    ...
