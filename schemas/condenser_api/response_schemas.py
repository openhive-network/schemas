from __future__ import annotations

from pydantic import Field

import schemas.block_api.fundaments_of_responses as fundaments_block_api
import schemas.database_api.fundaments_of_reponses as fundaments_database_api
import schemas.database_api.response_schemas as database_api
import schemas.network_broadcast_api.response_schemas as broadcast_api
import schemas.wallet_bridge_api.response_schemas as wallet_bridge_api
from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbdLegacy,
    AssetHiveLegacy,
    AssetVestsLegacy,
    HiveInt,
)
from schemas.__private.hive_fields_custom_schemas import Proposal
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.condenser_api.fundaments_of_responses import (
    GetAccountHistoryFundament,
    GetAccountsFundament,
    GetActiveVotesFundament,
    GetBlockFundament,
    GetBlockHeaderFundament,
    GetBlogEntriesFundament,
    GetBlogFundament,
)


class BroadcastTransaction(broadcast_api.BroadcastTransaction):
    """This response as it is in network_broadcast api should return an empty dict"""


class BroadcastTransactionSynchronous(wallet_bridge_api.BroadcastTransactionSynchronous):
    """Identical response as response from wallet_bridge_api"""


class FindProposals(Proposal[AssetHbdLegacy]):
    """This response is identical as Proposal field, but here Legacy format is required and status excluded"""

    status: str = Field(None, exclude=True)  # type: ignore


FindRcAccounts = wallet_bridge_api.FindRcAccounts[AssetVestsLegacy]  # identical as in wallet_bridge_api, but legacy


class FindRecurrentTransfers(fundaments_database_api.FindRecurrentTransfersFundament[AssetHiveLegacy]):
    """Identical response like fundament for find_recurrent_transfers from database_api, but assets are legacy"""


GetAccountCount = HiveInt  # should return just integer


GetAccountHistory = GetAccountHistoryFundament  # to change


class GetAccountReputations(PreconfiguredBaseModel):
    account: AccountName
    reputation: HiveInt


GetAccounts = list[GetAccountsFundament]


GetActiveVotes = list[GetActiveVotesFundament]


class GetActiveWitnesses(database_api.GetActiveWitnesses):
    """Identical response as in database_api"""


GetBlock = GetBlockFundament | fundaments_block_api.EmptyModel


GetBlockHeader = list[GetBlockHeaderFundament]


GetBlog = list[GetBlogFundament]


GetBlogEntries = list[GetBlogEntriesFundament]


GetChainProperties = wallet_bridge_api.GetChainProperties[AssetHiveLegacy]  # like in wallet_bridge_api, just legacy
