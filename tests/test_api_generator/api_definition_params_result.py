from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class TestCustomType: ...


@dataclass
class TestApiParams:
    some_custom_type: TestCustomType
    some_string: str = ""
    some_int: int = 0


TestApiResult = str


VALID_ENDPOINT_PARAMS: dict[str, Any] = {
    "return": str,
    "some_custom_type": TestCustomType,
    "some_string": str,
    "some_int": int,
}

VALID_ENDPOINT_PARAMS_LIST_RETURN: dict[str, Any] = {
    "return": list[str],
    "some_custom_type": TestCustomType,
    "some_string": str,
    "some_int": int,
}

GENERATOR_TEST_SINGLE_API = {
    "test_api": {
        "first_endpoint": {
            "params": TestApiParams,
            "result": TestApiResult,
        },
        "second_endpoint": {
            "params": TestApiParams,
            "result": TestApiResult,
        },
        "third_endpoint": {
            "params": TestApiParams,
            "result": TestApiResult,
            "description": "This is a test endpoint",
            "response_array": True,
        },
    }
}

GENERATOR_TEST_API_COLLECTION = {
    "first_test_api": {
        "first_endpoint": {
            "params": TestApiParams,
            "result": TestApiResult,
        },
        "second_endpoint": {
            "params": TestApiParams,
            "result": TestApiResult,
        },
    },
    "second_test_api": {
        "first_endpoint": {
            "params": TestApiParams,
            "result": TestApiResult,
        },
    },
}
