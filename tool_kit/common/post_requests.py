import json
from typing import List, Any, Dict, Optional
from tool_kit.helpers.core_api_helper import api_request


def create_account_schedule_tag(
    request_id: str = "",
    tag_id: str = "",
    description: str = "",
    sends_scheduled_operation_reports: bool = False,
    schedule_status_override: str = "ACCOUNT_SCHEDULE_TAG_SCHEDULE_STATUS_OVERRIDE_UNKNOWN",
    override_start_timestamp: str = "",
    override_end_timestamp: str = "",
    test_pause_at_timestamp: str = "",
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "account_schedule_tag": {
            "id": tag_id,
            "description": description,
            "sends_scheduled_operation_reports": sends_scheduled_operation_reports,
            "schedule_status_override": schedule_status_override,
            "schedule_status_override_start_timestamp": override_start_timestamp,
            "schedule_status_override_end_timestamp": override_end_timestamp,
            "test_pause_at_timestamp": test_pause_at_timestamp,
        },
    }
    return api_request("post", "/v1/account-schedule-tags", data=json.dumps(request_body))


def create_account_migration(
    request_id: str = "",
    migration_id: str = "",
    from_product_version_ids: List[str] = None,
    to_product_version_id: str = "",
    schedule_migration_type: str = "SCHEDULE_MIGRATION_TYPE_RECREATE_ALL_SCHEDULES_AND_GROUPS",
) -> List[Any]:
    if from_product_version_ids is None:
        from_product_version_ids = []

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "account_migration": {
            "id": migration_id,
            "product_version_migration": {
                "from_product_version_ids": from_product_version_ids,
                "to_product_version_id": to_product_version_id,
                "schedule_migration_type": schedule_migration_type,
            },
        },
    }
    return api_request("post", "/v1/account-migrations", data=json.dumps(request_body))


def create_account_update_batch(
    request_id: str = "",
    batch_id: str = "",
    account_updates: Optional[List[Dict[str, Any]]] = None,
    invalid_account_update_handling_type: str = "INVALID_ACCOUNT_UPDATE_HANDLING_TYPE_FAIL_BATCH",
) -> List[Any]:
    if account_updates is None:
        account_updates = []

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "account_update_batch": {"id": batch_id, "account_updates": account_updates},
        "create_options": {
            "invalid_account_update_handling_type": invalid_account_update_handling_type
        },
    }
    return api_request("post", "/v1/account-update-batches", data=json.dumps(request_body))


def create_account_update(
    request_id: str = "",
    update_id: str = "",
    account_id: str = "",
    instance_param_vals: Optional[Dict[str, Any]] = None,
) -> List[Any]:
    if instance_param_vals is None:
        instance_param_vals = {}

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "account_update": {
            "id": update_id,
            "account_id": account_id,
            "instance_param_vals_update": {"instance_param_vals": instance_param_vals},
        },
    }
    return api_request("post", "/v1/account-updates", data=json.dumps(request_body))


def create_account(
    request_id: str = "",
    account_id: str = "",
    product_id: str = "",
    product_version_id: str = "",
    permitted_denominations: Optional[List[str]] = None,
    status: str = "ACCOUNT_STATUS_UNKNOWN",
    opening_timestamp: str = "",
    stakeholder_ids: Optional[List[str]] = None,
    instance_param_vals: Optional[Dict[str, Any]] = None,
    details: Optional[Dict[str, Any]] = None,
) -> List[Any]:
    if permitted_denominations is None:
        permitted_denominations = []
    if stakeholder_ids is None:
        stakeholder_ids = []
    if instance_param_vals is None:
        instance_param_vals = {}
    if details is None:
        details = {}

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "account": {
            "id": account_id,
            "product_id": product_id,
            "product_version_id": product_version_id,
            "permitted_denominations": permitted_denominations,
            "status": status,
            "opening_timestamp": opening_timestamp,
            "stakeholder_ids": stakeholder_ids,
            "instance_param_vals": instance_param_vals,
            "details": details,
        },
    }
    return api_request("post", "/v1/accounts", data=json.dumps(request_body))


def create_service_account(
    name: str = "", permissions: Optional[List[str]] = None, request_id: str = ""
) -> List[Any]:
    if permissions is None:
        permissions = []

    request_body: Dict[str, Any] = {
        "service_account": {"name": name, "permissions": permissions},
        "request_id": request_id,
    }
    return api_request("post", "/v1/service-accounts", data=json.dumps(request_body))


def create_calendar(
    request_id: str = "",
    calendar_id: str = "",
    calendar_period_descriptor_id: str = "",
    is_active: bool = False,
    create_timestamp: str = "",
    display_name: str = "",
    description: str = "",
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "calendar": {
            "id": calendar_id,
            "calendar_period_descriptor_id": calendar_period_descriptor_id,
            "is_active": is_active,
            "create_timestamp": create_timestamp,
            "display_name": display_name,
            "description": description,
        },
    }
    return api_request("post", "/v1/calendar", data=json.dumps(request_body))


def create_calendar_event(
    request_id: str = "",
    event_id: str = "",
    calendar_id: str = "",
    name: str = "",
    is_active: bool = False,
    start_timestamp: str = "",
    end_timestamp: str = "",
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "calendar_event": {
            "id": event_id,
            "calendar_id": calendar_id,
            "name": name,
            "is_active": is_active,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
        },
    }
    return api_request("post", "/v1/calendar-event", data=json.dumps(request_body))


def create_calendar_period_descriptor(
    request_id: str = "",
    descriptor_id: str = "",
    name: str = "",
    start_timestamp: str = "",
    resolution_unit: str = "TIME_UNIT_UNKNOWN",
    resolution_value: int = 0,
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "calendar_period_descriptor": {
            "id": descriptor_id,
            "name": name,
            "start_timestamp": start_timestamp,
            "resolution": {"unit": resolution_unit, "value": resolution_value},
        },
    }
    return api_request("post", "/v1/calendar-period-descriptor", data=json.dumps(request_body))


def create_contract_module_version(
    request_id: str = "",
    version_id: str = "",
    contract_module_id: str = "",
    display_name: str = "",
    description: str = "",
    code: str = "",
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "contract_module_version": {
            "id": version_id,
            "contract_module_id": contract_module_id,
            "display_name": display_name,
            "description": description,
            "code": code,
        },
    }
    return api_request("post", "/v1/contract-module-versions", data=json.dumps(request_body))


def create_contract_module(
    request_id: str = "", module_id: str = "", display_name: str = "", description: str = ""
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "contract_module": {
            "id": module_id,
            "display_name": display_name,
            "description": description,
        },
    }
    return api_request("post", "/v1/contract-modules", data=json.dumps(request_body))


def create_smart_contract_module_versions_link(
    request_id: str = "",
    link_id: str = "",
    smart_contract_version_id: str = "",
    alias_to_contract_module_version_id: Optional[Dict[str, str]] = None,
) -> List[Any]:
    if alias_to_contract_module_version_id is None:
        alias_to_contract_module_version_id = {}

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "smart_contract_module_versions_link": {
            "id": link_id,
            "smart_contract_version_id": smart_contract_version_id,
            "alias_to_contract_module_version_id": alias_to_contract_module_version_id,
        },
    }
    return api_request(
        "post", "/v1/smart-contract-module-versions-links", data=json.dumps(request_body)
    )


def simulate_contracts(
    start_timestamp: str = "",
    end_timestamp: str = "",
    smart_contracts: Optional[List[Dict[str, Any]]] = None,
    existing_smart_contracts: Optional[List[Dict[str, Any]]] = None,
    supervisor_contracts: Optional[List[Dict[str, Any]]] = None,
    existing_supervisor_contracts: Optional[List[Dict[str, Any]]] = None,
    contract_modules: Optional[List[Dict[str, Any]]] = None,
    existing_contract_modules: Optional[List[Dict[str, Any]]] = None,
    existing_accounts: Optional[List[Dict[str, Any]]] = None,
    existing_product_data_behaviour: Optional[Dict[str, Any]] = None,
    instructions: Optional[List[Dict[str, Any]]] = None,
    outputs: Optional[List[Dict[str, Any]]] = None,
) -> List[Any]:
    if smart_contracts is None:
        smart_contracts = []
    if existing_smart_contracts is None:
        existing_smart_contracts = []
    if supervisor_contracts is None:
        supervisor_contracts = []
    if existing_supervisor_contracts is None:
        existing_supervisor_contracts = []
    if contract_modules is None:
        contract_modules = []
    if existing_contract_modules is None:
        existing_contract_modules = []
    if existing_accounts is None:
        existing_accounts = []
    if existing_product_data_behaviour is None:
        existing_product_data_behaviour = {"include_all": True, "include_data_types": []}
    if instructions is None:
        instructions = []
    if outputs is None:
        outputs = []

    request_body: Dict[str, Any] = {
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "smart_contracts": smart_contracts,
        "existing_smart_contracts": existing_smart_contracts,
        "supervisor_contracts": supervisor_contracts,
        "existing_supervisor_contracts": existing_supervisor_contracts,
        "contract_modules": contract_modules,
        "existing_contract_modules": existing_contract_modules,
        "existing_accounts": existing_accounts,
        "existing_product_data_behaviour": existing_product_data_behaviour,
        "instructions": instructions,
        "outputs": outputs,
    }
    return api_request("post", "/v1/contracts:simulate", data=json.dumps(request_body))


def create_customer_address(
    request_id: str = "",
    house_name: str = "",
    street_number: str = "",
    street: str = "",
    local_municipality: str = "",
    city: str = "",
    postal_area: str = "",
    governing_district: str = "",
    country: str = "",
    address_type: str = "CUSTOMER_ADDRESS_TYPE_UNKNOWN",
    start_timestamp: str = "",
    end_timestamp: str = "",
    customer_id: str = "",
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "customer_address": {
            "house_name": house_name,
            "street_number": street_number,
            "street": street,
            "local_municipality": local_municipality,
            "city": city,
            "postal_area": postal_area,
            "governing_district": governing_district,
            "country": country,
            "address_type": address_type,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "customer_id": customer_id,
        },
    }
    return api_request("post", "/v1/customer-addresses", data=json.dumps(request_body))


def create_customer() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/customers", data=json.dumps(request_body))


def search_customers() -> List[Any]:
    request_body = {}
    return api_request("post", "/v1/customers:search", data=json.dumps(request_body))


def replay_journal_events(
    resource_type: str = "RESOURCE_TYPE_UNKNOWN",
    journal_events_to_replay: List[Dict[str, str]] = None,
) -> List[Any]:
    if journal_events_to_replay is None:
        journal_events_to_replay = [{"event_identifier": "value1"}]

    request_body: Dict[str, Any] = {
        "resource_type": resource_type,
        "journal_events_to_replay": journal_events_to_replay,
    }
    return api_request("post", "/v1/journal-events:replay", data=json.dumps(request_body))


def create_flag_definition(
    id: str = "",
    name: str = "",
    description: str = "",
    required_flag_level: str = "FLAG_LEVEL_UNKNOWN",
    flag_visibility: str = "FLAG_VISIBILITY_UNKNOWN",
    request_id: str = "",
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "flag_definition": {
            "id": id,
            "name": name,
            "description": description,
            "required_flag_level": required_flag_level,
            "flag_visibility": flag_visibility,
        },
        "request_id": request_id,
    }
    return api_request("post", "/v1/flag-definitions", data=json.dumps(request_body))


def create_flag(
    flag_definition_id: str = "",
    description: str = "",
    effective_timestamp: str = "",
    expiry_timestamp: str = "",
    customer_id: str = "",
    request_id: str = "",
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "flag": {
            "flag_definition_id": flag_definition_id,
            "description": description,
            "effective_timestamp": effective_timestamp,
            "expiry_timestamp": expiry_timestamp,
            "customer_id": customer_id,
        },
        "request_id": request_id,
    }
    return api_request("post", "/v1/flags", data=json.dumps(request_body))


def create_global_parameter_value(
    request_id: str = "",
    global_parameter_id: str = "",
    value: str = "",
    effective_timestamp: str = "",
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "global_parameter_value": {
            "global_parameter_id": global_parameter_id,
            "value": value,
            "effective_timestamp": effective_timestamp,
        },
    }
    return api_request("post", "/v1/global-parameter-values", data=json.dumps(request_body))


def create_global_parameter(
    request_id: str = "",
    id: str = "",
    display_name: str = "",
    description: str = "",
    value_type: str = "NUMBER_FIELD_DISPLAY_STYLE_NOT_SPECIFIED",
    min_value: str = "",
    max_value: str = "",
    step: str = "",
    initial_value: str = "",
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "global_parameter": {
            "id": id,
            "display_name": display_name,
            "description": description,
            "number": {
                "value_type": value_type,
                "min_value": min_value,
                "max_value": max_value,
                "step": step,
            },
        },
        "initial_value": initial_value,
    }
    return api_request("post", "/v1/global-parameters", data=json.dumps(request_body))


def create_internal_account(
    request_id: str = "",
    id: str = "",
    product_id: str = "",
    permitted_denominations: List[str] = None,
    details: Dict[str, str] = None,
    tside: str = "TSIDE_UNKNOWN",
) -> List[Any]:
    if permitted_denominations is None:
        permitted_denominations = []
    if details is None:
        details = {}

    request_body: Dict[str, Any] = {
        "internal_account": {
            "id": id,
            "product_id": product_id,
            "permitted_denominations": permitted_denominations,
            "details": details,
            "accounting": {"tside": tside},
        },
        "request_id": request_id,
    }
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


def create_payment_device_link(
    request_id: str = "",
    id: str = "",
    token: str = "",
    payment_device_id: str = "",
    account_id: str = "",
    status: str = "PAYMENT_DEVICE_LINK_STATUS_UNKNOWN",
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "payment_device_link": {
            "id": id,
            "token": token,
            "payment_device_id": payment_device_id,
            "account_id": account_id,
            "status": status,
        },
        "request_id": request_id,
    }

    return api_request("post", "/v1/payment-device-links", data=json.dumps(request_body))


def create_payment_device(
    request_id: str = "",
    id: str = "",
    routing_info: Dict[str, str] = None,
    status: str = "PAYMENT_DEVICE_STATUS_UNKNOWN",
    start_timestamp: str = "",
    end_timestamp: str = "",
    tags: List[str] = None,
) -> List[Any]:
    if routing_info is None:
        routing_info = {}
    if tags is None:
        tags = []

    request_body: Dict[str, Any] = {
        "payment_device": {
            "id": id,
            "routing_info": routing_info,
            "status": status,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "tags": tags,
        },
        "request_id": request_id,
    }
    return api_request("post", "/v1/payment-devices", data=json.dumps(request_body))


def create_plan_migration(
    request_id: str = "",
    id: str = "",
    from_supervisor_contract_version_ids: List[str] = None,
    to_supervisor_contract_version_id: str = "",
    schedule_migration_type: str = "SCHEDULE_MIGRATION_TYPE_RECREATE_ALL_SCHEDULES_AND_GROUPS",
) -> List[Any]:
    if from_supervisor_contract_version_ids is None:
        from_supervisor_contract_version_ids = []

    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "plan_migration": {
            "id": id,
            "supervisor_contract_version_migration": {
                "from_supervisor_contract_version_ids": from_supervisor_contract_version_ids,
                "to_supervisor_contract_version_id": to_supervisor_contract_version_id,
                "schedule_migration_type": schedule_migration_type,
            },
        },
    }

    return api_request("post", "/v1/plan-migrations", data=json.dumps(request_body))


def create_plan_update(
    request_id: str = "",
    id: str = "",
    plan_id: str = "",
    job_id: str = "",
    status: str = "PLAN_UPDATE_STATUS_UNKNOWN",
    account_id: str = "",
) -> List[Any]:
    request_body: Dict[str, Any] = {
        "request_id": request_id,
        "plan_update": {
            "id": id,
            "plan_id": plan_id,
            "job_id": job_id,
            "status": status,
            "associate_account_update": {"account_id": account_id},
        },
    }
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
    restriction_set_definition_id=None,
) -> List[Any]:
    return api_request(
        "post",
        f"/v1/restriction-set-definition/{restriction_set_definition_id}/versions",
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
