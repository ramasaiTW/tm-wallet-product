_© Thought Machine Group Limited 2022_

_All Rights Reserved. Confidential - Limited Distribution to Authorized Persons Only, Pursuant to the Terms of the Agreement between You and Thought Machine Group Limited granting you a licence for the software to which this documentation relates. This software is protected as an unpublished work and constitutes a trade secret of Thought Machine Group Limited, 5 New Street Square, London EC4A 3TW._

This file covers implementation guidance specific to the way we create and instruct different types of directives (schedules, notifications, postings)

# Directives

Unless specified otherwise `PostingInstruction` is interchangeable with `Union[AuthorisationAdjustment, CustomInstruction, InboundAuthorisation, InboundHardSettlement, OutboundAuthorisation, OutboundHardSettlement, Release, Settlement, Transfer]` for fetched / hook argument data, or `CustomInstruction` for contract-generated data.
`PostingInstructionBatch` refers to the Posting API type, which is provided as a `list[PostingInstruction]` in `pre_posting_hook` and `post_posting_hook` hook arguments. Some `PostingInstructionBatch` attributes, like `batch_details` are denormalised onto the `PostingInstruction`.

## Posting Instruction Directives

### Atomicity and Consolidation of Directives

As a general rule, keep the number of directives instructed in a hook to a minimum (ideally one).

#### Why

A single `PostingInstructionDirective` is processed atomically. Either all `CustomInstruction` in the directive are accepted and committed or all are rejected and not committed. Instructing multiple `PostingInstructionDirective`s breaks this atomicity and can lead to scenarios where some are accepted and others are rejected, despite them coming from the same hook execution. This in turn introduces complex scenarios to debug and remediate.

Committing directives is also typically one, if not the longest part of contract execution. As the postings processor has a finite throughput reducing the number of directives to be committed helps with this.

#### How

There are many ways to accidentally instruct multiple directives. One common anti-pattern is:

```python
# DO NOT
for day in days:
    instructions = _some_method_to_generate_postings()
    PostingInstructionsDirective(
        posting_instructions=instructions,
        value_datetime=hook_arguments.effective_date,
    )
```

versus

```python
posting_instructions = []
for day in days:
    instructions.extend(_some_method_to_generate_postings())
PostingInstructionsDirective(
    posting_instructions=instructions,
    value_datetime=hook_arguments.effective_date,
)
```

### Avoid mutating contract API Types in place

It may be necessary to modify or change the attributes of a Contracts API object after it has been instantiated. However it is strongly recommended to not modify the object in place.

#### Why

Modifying an object in place will bypass any class level validation

#### How

If it is necessary to modify an object after it has been instantiated then it is recommended that a new object is instantiated instead. An example is shown below:

```python
    original_custom_instruction = CustomInstruction(
        postings=[Posting(...), Posting(...)],
        override_all_restrictions=True,
        instruction_details={
            "description": "Example CustomInstruction object",
            "event": f"Best Practice Documentation",
        },
    )
    # now lets say we want to add 2 more Posting objects to the postings attribute of the CustomInstruction object
    new_postings = [Posting(...), Posting(...)]

    # DO NOT
    original_custom_instruction.postings += new_postings

    # Instead, instantiate a new CustomInstruction object. This will ensure class validation is not bypassed
    new_custom_instruction = CustomInstruction(
        postings=original_custom_instruction.postings + new_postings,
        override_all_restrictions=original_custom_instruction.override_all_restrictions,
        instruction_details=original_custom_instruction.instruction_details
    )
```

### Use of effective_date / value_timestamp

`PostingInstructionDirective.value_timestamp` defaults to `now()`.  We recommend still using the hook effective_date as the value_timestamp unless you have a specific reason to not do so as there are some tricky nuances to be aware of:

- Consider a `PostingInstructionDirective` that is accepted by a contract and committed at 2020-01-01T23:59:59.999999Z. Any side-effects (e.g. a `PostingInstructionDirective` containing a fee) will be committed a finite amount of time later and their `value_timestamp` will be larger (e.g. 2020-01-02T00:00:00.000100Z) if not explicitly set in the contract. A schedule that observes balances as of midnight (i.e. 2020-01-02T00:00:00.000000Z) will not see the side-effects, which is typically wrong.

- Consider two schedules in a schedule group with same `effective_date`, and the second schedule relies on a balance update from the first schedule's directives. Because fetching is based on effective_date, the second schedule won't pick up the update if it's using latest balances and the posting's `value_timestamp` is > `effective_date`. This would always be the case if `value_timestamp` is set to `now()` at the postings processor level. Should you switch to `latest live` requirements to accommodate for this, you could pick up unexpected data too, so be wary of this.

- If these two schedules have different `effective_date`, there's still potentially a risk due to processing delays. Although for a given account the second schedule won't start until the first schedule is completed, the `PostingInstructionDirective` could be processed such that `now()` is greater than the second schedule’s `effective_date`. E.g. schedule 1 runs at 00:00:00, schedule 2 runs 01:00:00. Processing delays means that some of schedule 1 jobs run at 01:01:00 and then the corresponding `PostingInstructionDirective` have a `value_timestamp` > 01:00:00.

### Client Batch Id

Set this field sensibly so it can be useful in relevant use cases.

#### Why

The client_batch_id has a functional use to group thematically related posting instructions that do not belong in the same batch (e.g. a client may decide to group postings related to a transaction and its disputes). It can be searched by in Ops Dash ledger and is a parameter to `/v1/posting-instruction-batches GET`. It may therefore be partially driven by client requirements.

#### How

A sensible convention to follow is `<hook_name/event type>-<hook_execution_id>`. The event type is used for scheduled code given there could be different event types with very different directives for the same hook. For example:

`POST_POSTING-<hook_execution_id>`

`ACCRUE_INTEREST-<hook_execution_id>`

### Batch Details

Batch details are intended for all sorts of metadata, whether for human or machine consumption. Here are some suggestions.

#### Linking PIDs to their triggers

It is useful to link the posting instruction directive created by `post_posting_hook` to the triggering posting instruction batch via the batch_details. For example:

```python
batch_details = {
    'trigger_posting_instruction_batch_id' = postings.batch_id
}
```

Alternatively, we can tag them against an event_type for schedules.

#### Metadata for downstream systems

Integration requirements often drive what metadata is required. One example is providing a booking date for end-of-day processing like interest accrual, which may be delayed for operational reasons. Having the date will avoid confusion.

## Custom Instructions

### Netting Instructions

Consider whether multiple `CustomInstruction`s can be netted

#### Why

In the [Posting Instruction Directive](#posting-instruction-directives) section, we highlight that the number of directives has a significant throughput impact, but the number of instructions in a directive also matters. It is worth considering ‘netting’ postings where possible. However, this does result in a lack of granularity, so it must be confirmed against requirements (e.g. each `CustomInstruction` could have separate metadata and should be processed differently by downstream systems).

#### How

Consider a contract creating a single `PostingInstructionDirective` with the following `CustomInstruction`s:

1. Custom Instruction 1 - Accrue interest on balance tier 1 at 1%, totalling 0.12
2. Custom Instruction 2 - Accrue interest on balance tier 2 at 2%, totalling 0.05

Assuming instructions 1 and 2 are using the same accounts and balance definitions, they can be netted with no functional impact. The best option is to calculate the amounts for each accrual and then sum them to create a single `Custom`. This is preferable to generating separate `CustomInstruction` and then merging them later, as this is typically more expensive. As mentioned above, metadata can then be used to ensure no information is lost:

```python
{
    "tier_1": "0.12",
    "tier_2": "0.05"
}
```

You can also consider netting individual `Posting` objects within a `CustomInstruction`.

### Overriding Restrictions

Confirm desired behaviour with clients regarding restrictions and contract-initiated `CustomInstruction`

#### Why

Restrictions are a useful mechanism to limit or prevent certain actions, including credit and/or debit `CustomInstruction`. However, clients may have differing views on whether these should affect contract features, such as accruing interest or charging fees. Inception contracts default to `True` as this is a common request, but it can be changed easily. If there is a request to control these features more granularly, consider solutions such as flag-based controls.

#### How

Simply change the `override_all_restrictions` parameter when instantiating a `CustomInstruction`.

### Instruction Details

Set this field sensibly to meet contract or external system requirements

#### Why

Instruction details are often driven by client requirements who need specific metadata on a posting for downstream processing (e.g. feeding into the General Ledger). They are also displayed in Ops Dashboard, and provide a good opportunity to provide information to users.
In some cases, the requirements are driven by contracts themselves, as the metadata can provide additional information to the contract. Although this is typically used for external `PostingInstruction`s, contracts may also consume `CustomInstruction`s created by the same or another contract.

#### How

Some useful key-value pairs include:
    description - provides a human-friendly textual description of what this posting is doing/why
    event - if applicable, the event type that resulted in the posting instruction

## Schedules

### Updating Schedules

#### Known Race Condition

There is a known race condition when updating schedules in CLv4 where if a schedule is updated before the next schedule job is published, the updated schedule overrides the outstanding job and hence the original job may never get published. There is no way to handle this scenario from within the contract, so the guidance is to be cautious not to update schedules near to the expected execution time.
