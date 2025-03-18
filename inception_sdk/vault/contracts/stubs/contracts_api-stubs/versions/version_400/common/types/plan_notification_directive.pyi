from typing import Any, Dict

class PlanNotificationDirective:
    notification_type: str
    notification_details: Dict[str, str]

    def __init__(self, notification_type: str, notification_details: Dict[str, str]) -> None:
        ...