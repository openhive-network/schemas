from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import AccountName


class GetKeyReferences(PreconfiguredBaseModel):
    accounts: list[list[AccountName]]
