from __future__ import annotations

from schemas.__private.operations.virtual import (
    AccountCreatedOperationHF26,
    AnyHF26VirtualOperation,
    AnyLegacyVirtualOperation,
    AuthorRewardOperationHF26,
    ChangedRecoveryAccountOperation,
    ClearNullAccountBalanceOperationHF26,
    CollateralizedConvertImmediateConversionOperationHF26,
    CommentBenefactorRewardOperationHF26,
    CommentPayoutUpdateOperation,
    CommentRewardOperationHF26,
    ConsolidateTreasuryBalanceOperationHF26,
    CurationRewardOperationHF26,
    DeclinedVotingRightsOperation,
    DelayedVotingOperation,
    DhfConversionOperationHF26,
    DhfFundingOperationHF26,
    EffectiveCommentVoteOperationHF26,
    EscrowApprovedOperationHF26,
    EscrowRejectedOperationHF26,
    ExpiredAccountNotificationOperation,
    FailedRecurrentTransferOperationHF26,
    FillCollateralizedConvertRequestOperationHF26,
    FillConvertRequestOperationHF26,
    FillOrderOperationHF26,
    FillRecurrentTransferOperationHF26,
    FillTransferFromSavingsOperationHF26,
    FillVestingWithdrawOperationHF26,
    HardforkHiveOperationHF26,
    HardforkHiveRestoreOperationHF26,
    HardforkOperation,
    IneffectiveDeleteCommentOperation,
    InterestOperationHF26,
    LimitOrderCancelledOperationHF26,
    LiquidityRewardOperationHF26,
    PowRewardOperationHF26,
    ProducerMissedOperation,
    ProducerRewardOperationHF26,
    ProposalFeeOperationHF26,
    ProposalPayOperationHF26,
    ProxyClearedOperation,
    ReturnVestingDelegationOperationHF26,
    ShutDownWitnessOperation,
    SystemWarningOperation,
    TransferToVestingCompletedOperationHF26,
    VestingSharesSplitOperationHF26,
)

__all__ = [
    # ANY OPERATION
    "AnyHF26VirtualOperation",
    "AnyLegacyVirtualOperation",
    # OPERATIONS
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
]
