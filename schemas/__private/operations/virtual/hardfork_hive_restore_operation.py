from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive
from schemas.__private.preconfigured_base_model import VirtualOperation


class HardforkHiveRestoreOperation(Generic[AssetHive, AssetHbd], GenericModel, VirtualOperation):
    account: AccountName
    treasury: AccountName
    hbd_transferred: AssetHbd
    hive_transferred: AssetHive
