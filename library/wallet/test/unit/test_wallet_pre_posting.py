# standard libs
from decimal import Decimal
from unittest.mock import patch, sentinel

# library
import library.wallet.contracts.template.wallet as contract
from library.wallet.test.unit.test_wallet_common import DEFAULT_DATETIME, WalletTestBase

# features
import library.features.common.fetchers as fetchers
from library.features.common.test.mocks import mock_utils_get_parameter

# contracts api
from contracts_api import (
    BalanceDefaultDict,
    BalancesObservation,
    FlagTimeseries,
    PrePostingHookArguments,
)

# inception sdk
from inception_sdk.test_framework.contracts.unit.contracts_api_extension import RejectionReason


class PrePostingHookTest(WalletTestBase):
    def setUp(self):
        # get parameter
        patch_get_parameter = patch.object(contract.utils, "get_parameter")
        self.mock_get_parameter = patch_get_parameter.start()
        self.mock_get_parameter.side_effect = mock_utils_get_parameter(
            parameters={
                "denomination": sentinel.denomination,
                "daily_spending_limit": Decimal("100"),
                "nominated_account": "Some Account",
                "additional_denominations": [
                    sentinel.add_denomination_1,
                    sentinel.add_denomination_2,
                ],
                "customer_wallet_limit": Decimal("1000"),
            }
        )

    def test_posting_batch_with_additional_denom_and_sufficient_balance_is_accepted(
        self,
    ):
        posting = self.outbound_hard_settlement(
            amount=Decimal("30"), denomination=sentinel.add_denomination_1
        )

        balance_dict = {
            self.balance_coordinate(
                denomination=sentinel.add_denomination_1,
            ): self.balance(net=Decimal(100)),
        }
        balances_observation = BalancesObservation(
            balances=BalanceDefaultDict(mapping=balance_dict),
            value_datetime=DEFAULT_DATETIME,
        )
        balances_observation_fetchers_mapping = {
            fetchers.LIVE_BALANCES_BOF_ID: balances_observation
        }

        mock_vault = self.create_mock(
            balances_observation_fetchers_mapping=balances_observation_fetchers_mapping,
        )

        hook_arguments = PrePostingHookArguments(
            effective_datetime=DEFAULT_DATETIME,
            posting_instructions=[posting],
            client_transactions={},
        )
        hook_result = contract.pre_posting_hook(mock_vault, hook_arguments)
        self.assertIsNone(hook_result)

    def test_posting_batch_with_additional_denom_and_sufficient_balances_is_accepted(
        self,
    ):
        posting_1 = self.outbound_hard_settlement(
            amount=Decimal("20"), denomination=sentinel.add_denomination_1
        )
        posting_2 = self.outbound_hard_settlement(
            amount=Decimal("30"), denomination=sentinel.add_denomination_2
        )

        balance_dict = {
            self.balance_coordinate(
                denomination=sentinel.add_denomination_1,
            ): self.balance(net=Decimal(100)),
            self.balance_coordinate(
                denomination=sentinel.add_denomination_2,
            ): self.balance(net=Decimal(100)),
        }
        balances_observation = BalancesObservation(
            balances=BalanceDefaultDict(mapping=balance_dict),
            value_datetime=DEFAULT_DATETIME,
        )
        balances_observation_fetchers_mapping = {
            fetchers.LIVE_BALANCES_BOF_ID: balances_observation
        }

        mock_vault = self.create_mock(
            balances_observation_fetchers_mapping=balances_observation_fetchers_mapping,
        )

        hook_arguments = PrePostingHookArguments(
            effective_datetime=DEFAULT_DATETIME,
            posting_instructions=[posting_1, posting_2],
            client_transactions={},
        )
        hook_result = contract.pre_posting_hook(mock_vault, hook_arguments)
        self.assertIsNone(hook_result)

    def test_posting_batch_with_single_additional_denom_rejected_if_insufficient_balances(self):
        posting = self.outbound_hard_settlement(
            amount=Decimal("20"), denomination=sentinel.add_denomination_1
        )

        balance_dict = {
            self.balance_coordinate(
                denomination=sentinel.add_denomination_1,
            ): self.balance(net=Decimal(10)),
        }
        balances_observation = BalancesObservation(
            balances=BalanceDefaultDict(mapping=balance_dict),
            value_datetime=DEFAULT_DATETIME,
        )
        balances_observation_fetchers_mapping = {
            fetchers.LIVE_BALANCES_BOF_ID: balances_observation
        }

        mock_vault = self.create_mock(
            balances_observation_fetchers_mapping=balances_observation_fetchers_mapping,
        )

        hook_arguments = PrePostingHookArguments(
            effective_datetime=DEFAULT_DATETIME,
            posting_instructions=[posting],
            client_transactions={},
        )
        hook_result = contract.pre_posting_hook(mock_vault, hook_arguments)
        self.assertIsNotNone(hook_result)
        self.assertEqual(
            hook_result.rejection.message,
            f"Postings total {sentinel.add_denomination_1} -20, "
            f"which exceeds the available balance of {sentinel.add_denomination_1} 10",
        )
        self.assertEqual(hook_result.rejection.reason_code, RejectionReason.INSUFFICIENT_FUNDS)

    def test_posting_batch_with_supported_and_unsupported_denom_is_rejected(self):
        # not supported
        posting_1 = self.outbound_hard_settlement(
            denomination=sentinel.unsupported_denomination_1, amount=Decimal(1)
        )
        # supported
        posting_2 = self.outbound_hard_settlement(
            denomination=sentinel.add_denomination_1, amount=Decimal(1)
        )

        balances_observation = BalancesObservation(
            balances=BalanceDefaultDict(mapping={}),
            value_datetime=DEFAULT_DATETIME,
        )
        balances_observation_fetchers_mapping = {
            fetchers.LIVE_BALANCES_BOF_ID: balances_observation
        }

        mock_vault = self.create_mock(
            balances_observation_fetchers_mapping=balances_observation_fetchers_mapping,
        )

        hook_arguments = PrePostingHookArguments(
            effective_datetime=DEFAULT_DATETIME,
            posting_instructions=[posting_1, posting_2],
            client_transactions={},
        )
        hook_result = contract.pre_posting_hook(mock_vault, hook_arguments)
        self.assertIsNotNone(hook_result)
        self.assertEqual(
            hook_result.rejection.message, "Postings received in unauthorised denominations"
        )
        self.assertEqual(hook_result.rejection.reason_code, RejectionReason.WRONG_DENOMINATION)

    def test_posting_batch_with_single_unsupported_denom_is_rejected(self):
        posting = self.outbound_hard_settlement(
            denomination=sentinel.unsupported_denomination, amount=Decimal(1)
        )

        balances_observation = BalancesObservation(
            balances=BalanceDefaultDict(mapping={}),
            value_datetime=DEFAULT_DATETIME,
        )
        balances_observation_fetchers_mapping = {
            fetchers.LIVE_BALANCES_BOF_ID: balances_observation
        }

        mock_vault = self.create_mock(
            balances_observation_fetchers_mapping=balances_observation_fetchers_mapping,
        )

        hook_arguments = PrePostingHookArguments(
            effective_datetime=DEFAULT_DATETIME,
            posting_instructions=[posting],
            client_transactions={},
        )
        hook_result = contract.pre_posting_hook(mock_vault, hook_arguments)
        self.assertIsNotNone(hook_result)
        self.assertEqual(
            hook_result.rejection.message, "Postings received in unauthorised denominations"
        )
        self.assertEqual(hook_result.rejection.reason_code, RejectionReason.WRONG_DENOMINATION)

    def test_pre_posting_no_money_flag_false(self):
        posting = self.outbound_hard_settlement(
            denomination=sentinel.denomination, amount=Decimal("100")
        )

        balances_observation = BalancesObservation(
            balances=BalanceDefaultDict(mapping={}),
            value_datetime=DEFAULT_DATETIME,
        )
        balances_observation_fetchers_mapping = {
            fetchers.LIVE_BALANCES_BOF_ID: balances_observation
        }

        mock_vault = self.create_mock(
            balances_observation_fetchers_mapping=balances_observation_fetchers_mapping,
        )

        hook_arguments = PrePostingHookArguments(
            effective_datetime=DEFAULT_DATETIME,
            posting_instructions=[posting],
            client_transactions={},
        )
        hook_result = contract.pre_posting_hook(mock_vault, hook_arguments)
        self.assertIsNotNone(hook_result)
        self.assertEqual(hook_result.rejection.reason_code, RejectionReason.INSUFFICIENT_FUNDS)

    def test_pre_posting_no_money_flag_true(self):
        posting = self.outbound_hard_settlement(
            denomination=sentinel.denomination, amount=Decimal("100")
        )

        balances_observation = BalancesObservation(
            balances=BalanceDefaultDict(mapping={}),
            value_datetime=DEFAULT_DATETIME,
        )
        balances_observation_fetchers_mapping = {
            fetchers.LIVE_BALANCES_BOF_ID: balances_observation
        }

        mock_vault = self.create_mock(
            balances_observation_fetchers_mapping=balances_observation_fetchers_mapping,
            flags_ts={"AUTO_TOP_UP_WALLET": FlagTimeseries([(DEFAULT_DATETIME, True)])},
        )

        hook_arguments = PrePostingHookArguments(
            effective_datetime=DEFAULT_DATETIME,
            posting_instructions=[posting],
            client_transactions={},
        )
        hook_result = contract.pre_posting_hook(mock_vault, hook_arguments)
        self.assertIsNone(hook_result)

    def test_pre_posting_code_rejects_if_over_limit(self):
        posting = self.outbound_hard_settlement(
            denomination=sentinel.denomination, amount=Decimal("200")
        )

        balance_dict = {
            self.balance_coordinate(
                denomination=sentinel.denomination,
            ): self.balance(net=Decimal(200)),
        }
        balances_observation = BalancesObservation(
            balances=BalanceDefaultDict(mapping=balance_dict),
            value_datetime=DEFAULT_DATETIME,
        )
        balances_observation_fetchers_mapping = {
            fetchers.LIVE_BALANCES_BOF_ID: balances_observation
        }

        mock_vault = self.create_mock(
            balances_observation_fetchers_mapping=balances_observation_fetchers_mapping
        )

        hook_arguments = PrePostingHookArguments(
            effective_datetime=DEFAULT_DATETIME,
            posting_instructions=[posting],
            client_transactions={},
        )
        hook_result = contract.pre_posting_hook(mock_vault, hook_arguments)
        self.assertIsNotNone(hook_result)
        self.assertEqual(hook_result.rejection.reason_code, RejectionReason.AGAINST_TNC)

    def test_pre_posting_code_ignores_limits_with_withdrawal_override_true(self):
        posting = self.outbound_hard_settlement(
            denomination=sentinel.denomination,
            amount=Decimal("99"),
            instruction_details={"withdrawal_override": "true"},
        )

        balance_dict = {
            self.balance_coordinate(
                denomination=sentinel.denomination,
            ): self.balance(net=Decimal(98)),
        }
        balances_observation = BalancesObservation(
            balances=BalanceDefaultDict(mapping=balance_dict),
            value_datetime=DEFAULT_DATETIME,
        )
        balances_observation_fetchers_mapping = {
            fetchers.LIVE_BALANCES_BOF_ID: balances_observation
        }

        mock_vault = self.create_mock(
            balances_observation_fetchers_mapping=balances_observation_fetchers_mapping,
        )

        hook_arguments = PrePostingHookArguments(
            effective_datetime=DEFAULT_DATETIME,
            posting_instructions=[posting],
            client_transactions={},
        )
        hook_result = contract.pre_posting_hook(mock_vault, hook_arguments)
        self.assertIsNone(hook_result)

    def test_pre_posting_code_is_force_override_true(self):
        posting = self.outbound_hard_settlement(
            amount=Decimal("10"),
            denomination=sentinel.denomination,
            instruction_details={"force_override": "true"},
        )

        balance_dict = {
            self.balance_coordinate(denomination=sentinel.denomination): self.balance(
                net=Decimal("5")
            ),
        }
        balances_observation = BalancesObservation(
            balances=BalanceDefaultDict(mapping=balance_dict),
            value_datetime=DEFAULT_DATETIME,
        )
        balances_observation_fetchers_mapping = {
            fetchers.LIVE_BALANCES_BOF_ID: balances_observation
        }

        mock_vault = self.create_mock(
            balances_observation_fetchers_mapping=balances_observation_fetchers_mapping,
        )

        hook_arguments = PrePostingHookArguments(
            effective_datetime=DEFAULT_DATETIME,
            posting_instructions=[posting],
            client_transactions={},
        )
        hook_result = contract.pre_posting_hook(mock_vault, hook_arguments)
        self.assertIsNone(hook_result)
