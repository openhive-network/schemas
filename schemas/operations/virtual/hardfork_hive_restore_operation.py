from __future__ import annotations

from typing import Generic

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation
from pydantic import BaseModel


class _HardforkHiveRestoreOperation(VirtualOperation, BaseModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "hardfork_hive_restore"
    __offset__ = 19

    account: AccountName
    treasury: AccountName
    hbd_transferred: AssetHbdT
    hive_transferred: AssetHiveT


class HardforkHiveRestoreOperation(_HardforkHiveRestoreOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class HardforkHiveRestoreOperationLegacy(_HardforkHiveRestoreOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
