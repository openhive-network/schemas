from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetVest
from schemas.fields.basic import AccountName
from schemas.operation import Operation


class _DelegateVestingSharesOperation(Operation):
    __operation_name__ = "delegate_vesting_shares"
    __offset__ = 40

    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVest


class DelegateVestingSharesOperation(_DelegateVestingSharesOperation):
    ...


class DelegateVestingSharesOperationLegacy(_DelegateVestingSharesOperation):
    ...
