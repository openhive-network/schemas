from __future__ import annotations

from abc import abstractmethod
from typing import Any

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets._validators import validate_nai, validate_precision
from schemas.fields.assets.asset_info import AssetInfo
from schemas.fields.hive_int import HiveInt


class AssetSymbolType(PreconfiguredBaseModel):
    """Represents just asset characteristics"""

    decimals: HiveInt
    nai: str

    def __post_init__(self) -> None:
        self.check_nai(self.nai)
        self.check_decimals(self.decimals)

    @classmethod
    def check_nai(cls, value: Any) -> Any:
        return validate_nai(value=value, asset_info=cls.get_asset_information())

    @classmethod
    def check_decimals(cls, value: HiveInt) -> int:
        return validate_precision(value=value.value, asset_info=cls.get_asset_information())

    @staticmethod
    @abstractmethod
    def get_asset_information() -> AssetInfo:
        ...


class HiveSymbolType(AssetSymbolType):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return AssetInfo(precision=HiveInt(3), nai="@@000000021", symbol=("HIVE", "TESTS"))

    decimals: HiveInt = get_asset_information().precision
    nai: str = get_asset_information().nai


class HbdSymbolType(AssetSymbolType):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return AssetInfo(precision=HiveInt(3), nai="@@000000013", symbol=("HBD", "TBD"))

    decimals: HiveInt = get_asset_information().precision
    nai: str = get_asset_information().nai


class VestsSymbolType(AssetSymbolType):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return AssetInfo(precision=HiveInt(6), nai="@@000000037", symbol=("VESTS", "VESTS"))

    decimals: HiveInt = get_asset_information().precision
    nai: str = get_asset_information().nai
