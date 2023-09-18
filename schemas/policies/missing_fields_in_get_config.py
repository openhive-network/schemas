from __future__ import annotations

from dataclasses import dataclass
from typing import Generic

from pydantic import Field, create_model
from pydantic.generics import GenericModel

from schemas.policies.policy import Policy


@dataclass
class MissingFieldsInGetConfig(Policy):
    allow: bool

    def apply(self) -> None:
        from schemas._preconfigured_base_model import PreconfiguredBaseModel
        from schemas.apis import database_api
        from schemas.apis.database_api.response_schemas import GetConfigOrig
        from schemas.fields.basic import AssetHbdT, AssetHiveT

        if self.allow:
            field_definitions = {
                field.name: (field.type_ | None, Field(None, alias=field.alias))
                for field in GetConfigOrig.__fields__.values()
            }
            database_api.GetConfig = create_model(  # type: ignore[call-overload]
                "GetConfigWithDefaults",
                __base__=(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT]),
                **field_definitions,
            )
        else:
            database_api.GetConfig = GetConfigOrig
