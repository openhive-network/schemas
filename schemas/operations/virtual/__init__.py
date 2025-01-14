from __future__ import annotations

from schemas.operations.virtual.representation_types import HF26RepresentationAuthorRewardOperation
from schemas.operations.virtual.representation_types import HF26RepresentationAccountCreatedOperation
from schemas.operations.virtual.representation_types import HF26RepresentationChangedRecoveryAccountOperation
from schemas.operations.virtual.representation_types import HF26RepresentationClearNullAccountBalanceOperation
from schemas.operations.virtual.representation_types import HF26RepresentationCollateralizedConvertImmediateConversionOperation
from schemas.operations.virtual.representation_types import HF26RepresentationCommentBenefactorRewardOperation
from schemas.operations.virtual.representation_types import HF26RepresentationCommentPayoutUpdateOperation
from schemas.operations.virtual.representation_types import HF26RepresentationCommentRewardOperation
from schemas.operations.virtual.representation_types import HF26RepresentationConsolidateTreasuryBalanceOperation
from schemas.operations.virtual.representation_types import HF26RepresentationCurationRewardOperation
from schemas.operations.virtual.representation_types import HF26RepresentationDeclinedVotingRightsOperation
from schemas.operations.virtual.representation_types import HF26RepresentationDelayedVotingOperation
from schemas.operations.virtual.representation_types import HF26RepresentationDhfConversionOperation
from schemas.operations.virtual.representation_types import HF26RepresentationDhfFundingOperation
from schemas.operations.virtual.representation_types import HF26RepresentationEffectiveCommentVoteOperation
from schemas.operations.virtual.representation_types import HF26RepresentationEscrowApprovedOperation
from schemas.operations.virtual.representation_types import HF26RepresentationEscrowRejectedOperation
from schemas.operations.virtual.representation_types import HF26RepresentationExpiredAccountNotificationOperation
from schemas.operations.virtual.representation_types import HF26RepresentationFailedRecurrentTransferOperation
from schemas.operations.virtual.representation_types import HF26RepresentationFillCollateralizedConvertRequestOperation
from schemas.operations.virtual.representation_types import HF26RepresentationFillConvertRequestOperation
from schemas.operations.virtual.representation_types import HF26RepresentationFillOrderOperation
from schemas.operations.virtual.representation_types import HF26RepresentationFillRecurrentTransferOperation
from schemas.operations.virtual.representation_types import HF26RepresentationFillTransferFromSavingsOperation
from schemas.operations.virtual.representation_types import HF26RepresentationFillVestingWithdrawOperation
from schemas.operations.virtual.representation_types import HF26RepresentationHardforkHiveOperation
from schemas.operations.virtual.representation_types import HF26RepresentationHardforkHiveRestoreOperation
from schemas.operations.virtual.representation_types import HF26RepresentationHardforkOperation
from schemas.operations.virtual.representation_types import HF26RepresentationIneffectiveDeleteCommentOperation
from schemas.operations.virtual.representation_types import HF26RepresentationInterestOperation
from schemas.operations.virtual.representation_types import HF26RepresentationLimitOrderCancelledOperation
from schemas.operations.virtual.representation_types import HF26RepresentationLiquidityRewardOperation
from schemas.operations.virtual.representation_types import HF26RepresentationPowRewardOperation
from schemas.operations.virtual.representation_types import HF26RepresentationProducerMissedOperation
from schemas.operations.virtual.representation_types import HF26RepresentationProducerRewardOperation
from schemas.operations.virtual.representation_types import HF26RepresentationProposalFeeOperation
from schemas.operations.virtual.representation_types import HF26RepresentationProposalPayOperation
from schemas.operations.virtual.representation_types import HF26RepresentationProxyClearedOperation
from schemas.operations.virtual.representation_types import HF26RepresentationReturnVestingDelegationOperation
from schemas.operations.virtual.representation_types import HF26RepresentationShutDownWitnessOperation
from schemas.operations.virtual.representation_types import HF26RepresentationSystemWarningOperation
from schemas.operations.virtual.representation_types import HF26RepresentationTransferToVestingCompletedOperation
from schemas.operations.virtual.representation_types import HF26RepresentationVestingSharesSplitOperation

from schemas.operations.virtual.representation_types import LegacyRepresentationAuthorRewardOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationAccountCreatedOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationChangedRecoveryAccountOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationClearNullAccountBalanceOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationCollateralizedConvertImmediateConversionOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationCommentBenefactorRewardOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationCommentPayoutUpdateOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationCommentRewardOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationConsolidateTreasuryBalanceOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationCurationRewardOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationDeclinedVotingRightsOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationDelayedVotingOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationDhfConversionOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationDhfFundingOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationEffectiveCommentVoteOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationEscrowApprovedOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationEscrowRejectedOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationExpiredAccountNotificationOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationFailedRecurrentTransferOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationFillCollateralizedConvertRequestOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationFillConvertRequestOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationFillOrderOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationFillRecurrentTransferOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationFillTransferFromSavingsOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationFillVestingWithdrawOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationHardforkHiveOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationHardforkHiveRestoreOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationHardforkOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationIneffectiveDeleteCommentOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationInterestOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationLimitOrderCancelledOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationLiquidityRewardOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationPowRewardOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationProducerMissedOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationProducerRewardOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationProposalFeeOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationProposalPayOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationProxyClearedOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationReturnVestingDelegationOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationShutDownWitnessOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationSystemWarningOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationTransferToVestingCompletedOperation
from schemas.operations.virtual.representation_types import LegacyRepresentationVestingSharesSplitOperation



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

AnyVirtualOperationRepresentation = (
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

AnyLegacyVirtualOperationRepresentation = (
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
