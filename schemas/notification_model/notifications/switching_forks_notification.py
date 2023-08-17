from __future__ import annotations

from pydantic import Field

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class SwitchingForks(PreconfiguredBaseModel):
    id_: str = Field(alias="id")
    num: int
