from __future__ import annotations

from typing import Any

from pydantic import ConstrainedStr

from schemas.__private.hive_fields_basic_schemas import (
    HiveInt,
)
from schemas._preconfigured_base_model import PreconfiguredBaseModel


class PublicKeyData(ConstrainedStr):
    strict = True
    min_length = 66
    max_length = 66


class ApiPeerStatus(PreconfiguredBaseModel):
    version: HiveInt
    host: str
    info: Any
