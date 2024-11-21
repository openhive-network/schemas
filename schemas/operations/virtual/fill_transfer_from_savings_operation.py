from __future__ import annotations

from typing import Final, Generic

from pydantic import BaseModel, Field

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _FillTransferFromSavingsOperation(VirtualOperation, BaseModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "fill_transfer_from_savings"
    __offset__ = 9

    from_: AccountName = Field(alias="from")
    to: AccountName
    amount: AssetHiveT | AssetHbdT
    request_id: Uint32t = DEFAULT_REQUEST_ID
    memo: str


class FillTransferFromSavingsOperation(_FillTransferFromSavingsOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class FillTransferFromSavingsOperationLegacy(_FillTransferFromSavingsOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
