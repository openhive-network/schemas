from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName


class SetResetAccountOperation(PreconfiguredBaseModel):
    account: AccountName
    current_reset_account: AccountName
    reset_account: AccountName
