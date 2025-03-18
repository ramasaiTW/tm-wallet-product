# standard libs
from datetime import datetime
from decimal import Decimal
from unittest import TestCase
from zoneinfo import ZoneInfo

# contracts api
from contracts_api import (
    DEFAULT_ASSET,
    AdjustmentAmount,
    CalendarEvent,
    CalendarEvents,
    CustomInstruction,
    Next,
    Phase,
    Posting,
)

# inception sdk
from inception_sdk.test_framework.contracts.unit.contracts_api_extension import (
    AdjustmentAmount as AdjustmentAmountExtended,
    CalendarEvents as CalendarEventsExtended,
    CustomInstruction as CustomInstructionExtended,
    Posting as PostingExtended,
)


class DummyClass(AdjustmentAmountExtended):
    def __init__(self, amount):
        self.dummy_attribute = "dummy"
        super().__init__(amount=amount)


class TestTypesExtension(TestCase):
    def test_equality_is_commutative(self):
        base_object = AdjustmentAmount(amount="10")
        extended_object = AdjustmentAmountExtended(amount="10")

        self.assertTrue(base_object == extended_object)
        self.assertTrue(extended_object == base_object)

    def test_equality_of_different_objects(self):
        adjustment_object = AdjustmentAmount(amount="10")
        next_object = Next(day=1)

        self.assertFalse(adjustment_object == next_object)

    def test_equality_of_different_attribute_values(self):
        base_object = AdjustmentAmount(amount="10")
        extended_object = AdjustmentAmountExtended(amount="20")

        self.assertFalse(base_object == extended_object)

    def test_extended_attribute_ignored_in_equality(self):
        extended_class_object = DummyClass(amount="10")
        base_class_object = AdjustmentAmount(amount="10")

        self.assertDictEqual(
            {"dummy_attribute": "dummy", "amount": "10", "replacement_amount": None},
            extended_class_object.__dict__,
        )
        self.assertDictEqual(
            {"amount": "10", "replacement_amount": None},
            base_class_object.__dict__,
        )

        self.assertTrue(extended_class_object == base_class_object)

    def test_custom_instruction_equality_equal(self):
        extended_class_object = CustomInstructionExtended(
            postings=[
                PostingExtended(
                    credit=True,
                    amount=Decimal("100"),
                    denomination="GBP",
                    account_id="some_account_id",
                    account_address="some_address",
                    asset=DEFAULT_ASSET,
                    phase=Phase.COMMITTED,
                ),
                PostingExtended(
                    credit=False,
                    amount=Decimal("100"),
                    denomination="GBP",
                    account_id="some_account_id",
                    account_address="some_address",
                    asset=DEFAULT_ASSET,
                    phase=Phase.COMMITTED,
                ),
            ]
        )
        base_class_object = CustomInstruction(
            postings=[
                Posting(
                    credit=True,
                    amount=Decimal("100"),
                    denomination="GBP",
                    account_id="some_account_id",
                    account_address="some_address",
                    asset=DEFAULT_ASSET,
                    phase=Phase.COMMITTED,
                ),
                Posting(
                    credit=False,
                    amount=Decimal("100"),
                    denomination="GBP",
                    account_id="some_account_id",
                    account_address="some_address",
                    asset=DEFAULT_ASSET,
                    phase=Phase.COMMITTED,
                ),
            ]
        )
        self.assertTrue(extended_class_object == base_class_object)

    def test_custom_instruction_equality_not_equal(self):
        extended_class_object = CustomInstructionExtended(
            postings=[
                PostingExtended(
                    credit=True,
                    amount=Decimal("100"),
                    denomination="GBP",
                    account_id="some_account_id",
                    account_address="some_address",
                    asset=DEFAULT_ASSET,
                    phase=Phase.COMMITTED,
                ),
                PostingExtended(
                    credit=False,
                    amount=Decimal("100"),
                    denomination="GBP",
                    account_id="some_account_id",
                    account_address="some_address",
                    asset=DEFAULT_ASSET,
                    phase=Phase.COMMITTED,
                ),
            ]
        )
        base_class_object = CustomInstruction(
            postings=[
                Posting(
                    credit=True,
                    amount=Decimal("1000"),
                    denomination="GBP",
                    account_id="some_account_id",
                    account_address="some_address",
                    asset=DEFAULT_ASSET,
                    phase=Phase.COMMITTED,
                ),
                Posting(
                    credit=False,
                    amount=Decimal("1000"),
                    denomination="GBP",
                    account_id="some_account_id",
                    account_address="some_address",
                    asset=DEFAULT_ASSET,
                    phase=Phase.COMMITTED,
                ),
            ]
        )
        self.assertFalse(extended_class_object == base_class_object)

    def test_calendar_events_fails_when_list_objects_not_equal(self):
        extended_class_object = CalendarEventsExtended(
            calendar_events=[
                CalendarEvent(
                    id="1",
                    calendar_id="GREEN",
                    start_datetime=datetime(2020, 1, 1, tzinfo=ZoneInfo("UTC")),
                    end_datetime=datetime(2021, 1, 2, tzinfo=ZoneInfo("UTC")),
                )
            ]
        )
        base_class_object = CalendarEvents(
            calendar_events=[
                CalendarEvent(
                    id="2",
                    calendar_id="RED",
                    start_datetime=datetime(2022, 1, 1, tzinfo=ZoneInfo("UTC")),
                    end_datetime=datetime(2023, 1, 2, tzinfo=ZoneInfo("UTC")),
                )
            ]
        )
        self.assertFalse(extended_class_object == base_class_object)
