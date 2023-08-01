from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, AssetVests
from schemas.__private.preconfigured_base_model import VirtualOperation


class HardforkHiveOperation(Generic[AssetHive, AssetHbd, AssetVests], GenericModel, VirtualOperation):
    account: AccountName
    treasury: AccountName
    other_affected_accounts: list[AccountName]
    hbd_transferred: AssetHbd
    hive_transferred: AssetHive
    vests_converted: AssetVests
    total_hive_from_vests: AssetHive
