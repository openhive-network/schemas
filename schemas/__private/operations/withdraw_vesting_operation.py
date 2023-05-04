from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_schemas import AccountName, AssetVests
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class WithdrawVestingOperation(PreconfiguredBaseModel, GenericModel, Generic[AssetVests]):
    account: AccountName
    vesting_shares: AssetVests
