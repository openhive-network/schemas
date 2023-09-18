from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHbdT,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetHiveT,
    Uint32t,
)
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _EscrowApprovedOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "escrow_approved"

    from_: AccountName = Field(alias="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = DEFAULT_REQUEST_ID
    fee: AssetHiveT | AssetHbdT


class EscrowApprovedOperation(_EscrowApprovedOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class EscrowApprovedOperationLegacy(_EscrowApprovedOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
