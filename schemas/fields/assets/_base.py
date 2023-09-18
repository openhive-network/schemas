from __future__ import annotations

import re
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

from pydantic import ConstrainedStr, StrRegexError, validator

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets._validators import validate_nai, validate_precision
from schemas.fields.assets.asset_info import AssetInfo
from schemas.fields.hive_int import HiveInt

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator


class AssetBase(ABC):
    @staticmethod
    @abstractmethod
    def get_asset_information() -> AssetInfo:
        """This method returns asset details, which we use to perform checks"""


class AssetLegacy(ConstrainedStr, AssetBase, ABC):
    """Base class for all legacy assets"""

    @classmethod
    def legacy_regex_validator(cls, value: str) -> str:
        if "-" in value:
            raise ValueError("Asset could not be negative value!")
        info = cls.get_asset_information()
        regex = re.compile(r"^\d+\.\d{" + str(info.precision) + r"} (?:" + "|".join(info.symbol) + r")$")
        if regex.match(value) is None:
            raise StrRegexError(pattern=cls._get_pattern(regex))
        return value

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield from super().__get_validators__()
        yield cls.legacy_regex_validator


class AssetNaiAmount(HiveInt):
    """
    Amount in HF26 have to be serialized as str, to be properly recognized by c++
    """

    ge = 0

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield from super().__get_validators__()
        yield cls.__stringify

    @classmethod
    def __stringify(cls, value: int | str) -> str:
        return str(value)


class AssetHF26(PreconfiguredBaseModel, AssetBase, ABC):
    """Base class for all nai asset fields"""

    amount: AssetNaiAmount
    precision: HiveInt
    nai: str

    class Config:
        allow_reuse = True

    @validator("nai", allow_reuse=True)
    @classmethod
    def check_nai(cls, value: Any) -> Any:
        return validate_nai(value=value, asset_info=cls.get_asset_information())

    @validator("precision", allow_reuse=True)
    @classmethod
    def check_precision(cls, value: int) -> int:
        return validate_precision(value=value, asset_info=cls.get_asset_information())
