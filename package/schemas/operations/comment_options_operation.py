from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, AssetHbd, LegacyAssetHbd, Uint16t, HIVE_100_PERCENT
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class CommentOptionsOperation(PreconfiguredBaseModel):
    author: AccountName
    permlink: str
    max_accepted_payout: AssetHbd | LegacyAssetHbd  # 1000000000 HBD default value
    percent_hbd: Uint16t = HIVE_100_PERCENT
    allow_votes: bool = True
    allow_curation_rewards: bool = True
    extensions: str
