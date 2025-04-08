# standard libs
from datetime import datetime
from decimal import Decimal
from unittest.mock import Mock, sentinel
from zoneinfo import ZoneInfo

# contracts api
from contracts_api import Tside

# inception sdk
from inception_sdk.test_framework.contracts.unit.common import (
    ContractTest,
    construct_parameter_timeseries,
)

DEFAULT_DATETIME = datetime(2019, 1, 1, tzinfo=ZoneInfo("UTC"))

DECIMAL_ZERO = Decimal(0)

DEFAULT_CUSTOMER_WALLET_LIMIT = Decimal("1000")
DEFAULT_ACCOUNT_ID = "Main account"
DEFAULT_NOMINATED_ACCOUNT = "Some Account"
DEFAULT_INTERNAL_ACCOUNT = "1"
DEFAULT_DAILY_SPENDING_LIMIT = Decimal("100")

INTERNAL_CONTRA = "INTERNAL_CONTRA"
TODAY_SPENDING = "TODAY_SPENDING"

default_parameters = {
    "zero_out_daily_spend_hour": 23,
    "zero_out_daily_spend_minute": 59,
    "zero_out_daily_spend_second": 59,
    "denomination": sentinel.denomination,
    "daily_spending_limit": DEFAULT_DAILY_SPENDING_LIMIT,
    "nominated_account": DEFAULT_NOMINATED_ACCOUNT,
    "additional_denominations": [sentinel.add_denomination_1, sentinel.add_denomination_2],
    "customer_wallet_limit": DEFAULT_CUSTOMER_WALLET_LIMIT,
}


class WalletTestBase(ContractTest):
    tside = Tside.LIABILITY
    default_denomination = sentinel.denomination

    def create_mock(self, creation_date: datetime = DEFAULT_DATETIME, **kwargs) -> Mock:
        return super().create_mock(
            creation_date=creation_date,
            parameter_ts=construct_parameter_timeseries(
                default_parameters, default_datetime=DEFAULT_DATETIME
            ),
            **kwargs
        )
