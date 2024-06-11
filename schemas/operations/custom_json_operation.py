from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.custom_operations.follow_operation import FollowOperationLegacyRepresentation
from schemas.custom_operations.json_convertible import JsonConvertible
from schemas.fields.basic import AccountName, CustomIdType
from schemas.fields.json_string import JsonString
from schemas.operation import Operation

JsonTypeT = TypeVar(
    "JsonTypeT",
    bound=JsonString | JsonConvertible | FollowOperationLegacyRepresentation,
)


class CustomJsonOperation(Operation, GenericModel, Generic[JsonTypeT]):
    __operation_name__ = "custom_json"
    __offset__ = 18

    required_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    id_: CustomIdType = Field(alias="id")
    json_: JsonTypeT = Field(alias="json")
