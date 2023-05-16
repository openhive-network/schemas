"""
It is file with fields that are used to create model of operation and responses from api
"""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Any, Generic, TypeVar

from pydantic import ConstrainedInt, ConstrainedStr, Field, PrivateAttr, StrRegexError, validator
from pydantic.generics import GenericModel

from schemas.__private.hive_constants import HBD_INTEREST_RATE, MAXIMUM_BLOCK_SIZE
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from collections.abc import Iterator

    from pydantic.typing import CallableGenerator


class HiveInt(ConstrainedInt):
    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate
        yield from super().__get_validators__()

    @classmethod
    def validate(cls, value: Any) -> int:
        error_template = ValueError("The value could only be int or string that can be converted to int!")

        if type(value) is int:
            return value

        if type(value) is str:
            try:
                return int(value)
            except (ValueError, TypeError) as error:
                raise error_template from error
        raise error_template


class EmptyString(ConstrainedStr):
    min_length = 0
    max_length = 0


class AccountName(ConstrainedStr):
    __name_segment = PrivateAttr(r"[a-z][a-z0-9\-]+[a-z0-9]")
    regex = rf"^{__name_segment.default}(?:\.{__name_segment.default})*$"
    min_length = 3
    max_length = 16


class PublicKey(ConstrainedStr):
    regex = re.compile(r"^(?:STM|TST)[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{7,51}$")


class HiveDateTime(datetime):
    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate

    @classmethod
    def validate(cls, value: Any) -> datetime:
        if type(value) is datetime:
            return value

        try:
            return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
        except ValueError as error:
            raise ValueError("date must be in format %Y-%m-%dT%H:%M:%S") from error


class Authority(PreconfiguredBaseModel):
    weight_threshold: HiveInt
    account_auths: list[tuple[AccountName, HiveInt]]
    key_auths: list[tuple[PublicKey, HiveInt]]


class AssetNaiAmount(HiveInt):
    """
    Amount in nai have to be serialized as str, to be properly recognized by c++
    """

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield from super().__get_validators__()
        yield cls.__stringify

    @classmethod
    def __stringify(cls, value: int | str) -> str:
        return str(value)


@dataclass
class AssetInfo:
    precision: HiveInt
    nai: str
    symbol: tuple[str, str]


class AssetBase(ABC):
    @classmethod
    @abstractmethod
    def get_asset_information(cls) -> AssetInfo:
        """This method returns asset details, which we use to perform checks"""


class AssetLegacy(ConstrainedStr, AssetBase):
    """Base class for all legacy assets"""

    @classmethod
    def legacy_regex_validator(cls, value: str) -> str:
        info = cls.get_asset_information()
        regex = re.compile(r"^\d+\.\d{" + str(info.precision) + r"} (?:" + "|".join(info.symbol) + r")$")
        if regex.match(value) is None:
            raise StrRegexError(pattern=cls._get_pattern(regex))
        return value

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield from super().__get_validators__()
        yield cls.legacy_regex_validator


class AssetNai(PreconfiguredBaseModel, AssetBase):
    """Base class for all nai asset fields"""

    amount: AssetNaiAmount
    precision: HiveInt
    nai: str

    @validator("nai")
    @classmethod
    def check_nai(cls, value: Any) -> Any:
        if value != cls.get_asset_information().nai:
            raise ValueError("Invalid nai !")
        return value

    @validator("precision")
    @classmethod
    def check_precision(cls, value: int) -> int:
        if value != cls.get_asset_information().precision:
            raise ValueError("Invalid precision")
        return value


class AssetHiveNai(AssetNai):
    precision: HiveInt = Field(default_factory=lambda: AssetHiveNai.get_asset_information().precision)
    nai: str = Field(default_factory=lambda: AssetHiveNai.get_asset_information().nai)

    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return AssetInfo(precision=HiveInt(3), nai="@@000000021", symbol=("HIVE", "TESTS"))


class AssetHbdNai(AssetNai):
    precision: HiveInt = Field(default_factory=lambda: AssetHbdNai.get_asset_information().precision)
    nai: str = Field(default_factory=lambda: AssetHbdNai.get_asset_information().nai)

    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return AssetInfo(precision=HiveInt(3), nai="@@000000013", symbol=("HBD", "TBD"))


class AssetVestsNai(AssetNai):
    precision: HiveInt = Field(default_factory=lambda: AssetVestsNai.get_asset_information().precision)
    nai: str = Field(default_factory=lambda: AssetVestsNai.get_asset_information().nai)

    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return AssetInfo(precision=HiveInt(6), nai="@@000000037", symbol=("VESTS", "VESTS"))


class AssetHiveLegacy(AssetLegacy):
    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return AssetHiveNai.get_asset_information()


class AssetHbdLegacy(AssetLegacy):
    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return AssetHbdNai.get_asset_information()


class AssetVestsLegacy(AssetLegacy):
    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return AssetVestsNai.get_asset_information()


AssetHive = TypeVar("AssetHive", AssetHiveNai, AssetHiveLegacy)
AssetHbd = TypeVar("AssetHbd", AssetHbdNai, AssetHbdLegacy)
AssetVests = TypeVar("AssetVests", AssetVestsNai, AssetVestsLegacy)


class Uint32t(ConstrainedInt):
    ge = 0
    le = 4294967295


class Uint16t(ConstrainedInt):
    ge = 0
    le = 65535


class Int64t(ConstrainedInt):
    ge = -9223372036854775808
    le = 9223372036854775807


class Int16t(ConstrainedInt):
    ge = -32768
    le = 32767


class CustomIdType(int):
    @classmethod
    def __get_validators__(cls) -> Iterator[Any]:
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> int:
        max_id_length = 32
        if len(str(v)) > max_id_length:
            raise ValueError("Must be shorter than 32 !")
        return int(v)


class HbdExchangeRate(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """
    Field similar to price, but just base can be Hive or Hbd. Quote must be Hive.
    To choose format of Assets you can do it like in Price field:
    Legacy -> HbdExchangeRate[AssetHiveLegacy, AssetHbdLegacy](parameters)
    Nai -> HbdExchangeRate[AssetHiveNai, AssetNaiHbd](parameters)
    Here Hive also must be first parameter of generic
    """

    base: AssetHive | AssetHbd
    quote: AssetHive


class LegacyChainProperties(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    """
    You can choose of Asset format for this field, to do it:
    Legacy -> LegacyChainProperties[AssetHiveLegacy](parameters)
    Nai -> LegacyChainProperties[AssetHiveNai](parameters)
    """

    account_creation_fee: AssetHive
    maximum_block_size: Uint32t = Uint32t(MAXIMUM_BLOCK_SIZE)
    hbd_interest_rate: Uint16t = Uint16t(HBD_INTEREST_RATE)
