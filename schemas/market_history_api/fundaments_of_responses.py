from __future__ import annotations

from enum import IntEnum
from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AssetHbd, AssetHive, HiveDateTime, HiveInt
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class GetMarketHistoryField(PreconfiguredBaseModel):
    """This is schema of hive and non_hive fields in get_market_history_response"""

    high: HiveInt
    low: HiveInt
    open_: HiveInt = Field(..., alias="open")
    close: HiveInt
    volume: HiveInt


class GetMarketHistoryFundament(PreconfiguredBaseModel):
    id_: HiveInt = Field(..., alias="id")
    open_: HiveDateTime = Field(..., alias="open")
    seconds: HiveInt
    hive: GetMarketHistoryField
    non_hive: GetMarketHistoryField


class BucketSizes(IntEnum):
    """Enum which represents sizes of Buckets"""

    FIRST = 15
    SECOND = 60
    THIRD = 300
    FOURTH = 3600
    FIFTH = 86400


class GetRecentTradesFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    date: HiveDateTime
    current_pays: AssetHive | AssetHbd
    open_pays: AssetHive | AssetHbd


class GetTradeHistoryFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    date: HiveDateTime
    current_pays: AssetHive | AssetHbd
    open_pays: AssetHive | AssetHbd
