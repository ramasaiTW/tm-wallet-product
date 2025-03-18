from .exceptions import InvalidSmartContractError as InvalidSmartContractError
from datetime import datetime
from zoneinfo import ZoneInfo

def validate_dateime_is_timezone_aware(datetime: datetime, field_path: str, class_type: str):
    ...

def validate_timezone_is_utc(datetime: datetime, field_path: str, class_type: str):
    ...

def validate_and_convert_timezone_to_utc(datetime: datetime, field_path: str, class_type: str, events_timezone: ZoneInfo):
    ...

def validate_datetime_has_given_timezone(datetime: datetime, field_path: str, class_type: str, timezone: ZoneInfo):
    ...