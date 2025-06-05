from __future__ import annotations

import msgspec
import pytest

from schemas.fields.hive_int import HiveInt


def test_hiveint_creation() -> None:
    h1 = HiveInt(10)
    assert h1 == 10  # noqa: PLR2004

    h2 = HiveInt("20")
    assert h2 == 20  # noqa: PLR2004

    h3 = HiveInt(h1)
    assert h3 == h1

    with pytest.raises(msgspec.ValidationError):
        HiveInt(True)


def test_hiveint_eq() -> None:
    h1 = HiveInt(10)
    h2 = HiveInt(10)
    assert h1 == h2
    assert h1 != HiveInt(20)
    assert h1 == 10  # noqa: PLR2004


def test_hiveint_comparison() -> None:
    h1 = HiveInt(10)
    h2 = HiveInt(20)
    assert h1 < h2
    assert h1 <= h2
    assert h2 > h1
    assert h2 >= h1
    assert not (h1 > h2)
    assert not (h1 >= h2)


def test_hiveint_invalid_value() -> None:
    with pytest.raises(msgspec.ValidationError):
        HiveInt(True)

    with pytest.raises(msgspec.ValidationError):
        HiveInt("invalid")


def test_hiveint_repr_str() -> None:
    h1 = HiveInt(10)
    assert str(h1) == "10"
    assert repr(h1) == "10"


def test_hiveint_int_conversion() -> None:
    h1 = HiveInt(10)
    assert int(h1) == 10  # noqa: PLR2004
