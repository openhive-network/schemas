from __future__ import annotations

import json
from abc import ABC
from typing import Any, Generic, TypeVar

from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel


class CustomOperationBase(PreconfiguredBaseModel, ABC):
    __curtom_operation_name__: str

    @classmethod
    def get_name(cls) -> str:
        return cls.__curtom_operation_name__


RepresentationValueT = TypeVar("RepresentationValueT", bound=CustomOperationBase)


class LegacyRepresentation(PreconfiguredBaseModel, GenericModel, Generic[RepresentationValueT]):
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

    def dict(self, **kwargs: Any) -> Any:  # noqa: A003
        value_dict = self.value.dict(**kwargs)
        return [self.value.get_name(), value_dict]

    def json(self, **dumps_kwargs: Any) -> str:
        value_string = self.value.json(**dumps_kwargs)
        full_dict = [self.value.get_name(), json.loads(value_string)]
        return json.dumps(full_dict)

    @classmethod
    def validate(
        cls, value: str | LegacyRepresentation[RepresentationValueT]
    ) -> LegacyRepresentation[RepresentationValueT]:
        error_template = ValueError("The value could only be string or LegacyRepresentation[RepresentationValueT]!")

        if isinstance(value, LegacyRepresentation):
            return value

        if not isinstance(value, str):
            raise error_template

        try:
            parsed = json.loads(value)
        except (ValueError, TypeError) as error:
            raise error_template from error

        return cls(value=parsed[1])
