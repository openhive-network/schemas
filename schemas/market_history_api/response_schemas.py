from __future__ import annotations

from typing import Any, Generic

from pydantic import validator
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AssetHbd, AssetHbdHF26, AssetHive, AssetHiveHF26, HiveInt
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.market_history_api.fundaments_of_responses import (
    BucketSizes,
    GetMarketHistoryFundament,
    GetRecentTradesFundament,
    GetTradeHistoryFundament,
)


class GetMarketHistory(PreconfiguredBaseModel):
    buckets: list[GetMarketHistoryFundament]


class GetMarketHistoryBuckets(PreconfiguredBaseModel):
    bucket_sizes: list[HiveInt]

    @validator("bucket_sizes")
    @classmethod
    def check_bucket_sizes(cls, value: Any) -> Any:
        for enum, given in zip(BucketSizes, value, strict=True):
            if enum.value != given:
                raise ValueError("value from response is not the same as enum")
        return value


class GetRecentTrades(PreconfiguredBaseModel):
    trades: list[GetRecentTradesFundament[AssetHiveHF26, AssetHbdHF26]]


class GetTicker(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """Must specify type of Assets by generic when using"""

    latest: str
    lowest_ask: str
    highest_bid: str
    percent_change: str
    hive_volume: AssetHive
    hbd_volume: AssetHbd


class GetTradeHistory(PreconfiguredBaseModel):
    trades: list[GetTradeHistoryFundament[AssetHiveHF26, AssetHbdHF26]]


class GetVolume(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """Must specify type of Assets by generic when using"""

    hive_volume: AssetHive
    hbd_volume: AssetHbd
