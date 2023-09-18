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
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _FillTransferFromSavingsOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "fill_transfer_from_savings"

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHive | AssetHbd
    request_id: Uint32t = DEFAULT_REQUEST_ID
    memo: str


class FillTransferFromSavingsOperation(_FillTransferFromSavingsOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class FillTransferFromSavingsOperationLegacy(_FillTransferFromSavingsOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
