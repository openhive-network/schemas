from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, Uint32t
from schemas.__private.preconfigured_base_model import VirtualOperation

DEFAULT_CURRENT_ORDERID: Final[Uint32t] = Uint32t(0)
DEFAULT_OPEN_ORDERID: Final[Uint32t] = Uint32t(0)


class FillOrderOperation(Generic[AssetHive, AssetHbd], GenericModel, VirtualOperation):
    current_owner: AccountName
    current_orderid: Uint32t = DEFAULT_CURRENT_ORDERID
    current_pays: AssetHive | AssetHbd
    open_owner: AccountName
    open_orderid: Uint32t = DEFAULT_OPEN_ORDERID
    open_pays: AssetHive | AssetHbd
