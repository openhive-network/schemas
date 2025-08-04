from __future__ import annotations

from typing import Annotated, Final

import msgspec

from schemas.fields._init_validators import ValidatorString
from schemas.hive_constants import HIVE_MAX_URL_LENGTH, HIVE_MAX_WITNESS_URL_LENGTH

__all__ = [
    "AccountName",
    "CustomIdType",
    "EmptyString",
    "FloatAsString",
    "NodeType",
    "Permlink",
    "PrivateKey",
    "PublicKey",
    "Url",
    "WitnessUrl",
]


ACCOUNT_NAME_SEGMENT_REGEX: Final[str] = r"[a-z]{1}[a-z0-9\-]+[a-z0-9]{1}"
BASE_58_REGEX: Final[str] = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
ACCOUNT_NAME_REGEX = "^" + ACCOUNT_NAME_SEGMENT_REGEX + r"(:?\.{1}" + ACCOUNT_NAME_SEGMENT_REGEX + ")*$"


EmptyList = Annotated[list[int], msgspec.Meta(max_length=0)]
EmptyString = Annotated[str, msgspec.Meta(max_length=0, min_length=0)]

AccountName = ValidatorString.factory(
    "AccountName",
    msgspec.Meta(
        max_length=16,
        min_length=3,
        pattern=ACCOUNT_NAME_REGEX,
    ),
)

OptionallyEmptyAccountName = ValidatorString.factory(
    "OptionallyEmptyAccountName",
    msgspec.Meta(
        max_length=16,
        pattern=f"{ACCOUNT_NAME_REGEX}|^()$",
    ),
)
CustomIdType = ValidatorString.factory("CustomIdType", msgspec.Meta(max_length=32))
FloatAsString = ValidatorString.factory("FloatAsString", msgspec.Meta(pattern=r"^(?:(?:[1-9][0-9]*)|0)\.[0-9]+$"))
NodeType = ValidatorString.factory("NodeType", msgspec.Meta(pattern=r"^(mainnet|testnet|mirrornet)$"))
Permlink = ValidatorString.factory("Permlink", msgspec.Meta(max_length=256))
PublicKey = ValidatorString.factory("PublicKey", msgspec.Meta(pattern=rf"^(?:STM)[{BASE_58_REGEX}]{{7,51}}$"))
PrivateKey = ValidatorString.factory("PrivateKey", msgspec.Meta(pattern=rf"^[{BASE_58_REGEX}]{{51}}$"))
WitnessUrl = ValidatorString.factory("WitnessUrl", msgspec.Meta(max_length=HIVE_MAX_WITNESS_URL_LENGTH))
Url = ValidatorString.factory("Url", msgspec.Meta(max_length=HIVE_MAX_URL_LENGTH))
