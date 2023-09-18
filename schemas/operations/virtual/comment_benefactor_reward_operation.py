from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHbdT,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetHiveT,
    AssetVestsHF26,
    AssetVestsLegacy,
    AssetVestsT,
)
from schemas.virtual_operation import VirtualOperation

DEFAULT_PAYOUT_MUST_BE_CLAIMED: Final[bool] = False


class _CommentBenefactorRewardOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT, AssetVestsT]):
    __operation_name__ = "comment_benefactor_reward"

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
