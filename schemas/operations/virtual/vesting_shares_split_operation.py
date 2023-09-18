from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _VestingSharesSplitOperation(VirtualOperation, GenericModel, Generic[AssetVestsT]):
    __operation_name__ = "vesting_shares_split"

    owner: AccountName
    vesting_shares_before_split: AssetVestsT
    vesting_shares_after_split: AssetVestsT


class VestingSharesSplitOperation(_VestingSharesSplitOperation[AssetVestsHF26]):
    ...


class VestingSharesSplitOperationLegacy(_VestingSharesSplitOperation[AssetVestsLegacy]):
    ...
