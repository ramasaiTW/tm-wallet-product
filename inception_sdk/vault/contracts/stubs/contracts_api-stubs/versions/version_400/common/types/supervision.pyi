from .enums import SupervisionExecutionMode as SupervisionExecutionMode
from typing import Any, Optional

class SupervisedHooks:
    pre_posting_hook: SupervisionExecutionMode

    def __init__(self, *, pre_posting_hook: SupervisionExecutionMode=...) -> None:
        ...

class SmartContractDescriptor:
    alias: str
    smart_contract_version_id: str
    supervise_post_posting_hook: bool
    supervised_hooks: Optional[SupervisedHooks]

    def __init__(self, alias: str, smart_contract_version_id: str, *, supervise_post_posting_hook: bool=..., supervised_hooks: Optional[SupervisedHooks]=...) -> None:
        ...