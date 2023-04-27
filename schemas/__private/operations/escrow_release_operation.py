from __future__ import annotations

from typing import Final

from pydantic import Field

from schemas.__private.hive_fields_schemas import AccountName, AssetHbd, AssetHive, Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class EscrowReleaseOperation(PreconfiguredBaseModel):
    from_: AccountName = Field(..., alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    receiver: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    hbd_amount: AssetHbd  # here add default value
    hive_amount: AssetHive  # here add default value
