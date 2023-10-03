from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any

from pydantic import ConstrainedStr, PrivateAttr, errors

__all__ = [
    "AccountName",
    "CustomIdType",
    "EmptyString",
    "FloatAsString",
    "NodeType",
    "Permlink",
    "PublicKey",
]

from pydantic.validators import list_validator

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator


class AccountName(ConstrainedStr):
    __name_segment = PrivateAttr(r"[a-z][a-z0-9\-]+[a-z0-9]")
    regex = rf"^{__name_segment.default}(?:\.{__name_segment.default})*$"
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
    regex = re.compile(r"^(?:STM|TST)[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{7,51}$")
