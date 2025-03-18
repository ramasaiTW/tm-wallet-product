from .enums import RejectionReason as RejectionReason
from typing import Any, Optional

class Rejection:
    message: str
    reason_code: Optional[RejectionReason]

    def __init__(self, message: str, *, reason_code: Optional[RejectionReason]=..., _from_proto: Optional[bool]=...) -> None:
        ...