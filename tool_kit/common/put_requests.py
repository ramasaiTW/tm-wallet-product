import json
from typing import List, Any
from tool_kit.helpers.core_api_helper import api_request


def update_account_schedule_tag(account_schedule_tag_id=None) -> List[Any]:
    """
    :param account_schedule_tag_id: The ID of the AccountScheduleTag; it is used to tag schedules in a Smart Contract or Supervisor Contract.
    """

    request_body = {}

    return api_request(
        "put", f"/v1/account-schedule-tags/{account_schedule_tag_id}", data=json.dumps(request_body)
    )


def update_account_migration(account_migration_id=None) -> List[Any]:
    """
    :param account_migration_id: A unique identifier for the account migration. Optional.
    """

    request_body = {}

    return api_request(
        "put", f"/v1/account-migrations/{account_migration_id}", data=json.dumps(request_body)
    )


def update_account(account_id=None) -> List[Any]:
    """
    :param account_id: A unique ID for an account. Optional for create requests.
    """

    request_body = {
        "account.id": account_id,
    }

    return api_request("put", f"/v1/accounts/{account_id}", data=json.dumps(request_body))


def update_account_details(account_id=None) -> List[Any]:
    """
    :param account_id: The account that is to be updated. Required.
    """

    request_body = {
        "account_id": account_id,
    }

    return api_request(
        "put", f"/v1/accounts/{account_id}:updateDetails", data=json.dumps(request_body)
    )


def update_service_account(service_account_id=None) -> List[Any]:
    """
    :param service_account_id: A unique string ID for a service account. Output only.
    """

    request_body = {
        "service_account.id": service_account_id,
    }

    return api_request(
        "put", f"/v1/service-accounts/{service_account_id}", data=json.dumps(request_body)
    )


def update_service_account_permissions(service_account_id=None) -> List[Any]:
    """
    :param service_account_id: The ID of the service account that is to be updated. Required.
    """

    request_body = {}

    return api_request(
        "put",
        f"/v1/service-accounts/{service_account_id}:updatePermissions",
        data=json.dumps(request_body),
    )


def update_calendar_event(calendar_event_id=None) -> List[Any]:
    """
    :param calendar_event_id: The ID of the calendar event that is to be updated.
    """
    request_body = {}

    return api_request(
        "put",
        f"/v1/calendar-event/{calendar_event_id}:updateDetails",
        data=json.dumps(request_body),
    )


def update_bookkeeping_date(id=None) -> List[Any]:
    """
    :param id: The ID of the Calendar to be updated.
    """

    request_body = {}

    return api_request("put", f"/v1/calendar/bookkeeping-date/{id}", data=json.dumps(request_body))


def change_current_calendar_period(calendar_id=None) -> List[Any]:
    """
    :param calendar_id: ID of the calendar.
    """

    request_body = {}

    return api_request(
        "put", f"/v1/calendar/{calendar_id}/period/current:change", data=json.dumps(request_body)
    )


def update_calendar(calendar_id=None) -> List[Any]:
    """
    :param calendar_id: The ID of the calendar that is to be updated.
    """

    request_body = {}

    return api_request(
        "put", f"/v1/calendar/{calendar_id}:updateDetails", data=json.dumps(request_body)
    )


def update_customer_address(customer_address_id=None) -> List[Any]:
    """
    :param customer_address_id: The address ID. Output only.
    """
    request_body = {}

    return api_request(
        "put", f"/v1/customer-addresses/{customer_address_id}", data=json.dumps(request_body)
    )


def update_customer(customer_id=None) -> List[Any]:
    """
    :param customer_id: The unique ID of the customer. Defaults to a UUID if not provided on creation.
    """

    request_body = {}

    return api_request("put", f"/v1/customers/{customer_id}", data=json.dumps(request_body))


def update_customer_additional_details(customer_id=None) -> List[Any]:
    """
    :param customer_id: The unique ID of the customer.
    """

    request_body = {}

    return api_request(
        "put", f"/v1/customers/{customer_id}:updateAdditionalDetails", data=json.dumps(request_body)
    )


def update_flag_definition(flag_definition_id=None) -> List[Any]:
    """
    :param flag_definition_id: The ID of the Flag Definition. Matches the name field. One of ID or name must be provided for create requests. If both are provided, ID will be used.
    """

    request_body = {}

    return api_request(
        "put", f"/v1/flag-definitions/{flag_definition_id}", data=json.dumps(request_body)
    )


def update_flag(flag_id=None) -> List[Any]:
    """
    :param flag_id: The ID of the Flag. Output only. From Vault version 5.2 onwards, this defaults to a UUID.
    """

    request_body = {}

    return api_request("put", f"/v1/flags/{flag_id}", data=json.dumps(request_body))


def update_parameter_value_hierarchy_node(parameter_value_hierarchy_node_id=None) -> List[Any]:
    """
    :param parameter_value_hierarchy_node_id: Unique identifier for the Parameter Value Hierarchy Node. Forms part of the `parent_path` for child nodes. This should not have any meaning related to the resource. It must match the regex `^[A-Za-z0-9][A-Za-z0-9-_.]*$` and its length must not exceed 256 characters. Required for create or update requests.
    """

    request_body = {}

    return api_request(
        "put",
        f"/v1/parameter-value-hierarchy-nodes/{parameter_value_hierarchy_node_id}",
        data=json.dumps(request_body),
    )


def update_parameter_value(parameter_value_id=None) -> List[Any]:
    """
    :param parameter_value_id: Unique UUID identifier for the Parameter Value. Read-only and set to a random UUID on creation.
    """

    request_body = {}

    return api_request(
        "put", f"/v1/parameter-values/{parameter_value_id}", data=json.dumps(request_body)
    )


def update_payment_device_link(payment_device_link_id=None) -> List[Any]:
    """
    :param payment_device_link_id: A caller-injected or Vault auto-generated unique ID for the payment device link. When auto-generated, this is a UUID in the canonical 8-4-4-4-12 form.
    """
    request_body = {}

    return api_request(
        "put", f"/v1/payment-device-links/{payment_device_link_id}", data=json.dumps(request_body)
    )


def update_payment_device(payment_device_id=None) -> List[Any]:
    """
    :param payment_device_id: Caller injected or Vault auto-generated unique ID for payment device. Optional. When auto-generated, this is a UUID in the canonical 8-4-4-4-12 form.
    """

    request_body = {}

    return api_request(
        "put", f"/v1/payment-devices/{payment_device_id}", data=json.dumps(request_body)
    )


def update_policy(policy_id=None) -> List[Any]:
    """
    :param policy_id: The unique identifier for the Policy. Required.
    """

    request_body = {}

    return api_request("put", f"/v1/policies/{policy_id}", data=json.dumps(request_body))


def update_postings_apiclient(postings_api_client_id=None) -> List[Any]:
    """
    :param postings_api_client_id: A unique ID that identifies a `PostingsAPIClient` to the Postings API.
    """

    request_body = {}

    return api_request(
        "put", f"/v1/postings-api-clients/{postings_api_client_id}", data=json.dumps(request_body)
    )


def update_processing_group(processing_group_id=None) -> List[Any]:
    """
    :param processing_group_id: A unique ID for the Processing Group. Optional for create requests.
    """
    request_body = {}

    return api_request(
        "put", f"/v1/processing-groups/{processing_group_id}", data=json.dumps(request_body)
    )


def update_product_version_params(product_version_id=None) -> List[Any]:
    """
    :param product_version_id: The ID of the product version to be updated.
    """
    request_body = {}

    return api_request(
        "put",
        f"/v1/product-versions/{product_version_id}:updateParams",
        data=json.dumps(request_body),
    )


def update_restriction_set(restriction_set_id=None) -> List[Any]:
    """
    :param restriction_set_id: The unique identifier for this restriction set.
    """

    request_body = {}

    return api_request(
        "put", f"/v1/restriction-sets/{restriction_set_id}", data=json.dumps(request_body)
    )


def delete_post_posting_failures(id=None) -> List[Any]:
    """
    :param restriction_set_id: The unique identifier for this restriction set.
    """

    return api_request("put", f"/v1/post-posting-failures/{id}")
