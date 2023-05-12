from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas import AccountName
from schemas.__private.preconfigured_base_model import Operation

DEFAULT_APPROVE: Final[bool] = True


class AccountWitnessVoteOperation(Operation):
    account: AccountName
    witness: AccountName
    approve: bool = DEFAULT_APPROVE
