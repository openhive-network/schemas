from __future__ import annotations
import re

from pydantic import BaseModel, validator, ConstrainedStr, ConstrainedInt
from datetime import datetime
"""
We don't need as much fields as it was in old schemas. Pydantic gives us some ready fields or let us to 
create our own in much shorter and easier way than it was. That's the reason why it is one directory not 2 as it was.
"""
HIVE_100_PERCENT = 10000
HIVE_1_PERCENT = HIVE_100_PERCENT/100
HIVE_MAX_TRANSACTION_SIZE = 1024*64
HIVE_MIN_BLOCK_SIZE_LIMIT = HIVE_MAX_TRANSACTION_SIZE


class HiveInt(ConstrainedInt):
    """
    HiveInt can come into the str format. This custom type check and convert it to integer type as it should be.
    """
    ge = 0

    @classmethod
    @validator('hiveformat')
    def check_int_hive_format(cls, v):
        try:
            hive_int = int(v)
        except ValueError:
            raise ValueError('That is not int, and cant convert it to int')
        return hive_int


class EmptyString(ConstrainedStr):
    min_length = 0
    max_length = 0


class AccountName(ConstrainedStr):
    regex = re.compile(r'[a-z][a-z0-9\-]+[a-z0-9]')
    min_length = 3
    max_length = 16


class PublicKey(ConstrainedStr):
    regex = re.compile(r'^(?:STM|TST)[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{7,51}$')


class HiveDateTime(datetime):
    """
    Date and time in HIVE must bee in ISO format '%Y-%m-%dT%H:%M:%S'.
    """
    @classmethod
    @validator('isoformat')
    def check_custom_format(cls, v):
        try:
            datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            raise ValueError('date must be in format %Y-%m-%dT%H:%M:%S')
        return v


class Authority(BaseModel):
    weight_threshold: HiveInt
    account_auths: list[tuple[AccountName, HiveInt]]
    key_auths: list[tuple[PublicKey, HiveInt]]


class AssetHive(BaseModel):
    amount: HiveInt
    precision: HiveInt
    nai: str

    @classmethod
    @validator('nai')
    def check_nai(cls, nai):
        if nai != "@@000000021":
            raise ValueError("Invalid nai!")
        return nai


class AssetHbd(BaseModel):
    amount: HiveInt
    precision: HiveInt
    nai: str

    @classmethod
    @validator('nai')
    def check_nai(cls, nai):
        if nai != "@@000000013":
            raise ValueError("Invalid nai!")
        return nai


class AssetVests(BaseModel):
    amount: HiveInt
    precision: HiveInt
    nai: str

    @classmethod
    @validator('nai')
    def check_nai(cls, nai):
        if nai != "@@000000037":
            raise ValueError("Invalid nai!")
        return nai


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
    regex = re.compile(r'^[0-9]+\.[0-9]{3} (?:HIVE|TESTS)$')


class LegacyAssetHbd(ConstrainedStr):
    regex = re.compile(r'^[0-9]+\.[0-9]{3} (?:HBD|TBD)$')


class LegacyAssetVests(ConstrainedStr):
    regex = re.compile(r'^[0-9]+\.[0-9]{6} VESTS$')


class HbdExchangeRateLegacyTrue(BaseModel):
    base: LegacyAssetHbd | LegacyAssetHive
    quote: LegacyAssetHive


class HbdExchangeRateLegacyFalse(BaseModel):
    base: AssetHbd | AssetHive
    quote: AssetHive


class LegacyChainProperties(BaseModel):
    account_creation_fee: AssetHive | LegacyAssetHive
    maximum_block_size: Uint32t = HIVE_MIN_BLOCK_SIZE_LIMIT * 2
    hbd_interest_rate: Uint16t = 10*HIVE_1_PERCENT


class CustomIdType(ConstrainedInt):
    @classmethod
    @validator('length_checker')
    def check_length(cls, v):
        if len(str(v)) > 32:
            raise ValueError('Much be shorter than 32 !')
        else:
            return v