"""
Operations field in transaction could return any type of operation, so Operation type must include all
types of operations
"""
from __future__ import annotations

from schemas.__private.operations import (
    AccountCreateOperation,
    AccountUpdate2Operation,
    AccountUpdateOperation,
    AccountWitnessProxyOperation,
    AccountWitnessVoteOperation,
    CancelTransferFromSavingsOperation,
    ChangeRecoveryAccountOperation,
    ClaimAccountOperation,
    ClaimRewardBalanceOperation,
    CollateralizedConvertOperation,
    CommentOperation,
    CommentOptionsOperation,
    ConvertOperation,
    CreateClaimedAccountOperation,
    CreateProposalOperation,
    CustomBinaryOperation,
    CustomJsonOperation,
    CustomOperation,
    DeclineVotingRightsOperation,
    DelegateVestingSharesOperation,
    DeleteCommentOperation,
    EscrowApproveOperation,
    EscrowDisputeOperation,
    EscrowReleaseOperation,
    EscrowTransferOperation,
    FeedPublishOperation,
    LimitOrderCancelOperation,
    RecoverAccountOperation,
    RecurrentTransferOperation,
    RemoveProposalOperation,
    RequestAccountRecoveryOperation,
    ResetAccountOperation,
    SetResetAccountOperation,
    SetWithdrawVestingRouteOperation,
    TransferFromSavingsOperation,
    TransferOperation,
    TransferToSavingsOperation,
    TransferToVestingOperation,
    UpdateProposalOperation,
    VoteOperation,
    WithdrawVestingOperation,
    WitnessBlockApproveOperation,
    WitnessSetPropertiesOperation,
    WitnessUpdateOperation,
)

Operation: AccountCreateOperation | AccountUpdateOperation | AccountUpdate2Operation | AccountWitnessProxyOperation | AccountWitnessVoteOperation | CancelTransferFromSavingsOperation | ChangeRecoveryAccountOperation | ClaimAccountOperation | ClaimRewardBalanceOperation | CollateralizedConvertOperation | CommentOperation | CommentOptionsOperation | ConvertOperation | CreateClaimedAccountOperation | CreateProposalOperation | CustomBinaryOperation | CustomJsonOperation | CustomOperation | DeclineVotingRightsOperation | DelegateVestingSharesOperation | DeleteCommentOperation | EscrowApproveOperation | EscrowDisputeOperation | EscrowReleaseOperation | EscrowTransferOperation | FeedPublishOperation | LimitOrderCancelOperation | RecoverAccountOperation | RecurrentTransferOperation | RemoveProposalOperation | RequestAccountRecoveryOperation | ResetAccountOperation | SetResetAccountOperation | SetWithdrawVestingRouteOperation | TransferFromSavingsOperation | TransferOperation | TransferToSavingsOperation | TransferToVestingOperation | UpdateProposalOperation | VoteOperation | WithdrawVestingOperation | WitnessBlockApproveOperation | WitnessSetPropertiesOperation | WitnessUpdateOperation
