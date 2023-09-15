from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, AssetVests
from schemas.__private.virtual_operation import VirtualOperation


class HardforkHiveOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd, AssetVests]):
    account: AccountName
    treasury: AccountName
    other_affected_accounts: list[AccountName]
    hbd_transferred: AssetHbd
    hive_transferred: AssetHive
    vests_converted: AssetVests
    total_hive_from_vests: AssetHive
