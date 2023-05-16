from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AssetHbdNai, AssetHiveNai, AssetVestsNai
from schemas.__private.operations.account_create_operation import (
    AccountCreateOperation as AccountCreateOperationGeneric,
)
from schemas.__private.operations.account_update2_operation import AccountUpdate2Operation
from schemas.__private.operations.account_update_operation import AccountUpdateOperation
from schemas.__private.operations.account_witness_proxy_operation import AccountWitnessProxyOperation
from schemas.__private.operations.account_witness_vote_operation import AccountWitnessVoteOperation
from schemas.__private.operations.cancel_transfer_from_savings_operation import CancelTransferFromSavingsOperation
from schemas.__private.operations.change_recovery_account_operation import ChangeRecoveryAccountOperation
from schemas.__private.operations.claim_account_operation import ClaimAccountOperation as ClaimAccountOperationGeneric
from schemas.__private.operations.claim_reward_balance_operation import (
    ClaimRewardBalanceOperation as ClaimRewardBalanceOperationGeneric,
)
from schemas.__private.operations.collateralized_convert_operation import (
    CollateralizedConvertOperation as CollateralizedConvertOperationGeneric,
)
from schemas.__private.operations.comment_operation import CommentOperation
from schemas.__private.operations.comment_options_operation import (
    CommentOptionsOperation as CommentOptionsOperationGeneric,
)
from schemas.__private.operations.convert_operation import ConvertOperation as ConvertOperationGeneric
from schemas.__private.operations.create_claimed_account_operation import CreateClaimedAccountOperation
from schemas.__private.operations.create_proposal_operation import (
    CreateProposalOperation as CreateProposalOperationGeneric,
)
from schemas.__private.operations.custom_binary_operation import CustomBinaryOperation
from schemas.__private.operations.custom_json_operation import CustomJsonOperation
from schemas.__private.operations.custom_operation import CustomOperation
from schemas.__private.operations.decline_voting_rights_operation import DeclineVotingRightsOperation
from schemas.__private.operations.delegate_vesting_shares_operation import (
    DelegateVestingSharesOperation as DelegateVestingSharesOperationGeneric,
)
from schemas.__private.operations.delete_comment_operation import DeleteCommentOperation
from schemas.__private.operations.escrow_approve_operation import EscrowApproveOperation
from schemas.__private.operations.escrow_dispute_operation import EscrowDisputeOperation
from schemas.__private.operations.escrow_release_operation import (
    EscrowReleaseOperation as EscrowReleaseOperationGeneric,
)
from schemas.__private.operations.escrow_transfer_operation import (
    EscrowTransferOperation as EscrowTransferOperationGeneric,
)
from schemas.__private.operations.feed_publish_operation import FeedPublishOperation
from schemas.__private.operations.limit_order_cancel_operation import LimitOrderCancelOperation
from schemas.__private.operations.limit_order_create2_operation import (
    LimitOrderCreate2Operation as LimitOrderCreate2OperationGeneric,
)
from schemas.__private.operations.limit_order_create_operation import (
    LimitOrderCreateOperation as LimitOrderCreateOperationGeneric,
)
from schemas.__private.operations.recover_account_operation import RecoverAccountOperation
from schemas.__private.operations.recurrent_transfer_operation import (
    RecurrentTransferOperation as RecurrentTransferOperationGeneric,
)
from schemas.__private.operations.remove_proposal_operation import RemoveProposalOperation
from schemas.__private.operations.request_account_recovery_operation import RequestAccountRecoveryOperation
from schemas.__private.operations.reset_account_operation import ResetAccountOperation
from schemas.__private.operations.set_reset_account_operation import SetResetAccountOperation
from schemas.__private.operations.set_withdraw_vesting_route_operation import SetWithdrawVestingRouteOperation
from schemas.__private.operations.transfer_from_savings_operation import (
    TransferFromSavingsOperation as TransferFromSavingsOperationGeneric,
)
from schemas.__private.operations.transfer_operation import TransferOperation as TransferOperationGeneric
from schemas.__private.operations.transfer_to_savings_operation import (
    TransferToSavingsOperation as TransferToSavingsOperationGeneric,
)
from schemas.__private.operations.transfer_to_vesting_operation import (
    TransferToVestingOperation as TransferToVestingOperationGeneric,
)
from schemas.__private.operations.update_proposal_operation import (
    UpdateProposalOperation as UpdateProposalOperationGeneric,
)
from schemas.__private.operations.update_proposal_votes_operation import UpdateProposalVotesOperation
from schemas.__private.operations.vote_operation import VoteOperation
from schemas.__private.operations.withdraw_vesting_operation import (
    WithdrawVestingOperation as WithdrawVestingOperationGeneric,
)
from schemas.__private.operations.witness_block_approve_operation import WitnessBlockApproveOperation
from schemas.__private.operations.witness_set_properties_operation import WitnessSetPropertiesOperation
from schemas.__private.operations.witness_update_operation import (
    WitnessUpdateOperation as WitnessUpdateOperationGeneric,
)

AccountCreateOperation = AccountCreateOperationGeneric[AssetHiveNai]
ClaimAccountOperation = ClaimAccountOperationGeneric[AssetHiveNai]
ClaimRewardBalanceOperation = ClaimRewardBalanceOperationGeneric[AssetHiveNai, AssetHbdNai, AssetVestsNai]
CollateralizedConvertOperation = CollateralizedConvertOperationGeneric[AssetHiveNai]
CommentOptionsOperation = CommentOptionsOperationGeneric[AssetHbdNai]
ConvertOperation = ConvertOperationGeneric[AssetHbdNai]
CreateProposalOperation = CreateProposalOperationGeneric[AssetHbdNai]
DelegateVestingSharesOperation = DelegateVestingSharesOperationGeneric[AssetVestsNai]
EscrowReleaseOperation = EscrowReleaseOperationGeneric[AssetHiveNai, AssetHbdNai]
EscrowTransferOperation = EscrowTransferOperationGeneric[AssetHiveNai, AssetHbdNai]
LimitOrderCreate2Operation = LimitOrderCreate2OperationGeneric[AssetHbdNai, AssetHiveNai]
LimitOrderCreateOperation = LimitOrderCreateOperationGeneric[AssetHiveNai, AssetHbdNai]
RecurrentTransferOperation = RecurrentTransferOperationGeneric[AssetHiveNai, AssetHbdNai]
TransferFromSavingsOperation = TransferFromSavingsOperationGeneric[AssetHiveNai, AssetHbdNai]
TransferOperation = TransferOperationGeneric[AssetHiveNai, AssetHbdNai]
TransferToSavingsOperation = TransferToSavingsOperationGeneric[AssetHiveNai, AssetHbdNai]
TransferToVestingOperation = TransferToVestingOperationGeneric[AssetHiveNai]
UpdateProposalOperation = UpdateProposalOperationGeneric[AssetHbdNai]
WithdrawVestingOperation = WithdrawVestingOperationGeneric[AssetVestsNai]
WitnessUpdateOperation = WitnessUpdateOperationGeneric[AssetHiveNai]

OperationType = (
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
__all__ = [
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
    "OperationType",
]
