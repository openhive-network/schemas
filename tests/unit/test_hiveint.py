# ruff: noqa: PLR2004

from __future__ import annotations

from decimal import Decimal

import pytest

from schemas.fields.hive_int import HiveInt


def test_hiveint_creation() -> None:
    h1 = HiveInt(10)
    assert h1.value == 10

    h2 = HiveInt("20")
    assert h2.value == 20

    h3 = HiveInt(h1)
    assert h3.value == h1.value

    with pytest.raises(ValueError):
        HiveInt(True)


def test_hiveint_eq() -> None:
    h1 = HiveInt(10)
    h2 = HiveInt(10)
    assert h1 == h2
    assert h1 != HiveInt(20)
    assert h1 == 10
    assert h1 == "10"


def test_hiveint_comparison() -> None:
    h1 = HiveInt(10)
    h2 = HiveInt(20)
    assert h1 < h2
    assert h1 <= h2
    assert h2 > h1
    assert h2 >= h1
    assert not (h1 > h2)
    assert not (h1 >= h2)


def test_hiveint_safe_int_value() -> None:
    h1 = HiveInt(2**53)
    assert h1.safe_int_value == str(2**53)

    h2 = HiveInt(10)
    assert h2.safe_int_value == 10


def test_hiveint_arithmetic_operations() -> None:
    h1 = HiveInt(10)
    assert (h1 * 2).value == 20  # type: ignore[attr-defined]
    assert (2 * h1).value == 20  # type: ignore[attr-defined]

    assert (h1 / 2).value == 5  # type: ignore[attr-defined]
    with pytest.raises(ZeroDivisionError):
        h1 / 0

    assert (h1**2).value == 100  # type: ignore[union-attr]
    assert (h1 ** HiveInt(2)) == 100
    assert (h1 ** Decimal(2)) == Decimal(100)

    with pytest.raises(TypeError):
        h1 ** "str"


def test_hiveint_invalid_value() -> None:
    with pytest.raises(ValueError):
        HiveInt(True)

    with pytest.raises(ValueError):
        HiveInt("invalid")


def test_hiveint_repr_str() -> None:
    h1 = HiveInt(10)
    assert str(h1) == "10"
    assert repr(h1) == "10"


def test_hiveint_int_conversion() -> None:
    h1 = HiveInt(10)
    assert int(h1) == 10
