from __future__ import annotations

from typing import Generic, TypeAlias

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.basic import AccountName, CustomIdType
from schemas.fields.json_string import AnyJson, JsonFieldType, JsonString
from schemas.operation import Operation


class CustomJsonOperationGeneric(Operation):
    required_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    id_: CustomIdType = Field(alias="id")
    json_: JsonString[JsonFieldType] = Field(alias="json")


    @classmethod
    def get_name(cls):
        return "custom_json"
    
    @classmethod
    def offset(cls):
        return 18

CustomJsonOperation: TypeAlias = CustomJsonOperationGeneric
