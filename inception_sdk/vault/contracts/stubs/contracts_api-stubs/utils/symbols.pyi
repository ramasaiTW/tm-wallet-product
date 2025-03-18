from typing import Any
POSTINGS_V3_KAFKA_CLIENT_ID: str
DEFAULT_ASSET: str
DEFAULT_ADDRESS: str
TRANSACTION_REFERENCE_FIELD_NAME: str
ORIGINATING_ACCOUNT_ID_TAG: str

class VaultRejectionReasonCode:
    UNKNOWN_REASON: int
    INSUFFICIENT_FUNDS: int
    WRONG_DENOMINATION: int
    AGAINST_TNC: int
    CLIENT_CUSTOM_REASON: int

class Tside:
    ASSET: int
    LIABILITY: int
TSIDE_NET_BALANCE_MAP: Any

class ContractParameterLevel:
    GLOBAL: int
    TEMPLATE: int
    INSTANCE: int

class ContractParameterUpdatePermission:
    PERMISSION_UNKNOWN: int
    FIXED: int
    OPS_EDITABLE: int
    USER_EDITABLE: int
    USER_EDITABLE_WITH_OPS_PERMISSION: int

class Features:
    UNKNOWN_FEATURE: int
    MANDATES: int
    MULTIPLE_OWNERS: int
    CARD: int
    SUB_ACCOUNTS: int
    JOINT_ACCOUNT: int
    INVESTMENT: int

class NoteType:
    UNKNOWN: int
    RAW_TEXT: int
    REASON_CODE: int

class NumberKind:
    PLAIN: str
    PERCENTAGE: str
    MONEY: str
    MONTHS: str

class Languages:
    ENGLISH: int

class Phase:
    COMMITTED: str
    PENDING_IN: str
    PENDING_OUT: str

class PostingInstructionType:
    OUTBOUND_AUTHORISATION: str
    INBOUND_AUTHORISATION: str
    AUTHORISATION: str
    AUTHORISATION_ADJUSTMENT: str
    CUSTOM_INSTRUCTION: str
    OUTBOUND_HARD_SETTLEMENT: str
    INBOUND_HARD_SETTLEMENT: str
    HARD_SETTLEMENT: str
    RELEASE: str
    SETTLEMENT: str
    TRANSFER: str

class DefinedDateTime:
    LIVE: int
    EFFECTIVE_TIME: int
    INTERVAL_START: int
    EFFECTIVE_DATETIME: int

class ScheduleFailover:
    FIRST_VALID_DAY_BEFORE: int
    FIRST_VALID_DAY_AFTER: int

class SupervisionExecutionMode:
    OVERRIDE: int
    INVOKED: int