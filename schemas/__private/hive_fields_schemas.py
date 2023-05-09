"""
    It is module with hive fields to use in python code, and to check api response
"""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING, Any, Generic, TypeVar

from pydantic import ConstrainedInt, ConstrainedStr, Field, PrivateAttr, validator
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


class AssetNai(PreconfiguredBaseModel, ABC):
    """Base class for all nai asset fields"""

    amount: HiveInt
    precision: HiveInt
    nai: str

    @classmethod
    @abstractmethod
    def get_nai_pattern(cls) -> str:
        """This method set nai_pattern, which we use to check nai field"""

    @classmethod
    @abstractmethod
    def get_precision(cls) -> int:
        """This method set precision, which we use to check precision field"""

    @validator("nai")
    @classmethod
    def check_nai(cls, value: Any) -> Any:
        if value != cls.get_nai_pattern():
            raise ValueError("Invalid nai !")
        return value

    @validator("precision")
    @classmethod
    def check_precision(cls, value: int) -> int:
        if value != cls.get_precision():
            raise ValueError("Invalid precision")
        return value


class AssetHiveNai(AssetNai):
    precision: HiveInt = HiveInt(3)
    nai: str = "@@000000021"

    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000021"

    @classmethod
    def get_precision(cls) -> int:
        return 3


class AssetHbdNai(AssetNai):
    precision: HiveInt = HiveInt(3)
    nai: str = "@@000000013"

    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000013"

    @classmethod
    def get_precision(cls) -> int:
        return 3


class AssetVestsNai(AssetNai):
    precision: HiveInt = HiveInt(6)
    nai: str = "@@000000037"

    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000037"

    @classmethod
    def get_precision(cls) -> int:
        return 6


class AssetLegacy(ConstrainedStr, ABC):
    """Base class for all legacy assets"""


class AssetHiveLegacy(AssetLegacy):
    regex = re.compile(r"^[0-9]+\.[0-9]{3} (?:HIVE|TESTS)$")


class AssetHbdLegacy(AssetLegacy):
    regex = re.compile(r"^[0-9]+\.[0-9]{3} (?:HBD|TBD)$")


class AssetVestsLegacy(AssetLegacy):
    regex = re.compile(r"^[0-9]+\.[0-9]{6} VESTS$")


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


class Manabar(PreconfiguredBaseModel):
    current_mana: HiveInt
    last_update_time: HiveInt


class DelayedVotes(PreconfiguredBaseModel):
    time: HiveDateTime
    val: HiveInt


class Price(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """
    Valid structure for Price field is:
    base: Hive quote: Hbd or base: Hbd quote: Hive
    You can choose format of Assets, to choose legacy format -> Price[AssetHiveLegacy, AssetHbdLegacy](parameters).
    For Nai format -> Price[AssetHiveNai, AssetHbdNai].
    Remember that Hive must be first parameter of generic !
    """

    base: AssetHive | AssetHbd
    quote: AssetHive | AssetHbd


class Proposal(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    id_: HiveInt = Field(..., alias="id")
    proposal_id: HiveInt
    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbd
    subject: str
    permlink: str
    total_votes: HiveInt
    status: str


class Hex(ConstrainedStr):
    regex = re.compile(r"^[0-9a-fA-F]*$")


class Sha256(Hex):
    min_length = 64
    max_length = 64


class HardforkVersion(ConstrainedStr):
    regex = re.compile(r"^\d+\.\d+\.\d+$")


class Permlink(ConstrainedStr):
    max_length = 256
