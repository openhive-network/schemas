from __future__ import annotations

from typing import Final

from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVests
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation

DEFAULT_PAYOUT_MUST_BE_CLAIMED: Final[bool] = False


class AuthorRewardOperation(VirtualOperation, kw_only=True):
    author: AccountName
    permlink: str
    hbd_payout: AssetHbd
    hive_payout: AssetHive
    vesting_payout: AssetVests
    curators_vesting_payout: AssetVests
    payout_must_be_claimed: bool = DEFAULT_PAYOUT_MUST_BE_CLAIMED

    @classmethod
    def get_name(cls) -> str:
        return "author_reward"

    @classmethod
    def vop_offset(cls) -> int:
        return 1
