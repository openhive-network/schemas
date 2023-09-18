from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetVests, AssetVestsHF26, AssetVestsLegacy
from schemas.__private.virtual_operation import VirtualOperation

DEFAULT_PAYOUT_MUST_BE_CLAIMED: Final[bool] = False


class _CurationRewardOperation(VirtualOperation, GenericModel, Generic[AssetVests]):
    __operation_name__ = "curation_reward"

    curator: AccountName
    reward: AssetVests
    comment_author: AccountName
    comment_permlink: str
    payout_must_be_claimed: bool = DEFAULT_PAYOUT_MUST_BE_CLAIMED


class CurationRewardOperation(_CurationRewardOperation[AssetVestsHF26]):
    ...


class CurationRewardOperationLegacy(_CurationRewardOperation[AssetVestsLegacy]):
    ...
