from __future__ import annotations

from typing import Annotated, Final

import msgspec

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

ACCOUNT_NAME_SEGMENT_REGEX: Final[str] = r"[a-z]{1}[a-z0-9\-]+[a-z0-9]{1}"
BASE_58_REGEX: Final[str] = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
ACCOUNT_NAME_REGEX = "^" + ACCOUNT_NAME_SEGMENT_REGEX + r"(:?\.{1}" + ACCOUNT_NAME_SEGMENT_REGEX + ")*$"

AccountName = Annotated[
    str,
    msgspec.Meta(
        max_length=16,
        min_length=3,
        pattern=ACCOUNT_NAME_REGEX,
    ),
]

EmptyAccountName = Annotated[
    str,
    msgspec.Meta(
        max_length=16,
        pattern=f"{ACCOUNT_NAME_REGEX}|^()$",
    ),
]

CustomIdType = Annotated[str, msgspec.Meta(max_length=32)]

EmptyString = Annotated[str, msgspec.Meta(max_length=0, min_length=0)]

EmptyList = Annotated[list, msgspec.Meta(max_length=0)]

FloatAsString = Annotated[str, msgspec.Meta(pattern=r"^(?:(?:[1-9][0-9]*)|0)\.[0-9]+$")]

NodeType = Annotated[str, msgspec.Meta(pattern=r"^(mainnet|testnet|mirrornet)$")]

Permlink = Annotated[str, msgspec.Meta(max_length=256)]

PublicKey = Annotated[str, msgspec.Meta(pattern=rf"^(?:STM)[{BASE_58_REGEX}]{{7,51}}$")]

PrivateKey = Annotated[str, msgspec.Meta(pattern=rf"^[{BASE_58_REGEX}]{{51}}$")]

WitnessUrl = Annotated[str, msgspec.Meta(max_length=HIVE_MAX_WITNESS_URL_LENGTH)]

Url = Annotated[str, msgspec.Meta(max_length=HIVE_MAX_URL_LENGTH)]
