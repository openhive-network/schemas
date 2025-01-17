from __future__ import annotations

from schemas.operations.virtual import AnyVirtualOperationRepresentation, AnyLegacyVirtualOperationRepresentation
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

from schemas.operations.virtual.account_created_operation import (
    AccountCreatedOperation,
    AccountCreatedOperationLegacy,
)
from schemas.operations.virtual.author_reward_operation import (
    AuthorRewardOperation,
    AuthorRewardOperationLegacy,
)
from schemas.operations.virtual.changed_recovery_account_operation import ChangedRecoveryAccountOperation
from schemas.operations.virtual.clear_null_account_balance_operation import (
    ClearNullAccountBalanceOperation,
    ClearNullAccountBalanceOperationLegacy,
)
from schemas.operations.virtual.collateralized_convert_immediate_conversion_operation import (
    CollateralizedConvertImmediateConversionOperation,
    CollateralizedConvertImmediateConversionOperationLegacy,
)
from schemas.operations.virtual.comment_benefactor_reward_operation import (
    CommentBenefactorRewardOperation,
    CommentBenefactorRewardOperationLegacy,
)
from schemas.operations.virtual.comment_payout_update_operation import CommentPayoutUpdateOperation
from schemas.operations.virtual.comment_reward_operation import (
    CommentRewardOperation,
    CommentRewardOperationLegacy,
)
from schemas.operations.virtual.consolidate_treasury_balance_operation import (
    ConsolidateTreasuryBalanceOperation,
    ConsolidateTreasuryBalanceOperationLegacy,
)
from schemas.operations.virtual.curation_reward_operation import (
    CurationRewardOperation,
    CurationRewardOperationLegacy,
)
from schemas.operations.virtual.declined_voting_rights_operation import DeclinedVotingRightsOperation
from schemas.operations.virtual.delayed_voting_operation import DelayedVotingOperation
from schemas.operations.virtual.dhf_conversion_operation import (
    DhfConversionOperation,
    DhfConversionOperationLegacy,
)
from schemas.operations.virtual.dhf_funding_operation import (
    DhfFundingOperation,
    DhfFundingOperationLegacy,
)
from schemas.operations.virtual.effective_comment_vote_operation import (
    EffectiveCommentVoteOperation,
    EffectiveCommentVoteOperationLegacy,
)
from schemas.operations.virtual.escrow_approved_operation import (
    EscrowApprovedOperation,
    EscrowApprovedOperationLegacy,
)
from schemas.operations.virtual.escrow_rejected_operation import (
    EscrowRejectedOperation,
    EscrowRejectedOperationLegacy,
)
from schemas.operations.virtual.expired_account_notification_operation import (
    ExpiredAccountNotificationOperation,
)
from schemas.operations.virtual.failed_recurrent_transfer_operation import (
    FailedRecurrentTransferOperation,
    FailedRecurrentTransferOperationLegacy,
)
from schemas.operations.virtual.fill_collateralized_convert_request_operation import (
    FillCollateralizedConvertRequestOperation,
    FillCollateralizedConvertRequestOperationLegacy,
)
from schemas.operations.virtual.fill_convert_request_operation import (
    FillConvertRequestOperation,
    FillConvertRequestOperationLegacy,
)
from schemas.operations.virtual.fill_order_operation import FillOrderOperation, FillOrderOperationLegacy
from schemas.operations.virtual.fill_recurrent_transfer_operation import (
    FillRecurrentTransferOperation,
    FillRecurrentTransferOperationLegacy,
)
from schemas.operations.virtual.fill_transfer_from_savings_operation import (
    FillTransferFromSavingsOperation,
    FillTransferFromSavingsOperationLegacy,
)
from schemas.operations.virtual.fill_vesting_withdraw_operation import (
    FillVestingWithdrawOperation,
    FillVestingWithdrawOperationLegacy,
)
from schemas.operations.virtual.hardfork_hive_operation import (
    HardforkHiveOperation,
    HardforkHiveOperationLegacy,
)
from schemas.operations.virtual.hardfork_hive_restore_operation import (
    HardforkHiveRestoreOperation,
    HardforkHiveRestoreOperationLegacy,
)
from schemas.operations.virtual.hardfork_operation import HardforkOperation
from schemas.operations.virtual.ineffective_delete_comment_operation import IneffectiveDeleteCommentOperation
from schemas.operations.virtual.interest_operation import InterestOperation, InterestOperationLegacy
from schemas.operations.virtual.limit_order_cancelled_operation import (
    LimitOrderCancelledOperation,
    LimitOrderCancelledOperationLegacy,
)
from schemas.operations.virtual.liquidity_reward_operation import (
    LiquidityRewardOperation,
    LiquidityRewardOperationLegacy,
)
from schemas.operations.virtual.pow_reward_operation import PowRewardOperation, PowRewardOperationLegacy
from schemas.operations.virtual.producer_missed_operation import ProducerMissedOperation
from schemas.operations.virtual.producer_reward_operation import (
    ProducerRewardOperation,
    ProducerRewardOperationLegacy,
)
from schemas.operations.virtual.proposal_fee_operation import (
    ProposalFeeOperation,
    ProposalFeeOperationLegacy,
)
from schemas.operations.virtual.proposal_pay_operation import (
    ProposalPayOperation,
    ProposalPayOperationLegacy,
)
from schemas.operations.virtual.proxy_cleared_operation import ProxyClearedOperation
from schemas.operations.virtual.return_vesting_delegation_operation import (
    ReturnVestingDelegationOperation,
    ReturnVestingDelegationOperationLegacy,
)
from schemas.operations.virtual.shutdown_witness_operation import ShutDownWitnessOperation
from schemas.operations.virtual.system_warning_operation import SystemWarningOperation
from schemas.operations.virtual.transfer_to_vesting_completed_operation import (
    TransferToVestingCompletedOperation,
    TransferToVestingCompletedOperationLegacy,
)
from schemas.operations.virtual.vesting_shares_split_operation import (
    VestingSharesSplitOperation,
    VestingSharesSplitOperationLegacy,
)

from schemas.operations.account_create_operation import (
    AccountCreateOperation,
    AccountCreateOperationLegacy,
)
from schemas.operations.account_create_with_delegation_operation import (
    AccountCreateWithDelegationOperation,
    AccountCreateWithDelegationOperationLegacy,
)
from schemas.operations.account_update2_operation import AccountUpdate2Operation
from schemas.operations.account_update_operation import AccountUpdateOperation
from schemas.operations.account_witness_proxy_operation import AccountWitnessProxyOperation
from schemas.operations.account_witness_vote_operation import AccountWitnessVoteOperation
from schemas.operations.cancel_transfer_from_savings_operation import CancelTransferFromSavingsOperation
from schemas.operations.change_recovery_account_operation import ChangeRecoveryAccountOperation
from schemas.operations.claim_account_operation import ClaimAccountOperation, ClaimAccountOperationLegacy
from schemas.operations.claim_reward_balance_operation import (
    ClaimRewardBalanceOperation,
    ClaimRewardBalanceOperationLegacy,
)
from schemas.operations.collateralized_convert_operation import (
    CollateralizedConvertOperation,
    CollateralizedConvertOperationLegacy,
)
from schemas.operations.comment_operation import CommentOperation
from schemas.operations.comment_options_operation import (
    CommentOptionsOperation,
    CommentOptionsOperationLegacy,
)
from schemas.operations.convert_operation import ConvertOperation, ConvertOperationLegacy
from schemas.operations.create_claimed_account_operation import CreateClaimedAccountOperation
from schemas.operations.create_proposal_operation import (
    CreateProposalOperation,
    CreateProposalOperationLegacy,
)
from schemas.operations.custom_binary_operation import CustomBinaryOperation
from schemas.operations.custom_json_operation import CustomJsonOperation, CustomJsonOperationGeneric
from schemas.operations.custom_operation import CustomOperation
from schemas.operations.decline_voting_rights_operation import DeclineVotingRightsOperation
from schemas.operations.delegate_vesting_shares_operation import (
    DelegateVestingSharesOperation,
    DelegateVestingSharesOperationLegacy,
)
from schemas.operations.delete_comment_operation import DeleteCommentOperation
from schemas.operations.escrow_approve_operation import EscrowApproveOperation
from schemas.operations.escrow_dispute_operation import EscrowDisputeOperation
from schemas.operations.escrow_release_operation import (
    EscrowReleaseOperation,
    EscrowReleaseOperationLegacy,
)
from schemas.operations.escrow_transfer_operation import (
    EscrowTransferOperation,
    EscrowTransferOperationLegacy,
)
from schemas.operations.feed_publish_operation import FeedPublishOperation
from schemas.operations.limit_order_cancel_operation import LimitOrderCancelOperation
from schemas.operations.limit_order_create2_operation import (
    LimitOrderCreate2Operation,
    LimitOrderCreate2OperationLegacy,
)
from schemas.operations.limit_order_create_operation import (
    LimitOrderCreateOperation,
    LimitOrderCreateOperationLegacy,
)
from schemas.operations.pow2_operation import Pow2Operation, Pow2OperationLegacy
from schemas.operations.pow_operation import PowOperation, PowOperationLegacy
from schemas.operations.recover_account_operation import RecoverAccountOperation
from schemas.operations.recurrent_transfer_operation import (
    RecurrentTransferOperation,
    RecurrentTransferOperationLegacy,
)
from schemas.operations.remove_proposal_operation import RemoveProposalOperation
from schemas.operations.request_account_recovery_operation import RequestAccountRecoveryOperation
from schemas.operations.reset_account_operation import ResetAccountOperation
from schemas.operations.set_reset_account_operation import SetResetAccountOperation
from schemas.operations.set_withdraw_vesting_route_operation import SetWithdrawVestingRouteOperation
from schemas.operations.transfer_from_savings_operation import (
    TransferFromSavingsOperation,
    TransferFromSavingsOperationLegacy,
)
from schemas.operations.transfer_operation import TransferOperation, TransferOperationLegacy
from schemas.operations.transfer_to_savings_operation import (
    TransferToSavingsOperation,
    TransferToSavingsOperationLegacy,
)
from schemas.operations.transfer_to_vesting_operation import (
    TransferToVestingOperation,
    TransferToVestingOperationLegacy,
)
from schemas.operations.update_proposal_operation import (
    UpdateProposalOperation,
    UpdateProposalOperationLegacy,
)
from schemas.operations.update_proposal_votes_operation import UpdateProposalVotesOperation

from schemas.operations.vote_operation import VoteOperation
from schemas.operations.withdraw_vesting_operation import (
    WithdrawVestingOperation,
    WithdrawVestingOperationLegacy,
)
from schemas.operations.witness_block_approve_operation import WitnessBlockApproveOperation
from schemas.operations.witness_set_properties_operation import WitnessSetPropertiesOperation
from schemas.operations.witness_update_operation import (
    WitnessUpdateOperation,
    WitnessUpdateOperationLegacy,
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


AnyEveryOperation = AnyOperationRepresentation | AnyVirtualOperationRepresentation
AnyLegacyEveryOperation = AnyLegacyOperationRepresentation | AnyLegacyVirtualOperationRepresentation
