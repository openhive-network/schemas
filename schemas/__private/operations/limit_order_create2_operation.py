from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHive,
    AssetHiveHF26,
    HbdExchangeRate,
    HiveDateTime,
    Uint32t,
)
from schemas.__private.preconfigured_base_model import Operation

DEFAULT_FILL_OR_KILL: Final[bool] = False


class LimitOrderCreate2Operation(Operation, GenericModel, Generic[AssetHbd, AssetHive]):
    owner: AccountName
    order_id: Uint32t
    amount_to_sell: AssetHive | AssetHbd
    fill_or_kill: bool = DEFAULT_FILL_OR_KILL
    exchange_rate: HbdExchangeRate[AssetHiveHF26, AssetHbdHF26]
    expiration: HiveDateTime
