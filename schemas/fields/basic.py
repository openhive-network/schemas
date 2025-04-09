from __future__ import annotations

from abc import ABC, abstractmethod
from re import split
from typing import Annotated, ClassVar, Final

import msgspec
from typing_extensions import Self

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

class ValidatorString(str, ABC):
    _registered_types: ClassVar[dict[str, type[ValidatorString]]] = {}

    def __new__(cls, obj: object, *, skip_validation: bool = False) -> ValidatorString:
        if not skip_validation:
            cls.validate(str(obj))
        return super().__new__(
            cls,
            obj
        )

    @classmethod
    def validate(cls, value: str) -> Self:
        return ValidatorString(msgspec.convert(value, type=Annotated[str, cls._meta()]), skip_validation=True)

    @classmethod
    @abstractmethod
    def _meta(cls) -> msgspec.Meta: ...

    @classmethod
    def factory(cls, name: str, meta: msgspec.Meta) -> type[ValidatorString]:
        if name in cls._registered_types:
            return cls._registered_types[name]

        class ValidatorStringMeta(ValidatorString):
            @classmethod
            def _meta(cls) -> msgspec.Meta:
                return meta

        new_type = msgspec.defstruct(name=name, bases=(ValidatorStringMeta,))
        cls._registered_types[name] = new_type
        return new_type

    @classmethod
    def find_type_by_annotation_str(cls, typename: str) -> type[ValidatorString] | None:
        return cls._registered_types.get(typename)


AccountName = ValidatorString.factory(
    "AccountName",
    msgspec.Meta(
        max_length=16,
        min_length=3,
        pattern=ACCOUNT_NAME_REGEX,
    )
)

OptionallyEmptyAccountName = ValidatorString.factory(
    "OptionallyEmptyAccountName",
    msgspec.Meta(
        max_length=16,
        pattern=f"{ACCOUNT_NAME_REGEX}|^()$",
    )
)

EmptyList = Annotated[list[int], msgspec.Meta(max_length=0)]
EmptyString = Annotated[str, msgspec.Meta(max_length=0, min_length=0)]

CustomIdType = ValidatorString.factory("CustomIdType", msgspec.Meta(max_length=32))

FloatAsString = ValidatorString.factory("FloatAsString", msgspec.Meta(pattern=r"^(?:(?:[1-9][0-9]*)|0)\.[0-9]+$"))

NodeType = ValidatorString.factory("NodeType", msgspec.Meta(pattern=r"^(mainnet|testnet|mirrornet)$"))

Permlink = ValidatorString.factory("Permlink", msgspec.Meta(max_length=256))

PublicKey = ValidatorString.factory("PublicKey", msgspec.Meta(pattern=rf"^(?:STM)[{BASE_58_REGEX}]{{7,51}}$"))

PrivateKey = ValidatorString.factory("PrivateKey", msgspec.Meta(pattern=rf"^[{BASE_58_REGEX}]{{51}}$"))

WitnessUrl = ValidatorString.factory("WitnessUrl", msgspec.Meta(max_length=HIVE_MAX_WITNESS_URL_LENGTH))

Url = ValidatorString.factory("Url", msgspec.Meta(max_length=HIVE_MAX_URL_LENGTH))
