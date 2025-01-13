from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetVest
from schemas.fields.basic import AccountName
from schemas.operation import Operation


class _DelegateVestingSharesOperation(Operation):
    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVest


    @classmethod
    def get_name(cls):
        return "delegate_vesting_shares"
    
    @classmethod
    def offset(cls):
        return 40

class DelegateVestingSharesOperation(_DelegateVestingSharesOperation):
    ...


class DelegateVestingSharesOperationLegacy(_DelegateVestingSharesOperation):
    ...
