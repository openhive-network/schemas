from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetHive, AssetVests
from schemas.preconfigured_base_model import VirtualOperation


class TransferToVestingCompletedOperation(Generic[AssetHive, AssetVests], GenericModel, VirtualOperation):
    from_account: AccountName
    to_account: AccountName
    hive_vested: AssetHive
    vesting_shares_received: AssetVests
