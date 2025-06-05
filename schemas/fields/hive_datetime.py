from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from schemas.fields.resolvables import Resolvable
from schemas.hive_constants import HIVE_TIME_FORMAT

__all__ = [
    "HiveDateTime",
]


class HiveDateTime(datetime, Resolvable["HiveDateTime", str | datetime]):
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

    def serialize(self) -> Any:
        return self.strftime(HIVE_TIME_FORMAT)

    @classmethod
    def __convert_to_datetime(cls, value: str | datetime) -> datetime:
        if isinstance(value, datetime):
            return cls.__normalize(value)
        if isinstance(value, str):
            try:
                return cls.__normalize(datetime.strptime(value, HIVE_TIME_FORMAT))
            except ValueError as error:
                raise ValueError(f"Date must be in format {HIVE_TIME_FORMAT}") from error
        raise TypeError("Value must be a datetime or a string in the correct format.")

    @staticmethod
    def resolve(incoming_cls: type, value: str | datetime) -> HiveDateTime:  # noqa: ARG004
        return HiveDateTime(value=value)

    @classmethod
    def __normalize(cls, value: datetime) -> datetime:
        return value.replace(tzinfo=timezone.utc)

    @staticmethod
    def now() -> HiveDateTime:  # type: ignore[override]
        return HiveDateTime(value=datetime.now())

    def __copy__(self) -> HiveDateTime:
        return HiveDateTime.resolve(HiveDateTime, self.serialize())

    def __deepcopy__(self, memo: Any) -> HiveDateTime:
        return self.__copy__()
