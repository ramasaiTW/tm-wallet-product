from . import feature_flags_config as feature_flags_config
from typing import Any
CONTRACTS_NOTIFICATION_EVENT: str
MOVE_SCX_PARSE_ENDPOINT_TO_CP: str
PRE_PARAM_CHANGE_HOOK_VALIDATION: str
MOVE_CX_PARSE_ENDPOINT_TO_CP: str
ACCOUNTS_V2: str
CONTRACTS_SIMULATION_LOGGING: str
REJECTION_FROM_ACTIVATION_CONVERSION_HOOKS: str
CONTRACT_LANGUAGE_FFLAGS: Any

def is_fflag_enabled(feature_flag: str) -> bool:
    ...

def skip_if_not_enabled(feature_flag: str):
    ...