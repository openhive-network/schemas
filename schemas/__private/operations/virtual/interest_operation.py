from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd
from schemas.__private.virtual_operation import VirtualOperation

DEFAULT_IS_SAVED_INTO_HBD_BALANCE: Final[bool] = False


class InterestOperation(VirtualOperation, GenericModel, Generic[AssetHbd]):
    owner: AccountName
    interest: AssetHbd
    is_saved_into_hbd_balance: bool = DEFAULT_IS_SAVED_INTO_HBD_BALANCE
