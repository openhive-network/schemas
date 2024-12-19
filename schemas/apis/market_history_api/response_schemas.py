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
from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVest
from schemas.fields.hive_list import HiveList


class GetMarketHistory(PreconfiguredBaseModel):
    buckets: HiveList[GetMarketHistoryFundament]


class GetMarketHistoryBuckets(PreconfiguredBaseModel):
    bucket_sizes: list[BucketSizes]


class GetRecentTrades(PreconfiguredBaseModel):
    trades: HiveList[GetRecentTradesFundament]


class GetTicker(PreconfiguredBaseModel):
    """Must specify type of Assets by generic when using"""

    latest: str
    lowest_ask: str
    highest_bid: str
    percent_change: str
    hive_volume: AssetHive
    hbd_volume: AssetHbd


class GetTradeHistory(PreconfiguredBaseModel):
    trades: HiveList[GetTradeHistoryFundament]


class GetVolume(PreconfiguredBaseModel):
    """Must specify type of Assets by generic when using"""

    hive_volume: AssetHive
    hbd_volume: AssetHbd


class GetOrderBook(PreconfiguredBaseModel):
    bids: list[Order]
    asks: list[Order]
