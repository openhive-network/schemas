from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, AssetVests
from schemas.__private.virtual_operation import VirtualOperation

DEFAULT_PAYOUT_MUST_BE_CLAIMED: Final[bool] = False


class CommentBenefactorRewardOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd, AssetVests]):
    benefactor: AccountName
    author: AccountName
    permlink: str
    hbd_payout: AssetHbd
    hive_payout: AssetHive
    vesting_payout: AssetVests
    payout_must_be_claimed: bool = DEFAULT_PAYOUT_MUST_BE_CLAIMED
