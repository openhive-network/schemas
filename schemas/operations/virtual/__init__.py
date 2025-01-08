from __future__ import annotations

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
