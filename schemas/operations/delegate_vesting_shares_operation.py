from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import AccountName
from schemas.operation import Operation


class _DelegateVestingSharesOperation(Operation, GenericModel, Generic[AssetVestsT]):
    __operation_name__ = "delegate_vesting_shares"

    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVestsT


class DelegateVestingSharesOperation(_DelegateVestingSharesOperation[AssetVestsHF26]):
    ...


class DelegateVestingSharesOperationLegacy(_DelegateVestingSharesOperation[AssetVestsLegacy]):
    ...
