from __future__ import annotations

from typing import Any

import pytest
from pydantic import ValidationError

from schemas.apis import database_api
from schemas.jsonrpc import get_response_model
from schemas.policies import MissingFieldsInGetConfig

from . import responses_from_api


@pytest.mark.parametrize(
    "parameters, schema, endpoint",
    [
        (responses_from_api.FIND_PROPOSALS, database_api.FindProposals, "database_api.find_proposals"),
        (responses_from_api.LIST_ESCROWS, database_api.ListEscrows, "database_api.list_escrows"),
        (responses_from_api.LIST_COMMENTS, database_api.ListComments, "database_api.list_comments"),
        (responses_from_api.LIST_OWNER_HISTORIES, database_api.ListOwnerHistories, "database_api.list_owner_histories"),
        (responses_from_api.LIST_WITNESSES, database_api.ListWitnesses, "database_api.list_witnesses"),
        (
            responses_from_api.LIST_WITHDRAW_VESTING_ROUTES,
            database_api.ListWithdrawVestingRoutes,
            "database_api.list_withdraw_vesting_routes",
        ),
        (
            responses_from_api.LIST_DECLINE_VOTING_RIGHTS_REQUESTS,
            database_api.ListDeclineVotingRightsRequests,
            "database_api.list_decline_voting_rights_requests",
        ),
        (
            responses_from_api.FIND_VESTING_DELEGATIONS,
            database_api.FindVestingDelegations,
            "database_api.find_vesting_delegations",
        ),
        (responses_from_api.LIST_ACCOUNTS, database_api.ListAccounts, "database_api.list_accounts"),
        (
            responses_from_api.LIST_CHANGE_RECOVERY_ACCOUNT_REQUESTS,
            database_api.ListChangeRecoveryAccountRequests,
            "database_api.list_change_recovery_account_requests",
        ),
        (
            responses_from_api.LIST_ACCOUNT_RECOVERY_REQUESTS,
            database_api.ListAccountRecoveryRequests,
            "database_api.list_account_recovery_requests",
        ),
        (
            responses_from_api.LIST_VESTING_DELEGATION_EXPIRATIONS,
            database_api.ListVestingDelegationExpirations,
            "database_api.list_vesting_delegation_expirations",
        ),
        (
            responses_from_api.LIST_HBD_CONVERSION_REQUESTS,
            database_api.ListHbdConversionRequests,
            "database_api.list_hbd_conversion_requests",
        ),
        (
            responses_from_api.LIST_SAVINGS_WITHDRAWALS,
            database_api.ListSavingsWithdrawals,
            "database_api.list_savings_withdrawals",
        ),
        (responses_from_api.LIST_LIMIT_ORDERS, database_api.ListLimitOrders, "database_api.list_limit_orders"),
        (responses_from_api.LIST_WITNESS_VOTES, database_api.ListWitnessVotes, "database_api.list_witness_votes"),
        (responses_from_api.LIST_PROPOSAL_VOTES, database_api.ListProposalVotes, "database_api.list_proposal_votes"),
        (
            responses_from_api.LIST_VESTING_DELEGATIONS,
            database_api.ListVestingDelegations,
            "database_api.list_vesting_delegations",
        ),
        (responses_from_api.FIND_LIMIT_ORDERS, database_api.FindLimitOrders, "database_api.find_limit_orders"),
        (
            responses_from_api.GET_DYNAMIC_GLOBAL_PROPERTIES,
            database_api.GetDynamicGlobalProperties,
            "database_api.get_dynamic_global_properties",
        ),
        (responses_from_api.GET_CONFIG, database_api.GetConfig, "database_api.get_config"),
        (
            responses_from_api.GET_POTENTIAL_SIGNATURES,
            database_api.GetPotentialSignatures,
            "database_api.get_potential_signatures",
        ),
        (responses_from_api.GET_WITNESS_SCHEDULE, database_api.GetWitnessSchedule, "database_api.get_witness_schedule"),
        (
            responses_from_api.FIND_DECLINE_VOTING_RIGHTS_REQUESTS,
            database_api.FindDeclineVotingRightsRequests,
            "database_api.find_decline_voting_rights_requests",
        ),
        (
            responses_from_api.FIND_VESTING_DELEGATION_EXPIRATIONS,
            database_api.FindVestingDelegationExpirations,
            "database_api.find_vesting_delegation_expirations",
        ),
        (
            responses_from_api.GET_REQUIRED_SIGNATURES,
            database_api.GetRequiredSignatures,
            "database_api.get_required_signatures",
        ),
        (responses_from_api.GET_VERSION, database_api.GetVersion, "database_api.get_version"),
        (responses_from_api.GET_ORDER_BOOK, database_api.GetOrderBook, "database_api.get_order_book"),
        (responses_from_api.GET_FEED_HISTORY, database_api.GetFeedHistory, "database_api.get_feed_history"),
        (responses_from_api.GET_REWARD_FUNDS, database_api.GetRewardFunds, "database_api.get_reward_funds"),
        (responses_from_api.GET_ACTIVE_WITNESSES, database_api.GetActiveWitnesses, "database_api.get_active_witnesses"),
        (responses_from_api.GET_TRANSACTION_HEX, database_api.GetTransactionHex, "database_api.get_transaction_hex"),
        (
            responses_from_api.GET_HARDFORK_PROPERTIES,
            database_api.GetHardforkProperties,
            "database_api.get_hardfork_properties",
        ),
        (
            responses_from_api.GET_CURRENT_PRICE_FEED,
            database_api.GetCurrentPriceFeed,
            "database_api.get_current_price_feed",
        ),
        (responses_from_api.FIND_ACCOUNTS, database_api.FindAccounts, "database_api.find_accounts"),
        (responses_from_api.VERIFY_AUTHORITY, database_api.VerifyAuthority, "database_api.verify_authority"),
        (
            responses_from_api.VERIFY_ACCOUNT_AUTHORITY,
            database_api.VerifyAccountAuthority,
            "database_api.verify_account_authority",
        ),
        (
            responses_from_api.FIND_RECURRENT_TRANSFERS,
            database_api.FindRecurrentTransfers,
            "database_api.find_recurrent_transfers",
        ),
        (responses_from_api.FIND_COMMENTS, database_api.FindComments, "database_api.find_comments"),
        (responses_from_api.IS_KNOWN_TRANSACTION, database_api.IsKnownTransaction, "database_api.is_known_transaction"),
        (responses_from_api.FIND_OWNER_HISTORIES, database_api.FindOwnerHistories, "database_api.find_owner_histories"),
        (responses_from_api.FIND_ESCROWS, database_api.FindEscrows, "database_api.find_escrows"),
        (responses_from_api.FIND_WITNESSES, database_api.FindWitnesses, "database_api.find_witnesses"),
        (
            responses_from_api.FIND_ACCOUNT_RECOVERY_REQUESTS,
            database_api.FindAccountRecoveryRequests,
            "database_api.find_account_recovery_requests",
        ),
        (
            responses_from_api.FIND_HBD_CONVERSION_REQUESTS,
            database_api.FindHbdConversionRequests,
            "database_api.find_hbd_conversion_requests",
        ),
        (
            responses_from_api.FIND_CHANGE_RECOVERY_ACCOUNT_REQUESTS,
            database_api.FindChangeRecoveryAccountRequests,
            "database_api.find_change_recovery_account_requests",
        ),
        (responses_from_api.VERIFY_SIGNATURES, database_api.VerifySignatures, "database_api.verify_signatures"),
        (
            responses_from_api.FIND_WITHDRAW_VESTING_ROUTES,
            database_api.FindWithdrawVestingRoutes,
            "database_api.find_withdraw_vesting_routes",
        ),
        (
            responses_from_api.GET_COMMENT_PENDING_PAYOUTS,
            database_api.GetCommentPendingPayouts,
            "database_api.get_comment_pending_payouts",
        ),
        (
            responses_from_api.FIND_SAVINGS_WITHDRAWALS,
            database_api.FindSavingsWithdrawals,
            "database_api.find_savings_withdrawals",
        ),
        (responses_from_api.LIST_PROPOSALS, database_api.ListProposals, "database_api.list_proposals"),
    ],
)
def test_schemas_of_database_api_responses(parameters: dict[str, Any], schema: Any, endpoint: Any) -> None:
    # ACT & ASSERT
    get_response_model(schema, endpoint, **parameters)


def test_get_config_policy() -> None:
    try:
        MissingFieldsInGetConfig(allow=True).apply()
        from schemas.apis import database_api

        database_api.GetConfig()  # type: ignore[call-arg]
    finally:
        MissingFieldsInGetConfig(allow=False).apply()  # this is in finally so it won't interfere other tests

    with pytest.raises(ValidationError):
        database_api.GetConfig()  # type: ignore[call-arg]
