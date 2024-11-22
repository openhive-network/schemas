from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from pydantic import GetCoreSchemaHandler, ValidationError
from pydantic_core.core_schema import CoreSchema, ValidationFunction
from schemas.hive_constants import HIVE_TIME_FORMAT

__all__ = [
    "HiveDateTime",
]


class HiveDateTime(datetime):
    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type: Any, handler: GetCoreSchemaHandler) -> CoreSchema:
        """
        Define the schema for this custom type.
        """
        return CoreSchema(
            source_type=cls,
            validation=ValidationFunction(cls.validate),
            metadata={"description": "HiveDateTime type for custom datetime handling"}
        )

    @classmethod
    def validate(cls, value: Any) -> HiveDateTime:
        """
        Validation logic for HiveDateTime.
        """
        if isinstance(value, datetime):
            return cls.__normalize(value)

        if isinstance(value, str):
            try:
                parsed_date = datetime.strptime(value, HIVE_TIME_FORMAT)
                return cls.__normalize(parsed_date)
            except ValueError as error:
                raise ValidationError(f"date must be in format {HIVE_TIME_FORMAT}") from error

        raise ValidationError(f"Invalid type for HiveDateTime: {type(value)}")

    @classmethod
    def __normalize(cls, value: datetime) -> HiveDateTime:
        """
        Normalize datetime to use UTC timezone.
        """
        return cls(value.replace(tzinfo=timezone.utc))

    @classmethod
    def now(cls) -> HiveDateTime:
        """
        Override `now` to return a UTC-aware datetime instance.
        """
        return cls.utcnow()
