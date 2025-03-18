from . import enums as enums
from ....version_400.common.types import BalanceDefaultDict, Phase, PostingInstructionType, Tside
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union

class Posting:
    denomination: str
    account_id: str
    account_address: str
    asset: str
    credit: bool
    amount: Decimal
    phase: Phase

    def __init__(self, credit: bool, amount: Decimal, denomination: str, account_id: str, account_address: str, asset: str, phase: Phase, *, _from_proto: bool=...) -> None:
        ...

    def __eq__(self, other) -> bool:
        ...

class TransactionCode:
    domain: str
    family: str
    subfamily: str

    def __init__(self, domain: str, family: str, subfamily: str, *, _from_proto: Optional[bool]=...) -> None:
        ...

class PostingInstructionBase:
    type: Optional[PostingInstructionType]
    # MANUAL-FIX (TM-82499): the constructor type is genuinely Optional, as you can provide None
    # instruction_details, but this is is always defaulted to {} so the class attribute type should
    # not be Optional
    instruction_details: Dict[str, str]
    transaction_code: Optional[TransactionCode]
    override_all_restrictions: Optional[bool]

    def __init__(self, *, instruction_details: Optional[Dict[str, str]]=..., transaction_code: Optional[TransactionCode]=..., override_all_restrictions: Optional[bool]=..., _from_proto: bool=...) -> None:
        ...

    def __eq__(self, other):
        ...

    @property
    def id(self) -> Optional[str]:
        ...

    @property
    def batch_id(self) -> Optional[str]:
        ...

    @property
    def client_batch_id(self) -> Optional[str]:
        ...

    @property
    def unique_client_transaction_id(self) -> Optional[str]:
        ...

    @property
    def insertion_datetime(self) -> Optional[datetime]:
        ...

    @property
    def value_datetime(self) -> Optional[datetime]:
        ...

    @property
    def batch_details(self) -> Optional[Dict[str, str]]:
        ...

    def balances(self, account_id: Optional[str]=..., tside: Optional[Tside]=...) -> BalanceDefaultDict:
        ...

class Authorisation(PostingInstructionBase):
    client_transaction_id: str
    amount: Decimal
    denomination: str
    target_account_id: str
    internal_account_id: str
    advice: Optional[bool]

    def __init__(self, client_transaction_id: str, amount: Decimal, denomination: str, target_account_id: str, internal_account_id: str, *, advice: Optional[bool]=..., instruction_details: Optional[Dict[str, str]]=..., transaction_code: Optional[TransactionCode]=..., override_all_restrictions: Optional[bool]=..., _from_proto: bool=...) -> None:
        ...

class OutboundAuthorisation(Authorisation):
    type: Any

class InboundAuthorisation(Authorisation):
    type: Any

class CustomInstruction(PostingInstructionBase):
    type: Any
    postings: List[Posting]

    def __init__(self, postings: List[Posting], *, instruction_details: Optional[Dict[str, str]]=..., transaction_code: Optional[TransactionCode]=..., override_all_restrictions: Optional[bool]=..., _from_proto: bool=...) -> None:
        ...

class AdjustmentAmount:
    amount: Optional[Decimal]
    replacement_amount: Optional[Decimal]

    def __init__(self, amount: Optional[Decimal]=..., replacement_amount: Optional[Decimal]=..., _from_proto: bool=...) -> None:
        ...

class AuthorisationAdjustment(PostingInstructionBase):
    type: Any
    client_transaction_id: str
    adjustment_amount: AdjustmentAmount
    advice: Optional[bool]

    def __init__(self, client_transaction_id: str, adjustment_amount: AdjustmentAmount, *, advice: Optional[bool]=..., instruction_details: Optional[Dict[str, str]]=..., transaction_code: Optional[TransactionCode]=..., override_all_restrictions: Optional[bool]=..., _from_proto: bool=...) -> None:
        ...

    @property
    def authorised_amount(self) -> Optional[Decimal]:
        ...

    @property
    def delta_amount(self) -> Optional[Decimal]:
        ...

    @property
    def denomination(self) -> Optional[str]:
        ...

    @property
    def target_account_id(self) -> Optional[str]:
        ...

    @property
    def internal_account_id(self) -> Optional[str]:
        ...

class Settlement(PostingInstructionBase):
    type: Any
    client_transaction_id: str
    amount: Optional[Decimal]
    final: Optional[bool]

    def __init__(self, client_transaction_id: str, *, amount: Optional[Decimal]=..., final: Optional[bool]=..., instruction_details: Optional[Dict[str, str]]=..., transaction_code: Optional[TransactionCode]=..., override_all_restrictions: Optional[bool]=..., _from_proto: bool=...) -> None:
        ...

    @property
    def denomination(self) -> Optional[str]:
        ...

    @property
    def target_account_id(self) -> Optional[str]:
        ...

    @property
    def internal_account_id(self) -> Optional[str]:
        ...

class Release(PostingInstructionBase):
    type: Any
    client_transaction_id: str

    def __init__(self, client_transaction_id: str, *, instruction_details: Optional[Dict[str, str]]=..., transaction_code: Optional[TransactionCode]=..., override_all_restrictions: Optional[bool]=..., _from_proto: bool=...) -> None:
        ...

    @property
    def amount(self) -> Optional[Decimal]:
        ...

    @property
    def denomination(self) -> Optional[str]:
        ...

    @property
    def target_account_id(self) -> Optional[str]:
        ...

    @property
    def internal_account_id(self) -> Optional[str]:
        ...

class HardSettlement(PostingInstructionBase):
    amount: Decimal
    denomination: str
    target_account_id: str
    internal_account_id: str
    advice: Optional[bool]

    def __init__(self, amount: Decimal, denomination: str, target_account_id: str, internal_account_id: str, *, advice: Optional[bool]=..., instruction_details: Optional[Dict[str, str]]=..., transaction_code: Optional[TransactionCode]=..., override_all_restrictions: Optional[bool]=..., _from_proto: bool=...) -> None:
        ...

class OutboundHardSettlement(HardSettlement):
    type: Any

class InboundHardSettlement(HardSettlement):
    type: Any

class Transfer(PostingInstructionBase):
    type: Any
    amount: Decimal
    denomination: str
    debtor_target_account_id: str
    creditor_target_account_id: str

    def __init__(self, amount: Decimal, denomination: str, debtor_target_account_id: str, creditor_target_account_id: str, *, instruction_details: Optional[Dict[str, str]]=..., transaction_code: Optional[TransactionCode]=..., override_all_restrictions: Optional[bool]=..., _from_proto: bool=...) -> None:
        ...
PITypes = List[Union[AuthorisationAdjustment, CustomInstruction, InboundAuthorisation, InboundHardSettlement, OutboundAuthorisation, OutboundHardSettlement, Release, Settlement, Transfer]]

class ClientTransactionEffects:
    # MANUAL-FIX (TM-82501): this will always return a Decimal so shouldn't be Optional
    authorised: Decimal
    # MANUAL-FIX (TM-82501): this will always return a Decimal so shouldn't be Optional
    settled: Decimal
    # MANUAL-FIX (TM-82501): this will always return a Decimal so shouldn't be Optional
    unsettled: Decimal

    def __init__(self, *, authorised: Optional[Decimal]=..., settled: Optional[Decimal]=..., unsettled: Optional[Decimal]=...) -> None:
        ...

    def __eq__(self, other):
        ...

class ClientTransaction:
    posting_instructions: PITypes
    client_transaction_id: str
    account_id: str
    tside: Tside

    def __init__(self, client_transaction_id: str, account_id: str, posting_instructions: PITypes, *, tside: Tside=..., _from_proto: bool=...) -> None:
        ...

    def __eq__(self, other):
        ...

    def released(self, *, effective_datetime: datetime=...):
        ...

    def completed(self, *, effective_datetime: datetime=...):
        ...

    @property
    def denomination(self) -> Optional[str]:
        ...

    @property
    def is_custom(self) -> bool:
        ...

    @property
    def start_datetime(self) -> Optional[datetime]:
        ...

    def balances(self, *, effective_datetime: Optional[datetime]=..., tside: Optional[Tside]=...) -> BalanceDefaultDict:
        ...

    # MANUAL-FIX (TM-80286): this is handled as `Optional` but incorrectly annotated
    def effects(self, *, effective_datetime: Optional[datetime]=...) -> Optional[ClientTransactionEffects]:
        ...