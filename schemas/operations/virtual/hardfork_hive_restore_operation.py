from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
)
from schemas.virtual_operation import VirtualOperation


class _HardforkHiveRestoreOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "hardfork_hive_restore"

    account: AccountName
    treasury: AccountName
    hbd_transferred: AssetHbd
    hive_transferred: AssetHive


class HardforkHiveRestoreOperation(_HardforkHiveRestoreOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class HardforkHiveRestoreOperationLegacy(_HardforkHiveRestoreOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
