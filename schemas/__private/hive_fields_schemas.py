"""
    It is module with hive fields to use in python code. It helps to create hive fields without remember about
    for example fill nai when creating AssetNai. In situation when you can't find here field that you need that's
    probably mean that there was not need for creating strict and non-strict version of field and you will find it
    in hive_fields_schemas_strict without 'strict' suffix
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from schemas.__private.hive_fields_schemas_strict import AssetNaiStrict, HiveDateTimeStrict, HiveInt


class HiveDateTime(HiveDateTimeStrict):
    @classmethod
    def validate(cls, value: Any) -> datetime:
        if type(value) is datetime:
            return value

        return super().validate(value)


class AssetNaiHive(AssetNaiStrict):
    precision: HiveInt = HiveInt(3)
    nai: str = "@@000000021"

    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000021"


class AssetNaiHbd(AssetNaiStrict):
    precision: HiveInt = HiveInt(3)
    nai: str = "@@000000013"

    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000013"


class AssetNaiVests(AssetNaiStrict):
    precision: HiveInt = HiveInt(3)
    nai: str = "@@000000037"

    @classmethod
    def get_nai_pattern(cls) -> str:
        return "@@000000037"
