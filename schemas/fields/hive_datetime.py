from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

from schemas.hive_constants import HIVE_TIME_FORMAT

__all__ = [
    "HiveDateTime",
]


class HiveDateTime:
    def __init__(self, value: str | datetime):
        self.value = self._validate(value)

    def _validate(self, value: str | datetime) -> datetime:
        if isinstance(value, datetime):
            return self.__normalize(value)
        if isinstance(value, str):
            try:
                return self.__normalize(datetime.strptime(value, HIVE_TIME_FORMAT))
            except ValueError as error:
                raise ValueError(f"Date must be in format {HIVE_TIME_FORMAT}") from error
        raise TypeError("Value must be a datetime or a string in the correct format.")

    @staticmethod
    def __normalize(value: datetime) -> datetime:
        return value.replace(tzinfo=timezone.utc)

    @staticmethod
    def now() -> HiveDateTime:
        return HiveDateTime(value=datetime.now())

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, HiveDateTime):
            return self.value == other.value
        if isinstance(other, datetime):
            return self.value == other
        if isinstance(other, str):
            return self.value == self._validate(other)
        return False

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, HiveDateTime):
            return self.value < other.value
        if isinstance(other, datetime):
            return self.value < other
        if isinstance(other, str):
            return self.value < self._validate(other)
        return NotImplemented

    def __le__(self, other: Any) -> bool:
        return self == other or self < other  # type: ignore[no-any-return]

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, HiveDateTime):
            return self.value > other.value
        if isinstance(other, datetime):
            return self.value > other
        if isinstance(other, str):
            return self.value > self._validate(other)
        return NotImplemented

    def __ge__(self, other: Any) -> bool:
        return self == other or self > other  # type: ignore[no-any-return]

    def __ne__(self, other: Any) -> bool:
        return not self == other

    def __add__(self, other: timedelta) -> HiveDateTime:
        if isinstance(other, timedelta):
            return HiveDateTime(self.value + other)
        raise TypeError("Can only add timedelta to HiveDateTime.")

    def __sub__(self, other: Any) -> Any:
        if isinstance(other, timedelta):
            return HiveDateTime(self.value - other)
        if isinstance(other, HiveDateTime):
            return self.value - other.value
        if isinstance(other, datetime):
            return self.value - other
        raise TypeError("Subtraction only supports timedelta, datetime, or HiveDateTime.")

    def __str__(self) -> str:
        return self.value.strftime(HIVE_TIME_FORMAT)

    def __repr__(self) -> str:
        return self.value.strftime(HIVE_TIME_FORMAT)

    def __getattr__(self, other: Any) -> Any:
        return getattr(self.value, other)

    def __hash__(self) -> int:
        return hash(self.value)
