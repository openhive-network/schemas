from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.api_client_generator._private.common.models_aliased import AnyJson


class RestApiMethod(PreconfiguredBaseModel):
    tags: list[str]
    summary: str
    description: str
    operationId: str  # NOQA: N815
    responses: AnyJson
    parameters: list[AnyJson] | None = None
