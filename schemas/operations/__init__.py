from __future__ import annotations

# Importy dla HF26Representation
from schemas.operations.representation_types import (
    HF26RepresentationAccountCreateOperation,
    HF26RepresentationAccountCreateWithDelegationOperation,
    HF26RepresentationAccountUpdate2Operation,
    HF26RepresentationAccountUpdateOperation,
    HF26RepresentationAccountWitnessProxyOperation,
    HF26RepresentationAccountWitnessVoteOperation,
    HF26RepresentationCancelTransferFromSavingsOperation,
    HF26RepresentationChangeRecoveryAccountOperation,
    HF26RepresentationClaimAccountOperation,
    HF26RepresentationClaimRewardBalanceOperation,
    HF26RepresentationCollateralizedConvertOperation,
    HF26RepresentationCommentOperation,
    HF26RepresentationCommentOptionsOperation,
    HF26RepresentationConvertOperation,
    HF26RepresentationCreateClaimedAccountOperation,
    HF26RepresentationCreateProposalOperation,
    HF26RepresentationCustomBinaryOperation,
    HF26RepresentationCustomJsonOperation,
    HF26RepresentationCustomOperation,
    HF26RepresentationDeclineVotingRightsOperation,
    HF26RepresentationDelegateVestingSharesOperation,
    HF26RepresentationDeleteCommentOperation,
    HF26RepresentationEscrowApproveOperation,
    HF26RepresentationEscrowDisputeOperation,
    HF26RepresentationEscrowReleaseOperation,
    HF26RepresentationEscrowTransferOperation,
    HF26RepresentationFeedPublishOperation,
    HF26RepresentationLimitOrderCancelOperation,
    HF26RepresentationLimitOrderCreate2Operation,
    HF26RepresentationLimitOrderCreateOperation,
    HF26RepresentationPowOperation,
    HF26RepresentationPow2Operation,
    HF26RepresentationRecoverAccountOperation,
    HF26RepresentationRecurrentTransferOperation,
    HF26RepresentationRemoveProposalOperation,
    HF26RepresentationRequestAccountRecoveryOperation,
    HF26RepresentationResetAccountOperation,
    HF26RepresentationSetResetAccountOperation,
    HF26RepresentationSetWithdrawVestingRouteOperation,
    HF26RepresentationTransferFromSavingsOperation,
    HF26RepresentationTransferOperation,
    HF26RepresentationTransferToSavingsOperation,
    HF26RepresentationTransferToVestingOperation,
    HF26RepresentationUpdateProposalOperation,
    HF26RepresentationUpdateProposalVotesOperation,
    HF26RepresentationVoteOperation,
    HF26RepresentationWithdrawVestingOperation,
    HF26RepresentationWitnessBlockApproveOperation,
    HF26RepresentationWitnessSetPropertiesOperation,
    HF26RepresentationWitnessUpdateOperation,
)

# Importy dla LegacyRepresentation
from schemas.operations.representation_types import (
    LegacyRepresentationAccountCreateOperation,
    LegacyRepresentationAccountUpdate2Operation,
    LegacyRepresentationAccountUpdateOperation,
    LegacyRepresentationAccountWitnessProxyOperation,
    LegacyRepresentationAccountWitnessVoteOperation,
    LegacyRepresentationCancelTransferFromSavingsOperation,
    LegacyRepresentationChangeRecoveryAccountOperation,
    LegacyRepresentationClaimAccountOperation,
    LegacyRepresentationClaimRewardBalanceOperation,
    LegacyRepresentationCollateralizedConvertOperation,
    LegacyRepresentationCommentOperation,
    LegacyRepresentationCommentOptionsOperation,
    LegacyRepresentationConvertOperation,
    LegacyRepresentationCreateClaimedAccountOperation,
    LegacyRepresentationCreateProposalOperation,
    LegacyRepresentationCustomBinaryOperation,
    LegacyRepresentationCustomJsonOperation,
    LegacyRepresentationCustomOperation,
    LegacyRepresentationDeclineVotingRightsOperation,
    LegacyRepresentationDelegateVestingSharesOperation,
    LegacyRepresentationDeleteCommentOperation,
    LegacyRepresentationEscrowApproveOperation,
    LegacyRepresentationEscrowDisputeOperation,
    LegacyRepresentationEscrowReleaseOperation,
    LegacyRepresentationEscrowTransferOperation,
    LegacyRepresentationFeedPublishOperation,
    LegacyRepresentationLimitOrderCancelOperation,
    LegacyRepresentationLimitOrderCreate2Operation,
    LegacyRepresentationLimitOrderCreateOperation,
    LegacyRepresentationPowOperation,
    LegacyRepresentationPow2Operation,
    LegacyRepresentationRecoverAccountOperation,
    LegacyRepresentationRecurrentTransferOperation,
    LegacyRepresentationRemoveProposalOperation,
    LegacyRepresentationRequestAccountRecoveryOperation,
    LegacyRepresentationResetAccountOperation,
    LegacyRepresentationSetResetAccountOperation,
    LegacyRepresentationSetWithdrawVestingRouteOperation,
    LegacyRepresentationTransferFromSavingsOperation,
    LegacyRepresentationTransferOperation,
    LegacyRepresentationTransferToSavingsOperation,
    LegacyRepresentationTransferToVestingOperation,
    LegacyRepresentationUpdateProposalOperation,
    LegacyRepresentationUpdateProposalVotesOperation,
    LegacyRepresentationVoteOperation,
    LegacyRepresentationWithdrawVestingOperation,
    LegacyRepresentationWitnessBlockApproveOperation,
    LegacyRepresentationWitnessSetPropertiesOperation,
    LegacyRepresentationWitnessUpdateOperation,
)

__all__ = [
    # ANY OPERATION
    "AnyOperation",
    "AnyLegacyOperation",
    "AnyEveryOperation",
    "AnyLegacyEveryOperation",
    # OPERATIONS
    "AccountCreateOperation",
    "AccountCreateWithDelegationOperation",
    "AccountUpdate2Operation",
    "AccountUpdateOperation",
    "AccountWitnessProxyOperation",
    "AccountWitnessVoteOperation",
    "CancelTransferFromSavingsOperation",
    "ChangeRecoveryAccountOperation",
    "ClaimAccountOperation",
    "ClaimRewardBalanceOperation",
    "CollateralizedConvertOperation",
    "CommentOperation",
    "CommentOptionsOperation",
    "ConvertOperation",
    "CreateClaimedAccountOperation",
    "CreateProposalOperation",
    "CustomBinaryOperation",
    "CustomJsonOperation",
    "CustomJsonOperationGeneric",
    "CustomOperation",
    "DeclineVotingRightsOperation",
    "DelegateVestingSharesOperation",
    "DeleteCommentOperation",
    "EscrowApproveOperation",
    "EscrowDisputeOperation",
    "EscrowReleaseOperation",
    "EscrowTransferOperation",
    "FeedPublishOperation",
    "LimitOrderCancelOperation",
    "LimitOrderCreate2Operation",
    "LimitOrderCreateOperation",
    "PowOperation",
    "Pow2Operation",
    "RecoverAccountOperation",
    "RecurrentTransferOperation",
    "RemoveProposalOperation",
    "RequestAccountRecoveryOperation",
    "ResetAccountOperation",
    "SetResetAccountOperation",
    "SetWithdrawVestingRouteOperation",
    "TransferFromSavingsOperation",
    "TransferOperation",
    "TransferToSavingsOperation",
    "TransferToVestingOperation",
    "UpdateProposalOperation",
    "UpdateProposalVotesOperation",
    "VoteOperation",
    "WithdrawVestingOperation",
    "WitnessBlockApproveOperation",
    "WitnessSetPropertiesOperation",
    "WitnessUpdateOperation",
    # LEGACY OPERATIONS
    "AccountCreateOperationLegacy",
    "AccountCreateWithDelegationOperationLegacy",
    "ClaimAccountOperationLegacy",
    "ClaimRewardBalanceOperationLegacy",
    "CollateralizedConvertOperationLegacy",
    "CommentOptionsOperationLegacy",
    "ConvertOperationLegacy",
    "CreateProposalOperationLegacy",
    "DelegateVestingSharesOperationLegacy",
    "PowOperationLegacy",
    "Pow2OperationLegacy",
    "EscrowReleaseOperationLegacy",
    "EscrowTransferOperationLegacy",
    "LimitOrderCreate2OperationLegacy",
    "LimitOrderCreateOperationLegacy",
    "RecurrentTransferOperationLegacy",
    "TransferFromSavingsOperationLegacy",
    "TransferOperationLegacy",
    "TransferToSavingsOperationLegacy",
    "TransferToVestingOperationLegacy",
    "UpdateProposalOperationLegacy",
    "WithdrawVestingOperationLegacy",
    "WitnessUpdateOperationLegacy",
]

AnyOperationRepresentation = (
    HF26RepresentationAccountCreateOperation
    | HF26RepresentationAccountCreateWithDelegationOperation
    | HF26RepresentationAccountUpdate2Operation
    | HF26RepresentationAccountUpdateOperation
    | HF26RepresentationAccountWitnessProxyOperation
    | HF26RepresentationAccountWitnessVoteOperation
    | HF26RepresentationCancelTransferFromSavingsOperation
    | HF26RepresentationChangeRecoveryAccountOperation
    | HF26RepresentationClaimAccountOperation
    | HF26RepresentationClaimRewardBalanceOperation
    | HF26RepresentationCollateralizedConvertOperation
    | HF26RepresentationCommentOperation
    | HF26RepresentationCommentOptionsOperation
    | HF26RepresentationConvertOperation
    | HF26RepresentationCreateClaimedAccountOperation
    | HF26RepresentationCreateProposalOperation
    | HF26RepresentationCustomBinaryOperation
    | HF26RepresentationCustomJsonOperation
    | HF26RepresentationCustomOperation
    | HF26RepresentationDeclineVotingRightsOperation
    | HF26RepresentationDelegateVestingSharesOperation
    | HF26RepresentationDeleteCommentOperation
    | HF26RepresentationEscrowApproveOperation
    | HF26RepresentationEscrowDisputeOperation
    | HF26RepresentationEscrowReleaseOperation
    | HF26RepresentationEscrowTransferOperation
    | HF26RepresentationFeedPublishOperation
    | HF26RepresentationLimitOrderCancelOperation
    | HF26RepresentationLimitOrderCreate2Operation
    | HF26RepresentationLimitOrderCreateOperation
    | HF26RepresentationPowOperation
    | HF26RepresentationPow2Operation
    | HF26RepresentationRecoverAccountOperation
    | HF26RepresentationRecurrentTransferOperation
    | HF26RepresentationRemoveProposalOperation
    | HF26RepresentationRequestAccountRecoveryOperation
    | HF26RepresentationResetAccountOperation
    | HF26RepresentationSetResetAccountOperation
    | HF26RepresentationSetWithdrawVestingRouteOperation
    | HF26RepresentationTransferFromSavingsOperation
    | HF26RepresentationTransferOperation
    | HF26RepresentationTransferToSavingsOperation
    | HF26RepresentationTransferToVestingOperation
    | HF26RepresentationUpdateProposalOperation
    | HF26RepresentationUpdateProposalVotesOperation
    | HF26RepresentationVoteOperation
    | HF26RepresentationWithdrawVestingOperation
    | HF26RepresentationWitnessBlockApproveOperation
    | HF26RepresentationWitnessSetPropertiesOperation
    | HF26RepresentationWitnessUpdateOperation
)

AnyLegacyOperationRepresentation = (
    LegacyRepresentationAccountCreateOperation
    | LegacyRepresentationAccountUpdate2Operation
    | LegacyRepresentationAccountUpdateOperation
    | LegacyRepresentationAccountWitnessProxyOperation
    | LegacyRepresentationAccountWitnessVoteOperation
    | LegacyRepresentationCancelTransferFromSavingsOperation
    | LegacyRepresentationChangeRecoveryAccountOperation
    | LegacyRepresentationClaimAccountOperation
    | LegacyRepresentationClaimRewardBalanceOperation
    | LegacyRepresentationCollateralizedConvertOperation
    | LegacyRepresentationCommentOperation
    | LegacyRepresentationCommentOptionsOperation
    | LegacyRepresentationConvertOperation
    | LegacyRepresentationCreateClaimedAccountOperation
    | LegacyRepresentationCreateProposalOperation
    | LegacyRepresentationCustomBinaryOperation
    | LegacyRepresentationCustomJsonOperation
    | LegacyRepresentationCustomOperation
    | LegacyRepresentationDeclineVotingRightsOperation
    | LegacyRepresentationDelegateVestingSharesOperation
    | LegacyRepresentationDeleteCommentOperation
    | LegacyRepresentationEscrowApproveOperation
    | LegacyRepresentationEscrowDisputeOperation
    | LegacyRepresentationEscrowReleaseOperation
    | LegacyRepresentationEscrowTransferOperation
    | LegacyRepresentationFeedPublishOperation
    | LegacyRepresentationLimitOrderCancelOperation
    | LegacyRepresentationLimitOrderCreate2Operation
    | LegacyRepresentationLimitOrderCreateOperation
    | LegacyRepresentationPowOperation
    | LegacyRepresentationPow2Operation
    | LegacyRepresentationRecoverAccountOperation
    | LegacyRepresentationRecurrentTransferOperation
    | LegacyRepresentationRemoveProposalOperation
    | LegacyRepresentationRequestAccountRecoveryOperation
    | LegacyRepresentationResetAccountOperation
    | LegacyRepresentationSetResetAccountOperation
    | LegacyRepresentationSetWithdrawVestingRouteOperation
    | LegacyRepresentationTransferFromSavingsOperation
    | LegacyRepresentationTransferOperation
    | LegacyRepresentationTransferToSavingsOperation
    | LegacyRepresentationTransferToVestingOperation
    | LegacyRepresentationUpdateProposalOperation
    | LegacyRepresentationUpdateProposalVotesOperation
    | LegacyRepresentationVoteOperation
    | LegacyRepresentationWithdrawVestingOperation
    | LegacyRepresentationWitnessBlockApproveOperation
    | LegacyRepresentationWitnessSetPropertiesOperation
    | LegacyRepresentationWitnessUpdateOperation
)


AnyEveryOperation = AnyOperationRepresentation# | AnyVirtualOperationRepresentation
AnyLegacyEveryOperation = AnyLegacyOperationRepresentation# | AnyLegacyVirtualOperationRepresentation
