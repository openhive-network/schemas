from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetVests
from schemas.__private.preconfigured_base_model import VirtualOperation


class VestingSharesSplitOperation(VirtualOperation, GenericModel, Generic[AssetVests]):
    owner: AccountName
    vesting_shares_before_split: AssetVests
    vesting_shares_after_split: AssetVests
