"""
    Common configuration for all classes(except some hive_fields), here you can add config that all classes which
    inheritance from this class must have
"""

from __future__ import annotations

import re
from typing import Any

from pydantic import BaseModel, Extra, Field, create_model
from typing_extensions import Self


class PreconfiguredBaseModel(BaseModel):
    class Config:
        extra = Extra.forbid
        allow_population_by_field_name = True

    @classmethod
    def as_strict_model(cls, recursively: bool = True) -> type[Self]:
        """
        Generate a BaseModel class with all the same fields like the class on which the method was called but with
        required fields only (no defaults allowed).

        Returns:
            Strict version of the class
        """

        # ellipsis is used to indicate that the field is required
        field_definitions = {field.name: (field.type_, ...) for field in cls.__fields__.values()}

        if recursively:
            for field_name, pack in field_definitions.items():
                field_type = pack[0]
                if issubclass(field_type, PreconfiguredBaseModel):
                    strict_type = field_type.as_strict_model(recursively=True)
                    field_definitions[field_name] = (strict_type, ...)

        return create_model(f"{cls.__name__}Strict", **field_definitions)  # type: ignore


class OperationWrapper(BaseModel):
    """This clas is used to create model of operation in HF26 format"""

    type_: str = Field(..., alias="type")
    value: dict[str, Any]


class Operation(PreconfiguredBaseModel):
    """Base class for all operations to provide valid json serialization"""

    def get_name(self) -> str:
        """conversion name of operation from CamelCase to snake_case"""
        name = self.__repr_name__()
        name = re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
        return name
