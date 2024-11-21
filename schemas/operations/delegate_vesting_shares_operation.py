from __future__ import annotations

from typing import Generic

from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import AccountName
from schemas.operation import Operation
from pydantic import BaseModel


class _DelegateVestingSharesOperation(Operation, BaseModel, Generic[AssetVestsT]):
    __operation_name__ = "delegate_vesting_shares"
    __offset__ = 40

    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVestsT


class DelegateVestingSharesOperation(_DelegateVestingSharesOperation[AssetVestsHF26]):
    ...


class DelegateVestingSharesOperationLegacy(_DelegateVestingSharesOperation[AssetVestsLegacy]):
    ...
