# standard libs
from decimal import Decimal
from typing import Callable, NamedTuple

# contracts api
from contracts_api import CustomInstruction, Posting

EarlyRepaymentFee = NamedTuple(
    "EarlyRepaymentFee",
    [
        (
            "get_early_repayment_fee_amount",
            Callable[
                # vault: SmartContractVault,
                # balances: BalanceDefaultDict | None = None,
                # denomination: str | None = None,
                # precision: int = 2,
                ...,
                Decimal,
            ],
        ),
        (
            "charge_early_repayment_fee",
            Callable[
                # vault: SmartContractVault,
                # account_id: str,
                # amount_to_charge: Decimal,
                # fee_name: str,
                # denomination: str | None = None,
                ...,
                list[CustomInstruction],
            ],
        ),
        (
            "fee_name",
            # Name of the early repayment fee
            str,
        ),
    ],
)


InterestAmounts = NamedTuple(
    "InterestAmounts",
    [
        ("emi_rounded_accrued", Decimal),
        ("emi_accrued", Decimal),
        ("non_emi_rounded_accrued", Decimal),
        ("non_emi_accrued", Decimal),
        ("total_rounded", Decimal),
    ],
)

InterestApplication = NamedTuple(
    "InterestApplication",
    [
        (
            "apply_interest",
            Callable[
                # vault: SmartContractVault,
                # effective_datetime: datetime,
                # previous_application_datetime: datetime
                # balances_at_application: BalanceDefaultDict | None = None,
                ...,
                list[Posting],
            ],
        ),
        (
            "get_interest_to_apply",
            Callable[
                # vault: SmartContractVault,
                # effective_datetime: datetime,
                # previous_application_datetime: datetime,
                # balances_at_application: BalanceDefaultDict | None = None,
                # balances_one_repayment_period_ago: BalanceDefaultDict | None = None,
                # denomination: str,
                # application_precision: int | None = None,
                ...,
                InterestAmounts,
            ],
        ),
        (
            "get_application_precision",
            Callable[
                # vault: SmartContractVault,
                ...,
                int,
            ],
        ),
    ],
)

InterestRate = NamedTuple(
    "InterestRate",
    [
        (
            "get_daily_interest_rate",
            Callable[
                # vault: SmartContractVault,
                # effective_datetime: datetime,
                ...,
                Decimal,
            ],
        ),
        (
            "get_monthly_interest_rate",
            Callable[
                # vault: SmartContractVault,
                # effective_datetime: datetime | None,
                # balances: BalanceDefaultDict | None,
                # denomination: str | None
                ...,
                Decimal,
            ],
        ),
        (
            "get_annual_interest_rate",
            Callable[
                # vault: SmartContractVault,
                # effective_datetime: datetime | None,
                # balances: BalanceDefaultDict | None,
                # denomination: str | None
                ...,
                Decimal,
            ],
        ),
    ],
)

Overpayment = NamedTuple(
    "Overpayment",
    [
        (
            "handle_overpayment",
            Callable[
                # vault: SmartContractVault,
                # overpayment_amount: Decimal,
                # denomination: str,
                # balances: BalanceDefaultDict,
                ...,
                list[Posting],
            ],
        ),
    ],
)

MultiTargetOverpayment = NamedTuple(
    "MultiTargetOverpayment",
    [
        (
            "handle_overpayment",
            Callable[
                # main_vault: SuperviseeContractVault,
                # overpayment_amount: Decimal,
                # denomination: str,
                # balances_per_target_vault: dict[SuperviseeContractVault, BalanceDefaultDict],
                ...,
                dict[str, list[Posting]],
            ],
        )
    ],
)

PrincipalAdjustment = NamedTuple(
    "PrincipalAdjustment",
    [
        (
            "calculate_principal_adjustment",
            Callable[
                # vault: SmartContractVault,
                # balances: BalanceDefaultDict | None,
                # denomination: str | None
                ...,
                Decimal,
            ],
        ),
    ],
)

SupervisorPrincipalAdjustment = NamedTuple(
    "SupervisorPrincipalAdjustment",
    [
        (
            "calculate_principal_adjustment",
            Callable[
                # loan_vault: SuperviseeContractVault,
                # main_vault: SuperviseeContractVault,
                # balances: BalanceDefaultDict | None,
                # denomination: str | None
                ...,
                Decimal,
            ],
        ),
    ],
)

ResidualCleanup = NamedTuple(
    "ResidualCleanup",
    [
        (
            "get_residual_cleanup_postings",
            Callable[
                # balances: BalanceDefaultDict, account_id:str , denomination: str
                ...,
                list[Posting],
            ],
        ),
    ],
)

Amortisation = NamedTuple(
    "Amortisation",
    [
        (
            "calculate_emi",
            Callable[
                # vault: SmartContractVault,
                # effective_datetime: datetime,
                # use_expected_term: bool,
                # Decimal | None (principal_amount)
                # lending_interfaces.InterestRate | None (interest_calculation_feature)
                # list[lending_interfaces.PrincipalAdjustment] | None (principal_adjustments)
                # BalanceDefaultDict | None (balances)
                ...,
                Decimal,
            ],
        ),
        (
            "term_details",
            Callable[
                # vault: SmartContractVault,
                # effective_datetime: datetime,
                # use_expected_term: bool,
                # interest_rate: InterestRate | None,
                # principal_adjustments: list[PrincipalAdjustment] | None,
                # balances: BalanceDefaultDict | None,
                # denomination: str | None
                ...,
                # elapsed term, remaining term
                tuple[int, int],
            ],
        ),
        (
            "override_final_event",
            # Override the final event where we do not want to move the remaining principal
            # to principal due. An example of this is for balloon payments where the final
            # principal application will be deferred for the balloon payment.
            bool,
        ),
    ],
)

SupervisorAmortisation = NamedTuple(
    "SupervisorAmortisation",
    [
        (
            "calculate_emi",
            Callable[
                # loan_vault: SuperviseeContractVault,
                # main_vault: SuperviseeContractVault,
                # effective_datetime: datetime,
                # use_expected_term: bool,
                # principal_amount: Decimal | None,
                # interest_calculation_feature: InterestRate | None,
                # principal_adjustments: list[PrincipalAdjustment] | None,
                # balances: BalanceDefaultDict | None,
                ...,
                Decimal,
            ],
        ),
        (
            "term_details",
            Callable[
                # loan_vault: SuperviseeContractVault,
                # effective_datetime: datetime,
                # use_expected_term: bool,
                # interest_rate: InterestRate | None,
                # principal_adjustments: list[PrincipalAdjustment] | None,
                # balances: BalanceDefaultDict | None,
                # denomination: str | None
                ...,
                # elapsed term, remaining term
                tuple[int, int],
            ],
        ),
        (
            "override_final_event",
            # Override the final event where we do not want to move the remaining principal
            # to principal due. An example of this is for balloon payments where the final
            # principal application will be deferred for the balloon payment.
            bool,
        ),
    ],
)

ReamortisationCondition = NamedTuple(
    "ReamortisationCondition",
    [
        (
            "should_trigger_reamortisation",
            Callable[
                # vault: SmartContractVault,
                # period_start_datetime: datetime,
                # period_end_datetime: datetime,
                # int | None (elapsed_term)
                ...,
                bool,
            ],
        ),
    ],
)

SupervisorReamortisationCondition = NamedTuple(
    "SupervisorReamortisationCondition",
    [
        (
            "should_trigger_reamortisation",
            Callable[
                # loan_vault: SuperviseeContractVault,
                # main_vault: SuperviseeContractVault,
                # period_start_datetime: datetime,
                # period_end_datetime: datetime,
                # elapsed_term: int | None,
                # balances: BalanceDefaultDict | None,
                ...,
                bool,
            ],
        ),
    ],
)
