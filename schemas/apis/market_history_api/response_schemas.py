from __future__ import annotations

from typing import Generic

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.market_history_api.fundaments_of_responses import (
    BucketSizes,
    GetMarketHistoryFundament,
    GetRecentTradesFundament,
    GetTradeHistoryFundament,
    Order,
)
from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveT
from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsT
from schemas.fields.hive_list import HiveList
from pydantic import BaseModel


class GetMarketHistory(PreconfiguredBaseModel):
    buckets: HiveList[GetMarketHistoryFundament]


class GetMarketHistoryBuckets(PreconfiguredBaseModel):
    bucket_sizes: list[BucketSizes]


class GetRecentTrades(PreconfiguredBaseModel):
    trades: HiveList[GetRecentTradesFundament[AssetHiveHF26, AssetHbdHF26]]


class GetTickerFundament(PreconfiguredBaseModel, BaseModel, Generic[AssetHiveT, AssetHbdT]):
    """Must specify type of Assets by generic when using"""

    latest: str
    lowest_ask: str
    highest_bid: str
    percent_change: str
    hive_volume: AssetHiveT
    hbd_volume: AssetHbdT


GetTicker = GetTickerFundament[AssetHiveHF26, AssetHbdHF26]


class GetTradeHistory(PreconfiguredBaseModel):
    trades: HiveList[GetTradeHistoryFundament[AssetHiveHF26, AssetHbdHF26]]


class GetVolumeFundament(PreconfiguredBaseModel, BaseModel, Generic[AssetHiveT, AssetHbdT]):
    """Must specify type of Assets by generic when using"""

    hive_volume: AssetHiveT
    hbd_volume: AssetHbdT


GetVolume = GetVolumeFundament[AssetHiveHF26, AssetHbdHF26]


class GetOrderBookFundament(PreconfiguredBaseModel, BaseModel, Generic[AssetHiveT, AssetHbdT, AssetVestsT]):
    bids: list[Order[AssetHiveT, AssetHbdT, AssetVestsT]]
    asks: list[Order[AssetHiveT, AssetHbdT, AssetVestsT]]


GetOrderBook = GetOrderBookFundament[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]
