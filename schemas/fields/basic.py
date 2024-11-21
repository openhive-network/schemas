from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any, Final

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
    "WitnessUrl",
    "Url",
]

from pydantic.validators import list_validator

from schemas.hive_constants import HIVE_MAX_URL_LENGTH, HIVE_MAX_WITNESS_URL_LENGTH

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator

ACCOUNT_NAME_SEGMENT_REGEX: Final[str] = r"[a-z][a-z0-9\-]+[a-z0-9]"
BASE_58_REGEX: Final[str] = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


class AccountName(ConstrainedStr):
    regex = rf"^{ACCOUNT_NAME_SEGMENT_REGEX}(?:\.{ACCOUNT_NAME_SEGMENT_REGEX})*$"
    min_length = 3
    max_length = 16


class CustomIdType(ConstrainedStr):
    max_length = 32


class EmptyString(ConstrainedStr):
    min_length = 0
    max_length = 0


class EmptyList(list):  # type: ignore[type-arg] # See pydantic.ConstrainedList
    @classmethod
    # TODO[pydantic]: We couldn't refactor `__get_validators__`, please create the `__get_pydantic_core_schema__` manually.
    # Check https://docs.pydantic.dev/latest/migration/#defining-custom-types for more information.
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
    regex = rf"^(?:STM)[{BASE_58_REGEX}]{{7,51}}$"


class PrivateKey(ConstrainedStr):
    regex = re.compile(rf"^[{BASE_58_REGEX}]{{51}}$")


class WitnessUrl(ConstrainedStr):
    max_length = HIVE_MAX_WITNESS_URL_LENGTH


class Url(ConstrainedStr):
    max_length = HIVE_MAX_URL_LENGTH
