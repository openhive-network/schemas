from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation

DEFAULT_PAYOUT_MUST_BE_CLAIMED: Final[bool] = False


class _AuthorRewardOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT, AssetVestsT]):
    __operation_name__ = "author_reward"
    __offset__ = 1

    author: AccountName
    permlink: str
    hbd_payout: AssetHbdT
    hive_payout: AssetHiveT
    vesting_payout: AssetVestsT
    curators_vesting_payout: AssetVestsT
    payout_must_be_claimed: bool = DEFAULT_PAYOUT_MUST_BE_CLAIMED


class AuthorRewardOperation(_AuthorRewardOperation[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]):
    ...


class AuthorRewardOperationLegacy(_AuthorRewardOperation[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]):
    ...
