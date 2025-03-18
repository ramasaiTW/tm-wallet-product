_© Thought Machine Group Limited 2022_

_All Rights Reserved. Confidential - Limited Distribution to Authorized Persons Only, Pursuant to the Terms of the Agreement between You and Thought Machine Group Limited granting you a licence for the software to which this documentation relates. This software is protected as an unpublished work and constitutes a trade secret of Thought Machine Group Limited, 5 New Street Square, London EC4A 3TW._

This file covers guidance relating to specific hooks

# Hooks

Unless specified otherwise `PostingInstruction` is interchangeable with `Union[AuthorisationAdjustment, CustomInstruction, InboundAuthorisation, InboundHardSettlement, OutboundAuthorisation, OutboundHardSettlement, Release, Settlement, Transfer]` for fetched / hook argument data, or `CustomInstruction` for contract-generated data.
`PostingInstructionBatch` refers to the Posting API type, which is provided as a `list[PostingInstruction]` in `pre_posting_hook` and `post_posting_hook` hook arguments. Some `PostingInstructionBatch` attributes, like `batch_details` are denormalised onto the `PostingInstruction`.

## Do not add Empty hooks

Never add empty hooks to a contract

### Why

A hook will always be executed by Vault if a relevant event occurs, even if the hook has neither logic nor fetching. For example, an empty post-parameter hook will be triggered after every parameter change. This has a performance cost for no benefit and should be avoided.

## Posting Hooks

### Posting Overrides

Consider having `PostingInstruction`/`PostingInstructionBatch` level overrides in both posting hooks.

#### Why

There are often scenarios, such as unusual operational requests, or incident remediation, where we want to bypass hooks processing at varying levels. At times this can be useful for testing purposes too. For example, we may prevent withdrawals from Deposit products with specific T&Cs, but need to bypass this if a customer was accidentally credited excessive balances.

#### How

It is ultimately up to the client/contract writer to make a call on the level at which these overrides sit, and where they sit inside the hook (e.g. should they bypass all processing, or just specific features?).
The following example works at an `PostingInstructionBatch` level, making use of the `batch_details` metadata on the `PostingInstruction`. A custom `withdrawal_override` key is added and, if it's value is `true` (irrespective of case), we return early. The same concept could be applied to an individual posting, using `PostingInstruction`'s `instruction_details`.

```python
    if posting_instruction.batch_details.get("withdrawal_override", "false").lower() == "true":
        return
```

> While the `PostingInstruction` `advice` attribute aims to serve this purpose, we tend not to use is as a) it does not exist on all instruction types and b) it lacks the context-based granularity we sometimes need.

### Explicitly Support/Reject Multiple Instructions

A posting hook's hook arguments can include multiple `PostingInstruction`. We recommend explicitly rejecting these scenarios if the contract has not been designed with this in mind.

#### Why

There are a number of complexities that can arise from processing multiple `ProcessInstruction` in posting hooks. Unless the contract has been designed to handle these, blindly allowing them can be dangerous.

#### How

A simple block can be added to the `pre_posting_hook` and `post_posting_hook`. The latter is required as some instructions are not sent to `pre_posting_hook` and won't be caught there (e.g. `Settlement` instructions).

```python
def pre_posting_hook(
    vault: SmartContractVault, hook_arguments: PrePostingHookArguments
) -> Optional[PrePostingHookResult]:
    if len(hook_arguments.posting_instructions) > 1:
        return PrePostingHookResult(rejection=Rejection(
            message="Multiple postings in batch not supported",
            reason_code=RejectionReason.CLIENT_CUSTOM_REASON,
        ))
```

## Deactivation_hook

### Zero-out Custom Addresses

The `deactivation_hook` hook should zero out any custom addresses that the contract uses.

#### Why

Contracts should encapsulate their logic as much as possible and not rely on other services knowing about implementation details like custom addresses. Otherwise we risk tightly coupling the contract and these services, making upgrades more complicated. This is actually the main purpose behind the `deactivation_hook` hook.

#### How

The `deactivation_hook` should follow a few simple rules:

1. Consider every existing address that can be non-zero when deactivation_hook is run and define if and how they should be zero'd out. In some cases, it may not be ok for `deactivation_hook` to not zero-out these balances (e.g. we expect the customer to repay outstanding balances before they can close the account). If this is the case, `deactivation_hook` should be made to fail explicitly when these conditions are not met. This can be achieved as follows (example from the credit card).

    ```python
    if full_outstanding_balance != Decimal(0):
        return DeactivationHookResult(
            rejection=Rejection(
                message="Full Outstanding Balance is not zero",
                reason_code=RejectedReason.CLIENT_CUSTOM_REASON,
            )
        )
    ```

2. Do not create any new addresses within `deactivation_hook` that you cannot zero out within the same hook execution

A good example to consider is interest accrual. A contract may need closing before accrued interest has been applied, or there may be an accrued interest amount that is too small to be applied. In both cases there will be a non-zero accrual balance definition which `deactivation_hook` should deal with. The precise behaviour needs to be driven by business requirements. In this case the product may need to zero-out or apply any unapplied interest, and decide what to do with the remainder (zero-out, round up, round down).

## Derived Parameter Hook

### Use Effective Datetime

We recommend using `effective_datetime` as the reference point inside `derived_parameter_hook` logic.

#### Why

`derived_parameter_hook` is executed when an account is requested with derived parameters via Core API. The Core API request can include the `instance_param_vals_effective_timestamp` field, which provides a time to execute the hook as-of. Not using `effective_datetime` will prevent the field from being respected.

#### How

There are two key points:

- Fetchers should be anchored to effective datetime (e.g. either start or end explicitly on `DefinedDateTime.EFFECTIVE_DATETIME` or use a `RelativeDateTime` expression with `origin=DefinedDateTime.EFFECTIVE_DATETIME`).
- Contract code should use the `effective_datetime` hook argument where relevant
