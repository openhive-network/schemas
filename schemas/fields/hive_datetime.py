from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any

from typing_extensions import Self

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator

__all__ = [
    "HiveDateTime",
]


class HiveDateTime(datetime):
    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate

    @classmethod
    def validate(cls, value: Any) -> datetime:
        if isinstance(value, datetime):
            return cls.__normalize(value)

        try:
            return cls.__normalize(datetime.strptime(value, "%Y-%m-%dT%H:%M:%S"))
        except ValueError as error:
            raise ValueError("date must be in format %Y-%m-%dT%H:%M:%S") from error

    @classmethod
    def __normalize(cls, value: datetime) -> datetime:
        return value.replace(tzinfo=timezone.utc)

    @classmethod
    def now(cls) -> Self:  # type: ignore[override]
        return cls.utcnow()
