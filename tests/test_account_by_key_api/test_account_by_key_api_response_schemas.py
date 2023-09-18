from __future__ import annotations

from typing import Any

import pytest

from schemas.__private.hive_factory import HiveResult
from schemas.apis.account_by_key_api.response_schemas import GetKeyReferences

from .response_from_api import GET_KEY_REFERENCES


@pytest.mark.parametrize("schema, parameters", [(GetKeyReferences, GET_KEY_REFERENCES)])
def test_response_schema_correct_value(schema: Any, parameters: dict[str, Any]) -> None:
    # ACT & ASSERT
    HiveResult.factory(schema, **parameters)
