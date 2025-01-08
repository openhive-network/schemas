from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive

from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation


class _HardforkHiveRestoreOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "hardfork_hive_restore"
    __offset__ = 19

    account: AccountName
    treasury: AccountName
    hbd_transferred: AssetHbd
    hive_transferred: AssetHive


class HardforkHiveRestoreOperation(_HardforkHiveRestoreOperation):
    ...


class HardforkHiveRestoreOperationLegacy(_HardforkHiveRestoreOperation):
    ...
