from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import (
    AssetHbdT,
    AssetHiveT,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt


class GetMarketHistoryField(PreconfiguredBaseModel):
    """This is schema of hive and non_hive fields in get_market_history_response"""

    high: HiveInt
    low: HiveInt
    open_: HiveInt = Field(alias="open")
    close: HiveInt
    volume: HiveInt


class GetMarketHistoryFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(alias="id")
    open_: HiveDateTime = Field(alias="open")
    seconds: HiveInt
    hive: GetMarketHistoryField
    non_hive: GetMarketHistoryField


class BucketSizes(HiveInt):
    """Enum which represents sizes of Buckets"""


class GetRecentTradesFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    date: HiveDateTime
    current_pays: AssetHiveT | AssetHbdT
    open_pays: AssetHiveT | AssetHbdT


class GetTradeHistoryFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    date: HiveDateTime
    current_pays: AssetHiveT | AssetHbdT
    open_pays: AssetHiveT | AssetHbdT


class Price(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    base: AssetHiveT | AssetHbdT
    quote: AssetHiveT | AssetHbdT


class Order(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    order_price: Price[AssetHiveT, AssetHbdT]
    real_price: float
    hive: HiveInt
    hbd: HiveInt
    created: HiveDateTime
