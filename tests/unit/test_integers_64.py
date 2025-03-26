from __future__ import annotations

import msgspec
import pytest

from schemas.decoders import get_hf26_decoder
from schemas.encoders import get_hf26_encoder
from schemas.fields.integers import MAX_INT64_VALUE, MIN_INT64_VALUE, Int64t, Uint64t


@pytest.mark.parametrize(
    "value", [MAX_INT64_VALUE - 1, MAX_INT64_VALUE, MIN_INT64_VALUE + 1, MIN_INT64_VALUE, 0, 12, -12]
)
def test_int64t(value: int) -> None:
    # ARRANGE
    i64 = Int64t(value)

    # ACT & ASSERT
    encoded = get_hf26_encoder().encode(i64)
    get_hf26_decoder(Int64t).decode(encoded)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "value",
    [
        MAX_INT64_VALUE - 1,
        MAX_INT64_VALUE,
        0,
        12,
    ],
)
def test_uint64t(value: int) -> None:
    # ARRANGE
    u64 = Uint64t(value)

    # ACT & ASSERT
    encoded = get_hf26_encoder().encode(u64)
    get_hf26_decoder(Uint64t).decode(encoded)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "value",
    [
        MAX_INT64_VALUE + 1,
        MIN_INT64_VALUE - 1,
    ],
)
def test_fail_int64t(value: int) -> None:
    # ARRANGE, ACT & ASSERT
    with pytest.raises(msgspec.ValidationError):
        Int64t(value)


@pytest.mark.parametrize(
    "value",
    [
        MAX_INT64_VALUE + 1,
        -12,
    ],
)
def test_fail_uint64t(value: int) -> None:
    # ARRANGE, ACT & ASSERT
    with pytest.raises(msgspec.ValidationError):
        Uint64t(value)
