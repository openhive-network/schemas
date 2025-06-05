from __future__ import annotations

from schemas.fields.assets._base import AssetVests
from schemas.fields.basic import AccountName
from schemas.operation import Operation


class _DelegateVestingSharesOperation(Operation):
    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVests

    @classmethod
    def get_name(cls) -> str:
        return "delegate_vesting_shares"

    @classmethod
    def offset(cls) -> int:
        return 40


class DelegateVestingSharesOperation(_DelegateVestingSharesOperation):
    ...


class DelegateVestingSharesOperationLegacy(_DelegateVestingSharesOperation):
    ...
