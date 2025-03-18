from typing import Any, Dict

class AccountNotificationDirective:
    notification_type: str
    notification_details: Dict[str, str]

    def __init__(self, notification_type: str, notification_details: Dict[str, str], *, _from_proto: bool=...) -> None:
        ...