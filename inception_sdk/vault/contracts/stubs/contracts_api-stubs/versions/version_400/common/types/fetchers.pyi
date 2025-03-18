from .enums import DefinedDateTime as DefinedDateTime
from .filters import BalancesFilter as BalancesFilter
from .time_operations import RelativeDateTime as RelativeDateTime
from typing import Any, Optional, Union
requires: Any
fetch_account_data: Any

class IntervalFetcher:
    fetcher_id: str
    start: Union[RelativeDateTime, DefinedDateTime]
    end: Optional[Union[RelativeDateTime, DefinedDateTime]]

    def __init__(self, *, fetcher_id: str=..., start: Union[RelativeDateTime, DefinedDateTime]=..., end: Optional[Union[RelativeDateTime, DefinedDateTime]]=...) -> None:
        ...

class BalancesIntervalFetcher(IntervalFetcher):
    class_name: Any
    filter: Optional[BalancesFilter]

    def __init__(self, *, fetcher_id: str=..., start: Union[RelativeDateTime, DefinedDateTime]=..., end: Optional[Union[RelativeDateTime, DefinedDateTime]]=..., filter: Optional[BalancesFilter]=...) -> None:
        ...

class BalancesObservationFetcher:
    fetcher_id: str
    at: Union[DefinedDateTime, RelativeDateTime]
    filter: Optional[BalancesFilter]

    def __init__(self, fetcher_id: str=..., at: Union[DefinedDateTime, RelativeDateTime]=..., filter: Optional[BalancesFilter]=...) -> None:
        ...

class PostingsIntervalFetcher(IntervalFetcher):
    class_name: Any

    def __init__(self, *, fetcher_id: str=..., start: Union[RelativeDateTime, DefinedDateTime]=..., end: Optional[Union[RelativeDateTime, DefinedDateTime]]=...) -> None:
        ...