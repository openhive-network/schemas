from __future__ import annotations

from schemas.__private.operations.virtual.account_created_operation import (
    AccountCreatedOperation,
    AccountCreatedOperationLegacy,
)
from schemas.__private.operations.virtual.author_reward_operation import (
    AuthorRewardOperation,
    AuthorRewardOperationLegacy,
)
from schemas.__private.operations.virtual.changed_recovery_account_operation import ChangedRecoveryAccountOperation
from schemas.__private.operations.virtual.clear_null_account_balance_operation import (
    ClearNullAccountBalanceOperation,
    ClearNullAccountBalanceOperationLegacy,
)
from schemas.__private.operations.virtual.collateralized_convert_immediate_conversion_operation import (
    CollateralizedConvertImmediateConversionOperation,
    CollateralizedConvertImmediateConversionOperationLegacy,
)
from schemas.__private.operations.virtual.comment_benefactor_reward_operation import (
    CommentBenefactorRewardOperation,
    CommentBenefactorRewardOperationLegacy,
)
from schemas.__private.operations.virtual.comment_payout_update_operation import CommentPayoutUpdateOperation
from schemas.__private.operations.virtual.comment_reward_operation import (
    CommentRewardOperation,
    CommentRewardOperationLegacy,
)
from schemas.__private.operations.virtual.consolidate_treasury_balance_operation import (
    ConsolidateTreasuryBalanceOperation,
    ConsolidateTreasuryBalanceOperationLegacy,
)
from schemas.__private.operations.virtual.curation_reward_operation import (
    CurationRewardOperation,
    CurationRewardOperationLegacy,
)
from schemas.__private.operations.virtual.declined_voting_rights_operation import DeclinedVotingRightsOperation
from schemas.__private.operations.virtual.delayed_voting_operation import DelayedVotingOperation
from schemas.__private.operations.virtual.dhf_conversion_operation import (
    DhfConversionOperation,
    DhfConversionOperationLegacy,
)
from schemas.__private.operations.virtual.dhf_funding_operation import (
    DhfFundingOperation,
    DhfFundingOperationLegacy,
)
from schemas.__private.operations.virtual.effective_comment_vote_operation import (
    EffectiveCommentVoteOperation,
    EffectiveCommentVoteOperationLegacy,
)
from schemas.__private.operations.virtual.escrow_approved_operation import (
    EscrowApprovedOperation,
    EscrowApprovedOperationLegacy,
)
from schemas.__private.operations.virtual.escrow_rejected_operation import (
    EscrowRejectedOperation,
    EscrowRejectedOperationLegacy,
)
from schemas.__private.operations.virtual.expired_account_notification_operation import (
    ExpiredAccountNotificationOperation,
)
from schemas.__private.operations.virtual.failed_recurrent_transfer_operation import (
    FailedRecurrentTransferOperation,
    FailedRecurrentTransferOperationLegacy,
)
from schemas.__private.operations.virtual.fill_collateralized_convert_request_operation import (
    FillCollateralizedConvertRequestOperation,
    FillCollateralizedConvertRequestOperationLegacy,
)
from schemas.__private.operations.virtual.fill_convert_request_operation import (
    FillConvertRequestOperation,
    FillConvertRequestOperationLegacy,
)
from schemas.__private.operations.virtual.fill_order_operation import FillOrderOperation, FillOrderOperationLegacy
from schemas.__private.operations.virtual.fill_recurrent_transfer_operation import (
    FillRecurrentTransferOperation,
    FillRecurrentTransferOperationLegacy,
)
from schemas.__private.operations.virtual.fill_transfer_from_savings_operation import (
    FillTransferFromSavingsOperation,
    FillTransferFromSavingsOperationLegacy,
)
from schemas.__private.operations.virtual.fill_vesting_withdraw_operation import (
    FillVestingWithdrawOperation,
    FillVestingWithdrawOperationLegacy,
)
from schemas.__private.operations.virtual.hardfork_hive_operation import (
    HardforkHiveOperation,
    HardforkHiveOperationLegacy,
)
from schemas.__private.operations.virtual.hardfork_hive_restore_operation import (
    HardforkHiveRestoreOperation,
    HardforkHiveRestoreOperationLegacy,
)
from schemas.__private.operations.virtual.hardfork_operation import HardforkOperation
from schemas.__private.operations.virtual.ineffective_delete_comment_operation import IneffectiveDeleteCommentOperation
from schemas.__private.operations.virtual.interest_operation import InterestOperation, InterestOperationLegacy
from schemas.__private.operations.virtual.limit_order_cancelled_operation import (
    LimitOrderCancelledOperation,
    LimitOrderCancelledOperationLegacy,
)
from schemas.__private.operations.virtual.liquidity_reward_operation import (
    LiquidityRewardOperation,
    LiquidityRewardOperationLegacy,
)
from schemas.__private.operations.virtual.pow_reward_operation import PowRewardOperation, PowRewardOperationLegacy
from schemas.__private.operations.virtual.producer_missed_operation import ProducerMissedOperation
from schemas.__private.operations.virtual.producer_reward_operation import (
    ProducerRewardOperation,
    ProducerRewardOperationLegacy,
)
from schemas.__private.operations.virtual.proposal_fee_operation import (
    ProposalFeeOperation,
    ProposalFeeOperationLegacy,
)
from schemas.__private.operations.virtual.proposal_pay_operation import (
    ProposalPayOperation,
    ProposalPayOperationLegacy,
)
from schemas.__private.operations.virtual.proxy_cleared_operation import ProxyClearedOperation
from schemas.__private.operations.virtual.return_vesting_delegation_operation import (
    ReturnVestingDelegationOperation,
    ReturnVestingDelegationOperationLegacy,
)
from schemas.__private.operations.virtual.shutdown_witness_operation import ShutDownWitnessOperation
from schemas.__private.operations.virtual.system_warning_operation import SystemWarningOperation
from schemas.__private.operations.virtual.transfer_to_vesting_completed_operation import (
    TransferToVestingCompletedOperation,
    TransferToVestingCompletedOperationLegacy,
)
from schemas.__private.operations.virtual.vesting_shares_split_operation import (
    VestingSharesSplitOperation,
    VestingSharesSplitOperationLegacy,
)

__all__ = [
    # ANY VIRTUAL OPERATION
    "AnyVirtualOperation",
    "AnyLegacyVirtualOperation",
    # VIRTUAL OPERATIONS
    "AccountCreatedOperation",
    "AuthorRewardOperation",
    "ChangedRecoveryAccountOperation",
    "ClearNullAccountBalanceOperation",
    "CollateralizedConvertImmediateConversionOperation",
    "CommentBenefactorRewardOperation",
    "CommentPayoutUpdateOperation",
    "CommentRewardOperation",
    "ConsolidateTreasuryBalanceOperation",
    "CurationRewardOperation",
    "DeclinedVotingRightsOperation",
    "DelayedVotingOperation",
    "DhfConversionOperation",
    "DhfFundingOperation",
    "EffectiveCommentVoteOperation",
    "EscrowApprovedOperation",
    "EscrowRejectedOperation",
    "ExpiredAccountNotificationOperation",
    "FailedRecurrentTransferOperation",
    "FillCollateralizedConvertRequestOperation",
    "FillConvertRequestOperation",
    "FillOrderOperation",
    "FillRecurrentTransferOperation",
    "FillTransferFromSavingsOperation",
    "FillVestingWithdrawOperation",
    "HardforkHiveOperation",
    "HardforkHiveRestoreOperation",
    "HardforkOperation",
    "IneffectiveDeleteCommentOperation",
    "InterestOperation",
    "LimitOrderCancelledOperation",
    "LiquidityRewardOperation",
    "PowRewardOperation",
    "ProducerMissedOperation",
    "ProducerRewardOperation",
    "ProposalFeeOperation",
    "ProposalPayOperation",
    "ProxyClearedOperation",
    "ReturnVestingDelegationOperation",
    "ShutDownWitnessOperation",
    "SystemWarningOperation",
    "TransferToVestingCompletedOperation",
    "VestingSharesSplitOperation",
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

AnyVirtualOperation = (
    AuthorRewardOperation
    | AccountCreatedOperation
    | ChangedRecoveryAccountOperation
    | ClearNullAccountBalanceOperation
    | CollateralizedConvertImmediateConversionOperation
    | CommentBenefactorRewardOperation
    | CommentPayoutUpdateOperation
    | CommentRewardOperation
    | ConsolidateTreasuryBalanceOperation
    | CurationRewardOperation
    | DeclinedVotingRightsOperation
    | DelayedVotingOperation
    | DhfConversionOperation
    | DhfFundingOperation
    | EffectiveCommentVoteOperation
    | EscrowApprovedOperation
    | EscrowRejectedOperation
    | ExpiredAccountNotificationOperation
    | FailedRecurrentTransferOperation
    | FillCollateralizedConvertRequestOperation
    | FillConvertRequestOperation
    | FillOrderOperation
    | FillRecurrentTransferOperation
    | FillTransferFromSavingsOperation
    | FillVestingWithdrawOperation
    | HardforkHiveOperation
    | HardforkHiveRestoreOperation
    | HardforkOperation
    | IneffectiveDeleteCommentOperation
    | InterestOperation
    | LimitOrderCancelledOperation
    | LiquidityRewardOperation
    | PowRewardOperation
    | ProducerMissedOperation
    | ProducerRewardOperation
    | ProposalFeeOperation
    | ProposalPayOperation
    | ProxyClearedOperation
    | ReturnVestingDelegationOperation
    | ShutDownWitnessOperation
    | SystemWarningOperation
    | TransferToVestingCompletedOperation
    | VestingSharesSplitOperation
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
