from .exceptions import InvalidPostingInstructionException as InvalidPostingInstructionException
from .symbols import DEFAULT_ADDRESS as DEFAULT_ADDRESS, DEFAULT_ASSET as DEFAULT_ASSET, PostingInstructionType as PostingInstructionType
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, NamedTuple, Optional
SECONDARY_POSTING_INSTRUCTIONS: Any
PRIMARY_POSTING_INSTRUCTIONS: Any
NON_CHAINABLE_INSTRUCTIONS: Any
CUSTOM_INSTRUCTIONS: Any

class CommittedPosting(NamedTuple):
    account_id: str
    amount: Decimal
    denomination: str
    credit: bool
    phase: int
    account_address: str
    asset: str

class BalanceKey(NamedTuple):
    account_address: str
    asset: str
    denomination: str
    phase: int

class BalanceValue(NamedTuple):
    debit: Decimal
    credit: Decimal

class ClientTransactionUpdate(NamedTuple):
    at_datetime: datetime
    committed_postings: List[CommittedPosting]
    balances: Dict[BalanceKey, BalanceValue]
    completed: bool
    released: bool

class SingleAccountClientTransaction:

    def __init__(self, client_transaction_id: str, account_id: str) -> None:
        ...

    @property
    def last_update(self) -> Optional[ClientTransactionUpdate]:
        ...

    def balances(self, *, at_datetime: datetime=...) -> Dict[BalanceKey, BalanceValue]:
        ...

    def add_committed_postings(self, at_datetime: datetime, committed_postings: List[CommittedPosting], instruction_type: str, final: bool=...) -> None:
        ...

def derive_balance_diff_from_committed_postings(committed_postings: List[CommittedPosting]) -> Dict[BalanceKey, BalanceValue]:
    ...