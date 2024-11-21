from __future__ import annotations

from typing import Final, Generic

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation
from pydantic import BaseModel

DEFAULT_CURRENT_ORDERID: Final[Uint32t] = Uint32t(0)
DEFAULT_OPEN_ORDERID: Final[Uint32t] = Uint32t(0)


class _FillOrderOperation(VirtualOperation, BaseModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "fill_order"
    __offset__ = 7

    current_owner: AccountName
    current_orderid: Uint32t = DEFAULT_CURRENT_ORDERID
    current_pays: AssetHiveT | AssetHbdT
    open_owner: AccountName
    open_orderid: Uint32t = DEFAULT_OPEN_ORDERID
    open_pays: AssetHiveT | AssetHbdT


class FillOrderOperation(_FillOrderOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class FillOrderOperationLegacy(_FillOrderOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
