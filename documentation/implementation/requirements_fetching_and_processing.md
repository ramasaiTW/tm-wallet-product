_© Thought Machine Group Limited 2022_

_All Rights Reserved. Confidential - Limited Distribution to Authorized Persons Only, Pursuant to the Terms of the Agreement between You and Thought Machine Group Limited granting you a licence for the software to which this documentation relates. This software is protected as an unpublished work and constitutes a trade secret of Thought Machine Group Limited, 5 New Street Square, London EC4A 3TW._

This file covers guidance and assumptions relating to fetching and processing data requirements, regardless of the hooks they take place in.

# Requirements Fetching and Processing

Unless specified otherwise `PostingInstruction` is interchangeable with `Union[AuthorisationAdjustment, CustomInstruction, InboundAuthorisation, InboundHardSettlement, OutboundAuthorisation, OutboundHardSettlement, Release, Settlement, Transfer]` for fetched / hook argument data, or `CustomInstruction` for contract-generated data.
`PostingInstructionBatch` refers to the Posting API type, which is provided as a `list[PostingInstruction]` in `pre_posting_hook` and `post_posting_hook` hook arguments. Some `PostingInstructionBatch` attributes, like `batch_details` are denormalised onto the `PostingInstruction`.

## General Considerations

### Use of Observations and Intervals

Observations are preferred and Intervals should only really be used if there is no suitable Observation syntax for the required data.

#### Why

An observation allows us to constrain fetched data to (1 x n) data points. Using balances as an example,  `n` is the number of unique Balance Coordinates on the account. `n` is fairly well controlled by the contract writer, as they usually dictate the addresses being used. Of course, integrations can create postings with any combination of address, asset, denomination, and phase, but there is little to be done about that.
In contrast, an Interval will return (m x n) data points, where `m` is the number of entries in the timeseries. The contract writer has fairly little control on `m` as this is dictated by integrations. For example, an account may
have received any number of postings between two datetimes. Even if the interval is small, this only reduces the likelihood of `m` being large.

#### How

Contract writers must understand exactly why they need an interval and consider alternatives. There are tell-tale signs that an interval isn't actually needed:

- the contract only ever uses the `.latest()` method on the interval's timeseries - this is a clear indication that a latest or live observation could be used
- the contract only ever uses `.at()` method on the interval's timeseries, with a single datetime. In some cases this is acceptable, if that datetime is not known at fetching time

Even if an interval seems necessary, it is also worth considering alternatives. For example, using an extra address to avoid using an interval is likely to be much more performant.

### Decorator ordering

When providing decorators for a given hook, it should be defined in the following way:

```python
@requires(...)
@fetch_account_data(...)
def hook_name(vault, hook_arguments):
    ...
```

with `requires` first and `fetch_account_data` second. For `scheduled_event_hook`, the decorators for each event should be in this order, and kept together to keep it easy to read and maintain. i.e.

```python
@requires(EVENT_1)
@fetch_account_data(EVENT_1)
@requires(EVENT_2)
@fetch_account_data(EVENT_2)
def scheduled_event_hook(vault, hook_arguments):
    ...
```

### Performance

Please refer to the documentation hub reference at `<your_docs_hub_url>/reference/contracts/performance_considerations` for information concerning requirements fetching and impact to performance.

## Postings

### Determining posting amounts

Avoid relying on `amount` and `PostingInstruction` attributes to determine the impact of a `PostingInstruction` to an account's balances

#### Why

Relying on `amount` will work with the simplest uses of the various `PostingInstruction` types (e.g. hard settlements, transfers). As soon as multiple settlements, releases or authorisation adjustments are involved, the behaviour of these fields is not as intuitive and calculating the actual amount effectively requires replicating Posting API logic.

#### How

The `PostingInstruction` types have a `.balances()` method that will safely provide the net impact to each set of Balance dimensions. It can be useful to have a reusable helper to extract a Decimal from these balances. For example:

```python
def _available_balance(balances: BalanceDefaultDict) -> Decimal:
    pass
```

This helper can be used to check the available balance at a given point in time, by passing in data from `vault.get_balance_timeseries().latest()/at()/before()`, `vault.get_balances_observation(..).balances`, or can be used to check the impact of a given `PostingInstruction` by passing in the relevant `.balances()` output.

It is ok to rely on `amount` provided you have already filtered for the hard settlement/transfer types, as these behave intuitively

### Handling 0 amount Postings

Logic that handles `PostingInstruction` amounts (see [Determining posting amounts](#determining-posting-amounts)) should account for 0 and None amount postings.

#### Why

Although 0 amounts are not allowed on the Core/Postings API, there are scenarios where Vault's ledger behaviour can result in 0 amounts. For example:

- Outbound authorisation for $1
- Non-Final settlement for $1
- Final settlement with no amount - this last instruction result in 0 amount, as would a release

or when creating an authorisation adjustment with a replacement amount equal to the currently authorised amount:

- Outbound authorisation for $1
- Authorisation adjustment with replacement_amount = $1

#### How

If you use a condition like below, be aware that the `== 0` will go into one of the branches and the logic must be able to handle it.

```python
if amount > 0: # (or < 0)
    ...
else:
    ...
```

Alternatively, you might find it easier to discard/no-op the `== 0` scenario

```python
if amount<0:
    ...
elif amount > 0:
    ...
else
    pass
```

## Client Transactions

### Client Transaction Types

We allow client transactions to have a 'type' that is set by the first posting instruction in the client transaction.

#### Why

Product features often operate on a transaction type level (e.g. limit the number of ATM withdrawals in a month, charge a different interest rate for purchases). We need a consistent way of identifying the type, to reduce integration burden.
We are unaware of significant use cases where the type will change across the lifecycle of a client transaction, so we can reduce contract complexity by assuming that it is fixed at the creation of the client transaction (i.e. the first posting instruction with the specific client transaction id).

#### How

- We prefer to use the `type` key on `PostingInstruction.instruction_details`. Our client transaction utils support other keys if further granularity is required.
- We read this key on the first `PostingInstruction` returned by `ClientTransaction.posting_instructions`

### Client Transaction Granularity

We assume that each posting instruction within a client transaction that alters the client transaction's net balance represents an additional debit/credit of that client transaction's type.

#### Why

Consider an initial authorisation for $100. If this is settled via a non-final settlement and a subsequent final settlement, each for $50, we consider it would be arguably unfair to count it twice with respect to a transaction type limit.
Now consider that this authorisation is increased explicitly via authorisation adjustment or implicitly via a settlement above the initial authorisation amount. We consider this amendment to be more like an additional transaction, and would therefore count it with respect to a transaction type limit.

#### How

N/A
