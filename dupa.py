from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Annotated, Any

import msgspec

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import ValidatorString

DupStr = ValidatorString.factory(msgspec.Meta(max_length=3))

class Dupa(PreconfiguredBaseModel):
    dupa: DupStr

Dupa(dupa="abc")
