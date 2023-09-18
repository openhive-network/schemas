"""
It is file with fields that are used just in creation models of api responses !
Notice when model of field inheritance from GenericModel you must choose format of assets, when
want to use this field.
"""

from __future__ import annotations

import re
from typing import Generic

from pydantic import ConstrainedStr, Field
from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets.hbd import AssetHbdT
from schemas.fields.assets.hive import AssetHiveT
from schemas.fields.assets.vests import AssetVestsT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt


class Manabar(PreconfiguredBaseModel):
    current_mana: HiveInt
    last_update_time: HiveInt


class DelayedVotes(PreconfiguredBaseModel):
    time: HiveDateTime
    val: HiveInt


class Price(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    """
    Valid structure for Price field is:
    base: Hive quote: Hbd or base: Hbd quote: Hive
    You can choose format of Assets, to choose legacy format -> Price[AssetHiveLegacy, AssetHbdLegacy](parameters).
    For HF26 format -> Price[AssetHiveHF26, AssetHbdHF26].
    Remember that Hive must be first parameter of generic !
    """

    base: AssetHiveT | AssetHbdT
    quote: AssetHiveT | AssetHbdT


class Proposal(PreconfiguredBaseModel, GenericModel, Generic[AssetHbdT]):
    id_: HiveInt = Field(alias="id")
    proposal_id: HiveInt
    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbdT
    subject: str
    permlink: str
    total_votes: HiveInt
    status: str


class Hex(ConstrainedStr):
    regex = re.compile(r"^[0-9a-fA-F]*$")


class Sha256(Hex):
    min_length = 64
    max_length = 64


class Version(ConstrainedStr):
    regex = re.compile(r"^\d+\.\d+\.\d+$")


HardforkVersion = Version


class Permlink(ConstrainedStr):
    max_length = 256


class TransactionId(Hex):
    min_length = 40
    max_length = 40


class FloatAsString(ConstrainedStr):
    regex = re.compile(r"^(?:(?:[1-9][0-9]*)|0)\.[0-9]+$")


class NodeType(ConstrainedStr):
    regex = re.compile(r"^(mainnet|testnet|mirrornet)$")


class HiveVersion(PreconfiguredBaseModel):
    blockchain_version: HardforkVersion
    hive_revision: TransactionId
    fc_revision: TransactionId
    chain_id: Sha256
    node_type: NodeType


class Props(PreconfiguredBaseModel, GenericModel, Generic[AssetHiveT]):
    account_creation_fee: AssetHiveT | None = None
    maximum_block_size: HiveInt | None = None
    hbd_interest_rate: HiveInt | None = None
    account_subsidy_budget: HiveInt | None = None
    account_subsidy_decay: HiveInt | None = None


class RdDecayParams(PreconfiguredBaseModel):
    decay_per_time_unit: HiveInt
    decay_per_time_unit_denom_shift: HiveInt


class RdDynamicParams(PreconfiguredBaseModel):
    resource_unit: HiveInt
    budget_per_time_unit: HiveInt
    pool_eq: HiveInt
    max_pool_size: HiveInt
    decay_params: RdDecayParams
    min_decay: HiveInt


class Signature(Hex):
    min_length = 130
    max_length = 130


class RcAccountObject(PreconfiguredBaseModel, GenericModel, Generic[AssetVestsT]):
    account: AccountName
    rc_manabar: Manabar
    max_rc_creation_adjustment: AssetVestsT
    max_rc: HiveInt
    delegated_rc: HiveInt
    received_delegated_rc: HiveInt
