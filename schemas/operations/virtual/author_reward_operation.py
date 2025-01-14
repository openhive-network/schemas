from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVest
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation

DEFAULT_PAYOUT_MUST_BE_CLAIMED: Final[bool] = False


class _AuthorRewardOperation(VirtualOperation, kw_only=True):
    author: AccountName
    permlink: str
    hbd_payout: AssetHbd
    hive_payout: AssetHive
    vesting_payout: AssetVest
    curators_vesting_payout: AssetVest
    payout_must_be_claimed: bool = DEFAULT_PAYOUT_MUST_BE_CLAIMED


    @classmethod
    def get_name(cls):
        return "author_reward"
    
    @classmethod
    def offset(cls):
        return 1

class AuthorRewardOperation(_AuthorRewardOperation):
    ...


class AuthorRewardOperationLegacy(_AuthorRewardOperation):
    ...
