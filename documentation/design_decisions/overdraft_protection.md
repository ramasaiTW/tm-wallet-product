# US Checking Account - Overdraft Protection

## Scope

Overdraft protection (ODP) allows a customer to protect against utilising the overdraft balance on their checking account by providing funds from another source (the account providing these funds is referred to as the ODP source).

The first iteration of this feature will only consider the `us_savings_account` as the ODP source.

## Requirements

The requirements can be found in the **Overdraft Protection and Overdraft Protection Transfer Fee** section of the [US Checking Account Specific Requirements](https://docs.google.com/document/d/1wxTHreq1rBNt7zZdkfNLoJ_SIo9MP2eXYRP1yFhXmNU/edit) document.

## Assumptions

N/A

## Agreed Implementation

An `odp_supervisor` supervisor smart contract will need to be defined to achieve the following:

1. Handle the sweeping of funds from the ODP source account (if applicable) at EOD.
2. Validate incoming postings, rejecting the posting if there is not sufficient available combined balance to cover the posting.
3. Ensure any BAU schedules on the checking and savings account are executed after the ODP sweep, namely, interest accrual as this must account for the swept funds.

The best solution to achieve the list items above is as to utilise schedule groups within the supervisor contract, as detailed [here](#technical-logic).

### Data Definition

#### Contract Parameters

Two additional contract parameters are required in the US Checking Account product:

- `odp_sweep_fee`: Template parameter - `NumberShape` - the fee to be charged to process the sweeping of funds
- `odp_sweep_fee_income_account`: Template parameter - `AccountIdShape` - Internal account for overdraft protection sweep fee income balance.

#### Event Types & Schedules

An event type must be defined in the supervisor contract to handle the ODP sweep, this event should not override any functionality on the associated supervisees. In addition, a second event type must be defined to override the interest accrual events on the associated supervisees, as mentioned previously, this is only intended to ensure ordering of schedule executions.

- `SWEEP`: Defined in the odp_supervisor contract to handle the ODP sweep functionality
- `ACCRUE_INTEREST`: Defined in the odp_supervisor contract to override the supervisee interest accrual schedules

### Technical Logic

The supervisor will supervise the following products:

- `us_checking_account`
- `us_savings_account`

The US Checking Account `pre_posting_hook` should be supervised using the `INVOKED` mode. This will run the account level validation, and the supervisor must also validate the postings:

- If there is not exactly one US Checking Account associated with the supervisor, the postings should be rejected.
- Postings with the `force_override` instruction detail should be accepted.
- Any rejections from the the US Checking Account which are not classified as an `INSUFFICIENT_FUNDS` rejection should be propagated and returned by the supervisor
- If the combined available balance (the sum of the available balance on the linked US Checking Account, US Savings Account and the arranged overdraft amount) is not sufficient to cover the proposed transaction, it should be rejected.

To ensure interest accrual (on both supervised accounts) is processed after the ODP sweep, the supervisor `ACCRUE_INTEREST` schedule must override the `ACCRUE_INTEREST` schedules on both supervisees and define it's own schedules within a group, e.g.

```python
event_types = [
    SupervisorContractEventType(
        name="ODP_SWEEP",
        scheduler_tag_ids=["ODP_SUPERVISOR_ODP_SWEEP_AST"],
    ),
    SupervisorContractEventType(
        name="ACCRUE_INTEREST",
        overrides_event_types=[
            (US_SAVINGS_ACCOUNT_ALIAS, "ACCRUE_INTEREST"),
            (US_CHECKING_ACCOUNT_ALIAS, "ACCRUE_INTEREST"),
        ],
        scheduler_tag_ids=["ODP_SUPERVISOR_ACCRUE_INTEREST_AST"],
    ),
]

event_types_groups = [
  EventTypesGroup(
    name="ODP_SWEEP_GROUP", event_types_order=["SWEEP", "ACCRUE_INTEREST"]
  )
]
```

The `SWEEP` event should define the required functionality to process the sweeping of funds from the savings account to the checking account, in accordance to the requirements defined [here](#requirements).

The `ACCRUE_INTEREST` event is only required to ensure the supervisee schedules execute after the fund sweeping has occurred. Therefore, this schedule should implement no logic and simply return the directives from the supervisees.

### Further considerations

- Additional functionality to handle ODP on a per transaction basis
- Consider any type of product be act as the ODP source
