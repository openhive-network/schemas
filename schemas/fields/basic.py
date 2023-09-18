"""
It is file with fields that are used to create model of operation and responses from api
"""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Generic, TypeVar

from pydantic import ConstrainedInt, ConstrainedList, ConstrainedStr, PrivateAttr, StrRegexError, validator
from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.hive_int import HiveInt
from schemas.hive_constants import HIVE_HBD_INTEREST_RATE, HIVE_MAX_BLOCK_SIZE

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator


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
    @staticmethod
    @abstractmethod
    def get_asset_information() -> AssetInfo:
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


def validate_nai(value: Any, asset_info: AssetInfo) -> Any:
    if value != asset_info.nai:
        raise ValueError("Invalid nai !")
    return value


def validate_precision(value: int, asset_info: AssetInfo) -> int:
    if value != asset_info.precision:
        raise ValueError("Invalid decimals")
    return value


class AssetSymbolType(PreconfiguredBaseModel, AssetBase):
    """Represents just asset characteristics"""

    decimals: HiveInt
    nai: str

    class Config:
        allow_reuse = True

    @validator("nai", allow_reuse=True)
    @classmethod
    def check_nai(cls, value: Any) -> Any:
        return validate_nai(value=value, asset_info=cls.get_asset_information())

    @validator("decimals", allow_reuse=True)
    @classmethod
    def check_decimals(cls, value: int) -> int:
        return validate_precision(value=value, asset_info=cls.get_asset_information())


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


class AssetHF26(PreconfiguredBaseModel, AssetBase):
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


class AssetHiveHF26(AssetHF26):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return HiveSymbolType.get_asset_information()

    precision: HiveInt = get_asset_information().precision
    nai: str = get_asset_information().nai


class AssetHbdHF26(AssetHF26):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return HbdSymbolType.get_asset_information()

    nai: str = get_asset_information().nai
    precision: HiveInt = get_asset_information().precision


class AssetVestsHF26(AssetHF26):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return VestsSymbolType.get_asset_information()

    precision: HiveInt = get_asset_information().precision
    nai: str = get_asset_information().nai


class AssetHiveLegacy(AssetLegacy):
    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return HiveSymbolType.get_asset_information()


class AssetHbdLegacy(AssetLegacy):
    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return HbdSymbolType.get_asset_information()


class AssetVestsLegacy(AssetLegacy):
    @classmethod
    def get_asset_information(cls) -> AssetInfo:
        return VestsSymbolType.get_asset_information()


AssetHiveT = TypeVar("AssetHiveT", AssetHiveHF26, AssetHiveLegacy)
AssetHbdT = TypeVar("AssetHbdT", AssetHbdHF26, AssetHbdLegacy)
AssetVestsT = TypeVar("AssetVestsT", AssetVestsHF26, AssetVestsLegacy)


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


class HbdExchangeRate(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    """
    Field similar to price, but just base can be Hive or Hbd. Quote must be Hive.
    To choose format of Assets you can do it like in Price field:
    Legacy -> HbdExchangeRate[AssetHiveLegacy, AssetHbdLegacy](parameters)
    HF26 -> HbdExchangeRate[AssetHiveHF26, AssetHbdHF26](parameters)
    Here Hive also must be first parameter of generic
    """

    base: AssetHiveT | AssetHbdT
    quote: AssetHiveT | AssetHbdT


class LegacyChainProperties(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT]):
    """
    You can choose of Asset format for this field, to do it:
    Legacy -> LegacyChainProperties[AssetHiveLegacy](parameters)
    Nai -> LegacyChainProperties[AssetHiveHF26](parameters)
    """

    account_creation_fee: AssetHiveT
    maximum_block_size: Uint32t = Uint32t(HIVE_MAX_BLOCK_SIZE)
    hbd_interest_rate: Uint16t = Uint16t(HIVE_HBD_INTEREST_RATE)


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
