from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, Uint32t
from schemas.__private.preconfigured_base_model import VirtualOperation

DEFAULT_ORDERID: Final[Uint32t] = Uint32t(0)


class LimitOrderCancelledOperation(Generic[AssetHive, AssetHbd], GenericModel, VirtualOperation):
    seller: AccountName
    orderid: Uint32t = DEFAULT_ORDERID
    amount_back: AssetHive | AssetHbd
