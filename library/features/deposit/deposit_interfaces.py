# standard libs
from decimal import Decimal
from typing import Callable, NamedTuple

PartialFeeCollection = NamedTuple(
    "PartialFeeCollection",
    [
        ("outstanding_fee_address", str),
        ("fee_type", str),
        (
            "get_internal_account_parameter",
            Callable[
                # vault: SmartContractVault,
                # effective_datetime: datetime,
                ...,
                str,
            ],
        ),
    ],
)

AvailableBalance = NamedTuple(
    "AvailableBalance",
    [
        (
            "calculate",
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

DefaultBalanceAdjustment = NamedTuple(
    "DefaultBalanceAdjustment",
    [
        (
            "calculate_balance_adjustment",
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

WaiveFeeCondition = NamedTuple(
    "WaiveFeeCondition",
    [
        (
            "waive_fees",
            Callable[
                # vault: SmartContractVault,
                # effective_datetime: datetime,
                # denomination: str | None = None,
                ...,
                bool,
            ],
        ),
    ],
)
