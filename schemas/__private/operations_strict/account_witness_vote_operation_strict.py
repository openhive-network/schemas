from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class AccountWitnessVoteOperationStrict(PreconfiguredBaseModel):
    account: AccountName
    witness: AccountName
    approve: bool
