from .event_types import ScheduleExpression as ScheduleExpression, ScheduleSkip as ScheduleSkip
from .schedules import EndOfMonthSchedule as EndOfMonthSchedule
from datetime import datetime
from typing import Any, Optional, Union

class UpdatePlanEventTypeDirective:
    event_type: str
    expression: Optional[ScheduleExpression]
    schedule_method: Optional[EndOfMonthSchedule]
    end_datetime: Optional[datetime]
    skip: Optional[Union[bool, ScheduleSkip]]

    def __init__(self, event_type: str, *, expression: Optional[ScheduleExpression]=..., schedule_method: Optional[EndOfMonthSchedule]=..., end_datetime: Optional[datetime]=..., skip: Optional[Union[bool, ScheduleSkip]]=..., _from_proto: bool=...) -> None:
        ...