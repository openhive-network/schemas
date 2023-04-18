from __future__ import annotations

from typing import TYPE_CHECKING, Final

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName

DEFAULT_DECLINE: Final[bool] = True


class DeclineVotingRightsOperation(PreconfiguredBaseModel):
    account: AccountName
    decline: bool = DEFAULT_DECLINE
