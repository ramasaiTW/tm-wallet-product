# standard libs
from datetime import datetime
from decimal import Decimal
from unittest import TestCase
from unittest.mock import sentinel
from zoneinfo import ZoneInfo

# contracts api
from contracts_api import CalendarEvent, Release, ScheduledEventHookResult, Settlement, Tside

# inception sdk
from inception_sdk.test_framework.contracts.unit.common import ContractTest
from inception_sdk.test_framework.contracts.unit.contracts_api_extension import (
    CalendarEvents,
    ScheduledEventHookResult as ExtendedScheduledEventHookResult,
)


class TestCreateMock(TestCase):
    def test_mock_get_last_execution_datetime_raises(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(last_execution_datetimes={"some_event": None})
        with self.assertRaises(ValueError) as err:
            mock_vault.get_last_execution_datetime(event_type="another_event")
        self.assertEqual(
            err.exception.args[0],
            "Missing event_type in last_execution_datetimes mapping.",
        )

    def test_mock_get_last_execution_datetime_returns_datetime(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            last_execution_datetimes={
                "some_event": None,
                "another_event": datetime(2023, 1, 1, 1, 1),
            }
        )
        result = mock_vault.get_last_execution_datetime(event_type="another_event")
        self.assertEqual(result, datetime(2023, 1, 1, 1, 1))

    def test_mock_get_last_execution_datetime_returns_None(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            last_execution_datetimes={
                "some_event": None,
                "another_event": datetime(2023, 1, 1, 1, 1),
            }
        )
        result = mock_vault.get_last_execution_datetime(event_type="some_event")
        self.assertIsNone(result)

    def test_get_account_creation_datetime_defaulted_datetime(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock()
        result = mock_vault.get_account_creation_datetime()
        expected = datetime(2019, 1, 1, tzinfo=ZoneInfo("UTC"))
        self.assertEqual(result, expected)

    def test_get_account_creation_datetime_custom_datetime(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            creation_date=datetime(2019, 1, 2, tzinfo=ZoneInfo("UTC"))
        )
        result = mock_vault.get_account_creation_datetime()
        expected = datetime(2019, 1, 2, tzinfo=ZoneInfo("UTC"))
        self.assertEqual(result, expected)

    def test_get_permitted_denominations(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock()
        result = mock_vault.get_permitted_denominations()
        self.assertEqual(result, ["GBP"])

    def test_non_supervisee_mock_raises_on_get_alias(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock()
        with self.assertRaises(ValueError) as err:
            mock_vault.get_alias()
        self.assertEqual(
            err.exception.args[0],
            "get_alias method cannot be called on a non-supervisee Vault object, "
            "make sure the create_mock argument is set correctly",
        )

    def test_supervisee_mock_raises_on_get_alias_if_not_set(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(is_supervisee_vault=True)
        with self.assertRaises(ValueError) as err:
            mock_vault.get_alias()
        self.assertEqual(err.exception.args[0], "No supervisee alias provided")

    def test_supervisee_mock_returns_alias(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(is_supervisee_vault=True, supervisee_alias="some_alias")
        self.assertEqual(mock_vault.get_alias(), "some_alias")

    def test_non_supervisee_mock_raises_on_get_hook_result(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock()
        with self.assertRaises(ValueError) as err:
            mock_vault.get_hook_result()
        self.assertEqual(
            err.exception.args[0],
            "get_hook_result method cannot be called on a non-supervisee Vault object, "
            "make sure the create_mock argument is set correctly",
        )

    def test_supervisee_mock_raises_without_result_on_get_hook_result(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(is_supervisee_vault=True)
        with self.assertRaises(ValueError) as err:
            mock_vault.get_hook_result()
        self.assertEqual(
            err.exception.args[0],
            "get_hook_result must return one of PrePostingHookResult, "
            "PostPostingHookResult, ScheduledEventHookResult",
        )

    def test_supervisee_mock_returns_result_get_hook_result(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            is_supervisee_vault=True, supervisee_hook_result=ScheduledEventHookResult()
        )

        self.assertEqual(mock_vault.get_hook_result(), ExtendedScheduledEventHookResult())

    def test_supervisee_mock_returns_requires_fetched_postings(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            is_supervisee_vault=True, requires_fetched_postings=[sentinel.postings]
        )

        self.assertListEqual(mock_vault.get_posting_instructions(), [sentinel.postings])

    def test_non_supervisee_mock_raises_fetched_postings_without_fetcher_id(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            postings_interval_mapping={"some_fetcher_id": [sentinel.postings]},
        )
        with self.assertRaises(ValueError) as err:
            mock_vault.get_posting_instructions()
        self.assertEqual(
            err.exception.args[0],
            "You must provide a fetcher ID",
        )

    def test_non_supervisee_mock_fetched_postings_if_empty_list(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            postings_interval_mapping={"some_fetcher_id": []},
        )
        self.assertListEqual(mock_vault.get_posting_instructions(fetcher_id="some_fetcher_id"), [])

    def test_non_supervisee_mock_raises_fetched_postings_with_incorrect_fetcher_id(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            postings_interval_mapping={"some_fetcher_id": [sentinel.postings]},
        )
        with self.assertRaises(ValueError) as err:
            mock_vault.get_posting_instructions("another_fetcher_id")
        self.assertEqual(
            err.exception.args[0],
            "Missing posting interval in test setup for fetcher_id='another_fetcher_id'",
        )

    def test_supervisee_mock_returns_requires_fetched_client_transactions(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            is_supervisee_vault=True,
            requires_fetched_client_transactions={sentinel.unique_id: sentinel.client_transaction},
        )

        self.assertDictEqual(
            mock_vault.get_client_transactions(), {sentinel.unique_id: sentinel.client_transaction}
        )

    def test_supervisee_mock_raises_if_fetcher_id_in_get_client_transactions(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            is_supervisee_vault=True,
        )

        with self.assertRaises(ValueError) as err:
            mock_vault.get_client_transactions(fetcher_id="some_fetcher")
        self.assertEqual(
            err.exception.args[0],
            "Supervisee vault object cannot provide fetcher_id to get_client_transactions()",
        )

    def test_supervisee_mock_raises_if_missing_requires_fetched_get_client_transactions(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            is_supervisee_vault=True,
        )

        with self.assertRaises(ValueError) as err:
            mock_vault.get_client_transactions()
        self.assertEqual(
            err.exception.args[0],
            "Missing requires fetched client transactions in test setup",
        )

    def test_non_supervisee_mock_raises_fetched_client_transactions_without_fetcher_id(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            client_transactions_mapping={
                "some_fetcher_id": {sentinel.unique_id: sentinel.client_transaction}
            },
        )
        with self.assertRaises(ValueError) as err:
            mock_vault.get_client_transactions()
        self.assertEqual(
            err.exception.args[0],
            "You must provide a fetcher ID",
        )

    def test_non_supervisee_mock_fetched_client_transactions_if_empty_dict(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            client_transactions_mapping={"some_fetcher_id": {}},
        )
        self.assertDictEqual(mock_vault.get_client_transactions(fetcher_id="some_fetcher_id"), {})

    def test_non_supervisee_mock_fetched_client_transactions(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            client_transactions_mapping={
                "some_fetcher_id": {sentinel.unique_id: sentinel.client_transaction}
            },
        )
        self.assertDictEqual(
            mock_vault.get_client_transactions(fetcher_id="some_fetcher_id"),
            {sentinel.unique_id: sentinel.client_transaction},
        )

    def test_non_supervisee_mock_raises_fetched_client_transactions_with_incorrect_fetcher_id(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            client_transactions_mapping={"some_fetcher_id": {}},
        )
        with self.assertRaises(ValueError) as err:
            mock_vault.get_client_transactions("another_fetcher_id")
        self.assertEqual(
            err.exception.args[0],
            "Missing client transactions in test setup for fetcher_id='another_fetcher_id'",
        )

    def test_supervisee_mock_returns_requires_fetched_balances(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            is_supervisee_vault=True, requires_fetched_balances=sentinel.balances
        )

        self.assertEqual(mock_vault.get_balances_timeseries(), sentinel.balances)

    def test_supervisee_mock_returns_mapped_fetched_balances(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            is_supervisee_vault=True,
            balances_interval_fetchers_mapping={"some_fetcher_id": sentinel.balances},
        )

        self.assertEqual(
            mock_vault.get_balances_timeseries(fetcher_id="some_fetcher_id"), sentinel.balances
        )

    def test_non_supervisee_mock_raises_fetched_balances_without_fetcher_id(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            postings_interval_mapping={"some_fetcher_id": sentinel.balances},
        )
        with self.assertRaises(ValueError) as err:
            mock_vault.get_balances_timeseries()
        self.assertEqual(
            err.exception.args[0],
            "You must provide a fetcher ID",
        )

    def test_non_supervisee_mock_raises_fetched_balances_with_incorrect_fetcher_id(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        mock_vault = test_case.create_mock(
            postings_interval_mapping={"some_fetcher_id": sentinel.balances}
        )
        with self.assertRaises(ValueError) as err:
            mock_vault.get_balances_timeseries("another_fetcher_id")
        self.assertEqual(
            err.exception.args[0],
            "Missing balance interval in test setup for fetcher_id='another_fetcher_id'",
        )

    def test_get_calendar_events_replaces_clu_dependencies(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        # construct mocks
        calendar_events = [
            CalendarEvent(
                id="1",
                calendar_id="&{PUBLIC_HOLIDAYS}",
                start_datetime=datetime(2023, 1, 1, tzinfo=ZoneInfo("UTC")),
                end_datetime=datetime(2023, 1, 2, tzinfo=ZoneInfo("UTC")),
            ),
            CalendarEvent(
                id="2",
                calendar_id="&{PUBLIC_HOLIDAYS}",
                start_datetime=datetime(2023, 1, 2, tzinfo=ZoneInfo("UTC")),
                end_datetime=datetime(2023, 1, 3, tzinfo=ZoneInfo("UTC")),
            ),
        ]
        mock_vault = test_case.create_mock(calendar_events=calendar_events)
        # expected result

        non_clu_calendar_events = [
            CalendarEvent(
                id="1",
                calendar_id="PUBLIC_HOLIDAYS",
                start_datetime=datetime(2023, 1, 1, tzinfo=ZoneInfo("UTC")),
                end_datetime=datetime(2023, 1, 2, tzinfo=ZoneInfo("UTC")),
            ),
            CalendarEvent(
                id="2",
                calendar_id="PUBLIC_HOLIDAYS",
                start_datetime=datetime(2023, 1, 2, tzinfo=ZoneInfo("UTC")),
                end_datetime=datetime(2023, 1, 3, tzinfo=ZoneInfo("UTC")),
            ),
        ]
        calendar_events_object = CalendarEvents(calendar_events=non_clu_calendar_events)
        # run function
        self.assertListEqual(
            mock_vault.get_calendar_events(calendar_ids=["PUBLIC_HOLIDAYS"]),
            calendar_events_object,
        )

    def test_get_calendar_events_returns_events_for_specified_ids(self):
        test_case = ContractTest()
        test_case.tside = Tside.ASSET
        # construct mocks
        calendar_events = [
            CalendarEvent(
                id="1",
                calendar_id="&{PUBLIC_HOLIDAYS_1}",
                start_datetime=datetime(2023, 1, 1, tzinfo=ZoneInfo("UTC")),
                end_datetime=datetime(2023, 1, 2, tzinfo=ZoneInfo("UTC")),
            ),
            CalendarEvent(
                id="2",
                calendar_id="&{PUBLIC_HOLIDAYS_2}",
                start_datetime=datetime(2023, 1, 2, tzinfo=ZoneInfo("UTC")),
                end_datetime=datetime(2023, 1, 3, tzinfo=ZoneInfo("UTC")),
            ),
        ]
        mock_vault = test_case.create_mock(calendar_events=calendar_events)

        # run function
        self.assertListEqual(
            mock_vault.get_calendar_events(calendar_ids=["PUBLIC_HOLIDAYS_2"]),
            CalendarEvents(
                calendar_events=[
                    CalendarEvent(
                        id="2",
                        calendar_id="PUBLIC_HOLIDAYS_2",
                        start_datetime=datetime(2023, 1, 2, tzinfo=ZoneInfo("UTC")),
                        end_datetime=datetime(2023, 1, 3, tzinfo=ZoneInfo("UTC")),
                    ),
                ]
            ),
        )


class TestPostingHelpers(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract_test = ContractTest()
        cls.contract_test.tside = Tside.ASSET
        return super().setUpClass()

    def test_can_create_zero_amount_outbound_settlement_with_from_proto(self):
        self.assertIsInstance(
            self.contract_test.settle_outbound_auth(
                unsettled_amount=Decimal("0"), amount=Decimal("0"), _from_proto=True
            ),
            Settlement,
        )

    def test_cant_create_zero_amount_outbound_settlement_without_from_proto(self):
        # Can't access the InvalidSmartContractError from the contracts_api
        with self.assertRaisesRegex(Exception, r"Amount must be greater than 0"):
            self.contract_test.settle_outbound_auth(
                unsettled_amount=Decimal("0"),
                amount=Decimal("0"),
            )

    def test_can_create_zero_amount_inbound_settlement_with_from_proto(self):
        self.assertIsInstance(
            self.contract_test.settle_inbound_auth(
                unsettled_amount=Decimal("0"), amount=Decimal("0"), _from_proto=True
            ),
            Settlement,
        )

    def test_cant_create_zero_amount_inbound_settlement_without_from_proto(self):
        # Can't access the InvalidSmartContractError from the contracts_api
        with self.assertRaisesRegex(Exception, r"Amount must be greater than 0"):
            self.contract_test.settle_inbound_auth(
                unsettled_amount=Decimal("0"),
                amount=Decimal("0"),
            )

    def test_can_create_zero_amount_outbound_release_with_from_proto(self):
        self.assertIsInstance(
            self.contract_test.release_outbound_auth(
                unsettled_amount=Decimal("0"), amount=Decimal("0"), _from_proto=True
            ),
            Release,
        )

    def test_cant_create_zero_amount_outbound_release_without_from_proto(self):
        # Can't access the InvalidSmartContractError from the contracts_api
        with self.assertRaisesRegex(Exception, r"Amount must be greater than 0"):
            self.contract_test.release_outbound_auth(
                unsettled_amount=Decimal("0"),
                amount=Decimal("0"),
            )

    def test_can_create_zero_amount_inbound_release_with_from_proto(self):
        self.assertIsInstance(
            self.contract_test.release_inbound_auth(
                unsettled_amount=Decimal("0"), amount=Decimal("0"), _from_proto=True
            ),
            Release,
        )

    def test_cant_create_zero_amount_inbound_release_without_from_proto(self):
        # Can't access the InvalidSmartContractError from the contracts_api
        with self.assertRaisesRegex(Exception, r"Amount must be greater than 0"):
            self.contract_test.release_inbound_auth(
                unsettled_amount=Decimal("0"),
                amount=Decimal("0"),
            )
