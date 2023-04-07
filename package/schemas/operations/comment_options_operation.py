from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, AssetHbd, LegacyAssetHbd, Uint16t, HIVE_100_PERCENT


class CommentOptionsOperation(BaseModel, extra=Extra.forbid):
    author: AccountName
    permlink: str
    max_accepted_payout: AssetHbd | LegacyAssetHbd  # 1000000000 HBD default value
    percent_hbd: Uint16t = HIVE_100_PERCENT
    allow_votes: bool = True
    allow_curation_rewards: bool = True
    extensions: str  
