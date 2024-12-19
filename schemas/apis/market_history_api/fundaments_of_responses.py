from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets._base import AssetBase, AssetHbd, AssetHive, AssetHiveOrHbd, AssetVest
from schemas.fields.basic import AccountName
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt


class GetMarketHistoryField(PreconfiguredBaseModel, kw_only=True):
    """This is schema of hive and non_hive fields in get_market_history_response"""

    high: HiveInt
    low: HiveInt
    open_: HiveInt = Field(alias="open")
    close: HiveInt
    volume: HiveInt


class GetMarketHistoryFundament(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = Field(alias="id")
    open_: HiveDateTime = Field(alias="open")
    seconds: HiveInt
    hive: GetMarketHistoryField
    non_hive: GetMarketHistoryField


class BucketSizes(HiveInt):
    """Enum which represents sizes of Buckets"""


class GetRecentTradesFundament(PreconfiguredBaseModel, kw_only=True):
    date: HiveDateTime
    current_pays: AssetHive | AssetHbd
    open_pays: AssetHive | AssetHbd
    taker: AccountName
    maker: AccountName


class GetTradeHistoryFundament(PreconfiguredBaseModel, kw_only=True):
    date: HiveDateTime
    current_pays: AssetHive | AssetHbd
    open_pays:  AssetHive | AssetHbd
    taker: AccountName
    maker: AccountName


class Price(PreconfiguredBaseModel, kw_only=True):
    base: AssetBase
    quote: AssetBase


class Order(PreconfiguredBaseModel, kw_only=True):
    order_price: Price
    real_price: float
    hive: HiveInt
    hbd: HiveInt
    created: HiveDateTime
