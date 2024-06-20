from __future__ import annotations

import json
from typing import TypeAlias, TypeVar

from pydantic import BaseModel

from schemas.fields.basic import AccountName

AnyJson: TypeAlias = dict[str, "AnyJson"] | list["AnyJson"] | tuple["AnyJson", ...] | str | int | float | bool | None
T = TypeVar("T")


class CustomOperation(BaseModel):
    __operation_name__: str

    @classmethod
    def get_name(cls) -> str:
        return cls.__operation_name__

    def serialize(self) -> str:
        representation = [self.get_name(), self.dict()]
        return json.dumps(representation, separators=(",", ":"))


class FollowOperation(CustomOperation):
    __operation_name__ = "follow"

    follower: AccountName
    following: AccountName
    what: list[str]
