from .enums import ScheduleFailover as ScheduleFailover
from typing import Any

class EndOfMonthSchedule:
    day: int
    hour: int
    minute: int
    second: int
    failover: ScheduleFailover

    def __init__(self, day: int, *, hour: int=..., minute: int=..., second: int=..., failover: ScheduleFailover=...) -> None:
        ...