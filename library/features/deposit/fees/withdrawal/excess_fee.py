# Copyright @ 2023 Thought Machine Group Limited. All rights reserved.

# CBF: CPP-1965

# standard libs
from datetime import datetime
from dateutil.relativedelta import relativedelta
from decimal import Decimal

# features
import library.features.common.client_transaction_utils as client_transaction_utils
import library.features.common.common_parameters as common_parameters
import library.features.common.fees as fees
import library.features.common.fetchers as fetchers
import library.features.common.utils as utils

# contracts api
from contracts_api import (
    AccountIdShape,
    ClientTransaction,
    CustomInstruction,
    NumberShape,
    OptionalShape,
    OptionalValue,
    Parameter,
    ParameterLevel,
    Rejection,
    RejectionReason,
    StringShape,
)

# inception sdk
from inception_sdk.vault.contracts.extensions.contracts_api_extensions import SmartContractVault

# instruction detail key
INSTRUCTION_DETAIL_KEY = "TRANSACTION_TYPE"

# Parameters
PARAM_EXCESS_FEE = "excess_fee"
PARAM_PERMITTED_WITHDRAWALS = "permitted_withdrawals"
PARAM_EXCESS_FEE_MONITORED_TRANSACTION_TYPE = "excess_fee_monitored_transaction_type"
PARAM_EXCESS_FEE_ACCOUNT = "excess_fee_income_account"
PARAM_BLOCK_EXCESS_WITHDRAWALS = "block_excess_withdrawals"

parameters = [
    Parameter(
        name=PARAM_EXCESS_FEE,
        level=ParameterLevel.TEMPLATE,
        description="Fee charged for every withdrawal that exceeds the monthly withdrawal limit.",
        display_name="Excess Fee",
        shape=OptionalShape(shape=NumberShape(min_value=0, step=Decimal("0.01"))),
        default_value=OptionalValue(Decimal("0.00")),
    ),
    Parameter(
        name=PARAM_PERMITTED_WITHDRAWALS,
        level=ParameterLevel.TEMPLATE,
        description="Number of monthly permitted withdrawals. Please note that only transactions "
        "with the specified transaction type are counted towards this excess fee.",
        display_name="Permitted Withdrawals",
        shape=OptionalShape(shape=NumberShape(min_value=0, step=1)),
        default_value=OptionalValue(0),
    ),
    Parameter(
        name=PARAM_EXCESS_FEE_MONITORED_TRANSACTION_TYPE,
        level=ParameterLevel.TEMPLATE,
        description="Transaction type being monitored to determine how many operations of this type"
        " occurred in the current calendar month period. This parameter will only be used for the "
        " assessment of the excessive withdrawal fee.",
        display_name="Monitored Transaction Type",
        shape=OptionalShape(shape=StringShape()),
        default_value=OptionalValue(""),
    ),
    # Internal Account
    Parameter(
        name=PARAM_EXCESS_FEE_ACCOUNT,
        level=ParameterLevel.TEMPLATE,
        description="Internal account for excess fee income balance.",
        display_name="Withdrawal Excess Fee Account",
        shape=AccountIdShape(),
        default_value="EXCESS_FEE_INCOME_ACCOUNT",
    ),
    Parameter(
        name=PARAM_BLOCK_EXCESS_WITHDRAWALS,
        level=ParameterLevel.TEMPLATE,
        description="When configured, if the number of permitted withdrawals is exceeded,"
        " any subsequent withdrawals are blocked. If this is not configured, the withdrawal"
        " is accepted and the Excess Fee will be applied.",
        display_name="Block Excess Withdrawals",
        shape=OptionalShape(shape=common_parameters.BooleanShape),
        default_value=OptionalValue(common_parameters.BooleanValueFalse),
    ),
]


def validate(
    *,
    vault: SmartContractVault,
    proposed_client_transactions: dict[str, ClientTransaction],
    monthly_client_transactions: dict[str, ClientTransaction] | None = None,
    effective_datetime: datetime,
    denomination: str,
) -> Rejection | None:
    """
    For use in the pre_posting_hook.
    Check number of posting instructions have occurred month to date and reject proposed withdrawals
    if the monthly withdrawal limit has been exceeded and Block Excess Withdrawals is set.
    Only transactions with instruction details that has a key matching "INSTRUCTION_DETAIL_KEY"
    parameter, with a value matching "PARAM_MONITORED_TRANSACTION_TYPE" param are eligible for
    this excess withdrawal fee.

    :param vault: vault object used to retrieve parameters
    :param proposed_client_transactions: proposed client transactions to process
    :param monthly_client_transactions: monthly client transactions to process
    :param effective_datetime: datetime used to filter client transactions
    :param denomination: denomination used to filter posting instructions
    :return: rejection if the above condition is met
    """
    block_excess_withdrawals = bool(
        utils.get_parameter(
            vault,
            PARAM_BLOCK_EXCESS_WITHDRAWALS,
            is_boolean=True,
            is_optional=True,
            default_value=common_parameters.BooleanValueFalse,
        )
    )
    if not block_excess_withdrawals:
        return None

    withdrawals = _fetch_withdrawals(
        vault=vault,
        proposed_client_transactions=proposed_client_transactions,
        monthly_client_transactions=monthly_client_transactions,
        effective_datetime=effective_datetime,
        denomination=denomination,
    )
    if not withdrawals:
        return None
    current_withdrawals, proposed_withdrawals, permitted_withdrawals = withdrawals

    if current_withdrawals + proposed_withdrawals > permitted_withdrawals:
        return Rejection(
            message=f"Transactions would cause the maximum monthly withdrawal limit of "
            f"{permitted_withdrawals} to be exceeded.",
            reason_code=RejectionReason.AGAINST_TNC,
        )

    return None


def apply(
    *,
    vault: SmartContractVault,
    proposed_client_transactions: dict[str, ClientTransaction],
    monthly_client_transactions: dict[str, ClientTransaction] | None = None,
    effective_datetime: datetime,
    denomination: str,
    account_type: str = "",
) -> list[CustomInstruction]:
    """
    Check number of posting instructions have occurred month to date and return fees if the
    withdrawal limit has been exceeded.
    Only transactions with instruction details that has a key matching "INSTRUCTION_DETAIL_KEY"
    parameter, with a value matching "PARAM_MONITORED_TRANSACTION_TYPE" param are eligible for
    this excess withdrawal fee.

    :param vault: vault object used to retrieve parameters
    :param proposed_client_transactions: proposed client transactions to process
    :param monthly_client_transactions: monthly client transactions to process
    :param effective_datetime: datetime used to filter client transactions
    :param denomination: denomination used to filter posting instructions
    :param account_type: the account type
    :return: excess fee posting instructions
    """
    excess_fee_amount = Decimal(
        utils.get_parameter(vault, PARAM_EXCESS_FEE, is_optional=True, default_value=0)
    )

    if excess_fee_amount <= Decimal("0"):
        return []

    withdrawals = _fetch_withdrawals(
        vault=vault,
        proposed_client_transactions=proposed_client_transactions,
        monthly_client_transactions=monthly_client_transactions,
        effective_datetime=effective_datetime,
        denomination=denomination,
    )
    if not withdrawals:
        return []
    current_withdrawals, proposed_withdrawals, permitted_withdrawals = withdrawals

    if permitted_withdrawals < 0:
        return []

    proposed_exceeding_withdrawals = (
        proposed_withdrawals + current_withdrawals - permitted_withdrawals
    )

    if proposed_exceeding_withdrawals <= 0:
        return []

    # If withdrawals already exceeded then charge fee for every new withdrawal.
    if current_withdrawals > permitted_withdrawals:
        proposed_exceeding_withdrawals = proposed_withdrawals

    excess_fee_income_account = utils.get_parameter(vault, PARAM_EXCESS_FEE_ACCOUNT)
    return fees.fee_custom_instruction(
        customer_account_id=vault.account_id,
        denomination=denomination,
        amount=excess_fee_amount * proposed_exceeding_withdrawals,
        internal_account=excess_fee_income_account,
        instruction_details=utils.standard_instruction_details(
            description="Proposed withdrawals exceeded permitted "
            f"limit by {proposed_exceeding_withdrawals}",
            event_type="APPLY_EXCESS_FEES",
            gl_impacted=True,
            account_type=account_type,
        ),
    )


def _fetch_withdrawals(
    *,
    vault: SmartContractVault,
    proposed_client_transactions: dict[str, ClientTransaction],
    monthly_client_transactions: dict[str, ClientTransaction] | None = None,
    effective_datetime: datetime,
    denomination: str,
) -> tuple[int, int, int] | None:
    """
    Fetch the number of current_withdrawals, proposed_withdrawals, and permitted_withdrawals
    postings to be used in validate() and apply().
    current_withdrawals is the number of the filtered monthly posting instructions.
    proposed_withdrawals is the number of filtered proposed posting instructions.
    permitted_withdrawals is the number of monthly permitted withdrawals.

    :param vault: vault object used to retrieve parameters
    :param proposed_client_transactions: proposed client transactions to process
    :param monthly_client_transactions: monthly client transactions to process
    :param effective_datetime: datetime used to filter client transactions
    :param denomination: denomination used to filter posting instructions
    :return: numbers of current_withdrawals, proposed_withdrawals, permitted_withdrawals in a tuple
    """
    transaction_type: str = utils.get_parameter(
        vault, PARAM_EXCESS_FEE_MONITORED_TRANSACTION_TYPE, is_optional=True, default_value=""
    )
    if not transaction_type:
        return None

    filtered_proposed_posting_instructions = (
        client_transaction_utils.extract_debits_by_instruction_details_key(
            denomination=denomination,
            client_transactions=proposed_client_transactions,
            client_transaction_ids_to_ignore=[],
            cutoff_datetime=effective_datetime,
            key=INSTRUCTION_DETAIL_KEY,
            value=transaction_type,
        )
    )
    if not filtered_proposed_posting_instructions:
        return None

    if not monthly_client_transactions:
        monthly_client_transactions = vault.get_client_transactions(
            fetcher_id=fetchers.MONTH_TO_EFFECTIVE_POSTINGS_FETCHER_ID
        )

    filtered_monthly_posting_instructions = (
        client_transaction_utils.extract_debits_by_instruction_details_key(
            denomination=denomination,
            client_transactions=monthly_client_transactions,
            client_transaction_ids_to_ignore=list(proposed_client_transactions.keys()),
            cutoff_datetime=effective_datetime
            + relativedelta(day=1, hour=0, minute=0, second=0, microsecond=0),
            key=INSTRUCTION_DETAIL_KEY,
            value=transaction_type,
        )
    )

    current_withdrawals = len(filtered_monthly_posting_instructions)
    proposed_withdrawals = len(filtered_proposed_posting_instructions)
    permitted_withdrawals = int(
        utils.get_parameter(vault, PARAM_PERMITTED_WITHDRAWALS, is_optional=True, default_value=-1)
    )

    return current_withdrawals, proposed_withdrawals, permitted_withdrawals
