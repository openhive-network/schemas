from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.fields.resolvables import AssetUnion
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)

from msgspec import field

class _EscrowApprovedOperation(VirtualOperation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = DEFAULT_REQUEST_ID
    fee: AssetUnion[AssetHive, AssetHbd]

    @classmethod
    def get_name(cls):
        return "escrow_approved"
    
    @classmethod
    def offset(cls):
        return 39

class EscrowApprovedOperation(_EscrowApprovedOperation):
    ...


class EscrowApprovedOperationLegacy(_EscrowApprovedOperation):
    ...
