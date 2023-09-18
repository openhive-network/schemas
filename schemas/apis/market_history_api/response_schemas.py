from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.market_history_api.fundaments_of_responses import (
    BucketSizes,
    GetMarketHistoryFundament,
    GetRecentTradesFundament,
    GetTradeHistoryFundament,
    Order,
)
from schemas.fields.basic import (
    AssetHbdHF26,
    AssetHbdT,
    AssetHiveHF26,
    AssetHiveT,
    HiveList,
)


class GetMarketHistory(PreconfiguredBaseModel):
    buckets: HiveList[GetMarketHistoryFundament]


class GetMarketHistoryBuckets(PreconfiguredBaseModel):
    bucket_sizes: list[BucketSizes]


class GetRecentTrades(PreconfiguredBaseModel):
    trades: HiveList[GetRecentTradesFundament[AssetHiveHF26, AssetHbdHF26]]


class GetTicker(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    """Must specify type of Assets by generic when using"""

    latest: str
    lowest_ask: str
    highest_bid: str
    percent_change: str
    hive_volume: AssetHiveT
    hbd_volume: AssetHbdT


class GetTradeHistory(PreconfiguredBaseModel):
    trades: HiveList[GetTradeHistoryFundament[AssetHiveHF26, AssetHbdHF26]]


class GetVolume(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    """Must specify type of Assets by generic when using"""

    hive_volume: AssetHiveT
    hbd_volume: AssetHbdT


class GetOrderBook(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    bids: list[Order[AssetHiveT, AssetHbdT]]
    asks: list[Order[AssetHiveT, AssetHbdT]]
