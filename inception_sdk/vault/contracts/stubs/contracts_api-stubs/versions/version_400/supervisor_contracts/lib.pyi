import abc
from ....utils import types_utils
from ..common import types as common_types
from abc import abstractmethod
from datetime import datetime
from typing import Any, List
ALLOWED_BUILTINS: Any
ALLOWED_NATIVES: Any

class VaultFunctionsABC(types_utils.StrictInterface, metaclass=abc.ABCMeta):

    @abstractmethod
    def get_plan_opening_datetime(self) -> datetime:
        ...

    @abstractmethod
    def get_hook_execution_id(self) -> str:
        ...

    @abstractmethod
    def get_calendar_events(self, calendar_ids: List[str]) -> common_types.CalendarEvents:
        ...