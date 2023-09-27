from __future__ import annotations

from typing import Any, Generic

from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.operations.representations.representation_value_typevar import RepresentationValueT


class LegacyRepresentation(PreconfiguredBaseModel, GenericModel, Generic[RepresentationValueT]):
    type: str  # noqa: A003
    value: RepresentationValueT

    def __getitem__(self, key: str | int) -> Any:
        if isinstance(key, int):
            match key:
                case 0:
                    return self.value.get_name()
                case 1:
                    return self.value
                case _:
                    raise ValueError("out of bound")
        return super().__getitem__(key)
