from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import pytest

from schemas.apis.block_api.response_schemas import GetBlock
from schemas.jsonrpc import CACHED_MODELS, get_response_model

if TYPE_CHECKING:
    from collections.abc import Iterator


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
    model_1 = get_response_model(schema, json.dumps(get_block))
    assert len(CACHED_MODELS) == 1, "Invalid CACHED_MODELS, should have one GetBlock model"
    model_2 = get_response_model(schema, json.dumps(get_block))
    assert len(CACHED_MODELS) == 1, "Invalid CACHED_MODELS, should have one GetBlock model"
    assert model_1 == model_2, "Models have differnces. Every getted model of same schama should be identical."
