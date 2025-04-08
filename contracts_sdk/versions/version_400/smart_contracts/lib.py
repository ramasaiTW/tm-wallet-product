from abc import abstractmethod
from collections.abc import Mapping
from datetime import datetime
from functools import lru_cache
from typing import Dict, List, Optional, Union

from ..common import lib as common_lib, types as common_types
from ....utils import symbols, types_utils
from ....utils.feature_flags import (
    is_fflag_enabled,
    ACCOUNTS_V2,
)


ALLOWED_BUILTINS = common_lib.ALLOWED_BUILTINS
ALLOWED_NATIVES = common_lib.ALLOWED_NATIVES


class VaultFunctionsABC(types_utils.StrictInterface):
    @abstractmethod
    def get_last_execution_datetime(self, *, event_type: str) -> Optional[datetime]:
        pass

    @abstractmethod
    def get_posting_instructions(self, *, fetcher_id: Optional[str] = None) -> common_types.postings.PITypes:
        pass

    @abstractmethod
    def get_client_transactions(self, *, fetcher_id: Optional[str] = None) -> Dict[str, common_types.ClientTransaction]:
        pass

    @abstractmethod
    def get_account_creation_datetime(self) -> Optional[datetime]:
        pass

    @abstractmethod
    def get_balances_timeseries(self, *, fetcher_id: Optional[str] = None) -> Mapping[common_types.BalanceCoordinate, common_types.BalanceTimeseries]:
        pass

    @abstractmethod
    def get_hook_execution_id(self) -> str:
        pass

    @abstractmethod
    def get_parameter_timeseries(self, *, name: str) -> common_types.ParameterTimeseries:
        pass

    @abstractmethod
    def get_flag_timeseries(self, *, flag: str) -> common_types.FlagTimeseries:
        pass

    @abstractmethod
    def get_hook_result(
        self,
    ) -> Union[common_types.PostPostingHookResult, common_types.PrePostingHookResult, common_types.ScheduledEventHookResult,]:
        pass

    @abstractmethod
    def get_alias(self) -> str:
        pass

    @abstractmethod
    def get_permitted_denominations(self) -> List[str]:
        pass

    @abstractmethod
    def get_calendar_events(self, *, calendar_ids: List[str]) -> common_types.CalendarEvents:
        pass

    @abstractmethod
    def get_balances_observation(self, *, fetcher_id: str) -> common_types.BalancesObservation:
        pass

    @classmethod
    @lru_cache()
    def _spec(cls, language_code=symbols.Languages.ENGLISH):
        if language_code != symbols.Languages.ENGLISH:
            raise ValueError("Language not supported")
        spec = types_utils.ClassSpec(
            name="VaultFunctions",
            docstring="""
                The Vault object is present during the execution of every hook and is accessible
                via the `vault` variable.

                Apart from hook-specific arguments and return values, it is the sole method of
                fetching information from Vault or communicating "hook directives" back to Vault.

                All information fetched from the `vault` object must have been statically declared
                at the top of a hook using the `@requires` decorator, and is fetched in a batch
                before the hook starts executing.

                All hook directives are batched until the hook finishes executing, and then
                implemented in Vault at the same time.
            """,
            public_methods=[
                types_utils.MethodSpec(
                    name="get_last_execution_datetime",
                    docstring="""
                    Gets the most recent time that the `scheduled_event_hook` was called for
                    the given `event_type`.
                """,
                    args=[
                        types_utils.ValueSpec(
                            name="event_type",
                            type="str",
                            docstring="The `scheduled_event_hook`'s `event_type` string.",
                        ),
                    ],
                    return_value=types_utils.ReturnValueSpec(
                        docstring="""
                            The last execution time as a timezone-aware UTC datetime.
                            If the `event_type` has never been executed, `None` will be returned.
                        """,
                        type="Optional[datetime]",
                    ),
                    examples=[
                        types_utils.Example(
                            title="A simple example",
                            code="vault.get_last_execution_datetime(event_type='SERVICE_CHARGE')",
                        )
                    ],
                )
            ],
        )
        public_attributes = [
            types_utils.ValueSpec(
                name="account_id",
                type="str",
                docstring="The id of the Account currently being executed.",
            ),
            types_utils.ValueSpec(
                name="tside",
                type="Tside",
                docstring="""
                    The treasury side of the Account. It determines the Account
                    [Balance](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#Balance) net sign.
                """,  # noqa: E501
            ),
            types_utils.ValueSpec(
                name="events_timezone",
                type="str",
                docstring="The timezone defined in the accounts events_timezone.",
            ),
        ]
        for attr in public_attributes:
            spec.public_attributes[attr.name] = attr
        public_methods = [
            types_utils.MethodSpec(
                name="get_posting_instructions",
                docstring="""
                    Gets a list of posting instruction objects, whose `value_datetime`s fall within
                    the requested time window. If a duration is specified in the `@requires`
                    decorator, the size of the time window will fall within
                    `[hook_effective_date - requirement_duration, hook_effective_date]`. If a
                    `fetcher_id` is specified in the
                    [postings](../account_fetcher_requirements/#postings) argument of the
                    `@fetch_account_data` decorator and passed as an argument in the
                    `get_posting_instructions` function call, then the time window is specified in
                    the definition of the
                    [PostingsIntervalFetcher](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#PostingsIntervalFetcher) with the
                    specified `fetcher_id` in the
                    [data_fetchers](../../smart_contracts_api_reference4xx/metadata/#data_fetchers)
                    list of the Contract metadata. The default ordering of the list is by
                    `value_datetime`; you can order/filter further using the sorted builtin and
                    other builtin mechanisms.
                """,  # noqa: E501
                args=[
                    types_utils.ValueSpec(
                        name="fetcher_id",
                        type="Optional[str]",
                        docstring="""
                            The id of the
                            [PostingsIntervalFetcher](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#PostingsIntervalFetcher).
                            1. Define the fetcher in the [Contract Metadata](../metadata/)
                            [data_fetchers](../../smart_contracts_api_reference4xx/metadata/#data_fetchers)
                            list. 2. Define the fetcher
                            id in the postings argument in the `@fetch_account_data` decorator. If
                            this function is called using a supervisee Vault object, the population
                            of this argument will raise an `InvalidSmartContractError`.
                        """,  # noqa: E501
                    ),
                ],
                return_value=types_utils.ReturnValueSpec(
                    docstring="""
                        The sorted list of posting instructions.
                    """,
                    type=common_types.postings._PITypes_str,  # noqa: SLF001
                ),
                examples=[
                    types_utils.Example(
                        title="An example with `@requires` decorator",
                        code="""
                            @requires(postings="1 month")
                            def post_posting_hook(vault, hook_arguments):
                                # Returns posting instructions in required range
                                # and covering client transactions postings
                                vault.get_posting_instructions()
                                # Raises InvalidSmartContractError
                                vault.get_posting_instructions(fetcher_id="fetcher_id")
                        """,
                    ),
                    types_utils.Example(
                        title="An example with `@fetch_account_data` decorator",
                        code="""
                            @fetch_account_data(postings=["fetcher_id"])
                            def post_posting_hook(vault, hook_arguments):
                                # Raises InvalidSmartContractError
                                vault.get_posting_instructions()
                                # Returns posting instructions in range defined in the fetcher.
                                vault.get_posting_instructions(fetcher_id="fetcher_id")
                                # Raises InvalidSmartContractError
                                vault.get_posting_instructions(fetcher_id="fetcher_not_in_decorator")
                        """,
                    ),
                ],
            ),
            types_utils.MethodSpec(
                name="get_client_transactions",
                docstring="""
                    Gets a map of the `unique_client_transaction_id` to
                    [ClientTransaction](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#ClientTransaction) objects,
                    with the `value_datetime` of at least one of its posting instructions falling
                    in the requested time window. Note that each posting instruction class instance
                    has the read-only `unique_client_transaction_id` attribute, representing
                    the ClientTransaction that a posting instruction is impacting, which can be used
                    as key in this map. However, the `unique_client_transaction_id` value is
                    not deterministic and therefore is not guaranteed to be consistent between
                    different contract executions for the same ClientTransaction.
                    If a duration is specified in the `@requires` decorator, the time window size is
                    in the range
                    `[hook_effective_date - requirement_duration, hook_effective_date]`.
                    If a `fetcher_id` is specified in the
                    [postings](../account_fetcher_requirements/#postings) argument of the
                    `@fetch_account_data` decorator and passed as an argument in the
                    `get_client_transactions` function call, then the time window is specified in
                    the definition of the
                    [PostingsIntervalFetcher](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#PostingsIntervalFetcher) with the
                    specified `fetcher_id` in the
                    [data_fetchers](../../smart_contracts_api_reference4xx/metadata/#data_fetchers)
                    list of the Contract metadata. The default ordering of the list of
                    posting instructions in each
                    [ClientTransaction](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#ClientTransaction), is by
                    `value_datetime`; you can order/filter further using the sorted builtin and
                    other builtin mechanisms.
                """,  # noqa: E501
                args=[
                    types_utils.ValueSpec(
                        name="fetcher_id",
                        type="Optional[str]",
                        docstring="""
                            The id of the
                            [PostingsIntervalFetcher](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#PostingsIntervalFetcher).
                            1. Define the fetcher in the [Contract Metadata](../metadata/)
                            [data_fetchers](../../smart_contracts_api_reference4xx/metadata/#data_fetchers)
                            list. 2. Define the fetcher id in the postings argument in the
                            `@fetch_account_data` decorator. If this function is called using a
                            supervisee Vault object, the population
                            of this argument will raise an `InvalidSmartContractError`.
                        """,  # noqa: E501
                    ),
                ],
                return_value=types_utils.ReturnValueSpec(
                    docstring="""
                        The [ClientTransaction](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#ClientTransaction) dictionary,
                        keyed by the `unique_client_transaction_id`.
                    """,  # noqa: E501
                    type="Dict[str, ClientTransaction]",
                ),
                examples=[],
            ),
            types_utils.MethodSpec(
                name="get_account_creation_datetime",
                docstring="""
                    Returns the date that the currently executing Account was created, or None if
                    the account has not yet been created.
                    """,
                args=[],
                return_value=types_utils.ReturnValueSpec(
                    docstring="""
                        The Account creation date as a timezone-aware UTC datetime.
                        Do not use the return value from this method as the `start_datetime` for
                        a `ScheduledEvent` as the `start_datetime` cannot be before the hook
                        `effective_datetime`.
                        This can happen under different circumstances. For example, accounts
                        are created with PENDING status before moving to OPEN status. This means
                        the account creation datetime is earlier than the `effective_datetime`
                        of the `activation_hook`.
                        If an account is created in OPEN status, then the activation_hook will
                        return None for this method.
                        """,
                    type="Optional[datetime]",
                ),
            ),
            types_utils.MethodSpec(
                name="get_balances_timeseries",
                docstring="""
                    Returns a Python mapping object, mapping [BalanceCoordinate](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#BalanceCoordinate)
                    to [BalanceTimeseries](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#BalanceTimeseries) covering
                    all balances over the time period specified by the hook decorator. If a
                    duration is specified in the `@requires` decorator, the time window
                    size is in the range
                    `[hook_effective_date - requirement_duration, hook_effective_date]`. If a
                    `fetcher_id` is specified in the
                    [balances](../account_fetcher_requirements/#balances) argument of the
                    `@fetch_account_data` decorator and passed as an argument in the function call,
                    then the time window is specified in the definition of the
                    [BalancesIntervalFetcher](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#BalancesIntervalFetcher) with the
                    specified `fetcher_id` in the
                    [data_fetchers](../../smart_contracts_api_reference4xx/metadata/#data_fetchers)
                    list of the Contract metadata. If no hook decorator is provided, then an empty
                    result is returned if no `fetcher_id` is passed as an argument, otherwise an
                    `InvalidSmartContractError` is raised.
                    Note that for performance reasons, each timeseries is lazy evaluated. Whilst it
                    is possible, iterating over all keys/items is not recommended. If a given
                    BalanceCoordinate object does not exist in the mapping, an empty
                    BalanceTimeseries will be returned.
                """,  # noqa: E501
                args=[
                    types_utils.ValueSpec(
                        name="fetcher_id",
                        type="Optional[str]",
                        docstring="""
                            The id of the
                            [BalancesIntervalFetcher](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#BalancesIntervalFetcher).
                            1. Define the fetcher in the [Contract Metadata](../metadata/)
                            [data_fetchers](../../smart_contracts_api_reference4xx/metadata/#data_fetchers)
                            list. 2. Define the fetcher id in the balances argument in the
                            `@fetch_account_data` decorator. If
                            this function is called using a supervisee Vault object, the population
                            of this argument will raise an `InvalidSmartContractError`.
                        """,  # noqa: E501
                    ),
                ],
                return_value=types_utils.ReturnValueSpec(
                    docstring="A dictionary of balance coordinates to timeseries of balances.",
                    type="Mapping[BalanceCoordinate, BalanceTimeseries]",
                ),
                examples=[
                    types_utils.Example(
                        title="An example with no decorator in Smart Contracts",
                        code="""
                            def conversion_hook(vault, hook_arguments):
                                # Raises InvalidSmartContractError.
                                vault.get_balances_timeseries()
                                # Raises InvalidSmartContractError.
                                vault.get_balances_timeseries(fetcher_id="fetcher_id")
                        """,
                    ),
                    types_utils.Example(
                        title="An example with no decorator in Supervisor Contracts",
                        code="""
                            def conversion_hook(vault, hook_arguments):
                                for account_id, supervisee in vault.supervisees.items():
                                    # Returns empty results.
                                    supervisee.get_balances_timeseries()
                                    # Raises InvalidSmartContractError.
                                    supervisee.get_balances_timeseries(fetcher_id="fetcher_id")
                        """,
                    ),
                    types_utils.Example(
                        title="An example with `@fetch_account_data` decorator in Smart Contracts",
                        code="""
                            @fetch_account_data(balances=["fetcher_id"])
                            def conversion_hook(vault, hook_arguments):
                                # Raises InvalidSmartContractError.
                                vault.get_balances_timeseries()
                                # Returns defaultdict[BalanceCoordinate, BalanceTimeseries]
                                # in range defined in the fetcher.
                                vault.get_balances_timeseries(fetcher_id="fetcher_id")
                                # Raises InvalidSmartContractError.
                                vault.get_balances_timeseries(fetcher_id="fetcher_not_in_decorator")
                        """,
                    ),
                    types_utils.Example(
                        title="An example with `@requires` decorator in Supervisor Contracts",
                        code="""
                            @requires(data_scope="all", balances="1 month")
                            def conversion_hook(vault, hook_arguments):
                                for account_id, supervisee in vault.supervisees.items():
                                    # Returns defaultdict[BalanceCoordinate, BalanceTimeseries]
                                    # in required range.
                                    supervisee.get_balances_timeseries()
                                    # Raises InvalidSmartContractError.
                                    supervisee.get_balances_timeseries(fetcher_id="fetcher_id")
                        """,
                    ),
                ],
            ),
            types_utils.MethodSpec(
                name="get_hook_execution_id",
                docstring="""
                    Returns a string used in generating unique-enough ids
                    for attaching to side-effect
                    objects. The string returned is a combination of
                    account_id, hook, and effective_datetime.
                """,
                args=[],
                return_value=types_utils.ReturnValueSpec(docstring="The unique-enough id.", type="str"),
            ),
        ]
        get_parameter_methods = [
            types_utils.MethodSpec(
                name="get_parameter_timeseries",
                docstring="""
                    Get the ParameterTimeseries containing all timeseries across all contract
                    parameters defined and/or used by this Smart Contract.

                    If `parameters=True` is not specified in the `@requires` decorator, any call
                    to this function will fail.

                    Values for derived parameters are not returned from this function.
                """,
                args=[
                    types_utils.ValueSpec(
                        name="name",
                        type="str",
                        docstring="The name of the [ContractParameter](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#ContractParameter].",  # noqa: E501
                    ),
                ],
                return_value=types_utils.ReturnValueSpec(docstring="The timeseries of parameters.", type="ParameterTimeseries"),
            ),
        ]

        public_methods += get_parameter_methods
        public_methods += [
            types_utils.MethodSpec(
                name="get_flag_timeseries",
                docstring="""
                    Get the FlagTimeseries for a given flag definition.

                    If `flags=True` is not specified in the `@requires` decorator, any call
                    to this function will return an empty FlagTimeseries.
                """,
                args=[
                    types_utils.ValueSpec(
                        name="flag",
                        type="str",
                        docstring="The `flag_definition_id` to get the timeseries for.",
                    ),
                ],
                return_value=types_utils.ReturnValueSpec(docstring="The timeseries of flags.", type="FlagTimeseries"),
            ),
            types_utils.MethodSpec(
                name="get_hook_result",
                docstring="""
                    Returns the Supervisee Hook Result. Available for use only on the Supervisees
                    [Vault](/reference/contracts/contracts_api_4xx/smart_contracts_api_reference4xx/vault/)
                    object. This function allows the Supervisor Hook to access any Supervisee Hook
                    uncommitted `HookDirectives`, `Rejections` or Return Data.
                """,
                args=[],
                return_value=types_utils.ReturnValueSpec(
                    docstring="The Supervisee Hook Result",
                    type="Union[PostPostingHookResult, PrePostingHookResult, " "ScheduledEventHookResult]",
                ),
                examples=[
                    types_utils.Example(
                        title="An example with Rejection.",
                        code="""
                        # Supervisor Hook.
                        def pre_posting_hook(vault, hook_arguments):
                            for account_id, supervisee in vault.supervisees.items():
                                supervisee_hook_result = supervisee.get_hook_result()
                                # Check if Supervisee Hook returned Rejection.
                                if supervisee_hook_result.rejection:
                                    return SupervisorPrePostingHookResult(
                                        rejection=Rejection(
                                            message=(
                                                f"Supervisee Hook with account_id {account_id} "
                                                "Returned Rejection"
                                            ),
                                            reason_code=RejectionReason.AGAINST_TNC
                                        )
                                    )
                        """,
                    ),
                    types_utils.Example(
                        title="An example with Directives.",
                        code="""
                        # Supervisor Hook.
                        def scheduled_event_hook(vault, hook_arguments):
                            # Access and re-instruct Supervisee Hook Directives.
                            supervisee_posting_instructions_directives = {}
                            for account_id, supervisee in vault.supervisees.items():
                                supervisee_posting_instructions_directives[account_id] = []
                                supervisee_hook_result = supervisee.get_hook_result()
                                for (
                                    posting_instruction_directive
                                    in supervisee_hook_result.posting_instructions_directives
                                ):
                                    supervisee_posting_instructions_directives[account_id].append(
                                        posting_instructions_directive
                                    )

                            return SupervisorScheduledEventHookResult(
                                supervisee_posting_instructions_directives=(
                                    supervisee_posting_instructions_directives
                                )
                            )
                        """,
                    ),
                ],
            ),
            types_utils.MethodSpec(
                name="get_alias",
                docstring="""
                    Returns the alias value set for the Smart Contract Version in the Supervisor
                    [SmartContractDescriptor](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#SmartContractDescriptor)
                    object. Available in Supervisor Contract code for use on the Supervisee's
                    [Vault](/reference/contracts/contracts_api_4xx/smart_contracts_api_reference4xx/vault/)
                    object only. If no aliases are defined in the
                    Supervisor Contract metadata, then 'None' is returned. It cannot be used on a
                    non-supervised Vault object.
                """,  # noqa: E501
                args=[],
                return_value=types_utils.ReturnValueSpec(docstring="The Supervisee Smart Contract Version alias.", type="str"),
            ),
            types_utils.MethodSpec(
                name="get_permitted_denominations",
                docstring="""
                    Returns the permitted denominations of the account.
                """,
                args=[],
                return_value=types_utils.ReturnValueSpec(docstring="A list of denominations.", type="List[str]"),
            ),
            types_utils.MethodSpec(
                name="get_calendar_events",
                docstring="""
                    Returns a [CalendarEvents](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#CalendarEvents) object with the
                    chronologically ordered list of [CalendarEvent](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#CalendarEvent)
                    that exist in the Vault calendars with the given `calendar_ids`. These
                    `calendar_ids` have to be requested using the hook '@requires' decorator.
                    For information about the time range of events returned,
                    see [calendar](/reference/contracts/contracts_api_4xx/smart_contracts_api_reference4xx/hook_requirements/#calendar)
                """,  # noqa: E501
                args=[
                    types_utils.ValueSpec(name="calendar_ids", type="List[str]", docstring="List of Calendar Ids"),
                ],
                return_value=types_utils.ReturnValueSpec(
                    docstring="""
                        The chronologically ordered list of
                        [CalendarEvent](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#CalendarEvent) objects.
                    """,  # noqa: E501
                    type="CalendarEvents",
                ),
                examples=[
                    types_utils.Example(
                        title="The Vault calendar usage example",
                        code="""
                        @requires(calendar=["WEEKENDS", "BANK_HOLIDAYS", "PROMOTION_DAYS"])
                        def activation_hook(vault, hook_arguments):
                            vault.get_calendar_events(calendar_ids=["WEEKENDS", "BANK_HOLIDAYS"])
                        """,
                    )
                ],
            ),
            types_utils.MethodSpec(
                name="get_balances_observation",
                docstring="""
                    Returns the [BalancesObservation](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#BalancesObservation) at the
                    datetime defined by the
                    [BalancesObservationFetcher](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#BalancesObservationFetcher)
                    whose id is provided in the
                    [balances](../account_fetcher_requirements/#balances) argument of the
                    `@fetch_account_data` decorator.
                """,  # noqa: E501
                args=[
                    types_utils.ValueSpec(
                        name="fetcher_id",
                        type="str",
                        docstring="""
                            The id of the
                            [BalancesObservationFetcher](/reference/contracts/contracts_api_4xx/common_types_4xx/classes/#BalancesObservationFetcher).
                            1. Define the fetcher in the [Contract Metadata](../metadata/)
                            [data_fetchers](../../smart_contracts_api_reference4xx/metadata/#data_fetchers)
                            list. 2. Define the fetcher id in the balances argument in the
                            `@fetch_account_data` decorator.
                        """,  # noqa: E501
                    ),
                ],
                return_value=types_utils.ReturnValueSpec(
                    docstring="""
                        The observation which includes the Balances and the datetime at which the
                        values apply.
                    """,
                    type="BalancesObservation",
                ),
                examples=[
                    types_utils.Example(
                        title="An example with no decorator",
                        code="""
                            def activation_hook(vault, hook_arguments):
                                # Raises InvalidSmartContractError
                                vault.get_balances_observation()
                                # Raises InvalidSmartContractError
                                vault.get_balances_observation(fetcher_id="fetcher_id")
                        """,
                    ),
                    types_utils.Example(
                        title="An example with @requires decorator",
                        code="""
                            @requires(balances="1 month")
                            def activation_hook(vault, hook_arguments):
                                # Raises InvalidSmartContractError
                                vault.get_balances_observation()
                                # Raises InvalidSmartContractError
                                vault.get_balances_observation(fetcher_id="fetcher_id")
                        """,
                    ),
                    types_utils.Example(
                        title="An example with `@fetch_account_data` decorator",
                        code="""
                            @fetch_account_data(balances=["fetcher_id"])
                            def activation_hook(vault, hook_arguments):
                                # Raises InvalidSmartContractError
                                vault.get_balances_observation()
                                # Returns BalancesObservation at the datetime defined in the
                                # fetcher
                                vault.get_balances_observation(fetcher_id="fetcher_id")
                                # Raises InvalidSmartContractError
                                vault.get_balances_observation(fetcher_id="fetcher_not_in_decorator")
                        """,
                    ),
                ],
            ),
        ]
        for method in public_methods:
            spec.public_methods[method.name] = method
        return spec
