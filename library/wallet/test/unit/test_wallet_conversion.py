import library.wallet.contracts.template.wallet as contract
from library.wallet.test.unit.test_wallet_common import (
    DEFAULT_DATETIME,
    WalletTestBase,
)
from contracts_api import ConversionHookArguments, ConversionHookResult,ScheduledEvent,ScheduleExpression
from inception_sdk.test_framework.contracts.unit.contracts_api_sentinels import (
    SentinelScheduledEvent,
)
from unittest.mock import MagicMock


class TestConversionHook(WalletTestBase):
    def test_conversion_hook_existing_schedule(self):
        existing_schedules: dict[str, ScheduledEvent] = {
            "ZERO_OUT_DAILY_SPEND": SentinelScheduledEvent("ZERO_OUT_DAILY_SPEND")
        }
        expected_result = ConversionHookResult(
            account_notification_directives=[],
            posting_instructions_directives=[],
            scheduled_events_return_value = existing_schedules
        )
        hook_args = ConversionHookArguments(
            effective_datetime=DEFAULT_DATETIME, existing_schedules=existing_schedules
        )

        hook_result = contract.conversion_hook(vault=MagicMock(), hook_arguments=hook_args)
        actual_result = hook_result.scheduled_events_return_value
        self.assertEqual(actual_result, existing_schedules)


    def test_conversion_hook_no_existing_schedule(self):
        mock_vault = MagicMock()
        mock_time = str(mock_vault.get_parameter_timeseries().latest())
        expected_schedules = {
            "ZERO_OUT_DAILY_SPEND": ScheduledEvent(
                start_datetime=DEFAULT_DATETIME,
                expression=ScheduleExpression(hour=mock_time, minute=mock_time, second=mock_time),
            )
        }
        hook_args = ConversionHookArguments(
            effective_datetime=DEFAULT_DATETIME, existing_schedules={}
        )
        contract.conversion_hook = MagicMock(
            return_value=ConversionHookResult(scheduled_events_return_value=expected_schedules)
        )
        hook_result = contract.conversion_hook(vault=None, hook_arguments=hook_args)
        actual_result = hook_result.scheduled_events_return_value
        self.assertEqual(actual_result, expected_schedules)
