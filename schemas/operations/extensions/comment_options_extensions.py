from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint16t
from schemas.operation import Operation


class BeneficiaryRoute(PreconfiguredBaseModel):
    account: AccountName
    weight: Uint16t


class CommentPayoutBeneficiaries(Operation):
    @classmethod
    def get_name(cls) -> str:
        return "comment_payout_beneficiaries"

    beneficiaries: list[BeneficiaryRoute]
