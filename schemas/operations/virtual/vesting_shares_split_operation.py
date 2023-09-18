from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import AccountName, AssetVests, AssetVestsHF26, AssetVestsLegacy
from schemas.virtual_operation import VirtualOperation


class _VestingSharesSplitOperation(VirtualOperation, GenericModel, Generic[AssetVests]):
    __operation_name__ = "vesting_shares_split"

    owner: AccountName
    vesting_shares_before_split: AssetVests
    vesting_shares_after_split: AssetVests


class VestingSharesSplitOperation(_VestingSharesSplitOperation[AssetVestsHF26]):
    ...


class VestingSharesSplitOperationLegacy(_VestingSharesSplitOperation[AssetVestsLegacy]):
    ...
