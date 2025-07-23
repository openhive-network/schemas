from __future__ import annotations

from typing import overload

from schemas.operation import Operation
from schemas.operations.account_create_operation import (
    AccountCreateOperation,
)
from schemas.operations.account_create_with_delegation_operation import (
    AccountCreateWithDelegationOperation,
)
from schemas.operations.account_update2_operation import AccountUpdate2Operation
from schemas.operations.account_update_operation import AccountUpdateOperation
from schemas.operations.account_witness_proxy_operation import AccountWitnessProxyOperation
from schemas.operations.account_witness_vote_operation import AccountWitnessVoteOperation
from schemas.operations.cancel_transfer_from_savings_operation import CancelTransferFromSavingsOperation
from schemas.operations.change_recovery_account_operation import ChangeRecoveryAccountOperation
from schemas.operations.claim_account_operation import ClaimAccountOperation
from schemas.operations.claim_reward_balance_operation import (
    ClaimRewardBalanceOperation,
)
from schemas.operations.collateralized_convert_operation import (
    CollateralizedConvertOperation,
)
from schemas.operations.comment_operation import CommentOperation
from schemas.operations.comment_options_operation import (
    CommentOptionsOperation,
)
from schemas.operations.convert_operation import ConvertOperation
from schemas.operations.create_claimed_account_operation import CreateClaimedAccountOperation
from schemas.operations.create_proposal_operation import (
    CreateProposalOperation,
)
from schemas.operations.custom_binary_operation import CustomBinaryOperation
from schemas.operations.custom_json_operation import CustomJsonOperation, CustomJsonOperationGeneric
from schemas.operations.custom_operation import CustomOperation
from schemas.operations.decline_voting_rights_operation import DeclineVotingRightsOperation
from schemas.operations.delegate_rc_operation import DelegateRcOperation
from schemas.operations.delegate_vesting_shares_operation import (
    DelegateVestingSharesOperation,
)
from schemas.operations.delete_comment_operation import DeleteCommentOperation
from schemas.operations.escrow_approve_operation import EscrowApproveOperation
from schemas.operations.escrow_dispute_operation import EscrowDisputeOperation
from schemas.operations.escrow_release_operation import (
    EscrowReleaseOperation,
)
from schemas.operations.escrow_transfer_operation import (
    EscrowTransferOperation,
)
from schemas.operations.feed_publish_operation import FeedPublishOperation
from schemas.operations.follow_operation import FollowOperation
from schemas.operations.limit_order_cancel_operation import LimitOrderCancelOperation
from schemas.operations.limit_order_create2_operation import (
    LimitOrderCreate2Operation,
)
from schemas.operations.limit_order_create_operation import (
    LimitOrderCreateOperation,
)
from schemas.operations.pow2_operation import Pow2Operation
from schemas.operations.pow_operation import PowOperation
from schemas.operations.recover_account_operation import RecoverAccountOperation
from schemas.operations.recurrent_transfer_operation import (
    RecurrentTransferOperation,
)
from schemas.operations.remove_proposal_operation import RemoveProposalOperation
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
    HF26RepresentationDelegateRcOperation,
    HF26RepresentationDelegateVestingSharesOperation,
    HF26RepresentationDeleteCommentOperation,
    HF26RepresentationEscrowApproveOperation,
    HF26RepresentationEscrowDisputeOperation,
    HF26RepresentationEscrowReleaseOperation,
    HF26RepresentationEscrowTransferOperation,
    HF26RepresentationFeedPublishOperation,
    HF26RepresentationFollowOperation,
    HF26RepresentationLimitOrderCancelOperation,
    HF26RepresentationLimitOrderCreate2Operation,
    HF26RepresentationLimitOrderCreateOperation,
    HF26RepresentationPow2Operation,
    HF26RepresentationPowOperation,
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
    LegacyRepresentationAccountCreateOperation,
    LegacyRepresentationAccountCreateWithDelegationOperation,
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
    LegacyRepresentationDelegateRcOperation,
    LegacyRepresentationDelegateVestingSharesOperation,
    LegacyRepresentationDeleteCommentOperation,
    LegacyRepresentationEscrowApproveOperation,
    LegacyRepresentationEscrowDisputeOperation,
    LegacyRepresentationEscrowReleaseOperation,
    LegacyRepresentationEscrowTransferOperation,
    LegacyRepresentationFeedPublishOperation,
    LegacyRepresentationFollowOperation,
    LegacyRepresentationLimitOrderCancelOperation,
    LegacyRepresentationLimitOrderCreate2Operation,
    LegacyRepresentationLimitOrderCreateOperation,
    LegacyRepresentationPow2Operation,
    LegacyRepresentationPowOperation,
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
from schemas.operations.request_account_recovery_operation import RequestAccountRecoveryOperation
from schemas.operations.reset_account_operation import ResetAccountOperation
from schemas.operations.set_reset_account_operation import SetResetAccountOperation
from schemas.operations.set_withdraw_vesting_route_operation import SetWithdrawVestingRouteOperation
from schemas.operations.transfer_from_savings_operation import (
    TransferFromSavingsOperation,
)
from schemas.operations.transfer_operation import TransferOperation
from schemas.operations.transfer_to_savings_operation import (
    TransferToSavingsOperation,
)
from schemas.operations.transfer_to_vesting_operation import (
    TransferToVestingOperation,
)
from schemas.operations.update_proposal_operation import (
    UpdateProposalOperation,
)
from schemas.operations.update_proposal_votes_operation import UpdateProposalVotesOperation
from schemas.operations.virtual import (
    HF26RepresentationAndValuePairsVirtual,
    Hf26VirtualOperationRepresentation,
    LegacyRepresentationAndValuePairsVirtual,
    LegacyVirtualOperationRepresentation,
)
from schemas.operations.vote_operation import VoteOperation
from schemas.operations.withdraw_vesting_operation import (
    WithdrawVestingOperation,
)
from schemas.operations.witness_block_approve_operation import WitnessBlockApproveOperation
from schemas.operations.witness_set_properties_operation import WitnessSetPropertiesOperation
from schemas.operations.witness_update_operation import (
    WitnessUpdateOperation,
)
from schemas.virtual_operation import VirtualOperation

__all__ = [
    # ANY OPERATION BY TYPE
    "AnyHf26Operation",
    "AnyLegacyOperation",
    # ANY OPERATION BY VIRTUAL
    # NON-VIRTUAL
    "Hf26OperationRepresentation",
    "LegacyOperationRepresentation",
    # VIRTUAL
    "Hf26VirtualOperationRepresentation",
    "LegacyVirtualOperationRepresentation",
    # OPERATIONS
    "Hf26Operations",
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
    "DelegateRcOperation",
    "DelegateVestingSharesOperation",
    "DeleteCommentOperation",
    "EscrowApproveOperation",
    "EscrowDisputeOperation",
    "EscrowReleaseOperation",
    "EscrowTransferOperation",
    "FeedPublishOperation",
    "FollowOperation",
    "LimitOrderCancelOperation",
    "LimitOrderCreate2Operation",
    "LimitOrderCreateOperation",
    "Pow2Operation",
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
]

Hf26Operations = (
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
    | DelegateRcOperation
    | DelegateVestingSharesOperation
    | DeleteCommentOperation
    | EscrowApproveOperation
    | EscrowDisputeOperation
    | EscrowReleaseOperation
    | EscrowTransferOperation
    | FeedPublishOperation
    | FollowOperation
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

LegacyOperations = (
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
    | DelegateRcOperation
    | DelegateVestingSharesOperation
    | DeleteCommentOperation
    | EscrowApproveOperation
    | EscrowDisputeOperation
    | EscrowReleaseOperation
    | EscrowTransferOperation
    | FeedPublishOperation
    | FollowOperation
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

Hf26OperationRepresentation = (
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
    | HF26RepresentationDelegateRcOperation
    | HF26RepresentationDelegateVestingSharesOperation
    | HF26RepresentationDeleteCommentOperation
    | HF26RepresentationEscrowApproveOperation
    | HF26RepresentationEscrowDisputeOperation
    | HF26RepresentationEscrowReleaseOperation
    | HF26RepresentationEscrowTransferOperation
    | HF26RepresentationFeedPublishOperation
    | HF26RepresentationFollowOperation
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

LegacyOperationRepresentation = (
    LegacyRepresentationAccountCreateOperation
    | LegacyRepresentationAccountCreateWithDelegationOperation
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
    | LegacyRepresentationDelegateRcOperation
    | LegacyRepresentationDelegateVestingSharesOperation
    | LegacyRepresentationDeleteCommentOperation
    | LegacyRepresentationEscrowApproveOperation
    | LegacyRepresentationEscrowDisputeOperation
    | LegacyRepresentationEscrowReleaseOperation
    | LegacyRepresentationEscrowTransferOperation
    | LegacyRepresentationFeedPublishOperation
    | LegacyRepresentationFollowOperation
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


AnyHf26Operation = Hf26OperationRepresentation | Hf26VirtualOperationRepresentation
AnyLegacyOperation = LegacyOperationRepresentation | LegacyVirtualOperationRepresentation


LegacyRepresentationAndValuePairsNonVirtual: dict[type[Operation], type[LegacyOperationRepresentation]] = {
    AccountCreateOperation: LegacyRepresentationAccountCreateOperation,
    AccountCreateWithDelegationOperation: LegacyRepresentationAccountCreateWithDelegationOperation,
    AccountUpdate2Operation: LegacyRepresentationAccountUpdate2Operation,
    AccountUpdateOperation: LegacyRepresentationAccountUpdateOperation,
    AccountWitnessProxyOperation: LegacyRepresentationAccountWitnessProxyOperation,
    AccountWitnessVoteOperation: LegacyRepresentationAccountWitnessVoteOperation,
    CancelTransferFromSavingsOperation: LegacyRepresentationCancelTransferFromSavingsOperation,
    ChangeRecoveryAccountOperation: LegacyRepresentationChangeRecoveryAccountOperation,
    ClaimAccountOperation: LegacyRepresentationClaimAccountOperation,
    ClaimRewardBalanceOperation: LegacyRepresentationClaimRewardBalanceOperation,
    CollateralizedConvertOperation: LegacyRepresentationCollateralizedConvertOperation,
    CommentOperation: LegacyRepresentationCommentOperation,
    CommentOptionsOperation: LegacyRepresentationCommentOptionsOperation,
    ConvertOperation: LegacyRepresentationConvertOperation,
    CreateClaimedAccountOperation: LegacyRepresentationCreateClaimedAccountOperation,
    CreateProposalOperation: LegacyRepresentationCreateProposalOperation,
    CustomBinaryOperation: LegacyRepresentationCustomBinaryOperation,
    CustomJsonOperation: LegacyRepresentationCustomJsonOperation,
    CustomOperation: LegacyRepresentationCustomOperation,
    DeclineVotingRightsOperation: LegacyRepresentationDeclineVotingRightsOperation,
    DelegateRcOperation: LegacyRepresentationDelegateRcOperation,
    DelegateVestingSharesOperation: LegacyRepresentationDelegateVestingSharesOperation,
    DeleteCommentOperation: LegacyRepresentationDeleteCommentOperation,
    EscrowApproveOperation: LegacyRepresentationEscrowApproveOperation,
    EscrowDisputeOperation: LegacyRepresentationEscrowDisputeOperation,
    EscrowReleaseOperation: LegacyRepresentationEscrowReleaseOperation,
    EscrowTransferOperation: LegacyRepresentationEscrowTransferOperation,
    FeedPublishOperation: LegacyRepresentationFeedPublishOperation,
    FollowOperation: LegacyRepresentationFollowOperation,
    LimitOrderCancelOperation: LegacyRepresentationLimitOrderCancelOperation,
    LimitOrderCreate2Operation: LegacyRepresentationLimitOrderCreate2Operation,
    LimitOrderCreateOperation: LegacyRepresentationLimitOrderCreateOperation,
    PowOperation: LegacyRepresentationPowOperation,
    Pow2Operation: LegacyRepresentationPow2Operation,
    RecoverAccountOperation: LegacyRepresentationRecoverAccountOperation,
    RecurrentTransferOperation: LegacyRepresentationRecurrentTransferOperation,
    RemoveProposalOperation: LegacyRepresentationRemoveProposalOperation,
    RequestAccountRecoveryOperation: LegacyRepresentationRequestAccountRecoveryOperation,
    ResetAccountOperation: LegacyRepresentationResetAccountOperation,
    SetResetAccountOperation: LegacyRepresentationSetResetAccountOperation,
    SetWithdrawVestingRouteOperation: LegacyRepresentationSetWithdrawVestingRouteOperation,
    TransferFromSavingsOperation: LegacyRepresentationTransferFromSavingsOperation,
    TransferOperation: LegacyRepresentationTransferOperation,
    TransferToSavingsOperation: LegacyRepresentationTransferToSavingsOperation,
    TransferToVestingOperation: LegacyRepresentationTransferToVestingOperation,
    UpdateProposalOperation: LegacyRepresentationUpdateProposalOperation,
    UpdateProposalVotesOperation: LegacyRepresentationUpdateProposalVotesOperation,
    VoteOperation: LegacyRepresentationVoteOperation,
    WithdrawVestingOperation: LegacyRepresentationWithdrawVestingOperation,
    WitnessBlockApproveOperation: LegacyRepresentationWitnessBlockApproveOperation,
    WitnessSetPropertiesOperation: LegacyRepresentationWitnessSetPropertiesOperation,
    WitnessUpdateOperation: LegacyRepresentationWitnessUpdateOperation,
}


HF26RepresentationAndValuePairsNonVirtual: dict[type[Operation], type[Hf26OperationRepresentation]] = {
    AccountCreateOperation: HF26RepresentationAccountCreateOperation,
    AccountCreateWithDelegationOperation: HF26RepresentationAccountCreateWithDelegationOperation,
    AccountUpdate2Operation: HF26RepresentationAccountUpdate2Operation,
    AccountUpdateOperation: HF26RepresentationAccountUpdateOperation,
    AccountWitnessProxyOperation: HF26RepresentationAccountWitnessProxyOperation,
    AccountWitnessVoteOperation: HF26RepresentationAccountWitnessVoteOperation,
    CancelTransferFromSavingsOperation: HF26RepresentationCancelTransferFromSavingsOperation,
    ChangeRecoveryAccountOperation: HF26RepresentationChangeRecoveryAccountOperation,
    ClaimAccountOperation: HF26RepresentationClaimAccountOperation,
    ClaimRewardBalanceOperation: HF26RepresentationClaimRewardBalanceOperation,
    CollateralizedConvertOperation: HF26RepresentationCollateralizedConvertOperation,
    CommentOperation: HF26RepresentationCommentOperation,
    CommentOptionsOperation: HF26RepresentationCommentOptionsOperation,
    ConvertOperation: HF26RepresentationConvertOperation,
    CreateClaimedAccountOperation: HF26RepresentationCreateClaimedAccountOperation,
    CreateProposalOperation: HF26RepresentationCreateProposalOperation,
    CustomBinaryOperation: HF26RepresentationCustomBinaryOperation,
    CustomJsonOperation: HF26RepresentationCustomJsonOperation,
    CustomOperation: HF26RepresentationCustomOperation,
    DeclineVotingRightsOperation: HF26RepresentationDeclineVotingRightsOperation,
    DelegateRcOperation: HF26RepresentationDelegateRcOperation,
    DelegateVestingSharesOperation: HF26RepresentationDelegateVestingSharesOperation,
    DeleteCommentOperation: HF26RepresentationDeleteCommentOperation,
    EscrowApproveOperation: HF26RepresentationEscrowApproveOperation,
    EscrowDisputeOperation: HF26RepresentationEscrowDisputeOperation,
    EscrowReleaseOperation: HF26RepresentationEscrowReleaseOperation,
    EscrowTransferOperation: HF26RepresentationEscrowTransferOperation,
    FeedPublishOperation: HF26RepresentationFeedPublishOperation,
    FollowOperation: HF26RepresentationFollowOperation,
    LimitOrderCancelOperation: HF26RepresentationLimitOrderCancelOperation,
    LimitOrderCreate2Operation: HF26RepresentationLimitOrderCreate2Operation,
    LimitOrderCreateOperation: HF26RepresentationLimitOrderCreateOperation,
    PowOperation: HF26RepresentationPowOperation,
    Pow2Operation: HF26RepresentationPow2Operation,
    RecoverAccountOperation: HF26RepresentationRecoverAccountOperation,
    RecurrentTransferOperation: HF26RepresentationRecurrentTransferOperation,
    RemoveProposalOperation: HF26RepresentationRemoveProposalOperation,
    RequestAccountRecoveryOperation: HF26RepresentationRequestAccountRecoveryOperation,
    ResetAccountOperation: HF26RepresentationResetAccountOperation,
    SetResetAccountOperation: HF26RepresentationSetResetAccountOperation,
    SetWithdrawVestingRouteOperation: HF26RepresentationSetWithdrawVestingRouteOperation,
    TransferFromSavingsOperation: HF26RepresentationTransferFromSavingsOperation,
    TransferOperation: HF26RepresentationTransferOperation,
    TransferToSavingsOperation: HF26RepresentationTransferToSavingsOperation,
    TransferToVestingOperation: HF26RepresentationTransferToVestingOperation,
    UpdateProposalOperation: HF26RepresentationUpdateProposalOperation,
    UpdateProposalVotesOperation: HF26RepresentationUpdateProposalVotesOperation,
    VoteOperation: HF26RepresentationVoteOperation,
    WithdrawVestingOperation: HF26RepresentationWithdrawVestingOperation,
    WitnessBlockApproveOperation: HF26RepresentationWitnessBlockApproveOperation,
    WitnessSetPropertiesOperation: HF26RepresentationWitnessSetPropertiesOperation,
    WitnessUpdateOperation: HF26RepresentationWitnessUpdateOperation,
}

LegacyRepresentationAndValuePairs = (
    LegacyRepresentationAndValuePairsNonVirtual | LegacyRepresentationAndValuePairsVirtual
)
HF26RepresentationAndValuePairs = HF26RepresentationAndValuePairsNonVirtual | HF26RepresentationAndValuePairsVirtual


@overload
def convert_to_representation(op: Operation) -> Hf26OperationRepresentation: ...


@overload
def convert_to_representation(op: VirtualOperation) -> Hf26VirtualOperationRepresentation: ...


def convert_to_representation(
    op: Operation | VirtualOperation,
) -> Hf26OperationRepresentation | Hf26VirtualOperationRepresentation:
    return HF26RepresentationAndValuePairs[type(op)](value=op)  # type: ignore[index, arg-type]


@overload
def convert_to_representation_legacy(op: VirtualOperation) -> LegacyVirtualOperationRepresentation: ...


@overload
def convert_to_representation_legacy(op: Operation) -> LegacyOperationRepresentation: ...


def convert_to_representation_legacy(
    op: Operation | VirtualOperation,
) -> LegacyOperationRepresentation | LegacyVirtualOperationRepresentation:
    return LegacyRepresentationAndValuePairs[type(op)](value=op)  # type: ignore[index, arg-type]
