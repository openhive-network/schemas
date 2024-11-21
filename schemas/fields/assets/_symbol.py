from __future__ import annotations

from typing import Any

from pydantic import field_validator, ConfigDict
from typing_extensions import Self

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets._base import AssetBase
from schemas.fields.assets._validators import validate_nai, validate_precision
from schemas.fields.assets.asset_info import AssetInfo
from schemas.fields.hive_int import HiveInt


class AssetSymbolType(PreconfiguredBaseModel, AssetBase):
    """Represents just asset characteristics"""

    decimals: HiveInt
    nai: str
    model_config = ConfigDict(allow_reuse=True)

    @field_validator("nai")
    @classmethod
    @classmethod
    def check_nai(cls, value: Any) -> Any:
        return validate_nai(value=value, asset_info=cls.get_asset_information())

    @field_validator("decimals")
    @classmethod
    @classmethod
    def check_decimals(cls, value: int) -> int:
        return validate_precision(value=value, asset_info=cls.get_asset_information())

    # Part below is because requirements from AssetBase, it's not elegant, but have no solution for now

    @classmethod
    def from_legacy(cls, other: str) -> Self:
        raise NotImplementedError

    @classmethod
    def from_nai(cls, other: dict[str, str | int]) -> Self:
        raise NotImplementedError

    def _get_amount(self) -> int:
        raise NotImplementedError

    def _set_amount(self, amount: int) -> None:
        raise NotImplementedError

    def clone(self, *, amount: Any | int | str | AssetBase | None = None) -> Self:
        if amount is not None:
            raise NotImplementedError
        return self.__class__(decimals=self.decimals, nai=self.nai)


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
