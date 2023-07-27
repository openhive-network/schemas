from __future__ import annotations

from typing import Any

from schemas.preconfigured_base_model import PreconfiguredBaseModel

"""List of methods available in api"""
GetMethods = list[str]


class GetSignature(PreconfiguredBaseModel):
    args: Any
    ret: Any
