from .schedules import EndOfMonthSchedule as EndOfMonthSchedule
from datetime import datetime
from typing import Any, List, Optional, Tuple, Union

class EventTypesGroup:
    name: str
    event_types_order: List[str]

    def __init__(self, name: str, event_types_order: List[str]) -> None:
        ...

class ScheduleExpression:
    day: Optional[Union[str, int]]
    day_of_week: Optional[Union[str, int]]
    hour: Optional[Union[str, int]]
    minute: Optional[Union[str, int]]
    second: Optional[Union[str, int]]
    month: Optional[Union[str, int]]
    year: Optional[Union[str, int]]

    def __init__(self, *, second: Optional[Union[str, int]]=..., minute: Optional[Union[str, int]]=..., hour: Optional[Union[str, int]]=..., day_of_week: Optional[Union[str, int]]=..., day: Optional[Union[str, int]]=..., month: Optional[Union[str, int]]=..., year: Optional[Union[str, int]]=...) -> None:
        ...

class ScheduleSkip:
    end: datetime

    def __init__(self, end: datetime, *, _from_proto: bool=...) -> None:
        ...

class ScheduledEvent:
    start_datetime: datetime
    end_datetime: Optional[datetime]
    expression: Optional[ScheduleExpression]
    schedule_method: Optional[EndOfMonthSchedule]
    skip: Optional[Union[bool, ScheduleSkip]]

    def __init__(self, *, start_datetime: datetime=..., end_datetime: Optional[datetime]=..., expression: Optional[ScheduleExpression]=..., schedule_method: Optional[EndOfMonthSchedule]=..., skip: Optional[Union[bool, ScheduleSkip]]=..., _from_proto: bool=...) -> None:
        ...

class EventType:
    name: str
    scheduler_tag_ids: Optional[List[str]]

    def __init__(self, name: str, *, scheduler_tag_ids: Optional[List[str]]=...) -> None:
        ...

class SmartContractEventType(EventType):
    ...

class SupervisorContractEventType(EventType):
    overrides_event_types: Optional[List[Tuple[str, str]]]

    def __init__(self, name: str, *, scheduler_tag_ids: Optional[List[str]]=..., overrides_event_types: Optional[List[Tuple[str, str]]]=...) -> None:
        ...