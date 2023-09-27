from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint16t
from schemas.operations.extensions.extension import OperationExtension


class BeneficiaryRoute(PreconfiguredBaseModel):
    account: AccountName
    weight: Uint16t


class CommentPayoutBeneficiaries(OperationExtension):
    __extension_name__ = "comment_payout_beneficiaries"

    beneficiaries: list[BeneficiaryRoute]
