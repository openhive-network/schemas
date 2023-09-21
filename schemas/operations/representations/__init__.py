from __future__ import annotations

from schemas.operations.representations.hf26_representation import HF26OperationRepresentation
from schemas.operations.representations.legacy_representation import LegacyOperationRepresentation
from schemas.operations.representations.util import (
    convert_to_representation,
    get_hf26_representation,
    get_legacy_representation,
)

__all__ = [
    "convert_to_representation",
    "get_hf26_representation",
    "get_legacy_representation",
    "HF26OperationRepresentation",
    "LegacyOperationRepresentation",
]
