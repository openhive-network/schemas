from __future__ import annotations

import re
from typing import TYPE_CHECKING, Annotated, Any, Final

from pydantic import Field, StringConstraints

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


class AccountName(StringConstraints):
    regex = rf"^{ACCOUNT_NAME_SEGMENT_REGEX}(?:\.{ACCOUNT_NAME_SEGMENT_REGEX})*$"
    min_length = 3
    max_length = 16


class CustomIdType(StringConstraints):
    max_length = 32


class EmptyString(StringConstraints):
    min_length = 0
    max_length = 0

EmptyList = Annotated[list[Any], Field(max_length=0)]

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
