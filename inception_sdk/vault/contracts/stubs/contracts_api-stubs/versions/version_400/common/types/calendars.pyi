from datetime import datetime
from typing import Any, List, Optional

class CalendarEvent:
    id: str
    calendar_id: str
    start_datetime: datetime
    end_datetime: datetime

    def __init__(self, id: str, calendar_id: str, start_datetime: datetime, end_datetime: datetime, *, _from_proto: bool=...) -> None:
        ...

class CalendarEvents(list):

    def __init__(self, *, calendar_events: Optional[List[CalendarEvent]]=...) -> None:
        ...