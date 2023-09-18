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
    AssetVests,
    AssetVestsHF26,
    AssetVestsLegacy,
)
from schemas.virtual_operation import VirtualOperation


class _HardforkHiveOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd, AssetVests]):
    __operation_name__ = "hardfork_hive"

    account: AccountName
    treasury: AccountName
    other_affected_accounts: list[AccountName]
    hbd_transferred: AssetHbd
    hive_transferred: AssetHive
    vests_converted: AssetVests
    total_hive_from_vests: AssetHive


class HardforkHiveOperation(_HardforkHiveOperation[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]):
    ...


class HardforkHiveOperationLegacy(_HardforkHiveOperation[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]):
    ...
