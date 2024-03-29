from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class _EscrowReleaseOperation(Operation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "escrow_release"
    __offset__ = 29

    from_: AccountName = Field(alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    receiver: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    hbd_amount: AssetHbdT  # here add  default
    hive_amount: AssetHiveT  # here add default


class EscrowReleaseOperation(_EscrowReleaseOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class EscrowReleaseOperationLegacy(_EscrowReleaseOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
