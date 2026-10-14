from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

from schemas.errors import FieldValidationError
from schemas.fields.serializable import Serializable
from schemas.hive_constants import HIVE_TIME_FORMAT

__all__ = [
    "HiveDateTime",
]


class HiveDateTime(datetime, Serializable):
    def __new__(cls, value: str | datetime | HiveDateTime, *args: Any) -> HiveDateTime:
        # source: https://stackoverflow.com/a/45981230
        if len(args) > 0:
            value = datetime(value, *args)  # type: ignore[arg-type]
        date = cls.__convert_to_datetime(value)
        return super().__new__(
            cls,
            date.year,
            date.month,
            date.day,
            date.hour,
            date.minute,
            date.second,
            date.microsecond,
            date.tzinfo,
            fold=date.fold,
        )

    def __copy__(self) -> HiveDateTime:
        return HiveDateTime(self.serialize())

    def __deepcopy__(self, memo: Any) -> HiveDateTime:
        return self.__copy__()

    @classmethod
    def __convert_to_datetime(cls, value: str | datetime) -> datetime:
        if isinstance(value, datetime):
            return cls.__normalize(value)
        if isinstance(value, str):
            try:
                return cls.__normalize(datetime.strptime(value, HIVE_TIME_FORMAT))
            except ValueError as error:
                raise FieldValidationError(f"Date must be in format {HIVE_TIME_FORMAT}") from error
        raise FieldValidationError("Value must be a datetime or a string in the correct format.")

    @classmethod
    def __normalize(cls, value: datetime) -> datetime:
        return value.replace(tzinfo=UTC)

    @staticmethod
    def now() -> HiveDateTime:  # type: ignore[override]
        return HiveDateTime(value=datetime.now())

    def serialize(self) -> str:
        return self.strftime(HIVE_TIME_FORMAT)
