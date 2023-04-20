from __future__ import annotations

from datetime import datetime
from typing import Any

from schemas.__private.hive_fields_schemas_strict import HiveDateTimeStrict


class HiveDateTime(HiveDateTimeStrict):
    @classmethod
    def validate(cls, value: Any) -> datetime:
        if type(value) is datetime:
            return value

        return super().validate(value)
