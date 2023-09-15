from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, Uint32t
from schemas.__private.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class EscrowRejectedOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd]):
    from_: AccountName = Field(alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = DEFAULT_REQUEST_ID
    hbd_amount: AssetHbd
    hive_amount: AssetHive
    fee: AssetHive | AssetHbd
