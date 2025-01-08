from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetVest
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _VestingSharesSplitOperation(VirtualOperation):
    __operation_name__ = "vesting_shares_split"
    __offset__ = 29

    owner: AccountName
    vesting_shares_before_split: AssetVest
    vesting_shares_after_split: AssetVest


class VestingSharesSplitOperation(_VestingSharesSplitOperation):
    ...


class VestingSharesSplitOperationLegacy(_VestingSharesSplitOperation):
    ...
