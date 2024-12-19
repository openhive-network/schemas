from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING, Annotated, Any

import msgspec
from typing_extensions import Self

from schemas.hive_constants import HIVE_TIME_FORMAT

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator

__all__ = [
    "HiveDateTime",
]


HiveDateTime = Annotated[datetime, msgspec.Meta(tz=False)]

# class HiveDateTime(datetime):
#     @classmethod
#     def __get_validators__(cls) -> CallableGenerator:
#         yield cls.validate

#     @classmethod
#     def validate(cls, value: Any) -> datetime:
#         if isinstance(value, datetime):
#             return cls.__normalize(value)

#         try:
#             return cls.__normalize(datetime.strptime(value, HIVE_TIME_FORMAT))
#         except ValueError as error:
#             raise ValueError(f"date must be in format {HIVE_TIME_FORMAT}") from error

#     @classmethod
#     def __normalize(cls, value: datetime) -> datetime:
#         return value.replace(tzinfo=timezone.utc)

#     @classmethod
#     def now(cls) -> Self:  # type: ignore[override]
#         return cls.utcnow()
