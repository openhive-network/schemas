from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation

DEFAULT_PAYOUT_MUST_BE_CLAIMED: Final[bool] = False


class _CurationRewardOperation(VirtualOperation, GenericModel, Generic[AssetVestsT]):
    __operation_name__ = "curation_reward"
    __offset__ = 2

    curator: AccountName
    reward: AssetVestsT
    comment_author: AccountName
    comment_permlink: str
    payout_must_be_claimed: bool = DEFAULT_PAYOUT_MUST_BE_CLAIMED


class CurationRewardOperation(_CurationRewardOperation[AssetVestsHF26]):
    ...


class CurationRewardOperationLegacy(_CurationRewardOperation[AssetVestsLegacy]):
    ...
