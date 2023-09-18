from __future__ import annotations

import pytest
from pydantic import ValidationError

from schemas.apis.network_broadcast_api.response_schemas import BroadcastTransaction


def test_correct_values_broadcast_transaction() -> None:
    # ACT
    test_instance = BroadcastTransaction()

    # ASSERT
    assert bool(test_instance.dict()) is False


@pytest.mark.parametrize("parameter", ({"a": "b"}, {"a": 1, "b": 2, "c": 3}))
def test_incorrect_values_broadcast_transaction(parameter: dict[str, int | str]) -> None:
    # ACT & ASSERT
    with pytest.raises(ValidationError):
        BroadcastTransaction(**parameter)
