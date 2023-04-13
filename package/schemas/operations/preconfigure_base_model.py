from __future__ import annotations

from pydantic import BaseModel, Extra


class PreconfiguredBaseModel(BaseModel):
    class Config:
        extra = Extra.forbid
        allow_population_by_field_name = True
