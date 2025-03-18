from .event_types import ScheduledEvent as ScheduledEvent
from .parameters import OptionalValue as OptionalValue, UnionItemValue as UnionItemValue
from .postings import ClientTransaction as ClientTransaction, _PITypes_str
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, Optional, Union

class HookArguments:
    effective_datetime: datetime

    def __init__(self, effective_datetime: datetime, _from_proto: bool=...) -> None:
        ...

    def __eq__(self, other) -> bool:
        ...

class DeactivationHookArguments(HookArguments):
    ...

class DerivedParameterHookArguments(HookArguments):
    ...

class ActivationHookArguments(HookArguments):
    ...

class ConversionHookArguments(HookArguments):
    existing_schedules: Dict[str, ScheduledEvent]

    def __init__(self, effective_datetime: datetime, existing_schedules: Dict[str, ScheduledEvent]) -> None:
        ...

class PostParameterChangeHookArguments(HookArguments):
    old_parameter_values: Dict[str, Union[datetime, Decimal, int, OptionalValue, str, UnionItemValue]]
    updated_parameter_values: Dict[str, Union[datetime, Decimal, int, OptionalValue, str, UnionItemValue]]

    def __init__(self, effective_datetime: datetime, old_parameter_values: Dict[str, Union[datetime, Decimal, int, OptionalValue, str, UnionItemValue]], updated_parameter_values: Dict[str, Union[datetime, Decimal, int, OptionalValue, str, UnionItemValue]]) -> None:
        ...

class PostPostingHookArguments(HookArguments):
    posting_instructions: _PITypes_str
    client_transactions: Dict[str, ClientTransaction]

    def __init__(self, effective_datetime: datetime, posting_instructions: _PITypes_str, client_transactions: Dict[str, ClientTransaction]) -> None:
        ...

class PrePostingHookArguments(HookArguments):
    posting_instructions: _PITypes_str
    client_transactions: dict[str, ClientTransaction]

    def __init__(self, effective_datetime: datetime, posting_instructions: _PITypes_str, client_transactions: dict[str, ClientTransaction]) -> None:
        ...

class PreParameterChangeHookArguments(HookArguments):
    updated_parameter_values: Dict[str, Union[datetime, Decimal, int, OptionalValue, str, UnionItemValue]]

    def __init__(self, effective_datetime: datetime, updated_parameter_values: Dict[str, Union[datetime, Decimal, int, OptionalValue, str, UnionItemValue]]) -> None:
        ...

class ScheduledEventHookArguments(HookArguments):
    event_type: str
    pause_at_datetime: Optional[datetime]

    def __init__(self, effective_datetime: datetime, event_type: str, pause_at_datetime: Optional[datetime]=..., _from_proto: bool=...) -> None:
        ...

class SupervisorPostPostingHookArguments(HookArguments):
    supervisee_posting_instructions: Dict[str, _PITypes_str]
    supervisee_client_transactions: Dict[str, Dict[str, ClientTransaction]]

    def __init__(self, effective_datetime: datetime, supervisee_posting_instructions: Dict[str, _PITypes_str], supervisee_client_transactions: Dict[str, Dict[str, ClientTransaction]]) -> None:
        ...

class SupervisorPrePostingHookArguments(HookArguments):
    supervisee_posting_instructions: Dict[str, _PITypes_str]
    supervisee_client_transactions: Dict[str, Dict[str, ClientTransaction]]

    def __init__(self, effective_datetime: datetime, supervisee_posting_instructions: Dict[str, _PITypes_str], supervisee_client_transactions: Dict[str, Dict[str, ClientTransaction]]) -> None:
        ...

class SupervisorScheduledEventHookArguments(HookArguments):
    event_type: str
    supervisee_pause_at_datetime: Dict[str, Optional[datetime]]
    pause_at_datetime: Optional[datetime]

    def __init__(self, effective_datetime: datetime, event_type: str, supervisee_pause_at_datetime: Dict[str, Optional[datetime]], pause_at_datetime: Optional[datetime]=..., _from_proto: bool=...) -> None:
        ...

class SupervisorActivationHookArguments(HookArguments):
    ...

class SupervisorConversionHookArguments(HookArguments):
    existing_schedules: Dict[str, ScheduledEvent]

    def __init__(self, effective_datetime: datetime, existing_schedules: Dict[str, ScheduledEvent]) -> None:
        ...