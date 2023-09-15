from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHive, AssetVests
from schemas.__private.virtual_operation import VirtualOperation


class TransferToVestingCompletedOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetVests]):
    from_account: AccountName
    to_account: AccountName
    hive_vested: AssetHive
    vesting_shares_received: AssetVests
