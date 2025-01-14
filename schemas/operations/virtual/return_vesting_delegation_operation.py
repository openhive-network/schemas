from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetVest
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _ReturnVestingDelegationOperation(VirtualOperation, kw_only=True):
    account: AccountName
    vesting_shares: AssetVest


    @classmethod
    def get_name(cls):
        return "return_vesting_delegation"
    
    @classmethod
    def offset(cls):
        return 12

class ReturnVestingDelegationOperation(_ReturnVestingDelegationOperation):
    ...


class ReturnVestingDelegationOperationLegacy(_ReturnVestingDelegationOperation):
    ...
