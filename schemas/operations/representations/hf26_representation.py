from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.operation import Operation


class HF26OperationRepresentation(PreconfiguredBaseModel):
    type: str  # noqa: A003
    value: Operation
