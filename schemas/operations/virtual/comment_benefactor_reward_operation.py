from __future__ import annotations

from typing import Final, Generic

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation
from pydantic import BaseModel

DEFAULT_PAYOUT_MUST_BE_CLAIMED: Final[bool] = False


class _CommentBenefactorRewardOperation(VirtualOperation, BaseModel, Generic[AssetHiveT, AssetHbdT, AssetVestsT]):
    __operation_name__ = "comment_benefactor_reward"
    __offset__ = 13

    benefactor: AccountName
    author: AccountName
    permlink: str
    hbd_payout: AssetHbdT
    hive_payout: AssetHiveT
    vesting_payout: AssetVestsT
    payout_must_be_claimed: bool = DEFAULT_PAYOUT_MUST_BE_CLAIMED


class CommentBenefactorRewardOperation(_CommentBenefactorRewardOperation[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]):
    ...


class CommentBenefactorRewardOperationLegacy(
    _CommentBenefactorRewardOperation[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
):
    ...
