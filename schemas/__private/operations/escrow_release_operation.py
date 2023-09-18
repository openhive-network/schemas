from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    Uint32t,
)
from schemas.__private.operation import Operation

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class _EscrowReleaseOperation(Operation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "escrow_release"

    from_: AccountName = Field(alias="from")
    to: AccountName
    agent: AccountName
    who: AccountName
    receiver: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    hbd_amount: AssetHbd  # here add  default
    hive_amount: AssetHive  # here add default


class EscrowReleaseOperation(_EscrowReleaseOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class EscrowReleaseOperationLegacy(_EscrowReleaseOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
