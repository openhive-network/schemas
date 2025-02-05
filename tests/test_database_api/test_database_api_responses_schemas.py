from __future__ import annotations

import json
from typing import Any

import pytest

from schemas.apis import database_api
from schemas.jsonrpc import get_response_model
from schemas.policies.missing_fields_in_get_config import MissingFieldsInGetConfig

from . import responses_from_api


@pytest.mark.parametrize(
    "parameters, schema",
    [
        (responses_from_api.FIND_PROPOSALS, database_api.FindProposals),
        (responses_from_api.LIST_ESCROWS, database_api.ListEscrows),
        (responses_from_api.LIST_COMMENTS, database_api.ListComments),
        (responses_from_api.LIST_OWNER_HISTORIES, database_api.ListOwnerHistories),
        (responses_from_api.LIST_WITNESSES, database_api.ListWitnesses),
        (responses_from_api.LIST_WITHDRAW_VESTING_ROUTES, database_api.ListWithdrawVestingRoutes),
        (responses_from_api.LIST_DECLINE_VOTING_RIGHTS_REQUESTS, database_api.ListDeclineVotingRightsRequests),
        (responses_from_api.FIND_VESTING_DELEGATIONS, database_api.FindVestingDelegations),
        (responses_from_api.LIST_ACCOUNTS, database_api.ListAccounts),
        (responses_from_api.LIST_CHANGE_RECOVERY_ACCOUNT_REQUESTS, database_api.ListChangeRecoveryAccountRequests),
        (responses_from_api.LIST_ACCOUNT_RECOVERY_REQUESTS, database_api.ListAccountRecoveryRequests),
        (responses_from_api.LIST_VESTING_DELEGATION_EXPIRATIONS, database_api.ListVestingDelegationExpirations),
        (responses_from_api.LIST_HBD_CONVERSION_REQUESTS, database_api.ListHbdConversionRequests),
        (responses_from_api.LIST_SAVINGS_WITHDRAWALS, database_api.ListSavingsWithdrawals),
        (responses_from_api.LIST_LIMIT_ORDERS, database_api.ListLimitOrders),
        (responses_from_api.LIST_WITNESS_VOTES, database_api.ListWitnessVotes),
        (responses_from_api.LIST_PROPOSAL_VOTES, database_api.ListProposalVotes),
        (responses_from_api.LIST_VESTING_DELEGATIONS, database_api.ListVestingDelegations),
        (responses_from_api.FIND_LIMIT_ORDERS, database_api.FindLimitOrders),
        (responses_from_api.GET_DYNAMIC_GLOBAL_PROPERTIES, database_api.GetDynamicGlobalProperties),
        (responses_from_api.GET_CONFIG, database_api.GetConfig),
        (responses_from_api.GET_POTENTIAL_SIGNATURES, database_api.GetPotentialSignatures),
        (responses_from_api.GET_WITNESS_SCHEDULE, database_api.GetWitnessSchedule),
        (responses_from_api.FIND_DECLINE_VOTING_RIGHTS_REQUESTS, database_api.FindDeclineVotingRightsRequests),
        (responses_from_api.FIND_VESTING_DELEGATION_EXPIRATIONS, database_api.FindVestingDelegationExpirations),
        (responses_from_api.GET_REQUIRED_SIGNATURES, database_api.GetRequiredSignatures),
        (responses_from_api.GET_VERSION, database_api.GetVersion),
        (responses_from_api.GET_ORDER_BOOK, database_api.GetOrderBook),
        (responses_from_api.GET_FEED_HISTORY, database_api.GetFeedHistory),
        (responses_from_api.GET_REWARD_FUNDS, database_api.GetRewardFunds),
        (responses_from_api.GET_ACTIVE_WITNESSES, database_api.GetActiveWitnesses),
        (responses_from_api.GET_TRANSACTION_HEX, database_api.GetTransactionHex),
        (responses_from_api.GET_HARDFORK_PROPERTIES, database_api.GetHardforkProperties),
        (responses_from_api.GET_CURRENT_PRICE_FEED, database_api.GetCurrentPriceFeed),
        (responses_from_api.FIND_ACCOUNTS, database_api.FindAccounts),
        (responses_from_api.VERIFY_AUTHORITY, database_api.VerifyAuthority),
        (responses_from_api.VERIFY_ACCOUNT_AUTHORITY, database_api.VerifyAccountAuthority),
        (responses_from_api.FIND_RECURRENT_TRANSFERS, database_api.FindRecurrentTransfers),
        (responses_from_api.FIND_COMMENTS, database_api.FindComments),
        (responses_from_api.IS_KNOWN_TRANSACTION, database_api.IsKnownTransaction),
        (responses_from_api.FIND_OWNER_HISTORIES, database_api.FindOwnerHistories),
        (responses_from_api.FIND_ESCROWS, database_api.FindEscrows),
        (responses_from_api.FIND_WITNESSES, database_api.FindWitnesses),
        (responses_from_api.FIND_ACCOUNT_RECOVERY_REQUESTS, database_api.FindAccountRecoveryRequests),
        (responses_from_api.FIND_HBD_CONVERSION_REQUESTS, database_api.FindHbdConversionRequests),
        (responses_from_api.FIND_CHANGE_RECOVERY_ACCOUNT_REQUESTS, database_api.FindChangeRecoveryAccountRequests),
        (responses_from_api.VERIFY_SIGNATURES, database_api.VerifySignatures),
        (responses_from_api.FIND_WITHDRAW_VESTING_ROUTES, database_api.FindWithdrawVestingRoutes),
        (responses_from_api.GET_COMMENT_PENDING_PAYOUTS, database_api.GetCommentPendingPayouts),
        (responses_from_api.FIND_SAVINGS_WITHDRAWALS, database_api.FindSavingsWithdrawals),
        (responses_from_api.LIST_PROPOSALS, database_api.ListProposals),
    ],
)
def test_schemas_of_database_api_responses(parameters: dict[str, Any], schema: Any) -> None:
    # ACT & ASSERT
    get_response_model(schema, json.dumps(parameters), "hf26")


def test_get_config_policy() -> None:
    try:
        MissingFieldsInGetConfig(allow=True).apply()
        from schemas.apis import database_api

        database_api.GetConfig()  # type: ignore[call-arg]
    finally:
        MissingFieldsInGetConfig(allow=False).apply()  # this is in finally so it won't interfere other tests

    with pytest.raises(TypeError):
        database_api.GetConfig()  # type: ignore[call-arg]
