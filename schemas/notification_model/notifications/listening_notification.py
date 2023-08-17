from __future__ import annotations

from typing import Literal

from pydantic import Field

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class WebserverListening(PreconfiguredBaseModel):
    type_: Literal["HTTP", "WS"] = Field(alias="type")
    address: str
    port: int
