from __future__ import annotations

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
from schemas.operations.virtual.representation_types import HF26RepresentationAuthorRewardOperation, LegacyRepresentationAuthorRewardOperationLegacy
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
#     | AccountCreatedOperation
#     | ChangedRecoveryAccountOperation
#     | ClearNullAccountBalanceOperation
#     | CollateralizedConvertImmediateConversionOperation
#     | CommentBenefactorRewardOperation
#     | CommentPayoutUpdateOperation
#     | CommentRewardOperation
#     | ConsolidateTreasuryBalanceOperation
#     | CurationRewardOperation
#     | DeclinedVotingRightsOperation
#     | DelayedVotingOperation
#     | DhfConversionOperation
#     | DhfFundingOperation
#     | EffectiveCommentVoteOperation
#     | EscrowApprovedOperation
#     | EscrowRejectedOperation
#     | ExpiredAccountNotificationOperation
#     | FailedRecurrentTransferOperation
#     | FillCollateralizedConvertRequestOperation
#     | FillConvertRequestOperation
#     | FillOrderOperation
#     | FillRecurrentTransferOperation
#     | FillTransferFromSavingsOperation
#     | FillVestingWithdrawOperation
#     | HardforkHiveOperation
#     | HardforkHiveRestoreOperation
#     | HardforkOperation
#     | IneffectiveDeleteCommentOperation
#     | InterestOperation
#     | LimitOrderCancelledOperation
#     | LiquidityRewardOperation
#     | PowRewardOperation
#     | ProducerMissedOperation
#     | ProducerRewardOperation
#     | ProposalFeeOperation
#     | ProposalPayOperation
#     | ProxyClearedOperation
#     | ReturnVestingDelegationOperation
#     | ShutDownWitnessOperation
#     | SystemWarningOperation
#     | TransferToVestingCompletedOperation
#     | VestingSharesSplitOperation
)

AnyLegacyVirtualOperationRepresentation = (
    LegacyRepresentationAuthorRewardOperationLegacy
#     | AccountCreatedOperationLegacy
#     | ChangedRecoveryAccountOperation
#     | ClearNullAccountBalanceOperationLegacy
#     | CollateralizedConvertImmediateConversionOperationLegacy
#     | CommentBenefactorRewardOperationLegacy
#     | CommentPayoutUpdateOperation
#     | CommentRewardOperationLegacy
#     | ConsolidateTreasuryBalanceOperationLegacy
#     | CurationRewardOperationLegacy
#     | DeclinedVotingRightsOperation
#     | DelayedVotingOperation
#     | DhfConversionOperationLegacy
#     | DhfFundingOperationLegacy
#     | EffectiveCommentVoteOperationLegacy
#     | EscrowApprovedOperationLegacy
#     | EscrowRejectedOperationLegacy
#     | ExpiredAccountNotificationOperation
#     | FailedRecurrentTransferOperationLegacy
#     | FillCollateralizedConvertRequestOperationLegacy
#     | FillConvertRequestOperationLegacy
#     | FillOrderOperationLegacy
#     | FillRecurrentTransferOperationLegacy
#     | FillTransferFromSavingsOperationLegacy
#     | FillVestingWithdrawOperationLegacy
#     | HardforkHiveOperationLegacy
#     | HardforkHiveRestoreOperationLegacy
#     | HardforkOperation
#     | IneffectiveDeleteCommentOperation
#     | InterestOperationLegacy
#     | LimitOrderCancelledOperationLegacy
#     | LiquidityRewardOperationLegacy
#     | PowRewardOperationLegacy
#     | ProducerMissedOperation
#     | ProducerRewardOperationLegacy
#     | ProposalFeeOperationLegacy
#     | ProposalPayOperationLegacy
#     | ProxyClearedOperation
#     | ReturnVestingDelegationOperationLegacy
#     | ShutDownWitnessOperation
#     | SystemWarningOperation
#     | TransferToVestingCompletedOperationLegacy
#     | VestingSharesSplitOperationLegacy
)
