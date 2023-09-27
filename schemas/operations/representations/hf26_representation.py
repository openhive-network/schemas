from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.operations.representations.representation_value_typevar import RepresentationValueT


class HF26Representation(PreconfiguredBaseModel, GenericModel, Generic[RepresentationValueT]):
    type: str  # noqa: A003
    value: RepresentationValueT
