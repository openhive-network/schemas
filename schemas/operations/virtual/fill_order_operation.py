from __future__ import annotations

from typing import Final, Generic

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

DEFAULT_CURRENT_ORDERID: Final[Uint32t] = Uint32t(0)
DEFAULT_OPEN_ORDERID: Final[Uint32t] = Uint32t(0)


class _FillOrderOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "fill_order"

    current_owner: AccountName
    current_orderid: Uint32t = DEFAULT_CURRENT_ORDERID
    current_pays: AssetHive | AssetHbd
    open_owner: AccountName
    open_orderid: Uint32t = DEFAULT_OPEN_ORDERID
    open_pays: AssetHive | AssetHbd


class FillOrderOperation(_FillOrderOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class FillOrderOperationLegacy(_FillOrderOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
