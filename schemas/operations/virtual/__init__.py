from __future__ import annotations

from schemas.operations.virtual.account_created_operation import AccountCreatedOperation
from schemas.operations.virtual.author_reward_operation import AuthorRewardOperation
from schemas.operations.virtual.changed_recovery_account_operation import ChangedRecoveryAccountOperation
from schemas.operations.virtual.clear_null_account_balance_operation import ClearNullAccountBalanceOperation
from schemas.operations.virtual.collateralized_convert_immediate_conversion_operation import (
    CollateralizedConvertImmediateConversionOperation,
)
from schemas.operations.virtual.comment_benefactor_reward_operation import CommentBenefactorRewardOperation
from schemas.operations.virtual.comment_payout_update_operation import CommentPayoutUpdateOperation
from schemas.operations.virtual.comment_reward_operation import CommentRewardOperation
from schemas.operations.virtual.consolidate_treasury_balance_operation import ConsolidateTreasuryBalanceOperation
from schemas.operations.virtual.curation_reward_operation import CurationRewardOperation
from schemas.operations.virtual.declined_voting_rights_operation import DeclinedVotingRightsOperation
from schemas.operations.virtual.delayed_voting_operation import DelayedVotingOperation
from schemas.operations.virtual.dhf_conversion_operation import DhfConversionOperation
from schemas.operations.virtual.dhf_funding_operation import DhfFundingOperation
from schemas.operations.virtual.effective_comment_vote_operation import EffectiveCommentVoteOperation
from schemas.operations.virtual.escrow_approved_operation import EscrowApprovedOperation
from schemas.operations.virtual.escrow_rejected_operation import EscrowRejectedOperation
from schemas.operations.virtual.expired_account_notification_operation import ExpiredAccountNotificationOperation
from schemas.operations.virtual.failed_recurrent_transfer_operation import FailedRecurrentTransferOperation
from schemas.operations.virtual.fill_collateralized_convert_request_operation import (
    FillCollateralizedConvertRequestOperation,
)
from schemas.operations.virtual.fill_convert_request_operation import FillConvertRequestOperation
from schemas.operations.virtual.fill_order_operation import FillOrderOperation
from schemas.operations.virtual.fill_recurrent_transfer_operation import FillRecurrentTransferOperation
from schemas.operations.virtual.fill_transfer_from_savings_operation import FillTransferFromSavingsOperation
from schemas.operations.virtual.fill_vesting_withdraw_operation import FillVestingWithdrawOperation
from schemas.operations.virtual.hardfork_hive_operation import HardforkHiveOperation
from schemas.operations.virtual.hardfork_hive_restore_operation import HardforkHiveRestoreOperation
from schemas.operations.virtual.hardfork_operation import HardforkOperation
from schemas.operations.virtual.ineffective_delete_comment_operation import IneffectiveDeleteCommentOperation
from schemas.operations.virtual.interest_operation import InterestOperation
from schemas.operations.virtual.limit_order_cancelled_operation import LimitOrderCancelledOperation
from schemas.operations.virtual.liquidity_reward_operation import LiquidityRewardOperation
from schemas.operations.virtual.pow_reward_operation import PowRewardOperation
from schemas.operations.virtual.producer_missed_operation import ProducerMissedOperation
from schemas.operations.virtual.producer_reward_operation import ProducerRewardOperation
from schemas.operations.virtual.proposal_fee_operation import ProposalFeeOperation
from schemas.operations.virtual.proposal_pay_operation import ProposalPayOperation
from schemas.operations.virtual.proxy_cleared_operation import ProxyClearedOperation
from schemas.operations.virtual.representation_types import (
    HF26RepresentationAccountCreatedOperation,
    HF26RepresentationAuthorRewardOperation,
    HF26RepresentationChangedRecoveryAccountOperation,
    HF26RepresentationClearNullAccountBalanceOperation,
    HF26RepresentationCollateralizedConvertImmediateConversionOperation,
    HF26RepresentationCommentBenefactorRewardOperation,
    HF26RepresentationCommentPayoutUpdateOperation,
    HF26RepresentationCommentRewardOperation,
    HF26RepresentationConsolidateTreasuryBalanceOperation,
    HF26RepresentationCurationRewardOperation,
    HF26RepresentationDeclinedVotingRightsOperation,
    HF26RepresentationDelayedVotingOperation,
    HF26RepresentationDhfConversionOperation,
    HF26RepresentationDhfFundingOperation,
    HF26RepresentationEffectiveCommentVoteOperation,
    HF26RepresentationEscrowApprovedOperation,
    HF26RepresentationEscrowRejectedOperation,
    HF26RepresentationExpiredAccountNotificationOperation,
    HF26RepresentationFailedRecurrentTransferOperation,
    HF26RepresentationFillCollateralizedConvertRequestOperation,
    HF26RepresentationFillConvertRequestOperation,
    HF26RepresentationFillOrderOperation,
    HF26RepresentationFillRecurrentTransferOperation,
    HF26RepresentationFillTransferFromSavingsOperation,
    HF26RepresentationFillVestingWithdrawOperation,
    HF26RepresentationHardforkHiveOperation,
    HF26RepresentationHardforkHiveRestoreOperation,
    HF26RepresentationHardforkOperation,
    HF26RepresentationIneffectiveDeleteCommentOperation,
    HF26RepresentationInterestOperation,
    HF26RepresentationLimitOrderCancelledOperation,
    HF26RepresentationLiquidityRewardOperation,
    HF26RepresentationPowRewardOperation,
    HF26RepresentationProducerMissedOperation,
    HF26RepresentationProducerRewardOperation,
    HF26RepresentationProposalFeeOperation,
    HF26RepresentationProposalPayOperation,
    HF26RepresentationProxyClearedOperation,
    HF26RepresentationReturnVestingDelegationOperation,
    HF26RepresentationShutDownWitnessOperation,
    HF26RepresentationSystemWarningOperation,
    HF26RepresentationTransferToVestingCompletedOperation,
    HF26RepresentationVestingSharesSplitOperation,
    LegacyRepresentationAccountCreatedOperation,
    LegacyRepresentationAuthorRewardOperation,
    LegacyRepresentationChangedRecoveryAccountOperation,
    LegacyRepresentationClearNullAccountBalanceOperation,
    LegacyRepresentationCollateralizedConvertImmediateConversionOperation,
    LegacyRepresentationCommentBenefactorRewardOperation,
    LegacyRepresentationCommentPayoutUpdateOperation,
    LegacyRepresentationCommentRewardOperation,
    LegacyRepresentationConsolidateTreasuryBalanceOperation,
    LegacyRepresentationCurationRewardOperation,
    LegacyRepresentationDeclinedVotingRightsOperation,
    LegacyRepresentationDelayedVotingOperation,
    LegacyRepresentationDhfConversionOperation,
    LegacyRepresentationDhfFundingOperation,
    LegacyRepresentationEffectiveCommentVoteOperation,
    LegacyRepresentationEscrowApprovedOperation,
    LegacyRepresentationEscrowRejectedOperation,
    LegacyRepresentationExpiredAccountNotificationOperation,
    LegacyRepresentationFailedRecurrentTransferOperation,
    LegacyRepresentationFillCollateralizedConvertRequestOperation,
    LegacyRepresentationFillConvertRequestOperation,
    LegacyRepresentationFillOrderOperation,
    LegacyRepresentationFillRecurrentTransferOperation,
    LegacyRepresentationFillTransferFromSavingsOperation,
    LegacyRepresentationFillVestingWithdrawOperation,
    LegacyRepresentationHardforkHiveOperation,
    LegacyRepresentationHardforkHiveRestoreOperation,
    LegacyRepresentationHardforkOperation,
    LegacyRepresentationIneffectiveDeleteCommentOperation,
    LegacyRepresentationInterestOperation,
    LegacyRepresentationLimitOrderCancelledOperation,
    LegacyRepresentationLiquidityRewardOperation,
    LegacyRepresentationPowRewardOperation,
    LegacyRepresentationProducerMissedOperation,
    LegacyRepresentationProducerRewardOperation,
    LegacyRepresentationProposalFeeOperation,
    LegacyRepresentationProposalPayOperation,
    LegacyRepresentationProxyClearedOperation,
    LegacyRepresentationReturnVestingDelegationOperation,
    LegacyRepresentationShutDownWitnessOperation,
    LegacyRepresentationSystemWarningOperation,
    LegacyRepresentationTransferToVestingCompletedOperation,
    LegacyRepresentationVestingSharesSplitOperation,
)
from schemas.operations.virtual.return_vesting_delegation_operation import ReturnVestingDelegationOperation
from schemas.operations.virtual.shutdown_witness_operation import ShutDownWitnessOperation
from schemas.operations.virtual.system_warning_operation import SystemWarningOperation
from schemas.operations.virtual.transfer_to_vesting_completed_operation import TransferToVestingCompletedOperation
from schemas.operations.virtual.vesting_shares_split_operation import VestingSharesSplitOperation

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

Hf26VirtualOperationRepresentation = (
    HF26RepresentationAuthorRewardOperation
    | HF26RepresentationAccountCreatedOperation
    | HF26RepresentationChangedRecoveryAccountOperation
    | HF26RepresentationClearNullAccountBalanceOperation
    | HF26RepresentationCollateralizedConvertImmediateConversionOperation
    | HF26RepresentationCommentBenefactorRewardOperation
    | HF26RepresentationCommentPayoutUpdateOperation
    | HF26RepresentationCommentRewardOperation
    | HF26RepresentationConsolidateTreasuryBalanceOperation
    | HF26RepresentationCurationRewardOperation
    | HF26RepresentationDeclinedVotingRightsOperation
    | HF26RepresentationDelayedVotingOperation
    | HF26RepresentationDhfConversionOperation
    | HF26RepresentationDhfFundingOperation
    | HF26RepresentationEffectiveCommentVoteOperation
    | HF26RepresentationEscrowApprovedOperation
    | HF26RepresentationEscrowRejectedOperation
    | HF26RepresentationExpiredAccountNotificationOperation
    | HF26RepresentationFailedRecurrentTransferOperation
    | HF26RepresentationFillCollateralizedConvertRequestOperation
    | HF26RepresentationFillConvertRequestOperation
    | HF26RepresentationFillOrderOperation
    | HF26RepresentationFillRecurrentTransferOperation
    | HF26RepresentationFillTransferFromSavingsOperation
    | HF26RepresentationFillVestingWithdrawOperation
    | HF26RepresentationHardforkHiveOperation
    | HF26RepresentationHardforkHiveRestoreOperation
    | HF26RepresentationHardforkOperation
    | HF26RepresentationIneffectiveDeleteCommentOperation
    | HF26RepresentationInterestOperation
    | HF26RepresentationLimitOrderCancelledOperation
    | HF26RepresentationLiquidityRewardOperation
    | HF26RepresentationPowRewardOperation
    | HF26RepresentationProducerMissedOperation
    | HF26RepresentationProducerRewardOperation
    | HF26RepresentationProposalFeeOperation
    | HF26RepresentationProposalPayOperation
    | HF26RepresentationProxyClearedOperation
    | HF26RepresentationReturnVestingDelegationOperation
    | HF26RepresentationShutDownWitnessOperation
    | HF26RepresentationSystemWarningOperation
    | HF26RepresentationTransferToVestingCompletedOperation
    | HF26RepresentationVestingSharesSplitOperation
)

LegacyVirtualOperationRepresentation = (
    LegacyRepresentationAuthorRewardOperation
    | LegacyRepresentationAccountCreatedOperation
    | LegacyRepresentationChangedRecoveryAccountOperation
    | LegacyRepresentationClearNullAccountBalanceOperation
    | LegacyRepresentationCollateralizedConvertImmediateConversionOperation
    | LegacyRepresentationCommentBenefactorRewardOperation
    | LegacyRepresentationCommentPayoutUpdateOperation
    | LegacyRepresentationCommentRewardOperation
    | LegacyRepresentationConsolidateTreasuryBalanceOperation
    | LegacyRepresentationCurationRewardOperation
    | LegacyRepresentationDeclinedVotingRightsOperation
    | LegacyRepresentationDelayedVotingOperation
    | LegacyRepresentationDhfConversionOperation
    | LegacyRepresentationDhfFundingOperation
    | LegacyRepresentationEffectiveCommentVoteOperation
    | LegacyRepresentationEscrowApprovedOperation
    | LegacyRepresentationEscrowRejectedOperation
    | LegacyRepresentationExpiredAccountNotificationOperation
    | LegacyRepresentationFailedRecurrentTransferOperation
    | LegacyRepresentationFillCollateralizedConvertRequestOperation
    | LegacyRepresentationFillConvertRequestOperation
    | LegacyRepresentationFillOrderOperation
    | LegacyRepresentationFillRecurrentTransferOperation
    | LegacyRepresentationFillTransferFromSavingsOperation
    | LegacyRepresentationFillVestingWithdrawOperation
    | LegacyRepresentationHardforkHiveOperation
    | LegacyRepresentationHardforkHiveRestoreOperation
    | LegacyRepresentationHardforkOperation
    | LegacyRepresentationIneffectiveDeleteCommentOperation
    | LegacyRepresentationInterestOperation
    | LegacyRepresentationLimitOrderCancelledOperation
    | LegacyRepresentationLiquidityRewardOperation
    | LegacyRepresentationPowRewardOperation
    | LegacyRepresentationProducerMissedOperation
    | LegacyRepresentationProducerRewardOperation
    | LegacyRepresentationProposalFeeOperation
    | LegacyRepresentationProposalPayOperation
    | LegacyRepresentationProxyClearedOperation
    | LegacyRepresentationReturnVestingDelegationOperation
    | LegacyRepresentationShutDownWitnessOperation
    | LegacyRepresentationSystemWarningOperation
    | LegacyRepresentationTransferToVestingCompletedOperation
    | LegacyRepresentationVestingSharesSplitOperation
)


HF26RepresentationAndValuePairsVirtual = {
    AuthorRewardOperation: HF26RepresentationAuthorRewardOperation,
    AccountCreatedOperation: HF26RepresentationAccountCreatedOperation,
    ChangedRecoveryAccountOperation: HF26RepresentationChangedRecoveryAccountOperation,
    ClearNullAccountBalanceOperation: HF26RepresentationClearNullAccountBalanceOperation,
    CollateralizedConvertImmediateConversionOperation: HF26RepresentationCollateralizedConvertImmediateConversionOperation,
    CommentBenefactorRewardOperation: HF26RepresentationCommentBenefactorRewardOperation,
    CommentPayoutUpdateOperation: HF26RepresentationCommentPayoutUpdateOperation,
    CommentRewardOperation: HF26RepresentationCommentRewardOperation,
    ConsolidateTreasuryBalanceOperation: HF26RepresentationConsolidateTreasuryBalanceOperation,
    CurationRewardOperation: HF26RepresentationCurationRewardOperation,
    DeclinedVotingRightsOperation: HF26RepresentationDeclinedVotingRightsOperation,
    DelayedVotingOperation: HF26RepresentationDelayedVotingOperation,
    DhfConversionOperation: HF26RepresentationDhfConversionOperation,
    DhfFundingOperation: HF26RepresentationDhfFundingOperation,
    EffectiveCommentVoteOperation: HF26RepresentationEffectiveCommentVoteOperation,
    EscrowApprovedOperation: HF26RepresentationEscrowApprovedOperation,
    EscrowRejectedOperation: HF26RepresentationEscrowRejectedOperation,
    ExpiredAccountNotificationOperation: HF26RepresentationExpiredAccountNotificationOperation,
    FailedRecurrentTransferOperation: HF26RepresentationFailedRecurrentTransferOperation,
    FillCollateralizedConvertRequestOperation: HF26RepresentationFillCollateralizedConvertRequestOperation,
    FillConvertRequestOperation: HF26RepresentationFillConvertRequestOperation,
    FillOrderOperation: HF26RepresentationFillOrderOperation,
    FillRecurrentTransferOperation: HF26RepresentationFillRecurrentTransferOperation,
    FillTransferFromSavingsOperation: HF26RepresentationFillTransferFromSavingsOperation,
    FillVestingWithdrawOperation: HF26RepresentationFillVestingWithdrawOperation,
    HardforkHiveOperation: HF26RepresentationHardforkHiveOperation,
    HardforkHiveRestoreOperation: HF26RepresentationHardforkHiveRestoreOperation,
    HardforkOperation: HF26RepresentationHardforkOperation,
    IneffectiveDeleteCommentOperation: HF26RepresentationIneffectiveDeleteCommentOperation,
    InterestOperation: HF26RepresentationInterestOperation,
    LimitOrderCancelledOperation: HF26RepresentationLimitOrderCancelledOperation,
    LiquidityRewardOperation: HF26RepresentationLiquidityRewardOperation,
    PowRewardOperation: HF26RepresentationPowRewardOperation,
    ProducerMissedOperation: HF26RepresentationProducerMissedOperation,
    ProducerRewardOperation: HF26RepresentationProducerRewardOperation,
    ProposalFeeOperation: HF26RepresentationProposalFeeOperation,
    ProposalPayOperation: HF26RepresentationProposalPayOperation,
    ProxyClearedOperation: HF26RepresentationProxyClearedOperation,
    ReturnVestingDelegationOperation: HF26RepresentationReturnVestingDelegationOperation,
    ShutDownWitnessOperation: HF26RepresentationShutDownWitnessOperation,
    SystemWarningOperation: HF26RepresentationSystemWarningOperation,
    TransferToVestingCompletedOperation: HF26RepresentationTransferToVestingCompletedOperation,
    VestingSharesSplitOperation: HF26RepresentationVestingSharesSplitOperation,
}


LegacyRepresentationAndValuePairsVirtual = {
    AuthorRewardOperation: LegacyRepresentationAuthorRewardOperation,
    AccountCreatedOperation: LegacyRepresentationAccountCreatedOperation,
    ChangedRecoveryAccountOperation: LegacyRepresentationChangedRecoveryAccountOperation,
    ClearNullAccountBalanceOperation: LegacyRepresentationClearNullAccountBalanceOperation,
    CollateralizedConvertImmediateConversionOperation: LegacyRepresentationCollateralizedConvertImmediateConversionOperation,
    CommentBenefactorRewardOperation: LegacyRepresentationCommentBenefactorRewardOperation,
    CommentPayoutUpdateOperation: LegacyRepresentationCommentPayoutUpdateOperation,
    CommentRewardOperation: LegacyRepresentationCommentRewardOperation,
    ConsolidateTreasuryBalanceOperation: LegacyRepresentationConsolidateTreasuryBalanceOperation,
    CurationRewardOperation: LegacyRepresentationCurationRewardOperation,
    DeclinedVotingRightsOperation: LegacyRepresentationDeclinedVotingRightsOperation,
    DelayedVotingOperation: LegacyRepresentationDelayedVotingOperation,
    DhfConversionOperation: LegacyRepresentationDhfConversionOperation,
    DhfFundingOperation: LegacyRepresentationDhfFundingOperation,
    EffectiveCommentVoteOperation: LegacyRepresentationEffectiveCommentVoteOperation,
    EscrowApprovedOperation: LegacyRepresentationEscrowApprovedOperation,
    EscrowRejectedOperation: LegacyRepresentationEscrowRejectedOperation,
    ExpiredAccountNotificationOperation: LegacyRepresentationExpiredAccountNotificationOperation,
    FailedRecurrentTransferOperation: LegacyRepresentationFailedRecurrentTransferOperation,
    FillCollateralizedConvertRequestOperation: LegacyRepresentationFillCollateralizedConvertRequestOperation,
    FillConvertRequestOperation: LegacyRepresentationFillConvertRequestOperation,
    FillOrderOperation: LegacyRepresentationFillOrderOperation,
    FillRecurrentTransferOperation: LegacyRepresentationFillRecurrentTransferOperation,
    FillTransferFromSavingsOperation: LegacyRepresentationFillTransferFromSavingsOperation,
    FillVestingWithdrawOperation: LegacyRepresentationFillVestingWithdrawOperation,
    HardforkHiveOperation: LegacyRepresentationHardforkHiveOperation,
    HardforkHiveRestoreOperation: LegacyRepresentationHardforkHiveRestoreOperation,
    HardforkOperation: LegacyRepresentationHardforkOperation,
    IneffectiveDeleteCommentOperation: LegacyRepresentationIneffectiveDeleteCommentOperation,
    InterestOperation: LegacyRepresentationInterestOperation,
    LimitOrderCancelledOperation: LegacyRepresentationLimitOrderCancelledOperation,
    LiquidityRewardOperation: LegacyRepresentationLiquidityRewardOperation,
    PowRewardOperation: LegacyRepresentationPowRewardOperation,
    ProducerMissedOperation: LegacyRepresentationProducerMissedOperation,
    ProducerRewardOperation: LegacyRepresentationProducerRewardOperation,
    ProposalFeeOperation: LegacyRepresentationProposalFeeOperation,
    ProposalPayOperation: LegacyRepresentationProposalPayOperation,
    ProxyClearedOperation: LegacyRepresentationProxyClearedOperation,
    ReturnVestingDelegationOperation: LegacyRepresentationReturnVestingDelegationOperation,
    ShutDownWitnessOperation: LegacyRepresentationShutDownWitnessOperation,
    SystemWarningOperation: LegacyRepresentationSystemWarningOperation,
    TransferToVestingCompletedOperation: LegacyRepresentationTransferToVestingCompletedOperation,
    VestingSharesSplitOperation: LegacyRepresentationVestingSharesSplitOperation,
}
