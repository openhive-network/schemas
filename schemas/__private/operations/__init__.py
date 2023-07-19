from __future__ import annotations

from typing import Any, Literal, Union, get_args  # pyright: ignore

from pydantic import Field
from typing_extensions import Annotated  # noqa: UP035

from schemas.__private.hive_fields_basic_schemas import (
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetVests,
    AssetVestsHF26,
    AssetVestsLegacy,
)
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
from schemas.__private.operations.virtual import (
    AccountCreatedOperation,
    AuthorRewardOperation,
    ChangedRecoveryAccountOperation,
    ClearNullAccountBalanceOperation,
    CollateralizedConvertImmediateConversionOperation,
    CommentBenefactorRewardOperation,
    CommentPayoutUpdateOperation,
    CommentRewardOperation,
    ConsolidateTreasuryBalanceOperation,
    CurationRewardOperation,
    DeclinedVotingRightsOperation,
    DelayedVotingOperation,
    DhfConversionOperation,
    DhfFundingOperation,
    EscrowApprovedOperation,
    EscrowRejectedOperation,
    ExpiredAccountNotificationOperation,
    FailedRecurrentTransferOperation,
    FillCollateralizedConvertRequestOperation,
    FillConvertRequestOperation,
    FillOrderOperation,
    FillRecurrentTransferOperation,
    FillTransferFromSavingsOperation,
    FillVestingWithdrawOperation,
    HardforkHiveOperation,
    HardforkHiveRestoreOperation,
    HardforkOperation,
    IneffectiveDeleteCommentOperation,
    InterestOperation,
    LegacyEffectiveCommentVoteOperation,
    LimitOrderCancelledOperation,
    LiquidityRewardOperation,
    NaiEffectiveCommentVoteOperation,
    PowRewardOperation,
    ProducerMissedOperation,
    ProducerRewardOperation,
    ProposalFeeOperation,
    ProposalPayOperation,
    ProxyClearedOperation,
    ReturnVestingDelegationOperation,
    ShutDownWitnessOperation,
    SystemWarningOperation,
    TransferToVestingCompletedOperation,
    VestingSharesSplitOperation,
    VirtualOperationType,
)
from schemas.__private.operations.vote_operation import VoteOperation
from schemas.__private.operations.withdraw_vesting_operation import WithdrawVestingOperation
from schemas.__private.operations.witness_block_approve_operation import WitnessBlockApproveOperation
from schemas.__private.operations.witness_set_properties_operation import WitnessSetPropertiesOperation
from schemas.__private.operations.witness_update_operation import WitnessUpdateOperation
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

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

AllOperationType = (
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
    | AccountCreatedOperation[AssetVests]
    | AuthorRewardOperation[AssetHive, AssetHbd, AssetVests]
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

Hf26OperationType = OperationType[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]
LegacyOperationType = OperationType[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]

Hf26VirtualOperationType = VirtualOperationType[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]
LegacyVirtualOperationType = VirtualOperationType[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]

LegacyAllOperationType = AllOperationType[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
Hf26AllOperationType = AllOperationType[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]


class Hf26OperationRepresentation(PreconfiguredBaseModel):
    type: str  # noqa: A003
    value: Hf26AllOperationType


class LegacyOperationRepresentation(PreconfiguredBaseModel):
    type: str  # noqa: A003
    value: LegacyAllOperationType

    def __getitem__(self, key: str | int) -> str | LegacyAllOperationType | Any:
        if isinstance(key, int):
            match (key):
                case 0:
                    return self.value.get_name().replace("_operation", "")
                case 1:
                    return self.value
                case _:
                    raise ValueError("out of bound")
        return super().__getitem__(key)


__HF26OperationTypes: dict[str, type[Hf26OperationRepresentation]] = {}
__LegacyOperationTypes: dict[str, type[LegacyOperationRepresentation]] = {}


def __get_representation_from_type_dict(type_name: str, collection: dict[str, type]) -> type:
    assert type_name in collection, f"`{type_name}` not found, available are: {list(collection.keys())}"
    return collection[type_name]


def get_hf26_representation(type_name: str) -> type[Hf26OperationRepresentation]:
    return __get_representation_from_type_dict(type_name, __HF26OperationTypes)


def get_legacy_representation(type_name: str) -> type[LegacyOperationRepresentation]:
    return __get_representation_from_type_dict(type_name, __LegacyOperationTypes)


def __create_hf26_representation(incoming_type: type[Hf26OperationType]) -> type[Hf26OperationRepresentation]:
    class Hf26Operation(Hf26OperationRepresentation):
        type: Literal[f"{incoming_type.get_name()}"]  # type: ignore[valid-type]  # noqa: A003
        value: incoming_type  # type: ignore[valid-type]

    Hf26Operation.update_forward_refs(**locals())
    __HF26OperationTypes[incoming_type.get_name()] = Hf26Operation
    return Hf26Operation


def __create_legacy_representation(incoming_cls: type[LegacyOperationType]) -> type[LegacyOperationRepresentation]:
    """
    Representation of operation in legacy format
    Response from api has format [name_of_operation, {parameters}], to provide precise validation in root_validator
    it is converted to format below.
    """

    cls_name_snake: str = incoming_cls.get_name().replace("_operation", "")

    class LegacyOperation(LegacyOperationRepresentation):
        type: Literal[f"{cls_name_snake}"]  # type: ignore[valid-type] # noqa: A003
        value: incoming_cls  # type: ignore[valid-type]

    LegacyOperation.update_forward_refs(**locals())
    __LegacyOperationTypes[cls_name_snake] = LegacyOperation
    return LegacyOperation


# NON-VIRTUAL
__Hf26OperationRepresentationUnionType = Union[tuple(__create_hf26_representation(arg) for arg in get_args(Hf26OperationType))]  # type: ignore
__LegacyOperationRepresentationUnionType = Union[tuple(__create_legacy_representation(arg) for arg in get_args(LegacyOperationType))]  # type: ignore
Hf26OperationRepresentationType = Annotated[__Hf26OperationRepresentationUnionType, Field(discriminator="type")]  # type: ignore
LegacyOperationRepresentationType = Annotated[__LegacyOperationRepresentationUnionType, Field(discriminator="type")]  # type: ignore

# VIRTUAL
__Hf26VirtualOperationRepresentationUnionType = Union[tuple(__create_hf26_representation(arg) for arg in (*get_args(Hf26VirtualOperationType), NaiEffectiveCommentVoteOperation))]  # type: ignore
__LegacyVirtualOperationRepresentationUnionType = Union[tuple(__create_legacy_representation(arg) for arg in (*get_args(LegacyVirtualOperationType), LegacyEffectiveCommentVoteOperation))]  # type: ignore
Hf26VirtualOperationRepresentationType = Annotated[__Hf26VirtualOperationRepresentationUnionType, Field(discriminator="type")]  # type: ignore
LegacyVirtualOperationRepresentationType = Annotated[__LegacyVirtualOperationRepresentationUnionType, Field(discriminator="type")]  # type: ignore

# ALL
__Hf26AllOperationUnionType = Union[tuple(__create_hf26_representation(arg) for arg in (*get_args(AllOperationType), NaiEffectiveCommentVoteOperation))]  # type: ignore
__LegacyAllOperationUnionType = Union[tuple(__create_legacy_representation(arg) for arg in (*get_args(AllOperationType), LegacyEffectiveCommentVoteOperation))]  # type: ignore
Hf26AllOperationRepresentationType = Annotated[__Hf26AllOperationUnionType, Field(discriminator="type")]  # type: ignore
LegacyAllOperationRepresentationType = Annotated[__LegacyAllOperationUnionType, Field(discriminator="type")]  # type: ignore

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
    "PowOperation",
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
    "Hf26OperationRepresentationType",
    "LegacyOperationRepresentationType",
    "Hf26VirtualOperationRepresentationType",
    "LegacyVirtualOperationRepresentationType",
    "LegacyAllOperationRepresentationType",
]
