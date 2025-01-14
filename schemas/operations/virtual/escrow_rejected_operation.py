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


class _EscrowRejectedOperation(VirtualOperation, kw_only=True):
    from_: AccountName = Field(alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = DEFAULT_REQUEST_ID
    hbd_amount: AssetHbd
    hive_amount: AssetHive
    fee: AssetUnion[AssetHive, AssetHbd]


    @classmethod
    def get_name(cls):
        return "escrow_rejected"
    
    @classmethod
    def offset(cls):
        return 40

class EscrowRejectedOperation(_EscrowRejectedOperation):
    ...


class EscrowRejectedOperationLegacy(_EscrowRejectedOperation):
    ...
