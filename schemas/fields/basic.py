from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any

from pydantic import ConstrainedStr, errors

__all__ = [
    "AccountName",
    "CustomIdType",
    "EmptyString",
    "FloatAsString",
    "NodeType",
    "Permlink",
    "PublicKey",
    "PrivateKey",
]

from pydantic.validators import list_validator

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator

account_name_name_segment_regex = r"[a-z][a-z0-9\-]+[a-z0-9]"
base_58_regex = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


class AccountName(ConstrainedStr):
    regex = rf"^{account_name_name_segment_regex}(?:\.{account_name_name_segment_regex})*$"
    min_length = 3
    max_length = 16


class CustomIdType(ConstrainedStr):
    max_length = 32


class EmptyString(ConstrainedStr):
    min_length = 0
    max_length = 0


class EmptyList(list):  # type: ignore[type-arg] # See pydantic.ConstrainedList
    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.list_length_validator

    @classmethod
    def list_length_validator(cls, v: Any) -> list[Any]:
        v = list_validator(v)
        if len(v) > 0:
            raise errors.ListMaxLengthError(limit_value=0)
        return []


class FloatAsString(ConstrainedStr):
    regex = re.compile(r"^(?:(?:[1-9][0-9]*)|0)\.[0-9]+$")


class NodeType(ConstrainedStr):
    regex = re.compile(r"^(mainnet|testnet|mirrornet)$")


class Permlink(ConstrainedStr):
    max_length = 256


class PublicKey(ConstrainedStr):
    regex = re.compile(r"^(?:STM|TST)[" + base_58_regex + r"]{7,51}$")


class PrivateKey(ConstrainedStr):
    regex = re.compile(r"^[" + base_58_regex + r"]{51}$")
