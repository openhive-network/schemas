from __future__ import annotations

from typing import Literal

from msgspec import Struct, defstruct, field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.database_api.fundaments_of_reponses import (
    AccountItemFundament,
    EscrowsFundament,
    FindAccountRecoveryRequestsFundament,
    FindChangeRecoveryAccountRequestsFundament,
    FindCollateralizedConversionRequestsFundament,
    FindCommentsFundament,
    FindDeclineVotingRightsRequestsFundament,
    FindRecurrentTransfersFundament,
    GetCommentPendingPayoutsFundament,
    GetOrderBookFundament,
    GetRewardFundsFundament,
    GetWitnessScheduleFutureChangesFundament,
    HbdConversionRequestsFundament,
    LimitOrdersFundament,
    ListAccountRecoveryRequestsFundament,
    ListChangeRecoveryAccountRequestsFundament,
    ListCollateralizedConversionRequestsFundament,
    ListCommentsFundament,
    ListDeclineVotingRightsRequestsFundament,
    ListProposalVotesFundament,
    ListWitnessVotesFundament,
    OwnerHistoriesFundament,
    SavingsWithdrawalsFundament,
    VestingDelegationExpirationsFundament,
    VestingDelegationsFundament,
    WithdrawVestingRoutesFundament,
    WitnessesFundament,
)
from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVests
from schemas.fields.assets._symbol import HbdSymbolType, HiveSymbolType, VestsSymbolType
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import (
    Price,
    Proposal,
    Props,
    RdDynamicParams,
)
from schemas.fields.hex import Hex, TransactionId
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.fields.hive_list import HiveList
from schemas.fields.resolvables import OptionallyEmpty, OptionallyEmptyAccountName
from schemas.fields.version import HardforkVersion, HiveVersion


class FindAccountRecoveryRequests(PreconfiguredBaseModel, kw_only=True):
    requests: HiveList[FindAccountRecoveryRequestsFundament]


class FindAccounts(PreconfiguredBaseModel, kw_only=True):
    accounts: HiveList[AccountItemFundament]


class FindChangeRecoveryAccountRequests(PreconfiguredBaseModel, kw_only=True):
    requests: HiveList[FindChangeRecoveryAccountRequestsFundament]


class FindCollateralizedConversionRequests(PreconfiguredBaseModel, kw_only=True):
    requests: HiveList[FindCollateralizedConversionRequestsFundament]


class FindComments(PreconfiguredBaseModel, kw_only=True):
    comments: HiveList[FindCommentsFundament]


class FindDeclineVotingRightsRequests(PreconfiguredBaseModel, kw_only=True):
    requests: HiveList[FindDeclineVotingRightsRequestsFundament]


class FindEscrows(PreconfiguredBaseModel, kw_only=True):
    escrows: HiveList[EscrowsFundament]


class FindHbdConversionRequests(PreconfiguredBaseModel, kw_only=True):
    requests: HiveList[HbdConversionRequestsFundament]


class FindLimitOrders(PreconfiguredBaseModel, kw_only=True):
    orders: HiveList[LimitOrdersFundament]


class FindOwnerHistories(PreconfiguredBaseModel, kw_only=True):
    owner_auths: HiveList[OwnerHistoriesFundament]


class FindProposals(PreconfiguredBaseModel, kw_only=True):
    """
    This class does not have fundament in fundaments_of_responses.py.
    Fundament of this response is field Proposal
    """

    proposals: HiveList[Proposal]


class FindRecurrentTransfers(PreconfiguredBaseModel, kw_only=True):
    recurrent_transfers: HiveList[FindRecurrentTransfersFundament]


class FindSavingsWithdrawals(PreconfiguredBaseModel, kw_only=True):
    withdrawals: HiveList[SavingsWithdrawalsFundament]


class FindVestingDelegationExpirations(PreconfiguredBaseModel, kw_only=True):
    delegations: HiveList[VestingDelegationExpirationsFundament]


class FindVestingDelegations(PreconfiguredBaseModel, kw_only=True):
    delegations: HiveList[VestingDelegationsFundament]


class FindWithdrawVestingRoutes(PreconfiguredBaseModel, kw_only=True):
    routes: HiveList[WithdrawVestingRoutesFundament]


class FindWitnesses(PreconfiguredBaseModel, kw_only=True):
    witnesses: HiveList[WitnessesFundament]


class GetActiveWitnesses(PreconfiguredBaseModel, kw_only=True):
    """
    When witnesses are not elected they are displayed as empty string. The situation does not exist in mainnet.
    This response doesn't need fundament class
    """

    witnesses: list[OptionallyEmptyAccountName]
    future_witnesses: list[OptionallyEmptyAccountName] | None = None


class GetCommentPendingPayouts(PreconfiguredBaseModel, kw_only=True):
    cashout_infos: HiveList[GetCommentPendingPayoutsFundament]


class GetConfigOrig(PreconfiguredBaseModel, kw_only=True):
    """
    This response includes just one dict, so also doesn't need fundament class
    To use this class choose type of Assets so:
    Legacy -> GetConfig[AssetHiveLegacy, AssetHbdLegacy](parameters)
    HF26 -> GetConfig[AssetHiveNai, AssetHbdNai](parameters)
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
    VESTS_SYMBOL: VestsSymbolType
    HIVE_SYMBOL: HiveSymbolType
    HBD_SYMBOL: HbdSymbolType
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
    HIVE_MAX_TIME_UNTIL_SIGNATURE_EXPIRATION: HiveInt
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
    HIVE_MAX_COMMENT_BENEFICIARIES: HiveInt
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
    HIVE_RC_STATS_REPORT_FREQUENCY: HiveInt
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

    @classmethod
    def _optional_config(cls) -> type[Struct]:
        field_definitions = [
            (member, eval(GetConfigOrig.__annotations__[member] + " | None"), None)
            for member in GetConfigOrig.__annotations__
        ]
        return defstruct(
            "GetConfigWithDefaults",
            fields=field_definitions,
            bases=(PreconfiguredBaseModel,),
        )


GetConfig = GetConfigOrig


class GetCurrentPriceFeed(Price):
    """
    This response is identical as Price hive field.
    """


class GetDynamicGlobalPropertiesOrig(PreconfiguredBaseModel, kw_only=True):
    """
    This class doesn't need fundament class
    You need to choose asset format by generics when you want to use this class
    """

    available_account_subsidies: HiveInt
    content_reward_percent: HiveInt
    current_aslot: HiveInt
    current_hbd_supply: AssetHbd
    current_remove_threshold: HiveInt
    current_supply: AssetHive
    current_witness: AccountName
    delegation_return_period: HiveInt
    downvote_pool_percent: HiveInt
    early_voting_seconds: HiveInt
    hbd_interest_rate: HiveInt
    hbd_print_rate: HiveInt
    hbd_start_percent: HiveInt
    hbd_stop_percent: HiveInt
    head_block_id: TransactionId
    head_block_number: HiveInt
    id_: HiveInt = field(name="id")
    init_hbd_supply: AssetHbd
    last_budget_time: HiveDateTime
    last_irreversible_block_num: HiveInt
    max_consecutive_recurrent_transfer_failures: HiveInt
    max_open_recurrent_transfers: HiveInt
    max_recurrent_transfer_end_date: HiveInt
    maximum_block_size: HiveInt
    mid_voting_seconds: HiveInt
    min_recurrent_transfers_recurrence: HiveInt
    next_daily_maintenance_time: HiveDateTime
    next_maintenance_time: HiveDateTime
    num_pow_witnesses: HiveInt
    participation_count: HiveInt
    pending_rewarded_vesting_hive: AssetHive
    pending_rewarded_vesting_shares: AssetVests
    recent_slots_filled: HiveInt
    reverse_auction_seconds: HiveInt
    proposal_fund_percent: HiveInt
    dhf_interval_ledger: AssetHbd
    time: HiveDateTime
    total_pow: HiveInt
    total_reward_fund_hive: AssetHive
    total_reward_shares2: HiveInt
    total_vesting_fund_hive: AssetHive
    total_vesting_shares: AssetVests
    vesting_reward_percent: HiveInt
    virtual_supply: AssetHive
    vote_power_reserve_rate: HiveInt


GetDynamicGlobalProperties = GetDynamicGlobalPropertiesOrig


class GetFeedHistoryOrig(PreconfiguredBaseModel, kw_only=True):
    """
    This class doesn't need fundament class.
    """

    id_: HiveInt = field(name="id")
    current_median_history: Price
    market_median_history: Price
    current_min_history: Price
    current_max_history: Price
    price_history: list[Price]


GetFeedHistory = GetFeedHistoryOrig


class GetHardforkProperties(PreconfiguredBaseModel, kw_only=True):
    """
    This class doesn't need fundament class.
    """

    id_: HiveInt = field(name="id")
    processed_hardforks: list[HiveDateTime]
    last_hardfork: HiveInt
    current_hardfork_version: HardforkVersion
    next_hardfork: HardforkVersion
    next_hardfork_time: HiveDateTime


class GetOrderBook(PreconfiguredBaseModel, kw_only=True):
    asks: list[GetOrderBookFundament]
    bids: list[GetOrderBookFundament]


class GetPotentialSignatures(PreconfiguredBaseModel, kw_only=True):
    """
    This response is a list of keys, so doesn't need fundament class
    """

    keys: list[PublicKey]


class GetRequiredSignatures(GetPotentialSignatures):
    """
    Identical response as GetPotentialSignatures
    """


class GetRewardFunds(PreconfiguredBaseModel, kw_only=True):
    funds: HiveList[GetRewardFundsFundament]


class GetTransactionHex(PreconfiguredBaseModel, kw_only=True):
    hex_: Hex = field(name="hex")


class GetVersion(HiveVersion):
    """Identical response as HiveVersion field"""


class GetWitnessScheduleOrig(PreconfiguredBaseModel, kw_only=True):
    """When want to use must specify Asset type by Generic"""

    id_: HiveInt = field(name="id")
    current_virtual_time: HiveInt
    next_shuffle_block_num: HiveInt
    current_shuffled_witnesses: list[OptionallyEmptyAccountName]
    future_shuffled_witnesses: list[OptionallyEmptyAccountName] | None = None
    num_scheduled_witnesses: HiveInt
    elected_weight: HiveInt
    timeshare_weight: HiveInt
    miner_weight: HiveInt
    witness_pay_normalization_factor: HiveInt
    median_props: Props
    majority_version: HardforkVersion
    max_voted_witnesses: HiveInt
    max_miner_witnesses: HiveInt
    max_runner_witnesses: HiveInt
    hardfork_required_witnesses: HiveInt
    account_subsidy_rd: RdDynamicParams
    account_subsidy_witness_rd: RdDynamicParams
    min_witness_account_subsidy_decay: HiveInt
    future_changes: GetWitnessScheduleFutureChangesFundament | None = None


GetWitnessSchedule = GetWitnessScheduleOrig


class IsKnownTransaction(PreconfiguredBaseModel, kw_only=True):
    is_known: bool


class ListAccountRecoveryRequests(PreconfiguredBaseModel, kw_only=True):
    requests: HiveList[ListAccountRecoveryRequestsFundament]


class ListAccounts(PreconfiguredBaseModel, kw_only=True):
    accounts: HiveList[AccountItemFundament]


class ListChangeRecoveryAccountRequests(PreconfiguredBaseModel, kw_only=True):
    requests: HiveList[ListChangeRecoveryAccountRequestsFundament]


class ListCollateralizedConversionRequests(PreconfiguredBaseModel, kw_only=True):
    requests: HiveList[ListCollateralizedConversionRequestsFundament]


class ListComments(PreconfiguredBaseModel, kw_only=True):
    comments: HiveList[ListCommentsFundament]


class ListDeclineVotingRightsRequests(PreconfiguredBaseModel, kw_only=True):
    requests: HiveList[ListDeclineVotingRightsRequestsFundament]


class ListEscrows(PreconfiguredBaseModel, kw_only=True):
    escrows: HiveList[EscrowsFundament]


class ListHbdConversionRequests(PreconfiguredBaseModel, kw_only=True):
    requests: HiveList[HbdConversionRequestsFundament]


class ListLimitOrders(PreconfiguredBaseModel, kw_only=True):
    orders: HiveList[LimitOrdersFundament]


class ListOwnerHistories(PreconfiguredBaseModel, kw_only=True):
    owner_auths: HiveList[OwnerHistoriesFundament]


class ListProposals(PreconfiguredBaseModel, kw_only=True):
    proposals: HiveList[Proposal]


class ListProposalVotes(PreconfiguredBaseModel, kw_only=True):
    proposal_votes: HiveList[ListProposalVotesFundament]


class ListSavingsWithdrawals(PreconfiguredBaseModel, kw_only=True):
    withdrawals: HiveList[SavingsWithdrawalsFundament]


class ListVestingDelegationExpirations(PreconfiguredBaseModel, kw_only=True):
    delegations: HiveList[VestingDelegationExpirationsFundament]


class ListVestingDelegations(PreconfiguredBaseModel, kw_only=True):
    delegations: HiveList[VestingDelegationsFundament]


class ListWithdrawVestingRoutes(PreconfiguredBaseModel, kw_only=True):
    routes: HiveList[WithdrawVestingRoutesFundament]


class ListWitnesses(PreconfiguredBaseModel, kw_only=True):
    witnesses: HiveList[WitnessesFundament]


class ListWitnessVotes(PreconfiguredBaseModel, kw_only=True):
    votes: HiveList[ListWitnessVotesFundament]


class VerifyAccountAuthority(PreconfiguredBaseModel, kw_only=True):
    valid: bool


class VerifyAuthority(PreconfiguredBaseModel, kw_only=True):
    valid: bool


class VerifySignatures(PreconfiguredBaseModel, kw_only=True):
    valid: bool
