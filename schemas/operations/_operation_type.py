from __future__ import annotations

from schemas.hive_fields_basic_schemas import AssetHbd, AssetHive, AssetVests
from schemas.operations.account_create_operation import AccountCreateOperation
from schemas.operations.account_update2_operation import AccountUpdate2Operation
from schemas.operations.account_update_operation import AccountUpdateOperation
from schemas.operations.account_witness_proxy_operation import AccountWitnessProxyOperation
from schemas.operations.account_witness_vote_operation import AccountWitnessVoteOperation
from schemas.operations.cancel_transfer_from_savings_operation import CancelTransferFromSavingsOperation
from schemas.operations.change_recovery_account_operation import ChangeRecoveryAccountOperation
from schemas.operations.claim_account_operation import ClaimAccountOperation
from schemas.operations.claim_reward_balance_operation import ClaimRewardBalanceOperation
from schemas.operations.collateralized_convert_operation import CollateralizedConvertOperation
from schemas.operations.comment_operation import CommentOperation
from schemas.operations.comment_options_operation import CommentOptionsOperation
from schemas.operations.convert_operation import ConvertOperation
from schemas.operations.create_claimed_account_operation import CreateClaimedAccountOperation
from schemas.operations.create_proposal_operation import CreateProposalOperation
from schemas.operations.custom_binary_operation import CustomBinaryOperation
from schemas.operations.custom_json_operation import CustomJsonOperation
from schemas.operations.custom_operation import CustomOperation
from schemas.operations.decline_voting_rights_operation import DeclineVotingRightsOperation
from schemas.operations.delegate_vesting_shares_operation import DelegateVestingSharesOperation
from schemas.operations.delete_comment_operation import DeleteCommentOperation
from schemas.operations.escrow_approve_operation import EscrowApproveOperation
from schemas.operations.escrow_dispute_operation import EscrowDisputeOperation
from schemas.operations.escrow_release_operation import EscrowReleaseOperation
from schemas.operations.escrow_transfer_operation import EscrowTransferOperation
from schemas.operations.feed_publish_operation import FeedPublishOperation
from schemas.operations.limit_order_cancel_operation import LimitOrderCancelOperation
from schemas.operations.limit_order_create2_operation import LimitOrderCreate2Operation
from schemas.operations.limit_order_create_operation import LimitOrderCreateOperation
from schemas.operations.pow_operation import PowOperation
from schemas.operations.recover_account_operation import RecoverAccountOperation
from schemas.operations.recurrent_transfer_operation import RecurrentTransferOperation
from schemas.operations.remove_proposal_operation import RemoveProposalOperation
from schemas.operations.request_account_recovery_operation import RequestAccountRecoveryOperation
from schemas.operations.reset_account_operation import ResetAccountOperation
from schemas.operations.set_reset_account_operation import SetResetAccountOperation
from schemas.operations.set_withdraw_vesting_route_operation import SetWithdrawVestingRouteOperation
from schemas.operations.transfer_from_savings_operation import TransferFromSavingsOperation
from schemas.operations.transfer_operation import TransferOperation
from schemas.operations.transfer_to_savings_operation import TransferToSavingsOperation
from schemas.operations.transfer_to_vesting_operation import TransferToVestingOperation
from schemas.operations.update_proposal_operation import UpdateProposalOperation
from schemas.operations.update_proposal_votes_operation import UpdateProposalVotesOperation
from schemas.operations.vote_operation import VoteOperation
from schemas.operations.withdraw_vesting_operation import WithdrawVestingOperation
from schemas.operations.witness_block_approve_operation import WitnessBlockApproveOperation
from schemas.operations.witness_set_properties_operation import WitnessSetPropertiesOperation
from schemas.operations.witness_update_operation import WitnessUpdateOperation

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
