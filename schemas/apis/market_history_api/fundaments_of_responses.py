from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import (
    AssetHbd,
    AssetHive,
    HiveDateTime,
)
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


class GetRecentTradesFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    date: HiveDateTime
    current_pays: AssetHive | AssetHbd
    open_pays: AssetHive | AssetHbd


class GetTradeHistoryFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    date: HiveDateTime
    current_pays: AssetHive | AssetHbd
    open_pays: AssetHive | AssetHbd


class Price(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    base: AssetHive | AssetHbd
    quote: AssetHive | AssetHbd


class Order(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    order_price: Price[AssetHive, AssetHbd]
    real_price: float
    hive: HiveInt
    hbd: HiveInt
    created: HiveDateTime
