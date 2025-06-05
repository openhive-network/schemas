from __future__ import annotations

from typing import Annotated, Final

import msgspec
import pytest

# Define regex patterns and type
ACCOUNT_NAME_SEGMENT_REGEX: Final[str] = r"[a-z]{1}[a-z0-9\-]+[a-z0-9]{1}"
AccountName = Annotated[
    str,
    msgspec.Meta(
        max_length=16,
        min_length=3,
        pattern="^" + ACCOUNT_NAME_SEGMENT_REGEX + r"(:?\.{1}" + ACCOUNT_NAME_SEGMENT_REGEX + ")*$",
    ),
]


# Decoder class based on msgspec
class Account(msgspec.Struct):
    name: AccountName


@pytest.mark.parametrize(
    "valid_account_name",
    [
        "abc",
        "abc123",
        "a1-b2",
        "abc.def",
        "a-b-c",
        "abc.def12",
        "abc1-def2",
        "xyz.abc",
        "my-account",
        "z1-x9",
        "abc.def-ghi",
        "abc123.def456",
        "xyz-a",
        "test.test123",
        "a1b2c3",
        "good-name",
        "name.with-dots",
        "valid.name1",
        "short",
        "longname123",
        "alice",
        "bob",
    ],
)
def test_valid_account_names(valid_account_name: str) -> None:
    # ARRANGE
    data = {"name": valid_account_name}

    # ACT
    encoded = msgspec.json.encode(data)
    decoded = msgspec.json.decode(encoded, type=Account)

    # ASSERT
    assert decoded.name == valid_account_name


@pytest.mark.parametrize(
    "invalid_account_name",
    [
        "ab",  # Too short
        "a" * 17,  # Too long
        "a.b.c.d.e.f.g",  # Too short segments
        "abc.",  # Dot at the end
        ".abc",  # Dot at the beginning
        "abc..def",  # Double dots
        "123abc",  # Does not start with a letter
        "abc123!",  # Exclamation mark is not allowed
        "abc$",  # Dollar sign is not allowed
        "abc.def.",  # Dot at the end after a segment
        "a-1-",  # Dash at the end
        "-abc",  # Dash at the beginning
        "abc..",  # Double dots
        "ABC",  # Uppercase letters are not allowed
        "a.b.c.d.e",  # Too many segments
        "3ab",  # Starts with number
        "ab-",  # Dash at the end
        "abc.",  # Dot at the end
    ],
)
def test_invalid_account_names(invalid_account_name: str) -> None:
    # ARRANGE
    data = {"name": invalid_account_name}

    # ACT & ASSERT
    encoded = msgspec.json.encode(data)
    with pytest.raises(msgspec.ValidationError):
        msgspec.json.decode(encoded, type=Account)
