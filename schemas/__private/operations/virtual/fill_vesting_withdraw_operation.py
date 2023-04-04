from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHive, AssetVests
from schemas.__private.preconfigured_base_model import VirtualOperation


class FillVestingWithdrawOperation(Generic[AssetHive, AssetVests], GenericModel, VirtualOperation):
    from_account: AccountName
    to_account: AccountName
    withdrawn: AssetVests
    deposited: AssetVests | AssetHive
