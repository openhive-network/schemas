from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any

import msgspec
import pytest

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets._base import AssetNaiAmount
from schemas.fields.basic import (
    AccountName,
    CustomIdType,
    FloatAsString,
    NodeType,
    OptionallyEmptyAccountName,
    Permlink,
    PrivateKey,
    PublicKey,
    Url,
    WitnessUrl,
)
from schemas.fields.hex import Hex, Sha256, Signature, TransactionId
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.fields.integers import Int16t, Int64t, Uint8t, Uint16t, Uint32t, Uint64t
from schemas.fields.resolvables import JsonString


@pytest.mark.parametrize(
    ("type_in_class", "type_to_check", "value_in_class_init"),
    [
        (
            JsonString[Any],
            JsonString,
            {"type": "follow_operation", "value": {"follower": "alice", "following": "bob", "what": ["blog"]}},
        ),
        (Hex, Hex, "0987654321ABCDEF"),
        (Sha256, Sha256, "2A19DC59B319DDEDED68D5E07C765E940BA8229519E49E6575CDF3D512D26CC9"),
        (Signature, Signature, "A" * 130),
        (TransactionId, TransactionId, "B" * 40),
        (HiveInt, HiveInt, 12),
        (HiveDateTime, HiveDateTime, datetime.now()),
        (HiveInt, HiveInt, "12"),
        (AssetNaiAmount, AssetNaiAmount, 12),
        (AssetNaiAmount, AssetNaiAmount, "12"),
        (AccountName, AccountName, "alice"),
        (OptionallyEmptyAccountName, OptionallyEmptyAccountName, ""),
        (CustomIdType, CustomIdType, "a" * 31),
        (FloatAsString, FloatAsString, "12.34"),
        (NodeType, NodeType, "testnet"),
        (Permlink, Permlink, "test-permlink"),
        (PublicKey, PublicKey, "STM" + ("1" * 51)),
        (PrivateKey, PrivateKey, "2" * 51),
        (WitnessUrl, WitnessUrl, "http://witness.url"),
        (Url, Url, "http://normal.url"),
        (Uint8t, Uint8t, 255),
        (Int16t, Int16t, 32_767),
        (Uint16t, Uint16t, 65_535),
        (Uint32t, Uint32t, 4_294_967_295),
        (Int64t, Int64t, 9_223_372_036_854_775_807),
        (Uint64t, Uint64t, 18_446_744_073_709_551_615),
    ],
)
def test_swap_types(type_in_class: type[Any], type_to_check: type[Any], value_in_class_init: Any) -> None:
    # ARRAGNE
    if TYPE_CHECKING:

        class TestClass(PreconfiguredBaseModel):
            value: Any

        class TestClassWithDefault(PreconfiguredBaseModel):
            value: Any = value_in_class_init

    else:
        TestClass = msgspec.defstruct(  # noqa: N806
            "TestStruct", bases=(PreconfiguredBaseModel,), fields=[("value", type_in_class)]
        )

        TestClassWithDefault = msgspec.defstruct(  # noqa: N806
            "TestClassWithDefault",
            bases=(PreconfiguredBaseModel,),
            fields=[("value", type_in_class, msgspec.field(default_factory=lambda: value_in_class_init))],
        )

    # ACT
    instance = TestClass(value=value_in_class_init)
    instance_with_default = TestClassWithDefault()

    # ASSERT
    assert isinstance(instance.value, type_to_check)
    assert isinstance(instance_with_default.value, type_to_check)
