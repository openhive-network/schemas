from __future__ import annotations

from typing import Any

import pytest
from pydantic import ValidationError

from schemas.apis.database_api import (
    FindAccountRecoveryRequests,
    FindAccounts,
    FindChangeRecoveryAccountRequests,
    FindComments,
    FindDeclineVotingRightsRequests,
    FindEscrows,
    FindHbdConversionRequests,
    FindLimitOrders,
    FindOwnerHistories,
    FindProposals,
    FindRecurrentTransfers,
    FindSavingsWithdrawals,
    FindVestingDelegationExpirations,
    FindVestingDelegations,
    FindWithdrawVestingRoutes,
    FindWitnesses,
    GetActiveWitnesses,
    GetCommentPendingPayouts,
    GetConfig,
    GetCurrentPriceFeed,
    GetDynamicGlobalProperties,
    GetFeedHistory,
    GetHardforkProperties,
    GetOrderBook,
    GetPotentialSignatures,
    GetRequiredSignatures,
    GetRewardFunds,
    GetTransactionHex,
    GetVersion,
    GetWitnessSchedule,
    IsKnownTransaction,
    ListAccountRecoveryRequests,
    ListAccounts,
    ListChangeRecoveryAccountRequests,
    ListComments,
    ListDeclineVotingRightsRequests,
    ListEscrows,
    ListHbdConversionRequests,
    ListLimitOrders,
    ListOwnerHistories,
    ListProposals,
    ListProposalVotes,
    ListSavingsWithdrawals,
    ListVestingDelegationExpirations,
    ListVestingDelegations,
    ListWithdrawVestingRoutes,
    ListWitnesses,
    ListWitnessVotes,
    VerifyAccountAuthority,
    VerifyAuthority,
    VerifySignatures,
)
from schemas.fields.assets.hbd import AssetHbdHF26
from schemas.fields.assets.hive import AssetHiveHF26
from schemas.fields.assets.vests import AssetVestsHF26
from schemas.jsonrpc import get_response_model
from schemas.policies import MissingFieldsInGetConfig

from .reponses_from_api import (
    FIND_ACCOUNT_RECOVERY_REQUESTS,
    FIND_ACCOUNTS,
    FIND_CHANGE_RECOVERY_ACCOUNT_REQUESTS,
    FIND_COMMENTS,
    FIND_DECLINE_VOTING_RIGHTS_REQUESTS,
    FIND_ESCROWS,
    FIND_HBD_CONVERSION_REQUESTS,
    FIND_LIMIT_ORDERS,
    FIND_OWNER_HISTORIES,
    FIND_PROPOSALS,
    FIND_RECURRENT_TRANSFERS,
    FIND_SAVINGS_WITHDRAWALS,
    FIND_VESTING_DELEGATION_EXPIRATIONS,
    FIND_VESTING_DELEGATIONS,
    FIND_WITHDRAW_VESTING_ROUTES,
    FIND_WITNESSES,
    GET_ACTIVE_WITNESSES,
    GET_COMMENT_PENDING_PAYOUTS,
    GET_CONFIG,
    GET_CURRENT_PRICE_FEED,
    GET_DYNAMIC_GLOBAL_PROPERTIES,
    GET_FEED_HISTORY,
    GET_HARDFORK_PROPERTIES,
    GET_ORDER_BOOK,
    GET_POTENTIAL_SIGNATURES,
    GET_REQUIRED_SIGNATURES,
    GET_REWARD_FUNDS,
    GET_TRANSACTION_HEX,
    GET_VERSION,
    GET_WITNESS_SCHEDULE,
    IS_KNOWN_TRANSACTION,
    LIST_ACCOUNT_RECOVERY_REQUESTS,
    LIST_ACCOUNTS,
    LIST_CHANGE_RECOVERY_ACCOUNT_REQUESTS,
    LIST_COMMENTS,
    LIST_DECLINE_VOTING_RIGHTS_REQUESTS,
    LIST_ESCROWS,
    LIST_HBD_CONVERSION_REQUESTS,
    LIST_LIMIT_ORDERS,
    LIST_OWNER_HISTORIES,
    LIST_PROPOSAL_VOTES,
    LIST_PROPOSALS,
    LIST_SAVINGS_WITHDRAWALS,
    LIST_VESTING_DELEGATION_EXPIRATIONS,
    LIST_VESTING_DELEGATIONS,
    LIST_WITHDRAW_VESTING_ROUTES,
    LIST_WITNESS_VOTES,
    LIST_WITNESSES,
    VERIFY_ACCOUNT_AUTHORITY,
    VERIFY_AUTHORITY,
    VERIFY_SIGNATURES,
)


@pytest.mark.parametrize(
    "parameters, schema",
    [
        (FIND_PROPOSALS, FindProposals),
        (LIST_ESCROWS, ListEscrows),
        (LIST_COMMENTS, ListComments),
        (LIST_OWNER_HISTORIES, ListOwnerHistories),
        (LIST_WITNESSES, ListWitnesses),
        (LIST_WITHDRAW_VESTING_ROUTES, ListWithdrawVestingRoutes),
        (LIST_DECLINE_VOTING_RIGHTS_REQUESTS, ListDeclineVotingRightsRequests),
        (FIND_VESTING_DELEGATIONS, FindVestingDelegations),
        (LIST_ACCOUNTS, ListAccounts),
        (LIST_CHANGE_RECOVERY_ACCOUNT_REQUESTS, ListChangeRecoveryAccountRequests),
        (LIST_ACCOUNT_RECOVERY_REQUESTS, ListAccountRecoveryRequests),
        (LIST_VESTING_DELEGATION_EXPIRATIONS, ListVestingDelegationExpirations),
        (LIST_HBD_CONVERSION_REQUESTS, ListHbdConversionRequests),
        (LIST_SAVINGS_WITHDRAWALS, ListSavingsWithdrawals),
        (LIST_LIMIT_ORDERS, ListLimitOrders),
        (LIST_WITNESS_VOTES, ListWitnessVotes),
        (LIST_PROPOSAL_VOTES, ListProposalVotes),
        (LIST_VESTING_DELEGATIONS, ListVestingDelegations),
        (FIND_LIMIT_ORDERS, FindLimitOrders),
        (GET_DYNAMIC_GLOBAL_PROPERTIES, GetDynamicGlobalProperties[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]),
        (GET_CONFIG, GetConfig),
        (GET_POTENTIAL_SIGNATURES, GetPotentialSignatures),
        (GET_WITNESS_SCHEDULE, GetWitnessSchedule),
        (FIND_DECLINE_VOTING_RIGHTS_REQUESTS, FindDeclineVotingRightsRequests),
        (FIND_VESTING_DELEGATION_EXPIRATIONS, FindVestingDelegationExpirations),
        (GET_REQUIRED_SIGNATURES, GetRequiredSignatures),
        (GET_VERSION, GetVersion),
        (GET_ORDER_BOOK, GetOrderBook),
        (GET_FEED_HISTORY, GetFeedHistory[AssetHiveHF26, AssetHbdHF26]),
        (GET_REWARD_FUNDS, GetRewardFunds),
        (GET_ACTIVE_WITNESSES, GetActiveWitnesses),
        (GET_TRANSACTION_HEX, GetTransactionHex),
        (GET_HARDFORK_PROPERTIES, GetHardforkProperties),
        (GET_CURRENT_PRICE_FEED, GetCurrentPriceFeed),
        (FIND_ACCOUNTS, FindAccounts),
        (VERIFY_AUTHORITY, VerifyAuthority),
        (VERIFY_ACCOUNT_AUTHORITY, VerifyAccountAuthority),
        (FIND_RECURRENT_TRANSFERS, FindRecurrentTransfers),
        (FIND_COMMENTS, FindComments),
        (IS_KNOWN_TRANSACTION, IsKnownTransaction),
        (FIND_OWNER_HISTORIES, FindOwnerHistories),
        (FIND_ESCROWS, FindEscrows),
        (FIND_WITNESSES, FindWitnesses),
        (FIND_ACCOUNT_RECOVERY_REQUESTS, FindAccountRecoveryRequests),
        (FIND_HBD_CONVERSION_REQUESTS, FindHbdConversionRequests),
        (FIND_CHANGE_RECOVERY_ACCOUNT_REQUESTS, FindChangeRecoveryAccountRequests),
        (VERIFY_SIGNATURES, VerifySignatures),
        (FIND_WITHDRAW_VESTING_ROUTES, FindWithdrawVestingRoutes),
        (GET_COMMENT_PENDING_PAYOUTS, GetCommentPendingPayouts),
        (FIND_SAVINGS_WITHDRAWALS, FindSavingsWithdrawals),
        (LIST_PROPOSALS, ListProposals),
    ],
)
def test_schemas_of_database_api_responses(parameters: dict[str, Any], schema: Any) -> None:
    # ACT & ASSERT
    get_response_model(schema, **parameters)


def test_get_config_policy() -> None:
    try:
        MissingFieldsInGetConfig(allow=True).apply()
        from schemas.apis import database_api

        database_api.GetConfig()  # type: ignore[call-arg]
    finally:
        MissingFieldsInGetConfig(allow=False).apply()  # this is in finally so it won't interfere other tests

    with pytest.raises(ValidationError):
        GetConfig()  # type: ignore[call-arg]
