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


def create_plan(
    request_id: str = None,
    plan_id: str = None,
    supervisor_contract_version_id: str = None,
    status: str = None,
    processing_group_id: str = None,
    details: dict = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "plan": {
            "id": plan_id,
            "supervisor_contract_version_id": supervisor_contract_version_id,
            "status": status,
            "processing_group_id": processing_group_id,
            "details": details,
        },
    }
    return api_request("post", "/v1/plans", data=json.dumps(request_body))


def create_policy(
    request_id: str = None,
    policy_id: str = None,
    policy_schema_id: str = None,
    description: str = None,
    rego_source: str = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "policy": {
            "id": policy_id,
            "policy_schema_id": policy_schema_id,
            "description": description,
            "rego_source": rego_source,
        },
    }
    return api_request("post", "/v1/policies", data=json.dumps(request_body))


def republish_post_posting_failure(
    republish_type: str = None, contract_execution_behaviour: str = None, account_id: str = None
) -> List[Any]:
    request_body = {
        "republish_type": republish_type,
        "contract_execution_behaviour": contract_execution_behaviour,
        "account_id": account_id,
    }
    return api_request("post", "/v1/post-posting-failures:republish", data=json.dumps(request_body))


def validate_create_posting_instruction_batch_request(
    request_id: str = None,
    client_id: str = None,
    client_batch_id: str = None,
    client_transaction_id: str = None,
    amount: str = None,
    denomination: str = None,
    target_account_id: str = None,
    internal_account_id: str = None,
    advice: bool = None,
    instruction_details: dict = None,
    batch_details: dict = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "posting_instruction_batch": {
            "client_id": client_id,
            "client_batch_id": client_batch_id,
            "posting_instructions": [
                {
                    "client_transaction_id": client_transaction_id,
                    "outbound_authorisation": {
                        "amount": amount,
                        "denomination": denomination,
                        "target_account": {"account_id": target_account_id},
                        "internal_account_id": internal_account_id,
                        "advice": advice,
                    },
                    "instruction_details": instruction_details,
                }
            ],
            "batch_details": batch_details,
        },
    }
    return api_request(
        "post", "/v1/create-posting-instruction-batch:validate", data=json.dumps(request_body)
    )


def create_posting_instruction_batch(
    request_id: str = None,
    dry_run: bool = None,
    client_id: str = None,
    client_batch_id: str = None,
    client_transaction_id: str = None,
    pics: list = None,
    instruction_details: dict = None,
    restrictions: dict = None,
    transaction_code: dict = None,
    value_timestamp: str = None,
    booking_timestamp: str = None,
    enrichments: dict = None,
    outbound_authorisation: dict = None,
    batch_details: dict = None,
    time_to_live: str = None,
    shard_key: str = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "dry_run": dry_run,
        "posting_instruction_batch": {
            "client_id": client_id,
            "client_batch_id": client_batch_id,
            "posting_instructions": [
                {
                    "client_transaction_id": client_transaction_id,
                    "pics": pics,
                    "instruction_details": instruction_details,
                    "override": {"restrictions": restrictions},
                    "transaction_code": transaction_code,
                    "value_timestamp": value_timestamp,
                    "booking_timestamp": booking_timestamp,
                    "enrichments": enrichments,
                    "outbound_authorisation": outbound_authorisation,
                }
            ],
            "batch_details": batch_details,
            "value_timestamp": value_timestamp,
            "booking_timestamp": booking_timestamp,
        },
        "time_to_live": time_to_live,
        "shard_key": shard_key,
    }
    return api_request("post", "/v1/posting-instruction-batches", data=json.dumps(request_body))


def create_posting_instruction_batch_async(
    request_id: str = None,
    client_id: str = None,
    client_batch_id: str = None,
    client_transaction_id: str = None,
    amount: str = None,
    denomination: str = None,
    target_account_id: str = None,
    internal_account_id: str = None,
    advice: bool = None,
    instruction_details: dict = None,
    batch_details: dict = None,
    api_type: str = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "posting_instruction_batch": {
            "client_id": client_id,
            "client_batch_id": client_batch_id,
            "posting_instructions": [
                {
                    "client_transaction_id": client_transaction_id,
                    "outbound_authorisation": {
                        "amount": amount,
                        "denomination": denomination,
                        "target_account": {"account_id": target_account_id},
                        "internal_account_id": internal_account_id,
                        "advice": advice,
                    },
                    "instruction_details": instruction_details,
                }
            ],
            "batch_details": batch_details,
        },
        "api_type": api_type,
    }
    return api_request(
        "post", "/v1/posting-instruction-batches:asyncCreate", data=json.dumps(request_body)
    )


def create_postings_apiclient(
    request_id: str = None, postings_api_client_id: str = None, response_topic: str = None
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "postings_api_client": {"id": postings_api_client_id, "response_topic": response_topic},
    }
    return api_request("post", "/v1/postings-api-clients", data=json.dumps(request_body))


def create_processing_group(
    request_id: str = None,
    processing_group_id: str = None,
    timezone: str = None,
    minimum_observation_timestamp: str = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "processing_group": {
            "id": processing_group_id,
            "timezone": timezone,
            "minimum_observation_timestamp": minimum_observation_timestamp,
        },
    }
    return api_request("post", "/v1/processing-groups", data=json.dumps(request_body))


def create_product_version(
    request_id: str = None,
    display_name: str = None,
    description: str = None,
    summary: str = None,
    tags: list = None,
    core_tags: list = None,
    params: list = None,
    code: str = None,
    product_id: str = None,
    supported_denominations: list = None,
    migration_strategy: str = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "product_version": {
            "display_name": display_name,
            "description": description,
            "summary": summary,
            "tags": tags,
            "core_tags": core_tags,
            "params": params,
            "code": code,
            "product_id": product_id,
            "supported_denominations": supported_denominations,
            "high_volume_eligibility": {"ledger": True},
        },
        "migration_strategy": migration_strategy,
        "is_internal": True,
    }
    return api_request("post", "/v1/product-versions", data=json.dumps(request_body))


def create_restriction_set_definition_version(
    restriction_set_definition_id=None,
    restriction_type=None,
    required_restriction_levels=None,
    request_id=None,
) -> List[Any]:
    request_body = {
        "restriction_set_definition_version": {
            "restriction_definitions": [
                {
                    "restriction_type": restriction_type,
                    "required_restriction_levels": required_restriction_levels,
                }
            ],
            "restriction_set_definition_id": restriction_set_definition_id,
        },
        "request_id": request_id,
    }
    return api_request(
        "post", "/v1/restriction-set-definition-versions", data=json.dumps(request_body)
    )


def create_restriction_set_definition_version2(
    restriction_set_definition_id=None,
    restriction_type=None,
    required_restriction_levels=None,
    request_id=None,
) -> List[Any]:
    request_body = {
        "restriction_set_definition_version": {
            "restriction_definitions": [
                {
                    "restriction_type": restriction_type,
                    "required_restriction_levels": required_restriction_levels,
                }
            ],
            "restriction_set_definition_id": restriction_set_definition_id,
        },
        "request_id": request_id,
    }
    return api_request(
        "post",
        f"/v1/restriction-set-definition/{restriction_set_definition_id}/versions",
        data=json.dumps(request_body),
    )


def create_restriction_set(
    request_id: str = None,
    restriction_set_definition_id: str = None,
    restriction_set_definition_version_id: str = None,
    name: str = None,
    description: str = None,
    restriction_set_parameters: dict = None,
    customer_id: str = None,
    account_id: str = None,
    payment_device_id: str = None,
    effective_timestamp: str = None,
    expiry_timestamp: str = None,
) -> List[Any]:
    request_body = {
        "restriction_set": {
            "restriction_set_definition_id": restriction_set_definition_id,
            "restriction_set_definition_version_id": restriction_set_definition_version_id,
            "name": name,
            "description": description,
            "restriction_set_parameters": restriction_set_parameters,
            "customer_id": customer_id,
            "account_id": account_id,
            "payment_device_id": payment_device_id,
            "effective_timestamp": effective_timestamp,
            "expiry_timestamp": expiry_timestamp,
        },
        "request_id": request_id,
    }
    return api_request("post", "/v1/restriction-sets", data=json.dumps(request_body))


def republish_job(id=None) -> List[Any]:
    return api_request("post", f"/v1/jobs/{id}:republish")


def batch_republish_jobs(
    ids: List[str] = None, target_status: str = "JOB_STATUS_PUBLISHED"
) -> List[Any]:
    request_body = {"ids": ids, "target_status": target_status}
    return api_request("post", "/v1/jobs:batchRepublish", data=json.dumps(request_body))


def create_schedule_tag(
    request_id: str = None,
    schedule_tag_id: str = None,
    description: str = None,
    sends_scheduled_operation_reports: bool = True,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "schedule_tag": {
            "id": schedule_tag_id,
            "description": description,
            "sends_scheduled_operation_reports": sends_scheduled_operation_reports,
        },
    }
    return api_request("post", "/v1/schedule-tags", data=json.dumps(request_body))


def create_supervisor_contract_version(
    request_id: str = None,
    supervisor_contract_version_id: str = None,
    supervisor_contract_id: str = None,
    display_name: str = None,
    description: str = None,
    code: str = None,
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "supervisor_contract_version": {
            "id": supervisor_contract_version_id,
            "supervisor_contract_id": supervisor_contract_id,
            "display_name": display_name,
            "description": description,
            "code": code,
        },
    }
    return api_request("post", "/v1/supervisor-contract-versions", data=json.dumps(request_body))


def create_supervisor_contract(
    request_id: str = None, supervisor_contract_id: str = None, display_name: str = None
) -> List[Any]:
    request_body = {
        "request_id": request_id,
        "supervisor_contract": {"id": supervisor_contract_id, "display_name": display_name},
    }
    return api_request("post", "/v1/supervisor-contracts", data=json.dumps(request_body))