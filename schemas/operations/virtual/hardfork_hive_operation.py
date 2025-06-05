from __future__ import annotations

from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVests
from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation


class _HardforkHiveOperation(VirtualOperation, kw_only=True):
    account: AccountName
    treasury: AccountName
    other_affected_accounts: list[AccountName]
    hbd_transferred: AssetHbd
    hive_transferred: AssetHive
    vests_converted: AssetVests
    total_hive_from_vests: AssetHive

    @classmethod
    def get_name(cls) -> str:
        return "hardfork_hive"

    @classmethod
    def vop_offset(cls) -> int:
        return 18


class HardforkHiveOperation(_HardforkHiveOperation):
    ...


class HardforkHiveOperationLegacy(_HardforkHiveOperation):
    ...
