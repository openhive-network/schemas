from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVest
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation

DEFAULT_PAYOUT_MUST_BE_CLAIMED: Final[bool] = False


class _AuthorRewardOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "author_reward"
    __offset__ = 1

    author: AccountName
    permlink: str
    hbd_payout: AssetHbd
    hive_payout: AssetHive
    vesting_payout: AssetVest
    curators_vesting_payout: AssetVest
    payout_must_be_claimed: bool = DEFAULT_PAYOUT_MUST_BE_CLAIMED


class AuthorRewardOperation(_AuthorRewardOperation):
    ...


class AuthorRewardOperationLegacy(_AuthorRewardOperation):
    ...
