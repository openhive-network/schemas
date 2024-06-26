from __future__ import annotations

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
from schemas.operations.virtual import (
    AnyLegacyVirtualOperation,
    AnyVirtualOperation,
)
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

AnyOperation = (
    AccountCreateOperation
    | AccountCreateWithDelegationOperation
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
    | Pow2Operation
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
    | PowOperationLegacy
    | Pow2OperationLegacy
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
