from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel


from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)

from msgspec import field

class _EscrowReleaseOperation(Operation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    receiver: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    hbd_amount: AssetHbd  # here add  default
    hive_amount: AssetHive  # here add default


    @classmethod
    def get_name(cls):
        return "escrow_release"
    
    @classmethod
    def offset(cls):
        return 29

class EscrowReleaseOperation(_EscrowReleaseOperation):
    ...


class EscrowReleaseOperationLegacy(_EscrowReleaseOperation):
    ...
