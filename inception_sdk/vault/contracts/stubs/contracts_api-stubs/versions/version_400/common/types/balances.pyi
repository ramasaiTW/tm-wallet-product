from .enums import Phase as Phase, Tside as Tside
from collections import defaultdict
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, NamedTuple, Optional

class AddressDetails:
    account_address: str
    description: str
    tags: List[str]

    def __init__(self, account_address: str, description: str, tags: List[str], *, _from_proto: bool=...) -> None:
        ...

    def __eq__(self, other):
        ...

class Balance:
    credit: Decimal
    debit: Decimal
    net: Decimal

    def __init__(self, credit: Decimal=..., debit: Decimal=..., net: Decimal=...) -> None:
        ...

    def __eq__(self, other):
        ...

    def __add__(self, other):
        ...

    def __radd__(self, other):
        ...

    def __iadd__(self, other):
        ...

class BalanceCoordinate(NamedTuple):
    account_address: str
    asset: str
    denomination: str
    phase: Phase

class BalanceDefaultDict(defaultdict):

    def __init__(self, default_factory: Optional[Dict[BalanceCoordinate, Balance]]=..., mapping: Optional[Dict[BalanceCoordinate, Balance]]=..., **_):
        ...

    def __add__(self, other):
        ...

    def __radd__(self, other):
        ...

    def __iadd__(self, other):
        ...

class BalancesObservation:
    value_datetime: Optional[datetime]
    balances: BalanceDefaultDict

    def __init__(self, balances: BalanceDefaultDict, *, value_datetime: Optional[datetime]=..., _from_proto: bool=...) -> None:
        ...