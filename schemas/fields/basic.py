from __future__ import annotations

import re
from typing import Any, Final

from pydantic import StringConstraints
from pydantic_core import core_schema, PydanticCustomError

__all__ = [
    "AccountName",
    "CustomIdType",
    "EmptyString",
    "FloatAsString",
    "NodeType",
    "Permlink",
    "PublicKey",
    "PrivateKey",
    "WitnessUrl",
    "Url",
]


from schemas.hive_constants import HIVE_MAX_URL_LENGTH, HIVE_MAX_WITNESS_URL_LENGTH


ACCOUNT_NAME_SEGMENT_REGEX: Final[str] = r"[a-z][a-z0-9\-]+[a-z0-9]"
BASE_58_REGEX: Final[str] = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


class ListMaxLengthError(PydanticCustomError):
    def __init__(self, limit_value: int):
        super().__init__("list_max_length", f"List length must not exceed {limit_value}.")

class AccountName(StringConstraints):
    regex = rf"^{ACCOUNT_NAME_SEGMENT_REGEX}(?:\.{ACCOUNT_NAME_SEGMENT_REGEX})*$"
    min_length = 3
    max_length = 16


class CustomIdType(StringConstraints):
    max_length = 32


class EmptyString(StringConstraints):
    min_length = 0
    max_length = 0


class EmptyList(list):  # type: ignore[type-arg]
    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type: Any, _model: Any) -> core_schema.CoreSchema:
        """
        Tworzy schemat walidacji dla `EmptyList`.
        """
        return core_schema.no_info_plain_validator_function(cls.list_length_validator)

    @classmethod
    def list_length_validator(cls, v: Any) -> 'EmptyList':
        """
        Waliduje, że wejściowa wartość jest listą o maksymalnej długości 0.
        """
        if not isinstance(v, list):
            raise TypeError("Value must be a list.")
        if len(v) > 0:
            raise ListMaxLengthError(limit_value=0)
        return cls([])


class FloatAsString(StringConstraints):
    regex = re.compile(r"^(?:(?:[1-9][0-9]*)|0)\.[0-9]+$")


class NodeType(StringConstraints):
    regex = re.compile(r"^(mainnet|testnet|mirrornet)$")


class Permlink(StringConstraints):
    max_length = 256


class PublicKey(StringConstraints):
    regex = rf"^(?:STM)[{BASE_58_REGEX}]{{7,51}}$"


class PrivateKey(StringConstraints):
    regex = re.compile(rf"^[{BASE_58_REGEX}]{{51}}$")


class WitnessUrl(StringConstraints):
    max_length = HIVE_MAX_WITNESS_URL_LENGTH


class Url(StringConstraints):
    max_length = HIVE_MAX_URL_LENGTH
