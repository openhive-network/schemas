"""
It is file with fields that are used to create model of operation and responses from api
"""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, Generic, TypeVar

from pydantic import ConstrainedInt, ConstrainedList, ConstrainedStr, Field, PrivateAttr, StrRegexError, validator
from pydantic.generics import GenericModel

from schemas.__private.hive_constants import HBD_INTEREST_RATE, MAXIMUM_BLOCK_SIZE
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator
    from typing_extensions import Self


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
        if isinstance(value, datetime):
            return cls.__normalize(value)

        try:
            return cls.__normalize(datetime.strptime(value, "%Y-%m-%dT%H:%M:%S"))
        except ValueError as error:
            raise ValueError("date must be in format %Y-%m-%dT%H:%M:%S") from error

    @classmethod
    def __normalize(cls, value: datetime) -> datetime:
        return value.replace(tzinfo=timezone.utc)

    @classmethod
    def now(cls) -> Self:  # type: ignore[override]
        return cls.utcnow()


class Authority(PreconfiguredBaseModel):
    weight_threshold: HiveInt
    account_auths: list[tuple[AccountName, HiveInt]]
    key_auths: list[tuple[PublicKey, HiveInt]]


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


class AssetHF26(PreconfiguredBaseModel, AssetBase):
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


class AssetHiveHF26(AssetHF26):
    precision: HiveInt = Field(default_factory=lambda: AssetHiveHF26.get_asset_information().precision)
    nai: str = Field(default_factory=lambda: AssetHiveHF26.get_asset_information().nai)

    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return AssetInfo(precision=HiveInt(3), nai="@@000000021", symbol=("HIVE", "TESTS"))


class AssetHbdHF26(AssetHF26):
    precision: HiveInt = Field(default_factory=lambda: AssetHbdHF26.get_asset_information().precision)
    nai: str = Field(default_factory=lambda: AssetHbdHF26.get_asset_information().nai)

    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return AssetInfo(precision=HiveInt(3), nai="@@000000013", symbol=("HBD", "TBD"))


class AssetVestsHF26(AssetHF26):
    precision: HiveInt = Field(default_factory=lambda: AssetVestsHF26.get_asset_information().precision)
    nai: str = Field(default_factory=lambda: AssetVestsHF26.get_asset_information().nai)

    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return AssetInfo(precision=HiveInt(6), nai="@@000000037", symbol=("VESTS", "VESTS"))


class AssetHiveLegacy(AssetLegacy):
    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return AssetHiveHF26.get_asset_information()


class AssetHbdLegacy(AssetLegacy):
    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return AssetHbdHF26.get_asset_information()


class AssetVestsLegacy(AssetLegacy):
    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return AssetVestsHF26.get_asset_information()


AssetHive = TypeVar("AssetHive", AssetHiveHF26, AssetHiveLegacy)
AssetHbd = TypeVar("AssetHbd", AssetHbdHF26, AssetHbdLegacy)
AssetVests = TypeVar("AssetVests", AssetVestsHF26, AssetVestsLegacy)


class Uint8t(ConstrainedInt):
    ge = 0
    le = 255


class Uint16t(ConstrainedInt):
    ge = 0
    le = 65535


class Int16t(ConstrainedInt):
    ge = -32768
    le = 32767


class Uint32t(ConstrainedInt):
    ge = 0
    le = 4294967295


class Int64t(ConstrainedInt):
    ge = -9223372036854775808
    le = 9223372036854775807


class Uint64t(ConstrainedInt):
    ge = 0
    le = 18446744073709554615


class CustomIdType(ConstrainedStr):
    max_length = 32


class HbdExchangeRate(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """
    Field similar to price, but just base can be Hive or Hbd. Quote must be Hive.
    To choose format of Assets you can do it like in Price field:
    Legacy -> HbdExchangeRate[AssetHiveLegacy, AssetHbdLegacy](parameters)
    HF26 -> HbdExchangeRate[AssetHiveHF26, AssetHbdHF26](parameters)
    Here Hive also must be first parameter of generic
    """

    base: AssetHive | AssetHbd
    quote: AssetHive | AssetHbd


class LegacyChainProperties(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    """
    You can choose of Asset format for this field, to do it:
    Legacy -> LegacyChainProperties[AssetHiveLegacy](parameters)
    Nai -> LegacyChainProperties[AssetHiveHF26](parameters)
    """

    account_creation_fee: AssetHive
    maximum_block_size: Uint32t = Uint32t(MAXIMUM_BLOCK_SIZE)
    hbd_interest_rate: Uint16t = Uint16t(HBD_INTEREST_RATE)


class ShareType(Int64t):
    """Identical data-type as Int64t"""


class UShareType(Uint64t):
    """Identical data-type as Uint64t"""


HiveBaseModel = TypeVar("HiveBaseModel", bound=PreconfiguredBaseModel)

if TYPE_CHECKING:
    HiveList = list
else:

    class HiveList(ConstrainedList, Generic[HiveBaseModel]):
        """Some responses could return empty list, it should not raise any error. This type makes it possible"""

        min_items = 0
