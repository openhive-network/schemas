from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TestCustomType: ...


@dataclass
class TestApiParams:
    some_custom_type: TestCustomType
    some_string: str = ""
    some_int: int = 0


TestApiResult = str


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
