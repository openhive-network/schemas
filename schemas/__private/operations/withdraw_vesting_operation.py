from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetVests
from schemas.__private.operation import Operation


class WithdrawVestingOperation(Operation, GenericModel, Generic[AssetVests]):
    account: AccountName
    vesting_shares: AssetVests
