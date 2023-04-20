"""
    Common configuration for all classes(except some hive_fields), here you can add config that all classes which
    inheritance from this class must have
"""

from __future__ import annotations

from pydantic import BaseModel, Extra


class PreconfiguredBaseModel(BaseModel):
    class Config:
        extra = Extra.forbid
        allow_population_by_field_name = True
