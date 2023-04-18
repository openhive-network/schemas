from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, AssetHbdLegacy, Uint16t
    from schemas.types import AssetHbd


class CommentOptionsOperationStrict(PreconfiguredBaseModel):
    author: AccountName
    permlink: str
    max_accepted_payout: AssetHbd | AssetHbdLegacy  # 1000000000 HBD default value
    percent_hbd: Uint16t
    allow_votes: bool
    allow_curation_rewards: bool
    extensions: str
