from __future__ import annotations

from typing import Any, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hive_string_int import HiveStringInt
from schemas.operation import Operation


class _UpdateProposalOperation(Operation, GenericModel, Generic[AssetHbdT]):
    __operation_name__ = "update_proposal"
    __offset__ = 47

    proposal_id: HiveStringInt
    creator: AccountName
    daily_pay: AssetHbdT
    subject: str
    permlink: str
    extensions: list[Any] = Field(default_factory=list)


class UpdateProposalOperation(_UpdateProposalOperation[AssetHbdHF26]):
    ...


class UpdateProposalOperationLegacy(_UpdateProposalOperation[AssetHbdLegacy]):
    ...
