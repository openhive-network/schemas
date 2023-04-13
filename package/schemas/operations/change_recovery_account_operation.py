from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName


class ChangeRecoveryAccountOperation(PreconfiguredBaseModel):
    account_to_recover: AccountName
    new_recovery_account: AccountName
