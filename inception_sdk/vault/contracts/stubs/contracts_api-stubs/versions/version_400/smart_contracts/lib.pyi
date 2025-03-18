import abc
from ....utils import types_utils
from ....utils.feature_flags import ACCOUNTS_V2 as ACCOUNTS_V2, is_fflag_enabled as is_fflag_enabled
from ..common import types as common_types
from abc import abstractmethod
from collections.abc import Mapping
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
ALLOWED_BUILTINS: Any
ALLOWED_NATIVES: Any

class VaultFunctionsABC(types_utils.StrictInterface, metaclass=abc.ABCMeta):

    @abstractmethod
    def get_last_execution_datetime(self, event_type: str) -> Optional[datetime]:
        ...

    @abstractmethod
    def get_posting_instructions(self, *, fetcher_id: Optional[str]=...) -> common_types.postings.PITypes:
        ...

    @abstractmethod
    def get_client_transactions(self, *, fetcher_id: Optional[str]=...) -> Dict[str, common_types.ClientTransaction]:
        ...

    @abstractmethod
    def get_account_creation_datetime(self) -> datetime:
        ...

    @abstractmethod
    def get_balances_timeseries(self, *, fetcher_id: Optional[str]=...) -> Mapping[common_types.BalanceCoordinate, common_types.BalanceTimeseries]:
        ...

    @abstractmethod
    def get_hook_execution_id(self) -> str:
        ...

    @abstractmethod
    def get_parameter_timeseries(self, name: str) -> common_types.ParameterTimeseries:
        ...

    @abstractmethod
    def get_flag_timeseries(self, flag: str) -> common_types.FlagTimeseries:
        ...

    @abstractmethod
    def get_hook_result(self) -> Union[common_types.PostPostingHookResult, common_types.PrePostingHookResult, common_types.ScheduledEventHookResult]:
        ...

    @abstractmethod
    def get_alias(self) -> str:
        ...

    @abstractmethod
    def get_permitted_denominations(self) -> List[str]:
        ...

    @abstractmethod
    def get_calendar_events(self, calendar_ids: List[str]) -> common_types.CalendarEvents:
        ...

    @abstractmethod
    def get_balances_observation(self, fetcher_id: str) -> common_types.BalancesObservation:
        ...