# standard libs

# library
import library.wallet.contracts.template.wallet as contract
from library.wallet.test.unit.test_wallet_common import (
    DEFAULT_DATETIME,
    WalletTestBase,
)
from contracts_api import ScheduledEvent, ConversionHookArguments, ScheduleExpression


class ConversionHookTest(WalletTestBase):
    def test_conversion_hook_with_existing_schedule(self):
        ZERO_OUT_DAILY_SPEND_EVENT = "ZERO_OUT_DAILY_SPEND"

        # Create a ScheduleExpression instance
        existing_schedule_expression = ScheduleExpression(second="0", minute="0", hour="0")

        # Mock existing scheduled event with the ScheduleExpression
        existing_scheduled_event = ScheduledEvent(
            start_datetime=DEFAULT_DATETIME, expression=existing_schedule_expression
        )
        existing_schedules = {ZERO_OUT_DAILY_SPEND_EVENT: existing_scheduled_event}

        hook_arguments = ConversionHookArguments(
            effective_datetime=DEFAULT_DATETIME,
            existing_schedules=existing_schedules,
        )

        mock_vault = self.create_mock()

        # Call the hook
        hook_result = contract.conversion_hook(mock_vault, hook_arguments)

        # Assert that the existing schedule is returned without modification
        self.assertIn(ZERO_OUT_DAILY_SPEND_EVENT, hook_result.scheduled_events_return_value)
        self.assertEqual(
            hook_result.scheduled_events_return_value[ZERO_OUT_DAILY_SPEND_EVENT],
            existing_scheduled_event,
        )

    def test_conversion_hook_without_existing_schedule(self):
        ZERO_OUT_DAILY_SPEND_EVENT = "ZERO_OUT_DAILY_SPEND"

        # Mock no existing scheduled events
        existing_schedules = {}

        hook_arguments = ConversionHookArguments(
            effective_datetime=DEFAULT_DATETIME,
            existing_schedules=existing_schedules,
        )

        mock_vault = self.create_mock()

        # Call the hook
        hook_result = contract.conversion_hook(mock_vault, hook_arguments)

        # Assert that a new schedule is created
        self.assertIn(ZERO_OUT_DAILY_SPEND_EVENT, hook_result.scheduled_events_return_value)
        new_scheduled_event = hook_result.scheduled_events_return_value[ZERO_OUT_DAILY_SPEND_EVENT]
        self.assertEqual(new_scheduled_event.start_datetime, DEFAULT_DATETIME)

        expected_expression = contract._get_zero_out_daily_spend_schedule(mock_vault)
        actual_expression = new_scheduled_event.expression

        # Compare the relevant attributes of the ScheduleExpression instances
        self.assertEqual(actual_expression.hour, expected_expression.hour)
        self.assertEqual(actual_expression.minute, expected_expression.minute)
        self.assertEqual(actual_expression.second, expected_expression.second)
