from .symbols import VaultRejectionReasonCode as VaultRejectionReasonCode
from typing import Any

class ContractException(Exception):
    ...

class InvalidSmartContractError(ContractException):
    ...

class AmbiguousDatetimeProvided(ContractException):
    ...

class InvalidPostingInstructionException(Exception):
    ...

class InvalidContractParameter(ContractException):
    ...

class Rejected(ContractException):
    reason_code: Any

    def __init__(self, message, reason_code=...) -> None:
        ...

class IllegalPython(Exception):
    ...

class UnsupportedApiVersion(Exception):
    ...

class InDevelopmentApiVersion(UnsupportedApiVersion):
    ...

class StrongTypingError(ValueError):
    ...