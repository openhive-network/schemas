from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import msgspec
import pytest

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import AccountName, PublicKey
from schemas.fields.hex import BlockId, Signature, TransactionId
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.jsonrpc import CACHED_MODELS, JSONRPCError, JSONRPCResult, get_response_model

if TYPE_CHECKING:
    from collections.abc import Iterator


class Block(PreconfiguredBaseModel):
    previous: BlockId
    timestamp: HiveDateTime
    witness: AccountName
    transaction_merkle_root: str
    extensions: list[Any]
    witness_signature: Signature
    transactions: list[Any]
    block_id: BlockId
    signing_key: PublicKey
    transaction_ids: list[TransactionId]


class GetBlock(PreconfiguredBaseModel):
    block: Block


class FakePublicModel:
    """Mimics a generated public model - provides `from_builtins` and is not a msgspec struct."""

    def __init__(self, data: dict[str, Any]) -> None:
        self.data = data

    @classmethod
    def from_builtins(cls, data: dict[str, Any]) -> FakePublicModel:
        return cls(data)


@pytest.fixture(autouse=True)
def _temporarly_clear_cached_models() -> Iterator[None]:
    backup = CACHED_MODELS.copy()
    CACHED_MODELS.clear()
    yield
    CACHED_MODELS.clear()
    CACHED_MODELS.update(backup)


def test_get_response_model() -> None:
    schema: Any = GetBlock
    get_block: dict[str, Any] = {
        "id": 1,
        "jsonrpc": "2.0",
        "result": {
            "block": {
                "previous": "0000000000000000000000000000000000000000",
                "timestamp": "2016-03-24T16:05:00",
                "witness": "initminer",
                "transaction_merkle_root": "0000000000000000000000000000000000000000",
                "extensions": [],
                "witness_signature": "204f8ad56a8f5cf722a02b035a61b500aa59b9519b2c33c77a80c0a714680a5a5a7a340d909d19996613c5e4ae92146b9add8a7a663eef37d837ef881477313043",
                "transactions": [],
                "block_id": "0000000109833ce528d5bbfb3f6225b39ee10086",
                "signing_key": "STM8GC13uCZbP44HzMLV6zPZGwVQ8Nt4Kji8PapsPiNq1BK153XTX",
                "transaction_ids": [],
            }
        },
    }
    assert len(CACHED_MODELS) == 0, "Invalid CACHED_MODELS, should be empty"
    model_1 = get_response_model(schema, json.dumps(get_block), "hf26")
    assert len(CACHED_MODELS) == 1, "Invalid CACHED_MODELS, should have one GetBlock model"
    model_2 = get_response_model(schema, json.dumps(get_block), "hf26")
    assert len(CACHED_MODELS) == 1, "Invalid CACHED_MODELS, should have one GetBlock model"
    assert model_1 == model_2, "Models have differnces. Every getted model of same schama should be identical."


def test_get_response_model_does_not_validate_models_with_from_builtins() -> None:
    # ARRANGE
    response = {"id": 3, "jsonrpc": "2.0", "result": [{"name": 123, "unexpected": True}, {}]}

    # ACT
    model = get_response_model(list[FakePublicModel], json.dumps(response), "hf26")  # type: ignore[type-var]

    # ASSERT
    assert isinstance(model, JSONRPCResult)
    assert model.id_ == 3  # noqa: PLR2004
    assert [item.data for item in model.result] == response["result"]
    assert len(CACHED_MODELS) == 0, "Validation-free path should not create msgspec models"


def test_get_response_model_does_not_validate_builtins() -> None:
    # ARRANGE
    response = {"id": 1, "jsonrpc": "2.0", "result": ["text", 5, None]}

    # ACT
    model = get_response_model(list[str], json.dumps(response), "hf26")

    # ASSERT
    assert isinstance(model, JSONRPCResult)
    assert model.result == ["text", 5, None]


@pytest.mark.parametrize(
    ("expected_type", "result", "expected_result"),
    [
        (HiveInt, "12", HiveInt(12)),
        (list[HiveInt], ["1", 2], [HiveInt(1), HiveInt(2)]),
        (HiveDateTime, "2016-03-24T16:05:00", HiveDateTime("2016-03-24T16:05:00")),
        (AccountName | None, "initminer", AccountName("initminer")),
    ],
)
def test_get_response_model_decodes_field_types(expected_type: Any, result: Any, expected_result: Any) -> None:
    # ARRANGE
    response = {"id": 1, "jsonrpc": "2.0", "result": result}

    # ACT
    model = get_response_model(expected_type, json.dumps(response), "hf26")

    # ASSERT
    assert isinstance(model, JSONRPCResult)
    assert model.result == expected_result
    assert type(model.result) is type(expected_result)


@pytest.mark.parametrize("expected_type", [AccountName, list[AccountName]])
def test_get_response_model_validates_field_types(expected_type: Any) -> None:
    # ARRANGE
    response = {"id": 1, "jsonrpc": "2.0", "result": "x" if expected_type is AccountName else ["x"]}

    # ACT & ASSERT
    with pytest.raises(msgspec.ValidationError):
        get_response_model(expected_type, json.dumps(response), "hf26")


def test_get_response_model_returns_error_without_validation() -> None:
    # ARRANGE
    response = {"id": 1, "jsonrpc": "2.0", "error": {"code": -32000, "message": "boom"}}

    # ACT
    model = get_response_model(list[FakePublicModel], json.dumps(response), "hf26")  # type: ignore[type-var]

    # ASSERT
    assert isinstance(model, JSONRPCError)
    assert model.error["message"] == "boom"
