from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation


class _HardforkHiveOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT, AssetVestsT]):
    __operation_name__ = "hardfork_hive"
    __offset__ = 18

    account: AccountName
    treasury: AccountName
    other_affected_accounts: list[AccountName]
    hbd_transferred: AssetHbdT
    hive_transferred: AssetHiveT
    vests_converted: AssetVestsT
    total_hive_from_vests: AssetHiveT


class HardforkHiveOperation(_HardforkHiveOperation[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]):
    ...


class HardforkHiveOperationLegacy(_HardforkHiveOperation[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]):
    ...
