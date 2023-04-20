from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, AssetVestsLegacy
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class WithdrawVestingOperation(PreconfiguredBaseModel):
    account: AccountName
    vesting_shares: AssetVestsLegacy
