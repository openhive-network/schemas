from __future__ import annotations

from typing import Generic, TypeAlias, TypeVar

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.basic import AccountName, CustomIdType
from schemas.fields.json_string import AnyJson, JsonString
from schemas.operation import Operation

JsonFieldType = TypeVar("JsonFieldType")


class CustomJsonOperationGeneric(Operation, GenericModel, Generic[JsonFieldType]):
    __operation_name__ = "custom_json"
    __offset__ = 18

    required_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    id_: CustomIdType = Field(alias="id")
    json_: JsonString[JsonFieldType] = Field(alias="json")


CustomJsonOperation: TypeAlias = CustomJsonOperationGeneric[AnyJson]
