# Acceptance Criteria Coverage

To track the coverage provided by tests, the `@ac_coverage()` decorator can be added to test functions to easily reference the acceptance criteria covered by the given test. For example, the following test case would provide coverage for AC01 for CPP-123, and AC02 for CPP-456:

```python
@ac_mapping(["CPP-123-AC01", "CPP-456-AC02"])
def test_case_1(self):
    ...
```

When building a product with Product Composition, there will be acceptance criteria defined by the product itself, the CBFs it comprises of, and any CBF associations. The mapping to be provided in the decorator is constructed as follows:

- `CPP-123-AC01` for **CBF ACs**, where:
  - `CPP-123` is the relevant CPP number (found in the CBF document)
  - `AC01` is the AC number defined in the requirements table
- `CPP-456-X-AC02` for **Product ACs** and **CBF Association ACs**, where:
  - `CPP-123` is the relevant CPP number (found in the Product Requirements or CBF Associations document)
  - `X` is the section number in the document
  - `AC01` is the AC number defined in the requirements table

## Implementing in tests

The `@ac_coverage()` decorator should contain a list of all the ACs which the given test covers. However, some ACs will be covered by several tests so sensible judgement should be used to keep the list to a reasonable length. For example, basic interest accrual may be implicitly tested in multiple tests, so including the required ACs in some of the simple tests would suffice, and more complex edge cases can be added to cover less generic requirements.
