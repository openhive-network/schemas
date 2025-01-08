from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVest

from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation


class _HardforkHiveOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "hardfork_hive"
    __offset__ = 18

    account: AccountName
    treasury: AccountName
    other_affected_accounts: list[AccountName]
    hbd_transferred: AssetHbd
    hive_transferred: AssetHive
    vests_converted: AssetVest
    total_hive_from_vests: AssetHive


class HardforkHiveOperation(_HardforkHiveOperation):
    ...


class HardforkHiveOperationLegacy(_HardforkHiveOperation):
    ...
