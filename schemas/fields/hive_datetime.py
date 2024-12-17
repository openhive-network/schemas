from __future__ import annotations

from datetime import datetime, timezone
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

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, HiveDateTime):
            return self.value == other.value
        if isinstance(other, datetime):
            return self.value == other
        if isinstance(other, str):
            return self.value == self._validate(other)
        return False

    def __str__(self) -> str:
        return self.value.strftime(HIVE_TIME_FORMAT)

    def __repr__(self) -> str:
        return self.value.strftime(HIVE_TIME_FORMAT)

    def __getattr__(self, other: Any) -> Any:
        return getattr(self.value, other)

    def __hash__(self) -> int:
        return hash(self.value)
