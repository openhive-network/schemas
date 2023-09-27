from __future__ import annotations

from typing import TypeVar

from schemas.operation import Operation
from schemas.operations.extensions.extension import OperationExtension

RepresentationValueT = TypeVar("RepresentationValueT", bound=Operation | OperationExtension)
