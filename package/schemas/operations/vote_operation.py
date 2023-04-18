from __future__ import annotations

from typing import TYPE_CHECKING, Final

from schemas.__private.hive_fields_schemas import Int16t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName

DEFAULT_WEIGHT: Final[Int16t] = Int16t(0)


class VoteOperation(PreconfiguredBaseModel):
    voter: AccountName
    author: AccountName
    permlink: str
    weight: Int16t = DEFAULT_WEIGHT
