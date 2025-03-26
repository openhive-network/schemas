from __future__ import annotations

from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation


class _HardforkHiveRestoreOperation(VirtualOperation, kw_only=True):
    account: AccountName
    treasury: AccountName
    hbd_transferred: AssetHbd
    hive_transferred: AssetHive

    @classmethod
    def get_name(cls) -> str:
        return "hardfork_hive_restore"

    @classmethod
    def vop_offset(cls) -> int:
        return 19


class HardforkHiveRestoreOperation(_HardforkHiveRestoreOperation):
    ...


class HardforkHiveRestoreOperationLegacy(_HardforkHiveRestoreOperation):
    ...
