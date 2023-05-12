from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_schemas import AccountName
from schemas.__private.preconfigured_base_model import Operation

DEFAULT_DECLINE: Final[bool] = True


class DeclineVotingRightsOperation(Operation):
    account: AccountName
    decline: bool = DEFAULT_DECLINE
