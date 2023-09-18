from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
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

DEFAULT_PAYOUT_MUST_BE_CLAIMED: Final[bool] = False


class _CommentBenefactorRewardOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd, AssetVests]):
    __operation_name__ = "comment_benefactor_reward"

    benefactor: AccountName
    author: AccountName
    permlink: str
    hbd_payout: AssetHbd
    hive_payout: AssetHive
    vesting_payout: AssetVests
    payout_must_be_claimed: bool = DEFAULT_PAYOUT_MUST_BE_CLAIMED


class CommentBenefactorRewardOperation(_CommentBenefactorRewardOperation[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]):
    ...


class CommentBenefactorRewardOperationLegacy(
    _CommentBenefactorRewardOperation[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
):
    ...
