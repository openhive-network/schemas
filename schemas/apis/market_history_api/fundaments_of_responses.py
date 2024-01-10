from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets.hbd import AssetHbdT
from schemas.fields.assets.hive import AssetHiveT
from schemas.fields.assets.vests import AssetVestsT
from schemas.fields.basic import AccountName
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
    taker: AccountName
    maker: AccountName


class GetTradeHistoryFundament(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    date: HiveDateTime
    current_pays: AssetHiveT | AssetHbdT
    open_pays: AssetHiveT | AssetHbdT
    taker: AccountName
    maker: AccountName


class Price(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT, AssetVestsT]):
    base: AssetHiveT | AssetHbdT | AssetVestsT
    quote: AssetHiveT | AssetHbdT | AssetVestsT


class Order(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT, AssetVestsT]):
    order_price: Price[AssetHiveT, AssetHbdT, AssetVestsT]
    real_price: float
    hive: HiveInt
    hbd: HiveInt
    created: HiveDateTime
