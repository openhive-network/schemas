from __future__ import annotations

from dataclasses import dataclass

from schemas.policies.policy import Policy


@dataclass
class MissingFieldsInGetConfig(Policy):
    allow: bool

    def apply(self) -> None:
        from schemas.apis import database_api
        from schemas.apis.database_api.response_schemas import GetConfigOrig

        if self.allow:
            database_api.GetConfig = GetConfigOrig._optional_config()  #  type: ignore[assignment]
        else:
            database_api.GetConfig = GetConfigOrig
