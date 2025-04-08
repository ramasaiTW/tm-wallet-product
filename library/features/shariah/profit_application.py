# standard libs
from datetime import datetime
from dateutil.relativedelta import relativedelta

# features
import library.features.common.accruals as accruals
import library.features.common.fetchers as fetchers
import library.features.common.utils as utils
import library.features.shariah.tiered_profit_accrual as tiered_profit_accrual

# contracts api
from contracts_api import (
    DEFAULT_ADDRESS,
    AccountIdShape,
    BalanceDefaultDict,
    CustomInstruction,
    NumberShape,
    Parameter,
    ParameterLevel,
    ParameterUpdatePermission,
    ScheduledEvent,
    SmartContractEventType,
    UnionItem,
    UnionItemValue,
    UnionShape,
    UpdateAccountEventTypeDirective,
)

# inception sdk
from inception_sdk.vault.contracts.extensions.contracts_api_extensions import SmartContractVault

# Event
APPLICATION_EVENT = "APPLY_PROFIT"

# Fetchers
data_fetchers = [fetchers.EOD_FETCHER]

# Balance Addresses
ACCRUED_PROFIT_PAYABLE = tiered_profit_accrual.ACCRUED_PROFIT_PAYABLE

# Parameters
PROFIT_APPLICATION_PREFIX = "profit_application"

PARAM_PROFIT_APPLICATION_DAY = f"{PROFIT_APPLICATION_PREFIX}_day"
PARAM_PROFIT_APPLICATION_FREQUENCY = f"{PROFIT_APPLICATION_PREFIX}_frequency"
PARAM_PROFIT_APPLICATION_HOUR = f"{PROFIT_APPLICATION_PREFIX}_hour"
PARAM_PROFIT_APPLICATION_MINUTE = f"{PROFIT_APPLICATION_PREFIX}_minute"
PARAM_PROFIT_APPLICATION_SECOND = f"{PROFIT_APPLICATION_PREFIX}_second"
schedule_params = [
    Parameter(
        name=PARAM_PROFIT_APPLICATION_DAY,
        shape=NumberShape(min_value=1, max_value=31, step=1),
        level=ParameterLevel.INSTANCE,
        description="The day of the month on which profit is applied. If day does not exist"
        " in application month, applies on last day of month.",
        display_name="Profit Application Day",
        update_permission=ParameterUpdatePermission.USER_EDITABLE,
        default_value=1,
    ),
    Parameter(
        name=PARAM_PROFIT_APPLICATION_FREQUENCY,
        level=ParameterLevel.TEMPLATE,
        description="The frequency at which profit is applied.",
        display_name="Profit Application Frequency",
        shape=UnionShape(
            items=[
                UnionItem(key="monthly", display_name="Monthly"),
                UnionItem(key="quarterly", display_name="Quarterly"),
                UnionItem(key="annually", display_name="Annually"),
            ]
        ),
        default_value=UnionItemValue(key="monthly"),
    ),
    Parameter(
        name=PARAM_PROFIT_APPLICATION_HOUR,
        level=ParameterLevel.TEMPLATE,
        description="The hour of the day at which profit is applied.",
        display_name="Profit Application Hour",
        shape=NumberShape(min_value=0, max_value=23, step=1),
        default_value=0,
    ),
    Parameter(
        name=PARAM_PROFIT_APPLICATION_MINUTE,
        level=ParameterLevel.TEMPLATE,
        description="The minute of the hour at which profit is applied.",
        display_name="Profit Application Minute",
        shape=NumberShape(min_value=0, max_value=59, step=1),
        default_value=0,
    ),
    Parameter(
        name=PARAM_PROFIT_APPLICATION_SECOND,
        level=ParameterLevel.TEMPLATE,
        description="The second of the minute at which profit is applied.",
        display_name="Profit Application Second",
        shape=NumberShape(min_value=0, max_value=59, step=1),
        default_value=1,
    ),
]

PARAM_APPLICATION_PRECISION = "application_precision"
PARAM_PROFIT_PAID_ACCOUNT = "profit_paid_account"
parameters = [
    # Template parameters
    Parameter(
        name=PARAM_APPLICATION_PRECISION,
        level=ParameterLevel.TEMPLATE,
        description="Precision needed for profit applications.",
        display_name="Profit Application Precision",
        shape=NumberShape(min_value=0, max_value=15, step=1),
        default_value=2,
    ),
    # Internal accounts
    Parameter(
        name=PARAM_PROFIT_PAID_ACCOUNT,
        level=ParameterLevel.TEMPLATE,
        description="Internal account for profit paid.",
        display_name="Profit Paid Account",
        shape=AccountIdShape(),
        default_value="APPLIED_PROFIT_PAID",
    ),
    *schedule_params,
]


def event_types(product_name: str) -> list[SmartContractEventType]:
    return [
        SmartContractEventType(
            name=APPLICATION_EVENT,
            scheduler_tag_ids=[f"{product_name.upper()}_{APPLICATION_EVENT}_AST"],
        )
    ]


def scheduled_events(
    *,
    vault: SmartContractVault,
    start_datetime: datetime,
) -> dict[str, ScheduledEvent]:
    """
    Creates list of execution schedules for profit application
    :param vault: Vault object to retrieve application frequency and schedule params
    :param start_datetime: date to start schedules from e.g. account creation or loan start date
    :return: dict of profit application scheduled events
    """
    application_frequency: str = utils.get_parameter(
        vault, name=PARAM_PROFIT_APPLICATION_FREQUENCY, is_union=True
    )

    schedule_day = int(utils.get_parameter(vault, name=PARAM_PROFIT_APPLICATION_DAY))
    schedule_hour, schedule_minute, schedule_second = utils.get_schedule_time_from_parameters(
        vault=vault, parameter_prefix=PROFIT_APPLICATION_PREFIX
    )

    calendar_events = vault.get_calendar_events(calendar_ids=["&{PUBLIC_HOLIDAYS}"])

    next_datetime = utils.get_next_schedule_date_calendar_aware(
        start_datetime=start_datetime,
        schedule_frequency=application_frequency,
        intended_day=schedule_day,
        calendar_events=calendar_events,
    )
    modified_expression = utils.one_off_schedule_expression(
        next_datetime
        + relativedelta(hour=schedule_hour, minute=schedule_minute, second=schedule_second)
    )
    scheduled_event = ScheduledEvent(start_datetime=start_datetime, expression=modified_expression)

    return {APPLICATION_EVENT: scheduled_event}


def apply_profit(
    *,
    vault: SmartContractVault,
    accrual_address: str = ACCRUED_PROFIT_PAYABLE,
    account_type: str | None = None,
) -> list[CustomInstruction]:
    """
    Creates the posting instructions to consolidate accrued profit.
    Debit the rounded amount from the customer accrued address and credit the internal account
    Debit the rounded amount from the internal account to the customer applied address
    :param vault: the vault object to use to for retrieving data and instructing directives
    :param accrual_address: the address to check for profit that has accumulated
    :return: the accrual posting instructions
    """

    accrued_profit_payable_account: str = utils.get_parameter(
        vault, name=tiered_profit_accrual.PARAM_ACCRUED_PROFIT_PAYABLE_ACCOUNT
    )
    profit_paid_account: str = utils.get_parameter(vault, name=PARAM_PROFIT_PAID_ACCOUNT)

    application_precision: int = utils.get_parameter(vault, name=PARAM_APPLICATION_PRECISION)
    denomination: str = utils.get_parameter(vault, name="denomination")

    balances: BalanceDefaultDict = vault.get_balances_observation(
        fetcher_id=fetchers.EOD_FETCHER_ID
    ).balances
    amount_accrued = utils.balance_at_coordinates(
        balances=balances,
        address=accrual_address,
        denomination=denomination,
    )
    rounded_accrual = utils.round_decimal(amount_accrued, application_precision)

    custom_instructions: list[CustomInstruction] = []

    # negative profit not supported
    if amount_accrued > 0:
        if account_type is None:
            account_type = ""

        custom_instructions.extend(
            accruals.accrual_application_custom_instruction(
                customer_account=vault.account_id,
                denomination=denomination,
                application_amount=abs(rounded_accrual),
                accrual_amount=abs(amount_accrued),
                instruction_details=utils.standard_instruction_details(
                    description=f"Apply {rounded_accrual} {denomination} profit of "
                    f"{amount_accrued} rounded to {application_precision} and "
                    f"consolidate {amount_accrued} {denomination} to {vault.account_id}",
                    event_type=APPLICATION_EVENT,
                    gl_impacted=True,
                    account_type=account_type,
                ),
                accrual_customer_address=accrual_address,
                accrual_internal_account=accrued_profit_payable_account,
                application_customer_address=DEFAULT_ADDRESS,
                application_internal_account=profit_paid_account,
                payable=True,
            )
        )

    return custom_instructions


def update_next_schedule_execution(
    *, vault: SmartContractVault, effective_datetime: datetime
) -> UpdateAccountEventTypeDirective | None:
    """
    Update next scheduled execution.
    :param vault: Vault object to retrieve profit application params
    :param effective_datetime: datetime the schedule is running
    :return: update event directive
    """
    new_schedule = scheduled_events(vault=vault, start_datetime=effective_datetime)

    return UpdateAccountEventTypeDirective(
        event_type=APPLICATION_EVENT, expression=new_schedule[APPLICATION_EVENT].expression
    )
