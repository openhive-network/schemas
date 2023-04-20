"""
    It is module with hive fields to use in python code, and to check api response(fields without defaults - non-strict)
    It helps to create hive fields without remember about for example fill nai when creating AssetNai.
"""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING, Any, TypeAlias

from pydantic import ConstrainedInt, ConstrainedStr, validator

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
    regex = re.compile(r"[a-z][a-z0-9\-]+[a-z0-9]")
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

        return value


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
    @validator("nai")
    def check_nai(cls, v: Any) -> Any:
        if v != cls.get_nai_pattern():
            raise ValueError("Invalid nai !")
        return v


class AssetHiveNai(AssetNai):
    precision: HiveInt = HiveInt(3)
    nai: str = "@@000000021"

    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000021"


class AssetHbdNai(AssetNai):
    precision: HiveInt = HiveInt(3)
    nai: str = "@@000000013"

    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000013"


class AssetVestsNai(AssetNai):
    precision: HiveInt = HiveInt(3)
    nai: str = "@@000000037"

    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000037"


class AssetLegacy(ConstrainedStr, ABC):
    """Base class for all legacy assets"""


class AssetHiveLegacy(AssetLegacy):
    regex = re.compile(r"^[0-9]+\.[0-9]{3} (?:HIVE|TESTS)$")


class AssetHbdLegacy(AssetLegacy):
    regex = re.compile(r"^[0-9]+\.[0-9]{3} (?:HBD|TBD)$")


class AssetVestsLegacy(AssetLegacy):
    regex = re.compile(r"^[0-9]+\.[0-9]{6} VESTS$")


"""Assets to use just in situation when it doesn't matter that Assets must be in nai or legacy format"""
AssetHbd: TypeAlias = AssetHbdNai | AssetHbdLegacy
AssetHive: TypeAlias = AssetHiveNai | AssetHiveLegacy
AssetVests: TypeAlias = AssetVestsNai | AssetVestsLegacy


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


class HbdExchangeRate(PreconfiguredBaseModel):
    base: AssetHive | AssetHbd
    quote: AssetHive


class LegacyChainProperties(PreconfiguredBaseModel):
    account_creation_fee: AssetHive
    maximum_block_size: Uint32t = Uint32t(MAXIMUM_BLOCK_SIZE)
    hbd_interest_rate: Uint16t = Uint16t(HBD_INTEREST_RATE)
