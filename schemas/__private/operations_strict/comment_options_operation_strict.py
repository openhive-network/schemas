from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, Uint16t
from schemas.__private.hive_fields_schemas_strict import AssetHbdStrict
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class CommentOptionsOperationStrict(PreconfiguredBaseModel):
    author: AccountName
    permlink: str
    max_accepted_payout: AssetHbdStrict  # 1000000000 HBD default value
    percent_hbd: Uint16t
    allow_votes: bool
    allow_curation_rewards: bool
    extensions: str