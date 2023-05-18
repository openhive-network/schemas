"""
It is file with fields that are used just in creation models of api responses !
"""

from __future__ import annotations

import re
from typing import Generic

from pydantic import ConstrainedStr, Field
from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, HiveDateTime, HiveInt
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class Manabar(PreconfiguredBaseModel):
    current_mana: HiveInt
    last_update_time: HiveInt


class DelayedVotes(PreconfiguredBaseModel):
    time: HiveDateTime
    val: HiveInt


class Price(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """
    Valid structure for Price field is:
    base: Hive quote: Hbd or base: Hbd quote: Hive
    You can choose format of Assets, to choose legacy format -> Price[AssetHiveLegacy, AssetHbdLegacy](parameters).
    For Nai format -> Price[AssetHiveNai, AssetHbdNai].
    Remember that Hive must be first parameter of generic !
    """

    base: AssetHive | AssetHbd
    quote: AssetHive | AssetHbd


class Proposal(PreconfiguredBaseModel, GenericModel, Generic[AssetHbd]):
    id_: HiveInt = Field(..., alias="id")
    proposal_id: HiveInt
    creator: AccountName
    receiver: AccountName
    start_date: HiveDateTime
    end_date: HiveDateTime
    daily_pay: AssetHbd
    subject: str
    permlink: str
    total_votes: HiveInt
    status: str


class Hex(ConstrainedStr):
    regex = re.compile(r"^[0-9a-fA-F]*$")


class Sha256(Hex):
    min_length = 64
    max_length = 64


class HardforkVersion(ConstrainedStr):
    regex = re.compile(r"^\d+\.\d+\.\d+$")


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


class Props(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    account_creation_fee: AssetHive
    maximum_block_size: HiveInt
    hbd_interest_rate: HiveInt
    account_subsidy_budget: HiveInt
    account_subsidy_decay: HiveInt


class RdDynamicParams(PreconfiguredBaseModel):
    resource_unit: HiveInt
    budget_per_time_unit: HiveInt
    pool_eq: HiveInt
    max_pool_size: HiveInt
    decay_params: dict[str, HiveInt]
    min_decay: HiveInt


class Signature(Hex):
    min_length = 130
    max_length = 130
