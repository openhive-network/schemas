from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetVest
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _ReturnVestingDelegationOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "return_vesting_delegation"
    __offset__ = 12

    account: AccountName
    vesting_shares: AssetVest


class ReturnVestingDelegationOperation(_ReturnVestingDelegationOperation):
    ...


class ReturnVestingDelegationOperationLegacy(_ReturnVestingDelegationOperation):
    ...
