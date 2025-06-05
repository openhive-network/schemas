from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

import msgspec

from schemas.fields._init_validators import ValidatorInt

__all__ = [
    "Uint8t",
    "Int16t",
    "Uint16t",
    "Uint32t",
    "Int64t",
    "Uint64t",
]

MAX_INT64_VALUE: Final[int] = 9223372036854775807
MIN_INT64_VALUE: Final[int] = -9223372036854775808
MAX_UINT64_VALUE: Final[int] = 18446744073709551615
MIN_UINT64_VALUE: Final[int] = 0


def pre_int_validation(value: Any) -> ValidatorInt:
    return ValidatorInt(value, skip_validation=True)


def validate_int64t(value: ValidatorInt) -> ValidatorInt:
    if value < MIN_INT64_VALUE or value > MAX_INT64_VALUE:
        raise msgspec.ValidationError(f"Int64 out of range: `{value}` not in <{MIN_INT64_VALUE} ; {MAX_INT64_VALUE}>")
    return value


def validate_uint64t(value: ValidatorInt) -> ValidatorInt:
    if value < MIN_UINT64_VALUE or value > MAX_UINT64_VALUE:
        raise msgspec.ValidationError(
            f"Uint64 out of range: `{value}` not in <{MIN_UINT64_VALUE} ; {MAX_UINT64_VALUE}>"
        )
    return value


if TYPE_CHECKING:
    Uint8t = int
    Int16t = int
    Uint16t = int
    Uint32t = int
    Int64t = int
    Uint64t = int
else:
    Uint8t = ValidatorInt.factory("Uint8t", msgspec.Meta(ge=0, le=255))
    Int16t = ValidatorInt.factory("Int16t", msgspec.Meta(ge=-32768, le=32767))
    Uint16t = ValidatorInt.factory("Uint16t", msgspec.Meta(ge=0, le=65535))
    Uint32t = ValidatorInt.factory("Uint32t", msgspec.Meta(ge=0, le=4294967295))
    Int64t = ValidatorInt.factory(
        "Int64t",
        msgspec.Meta(),
        pre_validator=pre_int_validation,
        post_validator=validate_int64t,
        skip_default_validation=True,
    )
    Uint64t = ValidatorInt.factory(
        "Uint64t",
        msgspec.Meta(),
        pre_validator=pre_int_validation,
        post_validator=validate_uint64t,
        skip_default_validation=True,
    )


ShareType = Int64t
UShareType = Uint64t
