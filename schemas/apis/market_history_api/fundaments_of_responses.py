from __future__ import annotations

from msgspec import field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import AccountName, FloatAsString
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.fields.resolvables import AnyAsset, AssetUnionAssetHiveAssetHbd


class GetMarketHistoryField(PreconfiguredBaseModel, kw_only=True):
    """This is schema of hive and non_hive fields in get_market_history_response"""

    high: HiveInt
    low: HiveInt
    open_: HiveInt = field(name="open")
    close: HiveInt
    volume: HiveInt


class GetMarketHistoryFundament(PreconfiguredBaseModel, kw_only=True):
    id_: HiveInt = field(name="id")
    open_: HiveDateTime = field(name="open")
    seconds: HiveInt
    hive: GetMarketHistoryField
    non_hive: GetMarketHistoryField


class BucketSizes(HiveInt):
    """Enum which represents sizes of Buckets"""


class GetRecentTradesFundament(PreconfiguredBaseModel, kw_only=True):
    date: HiveDateTime
    current_pays: AssetUnionAssetHiveAssetHbd
    open_pays: AssetUnionAssetHiveAssetHbd
    taker: AccountName
    maker: AccountName


class GetTradeHistoryFundament(PreconfiguredBaseModel, kw_only=True):
    date: HiveDateTime
    current_pays: AssetUnionAssetHiveAssetHbd
    open_pays: AssetUnionAssetHiveAssetHbd
    taker: AccountName
    maker: AccountName


class Price(PreconfiguredBaseModel, kw_only=True):
    base: AnyAsset
    quote: AnyAsset


class Order(PreconfiguredBaseModel, kw_only=True):
    order_price: Price
    real_price: FloatAsString
    hive: HiveInt
    hbd: HiveInt
    created: HiveDateTime
