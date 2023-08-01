from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import (
    AssetHbd,
    AssetHive,
    AssetVests,
)
from schemas.__private.operations.virtual.account_created_operation import AccountCreatedOperation
from schemas.__private.operations.virtual.author_reward_operation import AuthorRewardOperation
from schemas.__private.operations.virtual.changed_recovery_account_operation import ChangedRecoveryAccountOperation
from schemas.__private.operations.virtual.clear_null_account_balance_operation import ClearNullAccountBalanceOperation
from schemas.__private.operations.virtual.collateralized_convert_immediate_conversion_operation import (
    CollateralizedConvertImmediateConversionOperation,
)
from schemas.__private.operations.virtual.comment_benefactor_reward_operation import CommentBenefactorRewardOperation
from schemas.__private.operations.virtual.comment_payout_update_operation import CommentPayoutUpdateOperation
from schemas.__private.operations.virtual.comment_reward_operation import CommentRewardOperation
from schemas.__private.operations.virtual.consolidate_treasury_balance_operation import (
    ConsolidateTreasuryBalanceOperation,
)
from schemas.__private.operations.virtual.curation_reward_operation import CurationRewardOperation
from schemas.__private.operations.virtual.declined_voting_rights_operation import DeclinedVotingRightsOperation
from schemas.__private.operations.virtual.delayed_voting_operation import DelayedVotingOperation
from schemas.__private.operations.virtual.dhf_conversion_operation import DhfConversionOperation
from schemas.__private.operations.virtual.dhf_funding_operation import DhfFundingOperation
from schemas.__private.operations.virtual.effective_comment_vote_operation import (
    LegacyEffectiveCommentVoteOperation,
    NaiEffectiveCommentVoteOperation,
)
from schemas.__private.operations.virtual.escrow_approved_operation import EscrowApprovedOperation
from schemas.__private.operations.virtual.escrow_rejected_operation import EscrowRejectedOperation
from schemas.__private.operations.virtual.expired_account_notification_operation import (
    ExpiredAccountNotificationOperation,
)
from schemas.__private.operations.virtual.failed_recurrent_transfer_operation import FailedRecurrentTransferOperation
from schemas.__private.operations.virtual.fill_collateralized_convert_request_operation import (
    FillCollateralizedConvertRequestOperation,
)
from schemas.__private.operations.virtual.fill_convert_request_operation import FillConvertRequestOperation
from schemas.__private.operations.virtual.fill_order_operation import FillOrderOperation
from schemas.__private.operations.virtual.fill_recurrent_transfer_operation import FillRecurrentTransferOperation
from schemas.__private.operations.virtual.fill_transfer_from_savings_operation import FillTransferFromSavingsOperation
from schemas.__private.operations.virtual.fill_vesting_withdraw_operation import FillVestingWithdrawOperation
from schemas.__private.operations.virtual.hardfork_hive_operation import HardforkHiveOperation
from schemas.__private.operations.virtual.hardfork_hive_restore_operation import HardforkHiveRestoreOperation
from schemas.__private.operations.virtual.hardfork_operation import HardforkOperation
from schemas.__private.operations.virtual.ineffective_delete_comment_operation import IneffectiveDeleteCommentOperation
from schemas.__private.operations.virtual.interest_operation import InterestOperation
from schemas.__private.operations.virtual.limit_order_cancelled_operation import LimitOrderCancelledOperation
from schemas.__private.operations.virtual.liquidity_reward_operation import LiquidityRewardOperation
from schemas.__private.operations.virtual.pow_reward_operation import PowRewardOperation
from schemas.__private.operations.virtual.producer_missed_operation import ProducerMissedOperation
from schemas.__private.operations.virtual.producer_reward_operation import ProducerRewardOperation
from schemas.__private.operations.virtual.proposal_fee_operation import ProposalFeeOperation
from schemas.__private.operations.virtual.proposal_pay_operation import ProposalPayOperation
from schemas.__private.operations.virtual.proxy_cleared_operation import ProxyClearedOperation
from schemas.__private.operations.virtual.return_vesting_delegation_operation import ReturnVestingDelegationOperation
from schemas.__private.operations.virtual.shutdown_witness_operation import ShutDownWitnessOperation
from schemas.__private.operations.virtual.system_warning_operation import SystemWarningOperation
from schemas.__private.operations.virtual.transfer_to_vesting_completed_operation import (
    TransferToVestingCompletedOperation,
)
from schemas.__private.operations.virtual.vesting_shares_split_operation import VestingSharesSplitOperation

VirtualOperationType = (
    AuthorRewardOperation[AssetHive, AssetHbd, AssetVests]
    | AccountCreatedOperation[AssetVests]
    | ChangedRecoveryAccountOperation
    | ClearNullAccountBalanceOperation[AssetHive, AssetHbd, AssetVests]
    | CollateralizedConvertImmediateConversionOperation[AssetHbd]
    | CommentBenefactorRewardOperation[AssetHive, AssetHbd, AssetVests]
    | CommentPayoutUpdateOperation
    | CommentRewardOperation[AssetHbd]
    | ConsolidateTreasuryBalanceOperation[AssetHive, AssetHbd, AssetVests]
    | CurationRewardOperation[AssetVests]
    | DeclinedVotingRightsOperation
    | DelayedVotingOperation
    | DhfConversionOperation[AssetHive, AssetHbd]
    | DhfFundingOperation[AssetHbd]
    | EscrowApprovedOperation[AssetHive, AssetHbd]
    | EscrowRejectedOperation[AssetHive, AssetHbd]
    | ExpiredAccountNotificationOperation
    | FailedRecurrentTransferOperation[AssetHive, AssetHbd]
    | FillCollateralizedConvertRequestOperation[AssetHive, AssetHbd]
    | FillConvertRequestOperation[AssetHive, AssetHbd]
    | FillOrderOperation[AssetHive, AssetHbd]
    | FillRecurrentTransferOperation[AssetHive, AssetHbd]
    | FillTransferFromSavingsOperation[AssetHive, AssetHbd]
    | FillVestingWithdrawOperation[AssetHive, AssetVests]
    | HardforkHiveOperation[AssetHive, AssetHbd, AssetVests]
    | HardforkHiveRestoreOperation[AssetHive, AssetHbd]
    | HardforkOperation
    | IneffectiveDeleteCommentOperation
    | InterestOperation[AssetHbd]
    | LimitOrderCancelledOperation[AssetHive, AssetHbd]
    | LiquidityRewardOperation[AssetHive]
    | PowRewardOperation[AssetHive, AssetVests]
    | ProducerMissedOperation
    | ProducerRewardOperation[AssetHive, AssetVests]
    | ProposalFeeOperation[AssetHbd]
    | ProposalPayOperation[AssetHbd]
    | ProxyClearedOperation
    | ReturnVestingDelegationOperation[AssetVests]
    | ShutDownWitnessOperation
    | SystemWarningOperation
    | TransferToVestingCompletedOperation[AssetHive, AssetVests]
    | VestingSharesSplitOperation[AssetVests]
)

__all__ = [
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
    "LegacyEffectiveCommentVoteOperation",
    "NaiEffectiveCommentVoteOperation",
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
]
