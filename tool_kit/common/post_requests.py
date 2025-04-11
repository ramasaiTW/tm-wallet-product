import json
from typing import List, Any
from tool_kit.helpers.core_api_helper import api_request


def create_account_schedule_tag() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/account-schedule-tags", data=json.dumps(request_body))


def create_account_migration() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/account-migrations", data=json.dumps(request_body))


def create_account_update_batch() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/account-update-batches", data=json.dumps(request_body))


def create_account_update() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/account-updates", data=json.dumps(request_body))


def create_account() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/accounts", data=json.dumps(request_body))


def create_service_account() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/service-accounts", data=json.dumps(request_body))


def create_calendar() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/calendar", data=json.dumps(request_body))


def create_calendar_event() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/calendar-event", data=json.dumps(request_body))


def create_calendar_period_descriptor() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/calendar-period-descriptor", data=json.dumps(request_body))


def create_contract_module_version() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/contract-module-versions", data=json.dumps(request_body))


def create_contract_module() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/contract-modules", data=json.dumps(request_body))


def create_smart_contract_module_versions_link() -> List[Any]:
    request_body = {}
    return api_request(
        "post", "/v1/smart-contract-module-versions-links", data=json.dumps(request_body)
    )


def simulate_contracts() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/contracts:simulate", data=json.dumps(request_body))


def create_customer_address() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/customer-addresses", data=json.dumps(request_body))


def create_customer() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/customers", data=json.dumps(request_body))


def search_customers() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/customers:search", data=json.dumps(request_body))


def replay_journal_events() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/journal-events:replay", data=json.dumps(request_body))


def create_flag_definition() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/flag-definitions", data=json.dumps(request_body))


def create_flag() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/flags", data=json.dumps(request_body))


def create_global_parameter_value() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/global-parameter-values", data=json.dumps(request_body))


def create_global_parameter() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/global-parameters", data=json.dumps(request_body))


def create_internal_account() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/internal-accounts", data=json.dumps(request_body))


def create_parameter_value_hierarchy_node() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/parameter-value-hierarchy-nodes", data=json.dumps(request_body))


def create_parameter_value() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/parameter-values", data=json.dumps(request_body))


def batch_create_parameter_values() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/parameter-values:batchCreate", data=json.dumps(request_body))


def create_parameter() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/parameters", data=json.dumps(request_body))


def create_payment_device_link() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/payment-device-links", data=json.dumps(request_body))


def create_payment_device() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/payment-devices", data=json.dumps(request_body))


def create_plan_migration() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/plan-migrations", data=json.dumps(request_body))


def create_plan_update() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/plan-updates", data=json.dumps(request_body))


def create_plan() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/plans", data=json.dumps(request_body))


def create_policy() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/policies", data=json.dumps(request_body))


def republish_post_posting_failure() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/post-posting-failures:republish", data=json.dumps(request_body))


def validate_create_posting_instruction_batch_request() -> List[Any]:
    request_body = {}
    return api_request(
        "post", "/v1/create-posting-instruction-batch:validate", data=json.dumps(request_body)
    )


def create_posting_instruction_batch() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/posting-instruction-batches", data=json.dumps(request_body))


def create_posting_instruction_batch_async() -> List[Any]:
    request_body = {}
    return api_request(
        "post", "/v1/posting-instruction-batches:asyncCreate", data=json.dumps(request_body)
    )


def create_postings_apiclient() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/postings-api-clients", data=json.dumps(request_body))


def create_processing_group() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/processing-groups", data=json.dumps(request_body))


def create_product_version() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/product-versions", data=json.dumps(request_body))


def create_restriction_set_definition_version() -> List[Any]:
    request_body = {}
    return api_request(
        "post", "/v1/restriction-set-definition-versions", data=json.dumps(request_body)
    )


def create_restriction_set_definition_version2(
    restriction_set_definition_version_restriction_set_definition_id=None,
) -> List[Any]:
    """
    :param restriction_set_definition_version_restriction_set_definition_id: The ID or name of the restriction set definition this version belongs to. Required for create requests.
    """
    if restriction_set_definition_version_restriction_set_definition_id is None:
        restriction_set_definition_version_restriction_set_definition_id = ""

    request_body = {
        "restriction_set_definition_version.restriction_set_definition_id": restriction_set_definition_version_restriction_set_definition_id,
    }
    return api_request(
        "post",
        f"/v1/restriction-set-definition/{restriction_set_definition_version_restriction_set_definition_id}/versions",
        data=json.dumps(request_body),
    )


def create_restriction_set() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/restriction-sets", data=json.dumps(request_body))


def republish_job(id=None) -> List[Any]:
    """
    :param id: The ID of the Job to be republished.
    """
    return api_request("post", f"/v1/jobs/{id}:republish")


def batch_republish_jobs() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/jobs:batchRepublish", data=json.dumps(request_body))


def create_schedule_tag() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/schedule-tags", data=json.dumps(request_body))


def create_supervisor_contract_version() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/supervisor-contract-versions", data=json.dumps(request_body))


def create_supervisor_contract() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/supervisor-contracts", data=json.dumps(request_body))
