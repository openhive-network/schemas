from __future__ import annotations

from typing import Generic

from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation
from pydantic import BaseModel


class _VestingSharesSplitOperation(VirtualOperation, BaseModel, Generic[AssetVestsT]):
    __operation_name__ = "vesting_shares_split"
    __offset__ = 29

    owner: AccountName
    vesting_shares_before_split: AssetVestsT
    vesting_shares_after_split: AssetVestsT


class VestingSharesSplitOperation(_VestingSharesSplitOperation[AssetVestsHF26]):
    ...


class VestingSharesSplitOperationLegacy(_VestingSharesSplitOperation[AssetVestsLegacy]):
    ...
