from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetVests
from schemas.preconfigured_base_model import Operation


class WithdrawVestingOperation(Generic[AssetVests], GenericModel, Operation):
    account: AccountName
    vesting_shares: AssetVests
