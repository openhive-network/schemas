from __future__ import annotations

from schemas.__private.operations.virtual.account_created_operation import (
    AccountCreatedOperationHF26,
    AccountCreatedOperationLegacy,
)
from schemas.__private.operations.virtual.author_reward_operation import (
    AuthorRewardOperationHF26,
    AuthorRewardOperationLegacy,
)
from schemas.__private.operations.virtual.changed_recovery_account_operation import ChangedRecoveryAccountOperation
from schemas.__private.operations.virtual.clear_null_account_balance_operation import (
    ClearNullAccountBalanceOperationHF26,
    ClearNullAccountBalanceOperationLegacy,
)
from schemas.__private.operations.virtual.collateralized_convert_immediate_conversion_operation import (
    CollateralizedConvertImmediateConversionOperationHF26,
    CollateralizedConvertImmediateConversionOperationLegacy,
)
from schemas.__private.operations.virtual.comment_benefactor_reward_operation import (
    CommentBenefactorRewardOperationHF26,
    CommentBenefactorRewardOperationLegacy,
)
from schemas.__private.operations.virtual.comment_payout_update_operation import CommentPayoutUpdateOperation
from schemas.__private.operations.virtual.comment_reward_operation import (
    CommentRewardOperationHF26,
    CommentRewardOperationLegacy,
)
from schemas.__private.operations.virtual.consolidate_treasury_balance_operation import (
    ConsolidateTreasuryBalanceOperationHF26,
    ConsolidateTreasuryBalanceOperationLegacy,
)
from schemas.__private.operations.virtual.curation_reward_operation import (
    CurationRewardOperationHF26,
    CurationRewardOperationLegacy,
)
from schemas.__private.operations.virtual.declined_voting_rights_operation import DeclinedVotingRightsOperation
from schemas.__private.operations.virtual.delayed_voting_operation import DelayedVotingOperation
from schemas.__private.operations.virtual.dhf_conversion_operation import (
    DhfConversionOperationHF26,
    DhfConversionOperationLegacy,
)
from schemas.__private.operations.virtual.dhf_funding_operation import (
    DhfFundingOperationHF26,
    DhfFundingOperationLegacy,
)
from schemas.__private.operations.virtual.effective_comment_vote_operation import (
    EffectiveCommentVoteOperationHF26,
    EffectiveCommentVoteOperationLegacy,
)
from schemas.__private.operations.virtual.escrow_approved_operation import (
    EscrowApprovedOperationHF26,
    EscrowApprovedOperationLegacy,
)
from schemas.__private.operations.virtual.escrow_rejected_operation import (
    EscrowRejectedOperationHF26,
    EscrowRejectedOperationLegacy,
)
from schemas.__private.operations.virtual.expired_account_notification_operation import (
    ExpiredAccountNotificationOperation,
)
from schemas.__private.operations.virtual.failed_recurrent_transfer_operation import (
    FailedRecurrentTransferOperationHF26,
    FailedRecurrentTransferOperationLegacy,
)
from schemas.__private.operations.virtual.fill_collateralized_convert_request_operation import (
    FillCollateralizedConvertRequestOperationHF26,
    FillCollateralizedConvertRequestOperationLegacy,
)
from schemas.__private.operations.virtual.fill_convert_request_operation import (
    FillConvertRequestOperationHF26,
    FillConvertRequestOperationLegacy,
)
from schemas.__private.operations.virtual.fill_order_operation import FillOrderOperationHF26, FillOrderOperationLegacy
from schemas.__private.operations.virtual.fill_recurrent_transfer_operation import (
    FillRecurrentTransferOperationHF26,
    FillRecurrentTransferOperationLegacy,
)
from schemas.__private.operations.virtual.fill_transfer_from_savings_operation import (
    FillTransferFromSavingsOperationHF26,
    FillTransferFromSavingsOperationLegacy,
)
from schemas.__private.operations.virtual.fill_vesting_withdraw_operation import (
    FillVestingWithdrawOperationHF26,
    FillVestingWithdrawOperationLegacy,
)
from schemas.__private.operations.virtual.hardfork_hive_operation import (
    HardforkHiveOperationHF26,
    HardforkHiveOperationLegacy,
)
from schemas.__private.operations.virtual.hardfork_hive_restore_operation import (
    HardforkHiveRestoreOperationHF26,
    HardforkHiveRestoreOperationLegacy,
)
from schemas.__private.operations.virtual.hardfork_operation import HardforkOperation
from schemas.__private.operations.virtual.ineffective_delete_comment_operation import IneffectiveDeleteCommentOperation
from schemas.__private.operations.virtual.interest_operation import InterestOperationHF26, InterestOperationLegacy
from schemas.__private.operations.virtual.limit_order_cancelled_operation import (
    LimitOrderCancelledOperationHF26,
    LimitOrderCancelledOperationLegacy,
)
from schemas.__private.operations.virtual.liquidity_reward_operation import (
    LiquidityRewardOperationHF26,
    LiquidityRewardOperationLegacy,
)
from schemas.__private.operations.virtual.pow_reward_operation import PowRewardOperationHF26, PowRewardOperationLegacy
from schemas.__private.operations.virtual.producer_missed_operation import ProducerMissedOperation
from schemas.__private.operations.virtual.producer_reward_operation import (
    ProducerRewardOperationHF26,
    ProducerRewardOperationLegacy,
)
from schemas.__private.operations.virtual.proposal_fee_operation import (
    ProposalFeeOperationHF26,
    ProposalFeeOperationLegacy,
)
from schemas.__private.operations.virtual.proposal_pay_operation import (
    ProposalPayOperationHF26,
    ProposalPayOperationLegacy,
)
from schemas.__private.operations.virtual.proxy_cleared_operation import ProxyClearedOperation
from schemas.__private.operations.virtual.return_vesting_delegation_operation import (
    ReturnVestingDelegationOperationHF26,
    ReturnVestingDelegationOperationLegacy,
)
from schemas.__private.operations.virtual.shutdown_witness_operation import ShutDownWitnessOperation
from schemas.__private.operations.virtual.system_warning_operation import SystemWarningOperation
from schemas.__private.operations.virtual.transfer_to_vesting_completed_operation import (
    TransferToVestingCompletedOperationHF26,
    TransferToVestingCompletedOperationLegacy,
)
from schemas.__private.operations.virtual.vesting_shares_split_operation import (
    VestingSharesSplitOperationHF26,
    VestingSharesSplitOperationLegacy,
)

AnyHF26VirtualOperation = (
    AuthorRewardOperationHF26
    | AccountCreatedOperationHF26
    | ChangedRecoveryAccountOperation
    | ClearNullAccountBalanceOperationHF26
    | CollateralizedConvertImmediateConversionOperationHF26
    | CommentBenefactorRewardOperationHF26
    | CommentPayoutUpdateOperation
    | CommentRewardOperationHF26
    | ConsolidateTreasuryBalanceOperationHF26
    | CurationRewardOperationHF26
    | DeclinedVotingRightsOperation
    | DelayedVotingOperation
    | DhfConversionOperationHF26
    | DhfFundingOperationHF26
    | EffectiveCommentVoteOperationHF26
    | EscrowApprovedOperationHF26
    | EscrowRejectedOperationHF26
    | ExpiredAccountNotificationOperation
    | FailedRecurrentTransferOperationHF26
    | FillCollateralizedConvertRequestOperationHF26
    | FillConvertRequestOperationHF26
    | FillOrderOperationHF26
    | FillRecurrentTransferOperationHF26
    | FillTransferFromSavingsOperationHF26
    | FillVestingWithdrawOperationHF26
    | HardforkHiveOperationHF26
    | HardforkHiveRestoreOperationHF26
    | HardforkOperation
    | IneffectiveDeleteCommentOperation
    | InterestOperationHF26
    | LimitOrderCancelledOperationHF26
    | LiquidityRewardOperationHF26
    | PowRewardOperationHF26
    | ProducerMissedOperation
    | ProducerRewardOperationHF26
    | ProposalFeeOperationHF26
    | ProposalPayOperationHF26
    | ProxyClearedOperation
    | ReturnVestingDelegationOperationHF26
    | ShutDownWitnessOperation
    | SystemWarningOperation
    | TransferToVestingCompletedOperationHF26
    | VestingSharesSplitOperationHF26
)

AnyLegacyVirtualOperation = (
    AuthorRewardOperationLegacy
    | AccountCreatedOperationLegacy
    | ChangedRecoveryAccountOperation
    | ClearNullAccountBalanceOperationLegacy
    | CollateralizedConvertImmediateConversionOperationLegacy
    | CommentBenefactorRewardOperationLegacy
    | CommentPayoutUpdateOperation
    | CommentRewardOperationLegacy
    | ConsolidateTreasuryBalanceOperationLegacy
    | CurationRewardOperationLegacy
    | DeclinedVotingRightsOperation
    | DelayedVotingOperation
    | DhfConversionOperationLegacy
    | DhfFundingOperationLegacy
    | EffectiveCommentVoteOperationLegacy
    | EscrowApprovedOperationLegacy
    | EscrowRejectedOperationLegacy
    | ExpiredAccountNotificationOperation
    | FailedRecurrentTransferOperationLegacy
    | FillCollateralizedConvertRequestOperationLegacy
    | FillConvertRequestOperationLegacy
    | FillOrderOperationLegacy
    | FillRecurrentTransferOperationLegacy
    | FillTransferFromSavingsOperationLegacy
    | FillVestingWithdrawOperationLegacy
    | HardforkHiveOperationLegacy
    | HardforkHiveRestoreOperationLegacy
    | HardforkOperation
    | IneffectiveDeleteCommentOperation
    | InterestOperationLegacy
    | LimitOrderCancelledOperationLegacy
    | LiquidityRewardOperationLegacy
    | PowRewardOperationLegacy
    | ProducerMissedOperation
    | ProducerRewardOperationLegacy
    | ProposalFeeOperationLegacy
    | ProposalPayOperationLegacy
    | ProxyClearedOperation
    | ReturnVestingDelegationOperationLegacy
    | ShutDownWitnessOperation
    | SystemWarningOperation
    | TransferToVestingCompletedOperationLegacy
    | VestingSharesSplitOperationLegacy
)

__all__ = [
    # ANY VIRTUAL OPERATION
    "AnyHF26VirtualOperation",
    "AnyLegacyVirtualOperation",
    # VIRTUAL OPERATIONS
    "AccountCreatedOperationHF26",
    "AuthorRewardOperationHF26",
    "ChangedRecoveryAccountOperation",
    "ClearNullAccountBalanceOperationHF26",
    "CollateralizedConvertImmediateConversionOperationHF26",
    "CommentBenefactorRewardOperationHF26",
    "CommentPayoutUpdateOperation",
    "CommentRewardOperationHF26",
    "ConsolidateTreasuryBalanceOperationHF26",
    "CurationRewardOperationHF26",
    "DeclinedVotingRightsOperation",
    "DelayedVotingOperation",
    "DhfConversionOperationHF26",
    "DhfFundingOperationHF26",
    "EffectiveCommentVoteOperationHF26",
    "EscrowApprovedOperationHF26",
    "EscrowRejectedOperationHF26",
    "ExpiredAccountNotificationOperation",
    "FailedRecurrentTransferOperationHF26",
    "FillCollateralizedConvertRequestOperationHF26",
    "FillConvertRequestOperationHF26",
    "FillOrderOperationHF26",
    "FillRecurrentTransferOperationHF26",
    "FillTransferFromSavingsOperationHF26",
    "FillVestingWithdrawOperationHF26",
    "HardforkHiveOperationHF26",
    "HardforkHiveRestoreOperationHF26",
    "HardforkOperation",
    "IneffectiveDeleteCommentOperation",
    "InterestOperationHF26",
    "LimitOrderCancelledOperationHF26",
    "LiquidityRewardOperationHF26",
    "PowRewardOperationHF26",
    "ProducerMissedOperation",
    "ProducerRewardOperationHF26",
    "ProposalFeeOperationHF26",
    "ProposalPayOperationHF26",
    "ProxyClearedOperation",
    "ReturnVestingDelegationOperationHF26",
    "ShutDownWitnessOperation",
    "SystemWarningOperation",
    "TransferToVestingCompletedOperationHF26",
    "VestingSharesSplitOperationHF26",
    # LEGACY VIRTUAL OPERATIONS
    "AccountCreatedOperationLegacy",
    "AuthorRewardOperationLegacy",
    "ClearNullAccountBalanceOperationLegacy",
    "CollateralizedConvertImmediateConversionOperationLegacy",
    "CommentBenefactorRewardOperationLegacy",
    "CommentRewardOperationLegacy",
    "ConsolidateTreasuryBalanceOperationLegacy",
    "CurationRewardOperationLegacy",
    "DhfConversionOperationLegacy",
    "DhfFundingOperationLegacy",
    "EffectiveCommentVoteOperationLegacy",
    "EscrowApprovedOperationLegacy",
    "EscrowRejectedOperationLegacy",
    "FailedRecurrentTransferOperationLegacy",
    "FillCollateralizedConvertRequestOperationLegacy",
    "FillConvertRequestOperationLegacy",
    "FillOrderOperationLegacy",
    "FillRecurrentTransferOperationLegacy",
    "FillTransferFromSavingsOperationLegacy",
    "FillVestingWithdrawOperationLegacy",
    "HardforkHiveOperationLegacy",
    "HardforkHiveRestoreOperationLegacy",
    "InterestOperationLegacy",
    "LimitOrderCancelledOperationLegacy",
    "LiquidityRewardOperationLegacy",
    "PowRewardOperationLegacy",
    "ProducerRewardOperationLegacy",
    "ProposalFeeOperationLegacy",
    "ProposalPayOperationLegacy",
    "ReturnVestingDelegationOperationLegacy",
    "TransferToVestingCompletedOperationLegacy",
    "VestingSharesSplitOperationLegacy",
]
