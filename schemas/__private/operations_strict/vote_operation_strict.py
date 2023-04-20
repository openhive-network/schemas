from __future__ import annotations

from schemas.__private.hive_fields_schemas_strict import AccountName, Int16t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class VoteOperationStrict(PreconfiguredBaseModel):
    voter: AccountName
    author: AccountName
    permlink: str
    weight: Int16t
