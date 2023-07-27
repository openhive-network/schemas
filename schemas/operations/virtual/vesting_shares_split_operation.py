from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetVests
from schemas.preconfigured_base_model import VirtualOperation


class VestingSharesSplitOperation(Generic[AssetVests], GenericModel, VirtualOperation):
    owner: AccountName
    vesting_shares_before_split: AssetVests
    vesting_shares_after_split: AssetVests
