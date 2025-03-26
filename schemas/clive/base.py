from __future__ import annotations

from typing import Final, TypeVar

from schemas._preconfigured_base_model import PreconfiguredBaseModel

TIME_FORMAT_WITH_SECONDS: Final[str] = "%Y-%m-%dT%H:%M:%S"

T = TypeVar("T")


class CliveBaseModel(PreconfiguredBaseModel):
    pass
