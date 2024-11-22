from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Type

from pydantic_core.core_schema import CoreSchema, ValidatorFunctionWrapHandler
from pydantic import GetCoreSchemaHandler
from typing_extensions import Self

from schemas.hive_constants import HIVE_TIME_FORMAT


__all__ = [
    "HiveDateTime",
]


class HiveDateTime(datetime):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Type[Any], handler: GetCoreSchemaHandler
    ) -> CoreSchema:

        def validate(value: Any, handler: ValidatorFunctionWrapHandler) -> datetime:
            if isinstance(value, datetime):
                return cls.__normalize(value)

            try:
                return cls.__normalize(datetime.strptime(value, HIVE_TIME_FORMAT))
            except ValueError as error:
                raise ValueError(f"date must be in format {HIVE_TIME_FORMAT}") from error

        return {
            'type': 'function-wrap',
            'function': validate,
            'schema': handler(object),
        }

    @classmethod
    def __normalize(cls, value: datetime) -> datetime:
        return value.replace(tzinfo=timezone.utc)

    @classmethod
    def now(cls) -> Self:  # type: ignore[override]
        return cls.utcnow()
