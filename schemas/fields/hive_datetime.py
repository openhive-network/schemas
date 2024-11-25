from __future__ import annotations

from datetime import timezone
from typing import Annotated

from pydantic import AfterValidator, AwareDatetime

__all__ = [
    "HiveDateTime",
]



HiveDateTime = Annotated[AwareDatetime, AfterValidator(lambda x: x.replace(tzinfo=timezone.utc))]
