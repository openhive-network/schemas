from __future__ import annotations

from typing import Generic, Literal

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdNai,
    AssetHive,
    AssetHiveNai,
    AssetVestsNai,
    EmptyString,
    HardforkVersion,
    Hex,
    HiveDateTime,
    HiveInt,
    Proposal,
    PublicKey,
)
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.database_api.fundaments_of_reponses import (
    AccountItemFundament,
    FindAccountRecoveryRequestsFundament,
    FindChangeRecoveryAccountRequestsFundament,
    FindCollateralizedConversionRequestsFundament,
    FindCommentsFundament,
    FindDeclineVotingRightsRequestsFundament,
    FindEscrowsFundament,
    FindHbdConversionRequestsFundament,
    FindLimitOrdersFundament,
    FindOwnerHistoriesFundament,
    FindRecurrentTransfersFundament,
    FindSavingsWithdrawalsFundament,
    FindVestingDelegationExpirationsFundament,
    FindVestingDelegationsFundament,
    FindWithdrawVestingRoutesFundament,
    FindWitnessFundament,
    GetCommentPendingPayoutsFundament,
)


class FindAccountRecoveryRequests(PreconfiguredBaseModel):
    requests: list[FindAccountRecoveryRequestsFundament]


class FindAccounts(PreconfiguredBaseModel):
    accounts: list[AccountItemFundament[AssetHiveNai, AssetHbdNai, AssetVestsNai]]


class FindChangeRecoveryAccountRequests(PreconfiguredBaseModel):
    requests: list[FindChangeRecoveryAccountRequestsFundament]


class FindCollateralizedConversionRequests(PreconfiguredBaseModel):
    requests: list[FindCollateralizedConversionRequestsFundament[AssetHiveNai, AssetHbdNai]]


class FindComments(PreconfiguredBaseModel):
    comments: list[FindCommentsFundament[AssetHbdNai]]


class FindDeclineVotingRightsRequests(PreconfiguredBaseModel):
    requests: list[FindDeclineVotingRightsRequestsFundament]


class FindEscrows(PreconfiguredBaseModel):
    escrows: list[FindEscrowsFundament[AssetHiveNai, AssetHbdNai]]


class FindHbdConversionRequests(PreconfiguredBaseModel):
    requests: list[FindHbdConversionRequestsFundament[AssetHbdNai]]


class FindLimitOrders(PreconfiguredBaseModel):
    orders: list[FindLimitOrdersFundament]


class FindOwnerHistories(PreconfiguredBaseModel):
    owner_auths: list[FindOwnerHistoriesFundament]


class FindProposals(PreconfiguredBaseModel):
    """
    This class does not have fundament in fundaments_of_responses.py.
    Fundament of this response is field Proposal
    """

    proposals: list[Proposal[AssetHbdNai]]


class FindRecurrentTransfers(PreconfiguredBaseModel):
    recurrent_transfers: list[FindRecurrentTransfersFundament[AssetHiveNai]]


class FindSavingsWithdrawals(PreconfiguredBaseModel):
    withdrawals: list[FindSavingsWithdrawalsFundament[AssetHiveNai, AssetHbdNai]]


class FindVestingDelegationExpirations(PreconfiguredBaseModel):
    delegations: FindVestingDelegationExpirationsFundament[AssetVestsNai]


class FindVestingDelegations(PreconfiguredBaseModel):
    delegations: FindVestingDelegationsFundament[AssetVestsNai]


class FindWithdrawVestingRoutes(PreconfiguredBaseModel):
    routes: list[FindWithdrawVestingRoutesFundament]


class FindWitness(PreconfiguredBaseModel):
    witnesses: list[FindWitnessFundament[AssetHiveNai]]


class GetActiveWitnesses(PreconfiguredBaseModel):
    """
    When witnesses are not elected they are displayed as empty string. The situation does not exist in mainnet.
    This response doesn't need fundament class
    """

    witnesses: list[AccountName | EmptyString]
    future_witnesses: list[AccountName | EmptyString] | None


class GetCommentPendingPayouts(PreconfiguredBaseModel):
    cashout_infos: list[GetCommentPendingPayoutsFundament]


class GetConfig(PreconfiguredBaseModel, GenericModel, Generic[AssetHive, AssetHbd]):
    """
    This response includes just one dict, so also doesn't need fundament class
    To use this class choose type of Assets so:
    Legacy -> GetConfig[AssetHiveLegacy, AssetHbdLegacy](parameters)
    Nai -> GetConfig[AssetHiveNai, AssetHbdNai](parameters)
    """

    HIVE_CHAIN_ID: Hex
    HIVE_TREASURY_ACCOUNT: AccountName
    IS_TEST_NET: bool
    HIVE_ENABLE_SMT: bool
    HIVE_DEFAULT_HF_9_COMPROMISED_ACCOUNTS_PUBLIC_KEY_STR: PublicKey
    HIVE_INIT_PUBLIC_KEY_STR: PublicKey
    HIVE_HF_9_COMPROMISED_ACCOUNTS_PUBLIC_KEY_STR: PublicKey
    HIVE_INIT_PUBLIC_KEY: PublicKey
    HIVE_BLOCKCHAIN_VERSION: HardforkVersion
    OLD_CHAIN_ID: Hex
    HIVE_ADDRESS_PREFIX: str
    HIVE_GENESIS_TIME: HiveDateTime
    HIVE_MINING_TIME: HiveDateTime
    HIVE_CASHOUT_WINDOW_SECONDS: HiveInt
    HIVE_CASHOUT_WINDOW_SECONDS_PRE_HF12: HiveInt
    HIVE_CASHOUT_WINDOW_SECONDS_PRE_HF17: HiveInt
    HIVE_SECOND_CASHOUT_WINDOW: HiveInt
    HIVE_MAX_CASHOUT_WINDOW_SECONDS: HiveInt
    HIVE_UPVOTE_LOCKOUT_HF7: HiveInt
    HIVE_UPVOTE_LOCKOUT_SECONDS: HiveInt
    HIVE_UPVOTE_LOCKOUT_HF17: HiveInt
    HIVE_MIN_ACCOUNT_CREATION_FEE: HiveInt
    HIVE_MAX_ACCOUNT_CREATION_FEE: HiveInt
    HIVE_OWNER_AUTH_RECOVERY_PERIOD: HiveInt
    HIVE_ACCOUNT_RECOVERY_REQUEST_EXPIRATION_PERIOD: HiveInt
    HIVE_OWNER_UPDATE_LIMIT: HiveInt
    HIVE_OWNER_AUTH_HISTORY_TRACKING_START_BLOCK_NUM: HiveInt
    HIVE_INIT_SUPPLY: HiveInt
    HIVE_HBD_INIT_SUPPLY: HiveInt
    HIVE_PROPOSAL_MAINTENANCE_PERIOD: HiveInt
    HIVE_PROPOSAL_MAINTENANCE_CLEANUP: HiveInt
    HIVE_DAILY_PROPOSAL_MAINTENANCE_PERIOD: HiveInt
    HIVE_GOVERNANCE_VOTE_EXPIRATION_PERIOD: HiveInt
    HIVE_WITNESS_SHUTDOWN_THRESHOLD: HiveInt
    HIVE_GLOBAL_REMOVE_THRESHOLD: HiveInt
    HIVE_START_MINER_VOTING_BLOCK: HiveInt
    HIVE_DELAYED_VOTING_TOTAL_INTERVAL_SECONDS: HiveInt
    HIVE_DELAYED_VOTING_INTERVAL_SECONDS: HiveInt
    HIVE_REVERSE_AUCTION_WINDOW_SECONDS_HF25: HiveInt
    HIVE_EARLY_VOTING_SECONDS_HF25: HiveInt
    HIVE_MID_VOTING_SECONDS_HF25: HiveInt
    VESTS_SYMBOL: dict[str, Literal["@@000000037"] | Literal[6]]
    HIVE_SYMBOL: dict[str, Literal["@@000000021"] | Literal[3]]
    HBD_SYMBOL: dict[str, Literal["@@000000013"] | Literal[3]]
    HIVE_BLOCKCHAIN_HARDFORK_VERSION: HardforkVersion
    HIVE_100_PERCENT: HiveInt
    HIVE_1_PERCENT: HiveInt
    HIVE_1_BASIS_POINT: HiveInt
    HIVE_BLOCK_INTERVAL: HiveInt
    HIVE_BLOCKS_PER_YEAR: HiveInt
    HIVE_BLOCKS_PER_DAY: HiveInt
    HIVE_START_VESTING_BLOCK: HiveInt
    HIVE_INIT_MINER_NAME: AccountName
    HIVE_NUM_INIT_MINERS: HiveInt
    HIVE_INIT_TIME: HiveDateTime
    HIVE_MAX_WITNESSES: HiveInt
    HIVE_MAX_VOTED_WITNESSES_HF0: HiveInt
    HIVE_MAX_MINER_WITNESSES_HF0: HiveInt
    HIVE_MAX_RUNNER_WITNESSES_HF0: HiveInt
    HIVE_MAX_VOTED_WITNESSES_HF17: HiveInt
    HIVE_MAX_MINER_WITNESSES_HF17: HiveInt
    HIVE_MAX_RUNNER_WITNESSES_HF17: HiveInt
    HIVE_HARDFORK_REQUIRED_WITNESSES: HiveInt
    HIVE_MAX_TIME_UNTIL_EXPIRATION: HiveInt
    HIVE_MAX_MEMO_SIZE: HiveInt
    HIVE_MAX_PROXY_RECURSION_DEPTH: HiveInt
    HIVE_VESTING_WITHDRAW_INTERVALS_PRE_HF_16: HiveInt
    HIVE_VESTING_WITHDRAW_INTERVALS: HiveInt
    HIVE_VESTING_WITHDRAW_INTERVAL_SECONDS: HiveInt
    HIVE_MAX_WITHDRAW_ROUTES: HiveInt
    HIVE_MAX_PENDING_TRANSFERS: HiveInt
    HIVE_MAX_OPEN_RECURRENT_TRANSFERS: HiveInt
    HIVE_MAX_CONSECUTIVE_RECURRENT_TRANSFER_FAILURES: HiveInt
    HIVE_MAX_RECURRENT_TRANSFER_END_DATE: HiveInt
    HIVE_MAX_RECURRENT_TRANSFERS_PER_BLOCK: HiveInt
    HIVE_MIN_RECURRENT_TRANSFERS_RECURRENCE: HiveInt
    HIVE_SAVINGS_WITHDRAW_TIME: HiveInt
    HIVE_SAVINGS_WITHDRAW_REQUEST_LIMIT: HiveInt
    HIVE_VOTING_MANA_REGENERATION_SECONDS: HiveInt
    HIVE_MAX_VOTE_CHANGES: HiveInt
    HIVE_REVERSE_AUCTION_WINDOW_SECONDS_HF6: HiveInt
    HIVE_REVERSE_AUCTION_WINDOW_SECONDS_HF20: HiveInt
    HIVE_REVERSE_AUCTION_WINDOW_SECONDS_HF21: HiveInt
    HIVE_MIN_VOTE_INTERVAL_SEC: HiveInt
    HIVE_VOTE_DUST_THRESHOLD: HiveInt
    HIVE_DOWNVOTE_POOL_PERCENT_HF21: HiveInt
    HIVE_MIN_ROOT_COMMENT_INTERVAL: HiveInt
    HIVE_MIN_REPLY_INTERVAL: HiveInt
    HIVE_MIN_REPLY_INTERVAL_HF20: HiveInt
    HIVE_MIN_COMMENT_EDIT_INTERVAL: HiveInt
    HIVE_POST_AVERAGE_WINDOW: HiveInt
    HIVE_POST_WEIGHT_CONSTANT: HiveInt
    HIVE_MAX_ACCOUNT_WITNESS_VOTES: HiveInt
    HIVE_DEFAULT_HBD_INTEREST_RATE: HiveInt
    HIVE_INFLATION_RATE_START_PERCENT: HiveInt
    HIVE_INFLATION_RATE_STOP_PERCENT: HiveInt
    HIVE_INFLATION_NARROWING_PERIOD: HiveInt
    HIVE_CONTENT_REWARD_PERCENT_HF16: HiveInt
    HIVE_VESTING_FUND_PERCENT_HF16: HiveInt
    HIVE_PROPOSAL_FUND_PERCENT_HF0: HiveInt
    HIVE_CONTENT_REWARD_PERCENT_HF21: HiveInt
    HIVE_PROPOSAL_FUND_PERCENT_HF21: HiveInt
    HIVE_HF21_CONVERGENT_LINEAR_RECENT_CLAIMS: HiveInt
    HIVE_CONTENT_CONSTANT_HF21: HiveInt
    HIVE_MINER_PAY_PERCENT: HiveInt
    HIVE_MAX_RATION_DECAY_RATE: HiveInt
    HIVE_BANDWIDTH_AVERAGE_WINDOW_SECONDS: HiveInt
    HIVE_BANDWIDTH_PRECISION: HiveInt
    HIVE_MAX_COMMENT_DEPTH_PRE_HF17: HiveInt
    HIVE_MAX_COMMENT_DEPTH: HiveInt
    HIVE_SOFT_MAX_COMMENT_DEPTH: HiveInt
    HIVE_MAX_RESERVE_RATIO: HiveInt
    HIVE_CREATE_ACCOUNT_WITH_HIVE_MODIFIER: HiveInt
    HIVE_CREATE_ACCOUNT_DELEGATION_RATIO: HiveInt
    HIVE_CREATE_ACCOUNT_DELEGATION_TIME: HiveInt
    HIVE_MINING_REWARD: AssetHive
    HIVE_EQUIHASH_N: HiveInt
    HIVE_EQUIHASH_K: HiveInt
    HIVE_LIQUIDITY_TIMEOUT_SEC: HiveInt
    HIVE_MIN_LIQUIDITY_REWARD_PERIOD_SEC: HiveInt
    HIVE_LIQUIDITY_REWARD_PERIOD_SEC: HiveInt
    HIVE_LIQUIDITY_REWARD_BLOCKS: HiveInt
    HIVE_MIN_LIQUIDITY_REWARD: AssetHive
    HIVE_MIN_CONTENT_REWARD: AssetHive
    HIVE_MIN_CURATE_REWARD: AssetHive
    HIVE_MIN_PRODUCER_REWARD: AssetHive
    HIVE_MIN_POW_REWARD: AssetHive
    HIVE_ACTIVE_CHALLENGE_FEE: AssetHive
    HIVE_OWNER_CHALLENGE_FEE: AssetHive
    HIVE_ACTIVE_CHALLENGE_COOLDOWN: HiveInt
    HIVE_OWNER_CHALLENGE_COOLDOWN: HiveInt
    HIVE_POST_REWARD_FUND_NAME: str
    HIVE_COMMENT_REWARD_FUND_NAME: str
    HIVE_RECENT_RSHARES_DECAY_TIME_HF17: HiveInt
    HIVE_RECENT_RSHARES_DECAY_TIME_HF19: HiveInt
    HIVE_CONTENT_CONSTANT_HF0: HiveInt
    HIVE_APR_PERCENT_MULTIPLY_PER_BLOCK: HiveInt
    HIVE_APR_PERCENT_SHIFT_PER_BLOCK: HiveInt
    HIVE_APR_PERCENT_MULTIPLY_PER_ROUND: HiveInt
    HIVE_APR_PERCENT_SHIFT_PER_ROUND: HiveInt
    HIVE_APR_PERCENT_MULTIPLY_PER_HOUR: HiveInt
    HIVE_APR_PERCENT_SHIFT_PER_HOUR: HiveInt
    HIVE_CURATE_APR_PERCENT: HiveInt
    HIVE_CONTENT_APR_PERCENT: HiveInt
    HIVE_LIQUIDITY_APR_PERCENT: HiveInt
    HIVE_PRODUCER_APR_PERCENT: HiveInt
    HIVE_POW_APR_PERCENT: HiveInt
    HIVE_MIN_PAYOUT_HBD: AssetHbd
    HIVE_HBD_START_PERCENT_HF14: HiveInt
    HIVE_HBD_STOP_PERCENT_HF14: HiveInt
    HIVE_HBD_START_PERCENT_HF20: HiveInt
    HIVE_HBD_STOP_PERCENT_HF20: HiveInt
    HIVE_HBD_START_PERCENT_HF26: HiveInt
    HIVE_HBD_STOP_PERCENT_HF26: HiveInt
    HIVE_HBD_HARD_LIMIT_PRE_HF26: HiveInt
    HIVE_HBD_HARD_LIMIT: HiveInt
    HIVE_MIN_ACCOUNT_NAME_LENGTH: Literal[3]
    HIVE_MAX_ACCOUNT_NAME_LENGTH: Literal[16]
    HIVE_MIN_PERMLINK_LENGTH: HiveInt
    HIVE_MAX_PERMLINK_LENGTH: Literal[256]
    HIVE_MAX_WITNESS_URL_LENGTH: HiveInt
    HIVE_MAX_SHARE_SUPPLY: HiveInt
    HIVE_MAX_SATOSHIS: HiveInt
    HIVE_MAX_SIG_CHECK_DEPTH: HiveInt
    HIVE_MAX_SIG_CHECK_ACCOUNTS: HiveInt
    HIVE_MIN_TRANSACTION_SIZE_LIMIT: HiveInt
    HIVE_SECONDS_PER_YEAR: HiveInt
    HIVE_HBD_INTEREST_COMPOUND_INTERVAL_SEC: HiveInt
    HIVE_MAX_TRANSACTION_SIZE: HiveInt
    HIVE_MIN_BLOCK_SIZE_LIMIT: HiveInt
    HIVE_MAX_BLOCK_SIZE: HiveInt
    HIVE_MIN_BLOCK_SIZE: HiveInt
    HIVE_BLOCKS_PER_HOUR: HiveInt
    HIVE_FEED_INTERVAL_BLOCKS: HiveInt
    HIVE_FEED_HISTORY_WINDOW_PRE_HF_16: HiveInt
    HIVE_FEED_HISTORY_WINDOW: HiveInt
    HIVE_MAX_FEED_AGE_SECONDS: HiveInt
    HIVE_MIN_FEEDS: HiveInt
    HIVE_CONVERSION_DELAY_PRE_HF_16: HiveInt
    HIVE_CONVERSION_DELAY: HiveInt
    HIVE_COLLATERALIZED_CONVERSION_DELAY: HiveInt
    HIVE_CONVERSION_COLLATERAL_RATIO: HiveInt
    HIVE_COLLATERALIZED_CONVERSION_FEE: HiveInt
    HIVE_MIN_UNDO_HISTORY: HiveInt
    HIVE_MAX_UNDO_HISTORY: HiveInt
    HIVE_MIN_TRANSACTION_EXPIRATION_LIMIT: HiveInt
    HIVE_BLOCKCHAIN_PRECISION: HiveInt
    HIVE_BLOCKCHAIN_PRECISION_DIGITS: HiveInt
    HIVE_MAX_INSTANCE_ID: HiveInt
    HIVE_MAX_AUTHORITY_MEMBERSHIP: HiveInt
    HIVE_MAX_ASSET_WHITELIST_AUTHORITIES: HiveInt
    HIVE_MAX_URL_LENGTH: HiveInt
    HIVE_IRREVERSIBLE_THRESHOLD: HiveInt
    HIVE_VIRTUAL_SCHEDULE_LAP_LENGTH: HiveInt
    HIVE_VIRTUAL_SCHEDULE_LAP_LENGTH2: HiveInt
    HIVE_INITIAL_VOTE_POWER_RATE: HiveInt
    HIVE_REDUCED_VOTE_POWER_RATE: HiveInt
    HIVE_MAX_LIMIT_ORDER_EXPIRATION: HiveInt
    HIVE_DELEGATION_RETURN_PERIOD_HF0: HiveInt
    HIVE_DELEGATION_RETURN_PERIOD_HF20: HiveInt
    HIVE_RC_BUCKET_TIME_LENGTH: HiveInt
    HIVE_RC_HISTORICAL_ACCOUNT_CREATION_ADJUSTMENT: HiveInt
    HIVE_RC_MAX_ACCOUNTS_PER_DELEGATION_OP: HiveInt
    HIVE_RC_REGEN_TIME: HiveInt
    HIVE_RC_WINDOW_BUCKET_COUNT: HiveInt
    HIVE_RD_MIN_DECAY_BITS: HiveInt
    HIVE_RD_MAX_DECAY_BITS: HiveInt
    HIVE_RD_DECAY_DENOM_SHIFT: HiveInt
    HIVE_RD_MAX_POOL_BITS: HiveInt
    HIVE_RD_MAX_BUDGET_1: HiveInt
    HIVE_RD_MAX_BUDGET_2: HiveInt
    HIVE_RD_MAX_BUDGET_3: HiveInt
    HIVE_RD_MAX_BUDGET: HiveInt
    HIVE_RD_MIN_DECAY: HiveInt
    HIVE_RD_MIN_BUDGET: HiveInt
    HIVE_RD_MAX_DECAY: HiveInt
    HIVE_ACCOUNT_SUBSIDY_PRECISION: HiveInt
    HIVE_WITNESS_SUBSIDY_BUDGET_PERCENT: HiveInt
    HIVE_WITNESS_SUBSIDY_DECAY_PERCENT: HiveInt
    HIVE_DEFAULT_ACCOUNT_SUBSIDY_DECAY: HiveInt
    HIVE_DEFAULT_ACCOUNT_SUBSIDY_BUDGET: HiveInt
    HIVE_DECAY_BACKSTOP_PERCENT: HiveInt
    HIVE_BLOCK_GENERATION_POSTPONED_TX_LIMIT: HiveInt
    HIVE_PENDING_TRANSACTION_EXECUTION_LIMIT: HiveInt
    HIVE_CUSTOM_OP_ID_MAX_LENGTH: HiveInt
    HIVE_CUSTOM_OP_DATA_MAX_LENGTH: HiveInt
    HIVE_BENEFICIARY_LIMIT: HiveInt
    HIVE_COMMENT_TITLE_LIMIT: HiveInt
    HIVE_ONE_DAY_SECONDS: HiveInt
    HIVE_MINER_ACCOUNT: AccountName
    HIVE_NULL_ACCOUNT: AccountName
    HIVE_TEMP_ACCOUNT: AccountName
    HIVE_PROXY_TO_SELF_ACCOUNT: str
    HIVE_ROOT_POST_PARENT: str
    OBSOLETE_TREASURY_ACCOUNT: AccountName
    NEW_HIVE_TREASURY_ACCOUNT: AccountName
    HIVE_TREASURY_FEE: HiveInt
    HIVE_PROPOSAL_SUBJECT_MAX_LENGTH: HiveInt
    HIVE_PROPOSAL_MAX_IDS_NUMBER: HiveInt
    HIVE_PROPOSAL_FEE_INCREASE_DAYS: HiveInt
    HIVE_PROPOSAL_FEE_INCREASE_DAYS_SEC: HiveInt
    HIVE_PROPOSAL_FEE_INCREASE_AMOUNT: HiveInt
    HIVE_PROPOSAL_CONVERSION_RATE: HiveInt
    HIVE_UP_TO_DATE_MARGIN__BLOCK_STATS: HiveInt
    HIVE_UP_TO_DATE_MARGIN__FAST_CONFIRM: HiveInt
    HIVE_UP_TO_DATE_MARGIN__PENDING_TXS: HiveInt
