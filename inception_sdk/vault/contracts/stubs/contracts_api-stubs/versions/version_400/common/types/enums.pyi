from .....utils.types_utils import EnumRepr
from enum import Enum
from typing import Any

class RejectionReason(EnumRepr, Enum):
    UNKNOWN_REASON: Any
    INSUFFICIENT_FUNDS: Any
    WRONG_DENOMINATION: Any
    AGAINST_TNC: Any
    CLIENT_CUSTOM_REASON: Any

class Tside(EnumRepr, Enum):
    ASSET: Any
    LIABILITY: Any

class Phase(EnumRepr, Enum):
    COMMITTED: Any
    PENDING_IN: Any
    PENDING_OUT: Any

class ParameterLevel(EnumRepr, Enum):
    GLOBAL: Any
    TEMPLATE: Any
    INSTANCE: Any

class ParameterUpdatePermission(EnumRepr, Enum):
    PERMISSION_UNKNOWN: Any
    FIXED: Any
    OPS_EDITABLE: Any
    USER_EDITABLE: Any
    USER_EDITABLE_WITH_OPS_PERMISSION: Any

class DefinedDateTime(EnumRepr, Enum):
    LIVE: Any
    INTERVAL_START: Any
    EFFECTIVE_DATETIME: Any

class ScheduleFailover(EnumRepr, Enum):
    FIRST_VALID_DAY_BEFORE: Any
    FIRST_VALID_DAY_AFTER: Any

class SupervisionExecutionMode(EnumRepr, Enum):
    OVERRIDE: Any
    INVOKED: Any

class PostingInstructionType(EnumRepr, Enum):
    OUTBOUND_AUTHORISATION: Any
    INBOUND_AUTHORISATION: Any
    AUTHORISATION: Any
    AUTHORISATION_ADJUSTMENT: Any
    CUSTOM_INSTRUCTION: Any
    OUTBOUND_HARD_SETTLEMENT: Any
    INBOUND_HARD_SETTLEMENT: Any
    HARD_SETTLEMENT: Any
    RELEASE: Any
    SETTLEMENT: Any
    TRANSFER: Any