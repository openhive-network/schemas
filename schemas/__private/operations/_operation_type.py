from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AssetHbd, AssetHive, AssetVests
from schemas.__private.operations.account_create_operation import AccountCreateOperation
from schemas.__private.operations.account_update2_operation import AccountUpdate2Operation
from schemas.__private.operations.account_update_operation import AccountUpdateOperation
from schemas.__private.operations.account_witness_proxy_operation import AccountWitnessProxyOperation
from schemas.__private.operations.account_witness_vote_operation import AccountWitnessVoteOperation
from schemas.__private.operations.cancel_transfer_from_savings_operation import CancelTransferFromSavingsOperation
from schemas.__private.operations.change_recovery_account_operation import ChangeRecoveryAccountOperation
from schemas.__private.operations.claim_account_operation import ClaimAccountOperation
from schemas.__private.operations.claim_reward_balance_operation import ClaimRewardBalanceOperation
from schemas.__private.operations.collateralized_convert_operation import CollateralizedConvertOperation
from schemas.__private.operations.comment_operation import CommentOperation
from schemas.__private.operations.comment_options_operation import CommentOptionsOperation
from schemas.__private.operations.convert_operation import ConvertOperation
from schemas.__private.operations.create_claimed_account_operation import CreateClaimedAccountOperation
from schemas.__private.operations.create_proposal_operation import CreateProposalOperation
from schemas.__private.operations.custom_binary_operation import CustomBinaryOperation
from schemas.__private.operations.custom_json_operation import CustomJsonOperation
from schemas.__private.operations.custom_operation import CustomOperation
from schemas.__private.operations.decline_voting_rights_operation import DeclineVotingRightsOperation
from schemas.__private.operations.delegate_vesting_shares_operation import DelegateVestingSharesOperation
from schemas.__private.operations.delete_comment_operation import DeleteCommentOperation
from schemas.__private.operations.escrow_approve_operation import EscrowApproveOperation
from schemas.__private.operations.escrow_dispute_operation import EscrowDisputeOperation
from schemas.__private.operations.escrow_release_operation import EscrowReleaseOperation
from schemas.__private.operations.escrow_transfer_operation import EscrowTransferOperation
from schemas.__private.operations.feed_publish_operation import FeedPublishOperation
from schemas.__private.operations.limit_order_cancel_operation import LimitOrderCancelOperation
from schemas.__private.operations.limit_order_create2_operation import LimitOrderCreate2Operation
from schemas.__private.operations.limit_order_create_operation import LimitOrderCreateOperation
from schemas.__private.operations.pow_operation import PowOperation
from schemas.__private.operations.recover_account_operation import RecoverAccountOperation
from schemas.__private.operations.recurrent_transfer_operation import RecurrentTransferOperation
from schemas.__private.operations.remove_proposal_operation import RemoveProposalOperation
from schemas.__private.operations.request_account_recovery_operation import RequestAccountRecoveryOperation
from schemas.__private.operations.reset_account_operation import ResetAccountOperation
from schemas.__private.operations.set_reset_account_operation import SetResetAccountOperation
from schemas.__private.operations.set_withdraw_vesting_route_operation import SetWithdrawVestingRouteOperation
from schemas.__private.operations.transfer_from_savings_operation import TransferFromSavingsOperation
from schemas.__private.operations.transfer_operation import TransferOperation
from schemas.__private.operations.transfer_to_savings_operation import TransferToSavingsOperation
from schemas.__private.operations.transfer_to_vesting_operation import TransferToVestingOperation
from schemas.__private.operations.update_proposal_operation import UpdateProposalOperation
from schemas.__private.operations.update_proposal_votes_operation import UpdateProposalVotesOperation
from schemas.__private.operations.vote_operation import VoteOperation
from schemas.__private.operations.withdraw_vesting_operation import WithdrawVestingOperation
from schemas.__private.operations.witness_block_approve_operation import WitnessBlockApproveOperation
from schemas.__private.operations.witness_set_properties_operation import WitnessSetPropertiesOperation
from schemas.__private.operations.witness_update_operation import WitnessUpdateOperation

OperationType = (
    AccountCreateOperation[AssetHive]
    | AccountUpdate2Operation
    | AccountUpdateOperation
    | AccountWitnessProxyOperation
    | AccountWitnessVoteOperation
    | CancelTransferFromSavingsOperation
    | ChangeRecoveryAccountOperation
    | ClaimAccountOperation[AssetHive]
    | ClaimRewardBalanceOperation[AssetHive, AssetHbd, AssetVests]
    | CollateralizedConvertOperation[AssetHive]
    | CommentOperation
    | CommentOptionsOperation[AssetHbd]
    | ConvertOperation[AssetHbd]
    | CreateClaimedAccountOperation
    | CreateProposalOperation[AssetHbd]
    | CustomBinaryOperation
    | CustomJsonOperation
    | PowOperation
    | CustomOperation
    | DeclineVotingRightsOperation
    | DelegateVestingSharesOperation[AssetVests]
    | DeleteCommentOperation
    | EscrowApproveOperation
    | EscrowDisputeOperation
    | EscrowReleaseOperation[AssetHive, AssetHbd]
    | EscrowTransferOperation[AssetHive, AssetHbd]
    | FeedPublishOperation
    | LimitOrderCancelOperation
    | LimitOrderCreate2Operation[AssetHbd, AssetHive]
    | LimitOrderCreateOperation[AssetHive, AssetHbd]
    | RecoverAccountOperation
    | RecurrentTransferOperation[AssetHive, AssetHbd]
    | RemoveProposalOperation
    | RequestAccountRecoveryOperation
    | ResetAccountOperation
    | SetResetAccountOperation
    | SetWithdrawVestingRouteOperation
    | TransferFromSavingsOperation[AssetHive, AssetHbd]
    | TransferOperation[AssetHive, AssetHbd]
    | TransferToSavingsOperation[AssetHive, AssetHbd]
    | TransferToVestingOperation[AssetHive]
    | UpdateProposalOperation[AssetHbd]
    | UpdateProposalVotesOperation
    | VoteOperation
    | WithdrawVestingOperation[AssetVests]
    | WitnessBlockApproveOperation
    | WitnessSetPropertiesOperation
    | WitnessUpdateOperation[AssetHive]
)

__all__ = ["OperationType"]
