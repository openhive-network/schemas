from __future__ import annotations

from typing import Final

from schemas.fields.assets._base import AssetVests
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation

DEFAULT_PAYOUT_MUST_BE_CLAIMED: Final[bool] = False


class CurationRewardOperation(VirtualOperation, kw_only=True):
    curator: AccountName
    reward: AssetVests
    author: AccountName
    permlink: str
    payout_must_be_claimed: bool = DEFAULT_PAYOUT_MUST_BE_CLAIMED

    @classmethod
    def get_name(cls) -> str:
        return "curation_reward"

    @classmethod
    def vop_offset(cls) -> int:
        return 2
