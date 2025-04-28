from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TestCustomType:
    ...


@dataclass
class TestApiParams:
    test: TestCustomType
    test_1: str = ""
    test_2: int = 0


TestApiResult = str


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
