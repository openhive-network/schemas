from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _ReturnVestingDelegationOperation(VirtualOperation, GenericModel, Generic[AssetVestsT]):
    __operation_name__ = "return_vesting_delegation"

    account: AccountName
    vesting_shares: AssetVestsT


class ReturnVestingDelegationOperation(_ReturnVestingDelegationOperation[AssetVestsHF26]):
    ...


class ReturnVestingDelegationOperationLegacy(_ReturnVestingDelegationOperation[AssetVestsLegacy]):
    ...
