from __future__ import annotations

import json


def normalize_json(json_string: str) -> str:
    return json.dumps(json.loads(json_string), sort_keys=True)


def assert_json_equals(actual: str, expected: str) -> None:
    actual_normalized = normalize_json(actual)
    expected_normalized = normalize_json(expected)
    assert (
        actual_normalized == expected_normalized
    ), f"actual doesnt match expected\n{actual_normalized=}\n{expected_normalized=}"


def assert_json_contains(json_substring: str, json_string: str) -> None:
    json_substring_normalized = normalize_json(json_substring)
    json_string_normalized = normalize_json(json_string)
    assert (
        json_substring_normalized in json_string_normalized
    ), f"{json_substring_normalized=}\nis not substring of\n{json_string_normalized=}"
