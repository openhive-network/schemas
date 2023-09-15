from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHive,
    HiveDateTime,
    Uint32t,
)
from schemas.__private.operation import Operation

DEFAULT_ORDER_ID: Final[Uint32t] = Uint32t(0)
DEFAULT_FILL_OR_KILL: Final[bool] = False


class LimitOrderCreateOperation(Operation, GenericModel, Generic[AssetHive, AssetHbd]):
    owner: AccountName
    orderid: Uint32t = DEFAULT_ORDER_ID
    amount_to_sell: AssetHive | AssetHbd
    min_to_receive: AssetHive | AssetHbd
    fill_or_kill: bool = DEFAULT_FILL_OR_KILL
    expiration: HiveDateTime
