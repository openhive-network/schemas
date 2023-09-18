from __future__ import annotations

from schemas.__private.operations.account_create_operation import (
    AccountCreateOperation,
    AccountCreateOperationLegacy,
)
from schemas.__private.operations.account_update2_operation import AccountUpdate2Operation
from schemas.__private.operations.account_update_operation import AccountUpdateOperation
from schemas.__private.operations.account_witness_proxy_operation import AccountWitnessProxyOperation
from schemas.__private.operations.account_witness_vote_operation import AccountWitnessVoteOperation
from schemas.__private.operations.cancel_transfer_from_savings_operation import CancelTransferFromSavingsOperation
from schemas.__private.operations.change_recovery_account_operation import ChangeRecoveryAccountOperation
from schemas.__private.operations.claim_account_operation import ClaimAccountOperation, ClaimAccountOperationLegacy
from schemas.__private.operations.claim_reward_balance_operation import (
    ClaimRewardBalanceOperation,
    ClaimRewardBalanceOperationLegacy,
)
from schemas.__private.operations.collateralized_convert_operation import (
    CollateralizedConvertOperation,
    CollateralizedConvertOperationLegacy,
)
from schemas.__private.operations.comment_operation import CommentOperation
from schemas.__private.operations.comment_options_operation import (
    CommentOptionsOperation,
    CommentOptionsOperationLegacy,
)
from schemas.__private.operations.convert_operation import ConvertOperation, ConvertOperationLegacy
from schemas.__private.operations.create_claimed_account_operation import CreateClaimedAccountOperation
from schemas.__private.operations.create_proposal_operation import (
    CreateProposalOperation,
    CreateProposalOperationLegacy,
)
from schemas.__private.operations.custom_binary_operation import CustomBinaryOperation
from schemas.__private.operations.custom_json_operation import CustomJsonOperation
from schemas.__private.operations.custom_operation import CustomOperation
from schemas.__private.operations.decline_voting_rights_operation import DeclineVotingRightsOperation
from schemas.__private.operations.delegate_vesting_shares_operation import (
    DelegateVestingSharesOperation,
    DelegateVestingSharesOperationLegacy,
)
from schemas.__private.operations.delete_comment_operation import DeleteCommentOperation
from schemas.__private.operations.escrow_approve_operation import EscrowApproveOperation
from schemas.__private.operations.escrow_dispute_operation import EscrowDisputeOperation
from schemas.__private.operations.escrow_release_operation import (
    EscrowReleaseOperation,
    EscrowReleaseOperationLegacy,
)
from schemas.__private.operations.escrow_transfer_operation import (
    EscrowTransferOperation,
    EscrowTransferOperationLegacy,
)
from schemas.__private.operations.feed_publish_operation import FeedPublishOperation
from schemas.__private.operations.limit_order_cancel_operation import LimitOrderCancelOperation
from schemas.__private.operations.limit_order_create2_operation import (
    LimitOrderCreate2Operation,
    LimitOrderCreate2OperationLegacy,
)
from schemas.__private.operations.limit_order_create_operation import (
    LimitOrderCreateOperation,
    LimitOrderCreateOperationLegacy,
)
from schemas.__private.operations.pow_operation import PowOperation
from schemas.__private.operations.recover_account_operation import RecoverAccountOperation
from schemas.__private.operations.recurrent_transfer_operation import (
    RecurrentTransferOperation,
    RecurrentTransferOperationLegacy,
)
from schemas.__private.operations.remove_proposal_operation import RemoveProposalOperation
from schemas.__private.operations.request_account_recovery_operation import RequestAccountRecoveryOperation
from schemas.__private.operations.reset_account_operation import ResetAccountOperation
from schemas.__private.operations.set_reset_account_operation import SetResetAccountOperation
from schemas.__private.operations.set_withdraw_vesting_route_operation import SetWithdrawVestingRouteOperation
from schemas.__private.operations.transfer_from_savings_operation import (
    TransferFromSavingsOperation,
    TransferFromSavingsOperationLegacy,
)
from schemas.__private.operations.transfer_operation import TransferOperation, TransferOperationLegacy
from schemas.__private.operations.transfer_to_savings_operation import (
    TransferToSavingsOperation,
    TransferToSavingsOperationLegacy,
)
from schemas.__private.operations.transfer_to_vesting_operation import (
    TransferToVestingOperation,
    TransferToVestingOperationLegacy,
)
from schemas.__private.operations.update_proposal_operation import (
    UpdateProposalOperation,
    UpdateProposalOperationLegacy,
)
from schemas.__private.operations.update_proposal_votes_operation import UpdateProposalVotesOperation
from schemas.__private.operations.virtual import (
    AnyLegacyVirtualOperation,
    AnyVirtualOperation,
)
from schemas.__private.operations.vote_operation import VoteOperation
from schemas.__private.operations.withdraw_vesting_operation import (
    WithdrawVestingOperation,
    WithdrawVestingOperationLegacy,
)
from schemas.__private.operations.witness_block_approve_operation import WitnessBlockApproveOperation
from schemas.__private.operations.witness_set_properties_operation import WitnessSetPropertiesOperation
from schemas.__private.operations.witness_update_operation import (
    WitnessUpdateOperation,
    WitnessUpdateOperationLegacy,
)

AnyOperation = (
    AccountCreateOperation
    | AccountUpdate2Operation
    | AccountUpdateOperation
    | AccountWitnessProxyOperation
    | AccountWitnessVoteOperation
    | CancelTransferFromSavingsOperation
    | ChangeRecoveryAccountOperation
    | ClaimAccountOperation
    | ClaimRewardBalanceOperation
    | CollateralizedConvertOperation
    | CommentOperation
    | CommentOptionsOperation
    | ConvertOperation
    | CreateClaimedAccountOperation
    | CreateProposalOperation
    | CustomBinaryOperation
    | CustomJsonOperation
    | CustomOperation
    | DeclineVotingRightsOperation
    | DelegateVestingSharesOperation
    | DeleteCommentOperation
    | EscrowApproveOperation
    | EscrowDisputeOperation
    | EscrowReleaseOperation
    | EscrowTransferOperation
    | FeedPublishOperation
    | LimitOrderCancelOperation
    | LimitOrderCreate2Operation
    | LimitOrderCreateOperation
    | PowOperation
    | RecoverAccountOperation
    | RecurrentTransferOperation
    | RemoveProposalOperation
    | RequestAccountRecoveryOperation
    | ResetAccountOperation
    | SetResetAccountOperation
    | SetWithdrawVestingRouteOperation
    | TransferFromSavingsOperation
    | TransferOperation
    | TransferToSavingsOperation
    | TransferToVestingOperation
    | UpdateProposalOperation
    | UpdateProposalVotesOperation
    | VoteOperation
    | WithdrawVestingOperation
    | WitnessBlockApproveOperation
    | WitnessSetPropertiesOperation
    | WitnessUpdateOperation
)

AnyLegacyOperation = (
    AccountCreateOperationLegacy
    | AccountUpdate2Operation
    | AccountUpdateOperation
    | AccountWitnessProxyOperation
    | AccountWitnessVoteOperation
    | CancelTransferFromSavingsOperation
    | ChangeRecoveryAccountOperation
    | ClaimAccountOperationLegacy
    | ClaimRewardBalanceOperationLegacy
    | CollateralizedConvertOperationLegacy
    | CommentOperation
    | CommentOptionsOperationLegacy
    | ConvertOperationLegacy
    | CreateClaimedAccountOperation
    | CreateProposalOperationLegacy
    | CustomBinaryOperation
    | CustomJsonOperation
    | CustomOperation
    | DeclineVotingRightsOperation
    | DelegateVestingSharesOperationLegacy
    | DeleteCommentOperation
    | EscrowApproveOperation
    | EscrowDisputeOperation
    | EscrowReleaseOperationLegacy
    | EscrowTransferOperationLegacy
    | FeedPublishOperation
    | LimitOrderCancelOperation
    | LimitOrderCreate2OperationLegacy
    | LimitOrderCreateOperationLegacy
    | PowOperation
    | RecoverAccountOperation
    | RecurrentTransferOperationLegacy
    | RemoveProposalOperation
    | RequestAccountRecoveryOperation
    | ResetAccountOperation
    | SetResetAccountOperation
    | SetWithdrawVestingRouteOperation
    | TransferFromSavingsOperationLegacy
    | TransferOperationLegacy
    | TransferToSavingsOperationLegacy
    | TransferToVestingOperationLegacy
    | UpdateProposalOperationLegacy
    | UpdateProposalVotesOperation
    | VoteOperation
    | WithdrawVestingOperationLegacy
    | WitnessBlockApproveOperation
    | WitnessSetPropertiesOperation
    | WitnessUpdateOperationLegacy
)


AnyEveryOperation = AnyOperation | AnyVirtualOperation
AnyLegacyEveryOperation = AnyLegacyOperation | AnyLegacyVirtualOperation


__all__ = [
    # ANY OPERATION
    "AnyOperation",
    "AnyLegacyOperation",
    "AnyEveryOperation",
    "AnyLegacyEveryOperation",
    # OPERATIONS
    "AccountCreateOperation",
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
    "ClaimAccountOperationLegacy",
    "ClaimRewardBalanceOperationLegacy",
    "CollateralizedConvertOperationLegacy",
    "CommentOptionsOperationLegacy",
    "ConvertOperationLegacy",
    "CreateProposalOperationLegacy",
    "DelegateVestingSharesOperationLegacy",
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
