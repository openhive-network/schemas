from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import AccountName, AssetVests, AssetVestsHF26, AssetVestsLegacy
from schemas.virtual_operation import VirtualOperation


class _ReturnVestingDelegationOperation(VirtualOperation, GenericModel, Generic[AssetVests]):
    __operation_name__ = "return_vesting_delegation"

    account: AccountName
    vesting_shares: AssetVests


class ReturnVestingDelegationOperation(_ReturnVestingDelegationOperation[AssetVestsHF26]):
    ...


class ReturnVestingDelegationOperationLegacy(_ReturnVestingDelegationOperation[AssetVestsLegacy]):
    ...
