from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetVests, AssetVestsHF26, AssetVestsLegacy
from schemas.__private.operation import Operation


class _DelegateVestingSharesOperation(Operation, GenericModel, Generic[AssetVests]):
    __operation_name__ = "delegate_vesting_shares"

    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVests


class DelegateVestingSharesOperationHF26(_DelegateVestingSharesOperation[AssetVestsHF26]):
    ...


class DelegateVestingSharesOperationLegacy(_DelegateVestingSharesOperation[AssetVestsLegacy]):
    ...
