"""
Response from API has three poles -> id, jsonrpc and result. The factory method from HiveResult class is using to
return result pole, cause is must be validated deeper and then all operations is being performed on result field.
Yoy must use it like this -> HiveResult.factory(type_of_response, **response_from_api_json/dict).
"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.preconfigured_base_model import PreconfiguredBaseModel

T = TypeVar("T", bound=PreconfiguredBaseModel | list[PreconfiguredBaseModel])


class HiveError(PreconfiguredBaseModel, GenericModel, Generic[T]):
    id_: int = Field(alias="id")
    jsonrpc: str
    error: T


class HiveResult(PreconfiguredBaseModel, GenericModel, Generic[T]):
    id_: int = Field(alias="id")
    jsonrpc: str
    result: T

    @staticmethod
    def factory(t: Any, **kwargs: Any) -> HiveResult[T] | HiveError[T]:
        """t -> type of response from api, **kwargs -> unpacked parameters got from api.
        This function is used to return validation on result field, you choose model of result field
        by generic. Factory return just result field from api.
        In case when something is wrong and result field is not present, but error this method return
        HiveError instance of class
        """
        response_cls = HiveResult[t] if "result" in kwargs else HiveError[t]
        response_cls.update_forward_refs(**locals())
        return response_cls(**kwargs)  # type: ignore[return-value]
