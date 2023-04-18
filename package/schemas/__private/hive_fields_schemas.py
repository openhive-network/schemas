from __future__ import annotations

import re
from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING, Any, TypeAlias

from pydantic import ConstrainedInt, ConstrainedStr, validator

from schemas.__private.defaults import HBD_INTEREST_RATE, MAXIMUM_BLOCK_SIZE
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from collections.abc import Iterator

"""
We don't need as much fields as it was in old schemas. Pydantic gives us some ready fields or let us to
create our own in much shorter and easier way than it was. That's the reason why it is one directory not 2 as it was.
"""


class HiveInt(int):
    @classmethod
    def __get_validators__(cls) -> Iterator[Any]:
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> Any:
        if type(v) is int:
            return v
        if type(v) is str:
            try:
                v = int(v)
            except ValueError as error:
                raise ValueError("The value is not int and not string that can be converted to int!") from error
            return v
        raise ValueError("The value is not string or int")


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
    """
    Date-time in HIVE must bee in ISO format '%Y-%m-%dT%H:%M:%S'.
    """

    @classmethod
    @validator("isoformat")
    def check_custom_format(cls, v: str) -> str:
        try:
            datetime.strptime(v, "%Y-%m-%dT%H:%M:%S")
        except ValueError as error:
            raise ValueError("date must be in format %Y-%m-%dT%H:%M:%S") from error
        return v


class Authority(PreconfiguredBaseModel):
    weight_threshold: HiveInt
    account_auths: list[tuple[AccountName, HiveInt]]
    key_auths: list[tuple[PublicKey, HiveInt]]


class BaseAsset(PreconfiguredBaseModel, ABC):
    """Base class for all asset fields"""

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


class AssetHive(BaseAsset):
    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000021"


class AssetHbd(BaseAsset):
    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000013"


class AssetVests(BaseAsset):
    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000037"


AssetAny: TypeAlias = AssetVests | AssetHbd | AssetHive


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


class LegacyAssetHive(ConstrainedStr):
    regex = re.compile(r"^[0-9]+\.[0-9]{3} (?:HIVE|TESTS)$")


class LegacyAssetHbd(ConstrainedStr):
    regex = re.compile(r"^[0-9]+\.[0-9]{3} (?:HBD|TBD)$")


class LegacyAssetVests(ConstrainedStr):
    regex = re.compile(r"^[0-9]+\.[0-9]{6} VESTS$")


class HbdExchangeRate(PreconfiguredBaseModel):
    base: LegacyAssetHbd | LegacyAssetHive | AssetHive | AssetHbd
    quote: LegacyAssetHive | AssetHive


class LegacyChainProperties(PreconfiguredBaseModel):
    account_creation_fee: AssetHive | LegacyAssetHive
    maximum_block_size: Uint32t = MAXIMUM_BLOCK_SIZE
    hbd_interest_rate: Uint16t = HBD_INTEREST_RATE


class CustomIdType(int):
    @classmethod
    def __get_validators__(cls) -> Iterator[Any]:
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> Any:
        max_id_length = 32
        if len(str(v)) > max_id_length:
            raise ValueError("Must be shorter than 32 !")
        return int(v)
