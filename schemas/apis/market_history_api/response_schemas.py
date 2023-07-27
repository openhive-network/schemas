from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.apis.market_history_api.fundaments_of_responses import (
    BucketSizes,
    GetMarketHistoryFundament,
    GetRecentTradesFundament,
    GetTradeHistoryFundament,
    Order,
)
from schemas.hive_fields_basic_schemas import (
    AssetHbd,
    AssetHbdHF26,
    AssetHive,
    AssetHiveHF26,
    HiveList,
)
from schemas.preconfigured_base_model import PreconfiguredBaseModel


class GetMarketHistory(PreconfiguredBaseModel):
    buckets: HiveList[GetMarketHistoryFundament]


class GetMarketHistoryBuckets(PreconfiguredBaseModel):
    bucket_sizes: list[BucketSizes]


class GetRecentTrades(PreconfiguredBaseModel):
    trades: HiveList[GetRecentTradesFundament[AssetHiveHF26, AssetHbdHF26]]


class GetTicker(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """Must specify type of Assets by generic when using"""

    latest: str
    lowest_ask: str
    highest_bid: str
    percent_change: str
    hive_volume: AssetHive
    hbd_volume: AssetHbd


class GetTradeHistory(PreconfiguredBaseModel):
    trades: HiveList[GetTradeHistoryFundament[AssetHiveHF26, AssetHbdHF26]]


class GetVolume(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """Must specify type of Assets by generic when using"""

    hive_volume: AssetHive
    hbd_volume: AssetHbd


class GetOrderBook(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    bids: list[Order[AssetHive, AssetHbd]]
    asks: list[Order[AssetHive, AssetHbd]]
