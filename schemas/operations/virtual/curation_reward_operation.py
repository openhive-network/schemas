from __future__ import annotations

from typing import Final


from schemas.fields.assets._base import AssetVest
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation

DEFAULT_PAYOUT_MUST_BE_CLAIMED: Final[bool] = False


class _CurationRewardOperation(VirtualOperation, kw_only=True):
    curator: AccountName
    reward: AssetVest
    author: AccountName
    permlink: str
    payout_must_be_claimed: bool = DEFAULT_PAYOUT_MUST_BE_CLAIMED


    @classmethod
    def get_name(cls):
        return "curation_reward"
    
    @classmethod
    def offset(cls):
        return 2

class CurationRewardOperation(_CurationRewardOperation):
    ...


class CurationRewardOperationLegacy(_CurationRewardOperation):
    ...
